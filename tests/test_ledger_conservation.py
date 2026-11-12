"""Exact symbolic unit tests for :mod:`geometor.pacioli.ledger_conservation`."""

from __future__ import annotations

import pytest
import sympy as sp

from geometor.pacioli.ledger_conservation import (
    QuadernoLedger,
    VenetianAmount,
    build_venetian_merchant_quaderno_1493,
    compare_problem_of_points,
)


def test_venetian_amount_lsgp_and_ducati_fol_201v() -> None:
    """Verify Venetian money-of-account conversions (1 lira = 10 ducati = 240 grossi = 7680 piccoli)."""
    one_ducat = VenetianAmount.from_ducati(1)
    assert one_ducat.piccoli_total == sp.Integer(768)
    assert one_ducat.to_lsgp() == (0, 2, 0, 0)
    assert one_ducat.to_ducati_rational() == sp.Integer(1)
    assert one_ducat.to_lire_rational() == sp.Rational(1, 10)

    one_lira = VenetianAmount.from_lsgp(lire=1)
    assert one_lira.piccoli_total == sp.Integer(7680)
    assert one_lira.to_ducati_rational() == sp.Integer(10)

    mixed = VenetianAmount.from_ducati(6, 12, 16)
    assert mixed.to_ducati_rational() == sp.Rational(6, 1) + sp.Rational(12, 24) + sp.Rational(16, 768)
    lire, soldi, grossi, piccoli = mixed.to_lsgp()
    rebuilt = VenetianAmount.from_lsgp(lire, soldi, grossi, piccoli)
    assert rebuilt == mixed


def test_quaderno_skew_symmetric_conservation_and_bilancio() -> None:
    """Verify conservation algebra (1^T B = 0, F^T = -F, Summa Dare = Summa Avere, Bilancio)."""
    ledger = build_venetian_merchant_quaderno_1493()
    mat_b = ledger.incidence_matrix()
    ones = sp.ones(1, mat_b.rows)
    assert ones * mat_b == sp.zeros(1, mat_b.cols)

    flow_f = ledger.skew_symmetric_flow_matrix()
    assert flow_f + flow_f.T == sp.zeros(flow_f.rows, flow_f.cols)

    tb = ledger.trial_balance()
    assert tb.is_balanced
    assert tb.cassa_non_negative
    assert tb.summa_dare_ducati == tb.summa_avere_ducati
    assert tb.net_conservation_sum == sp.Integer(0)

    # Verify net balances match B * w
    vec_w = ledger.weight_vector_ducati()
    net_vec = mat_b * vec_w
    for idx, acc_summary in enumerate(tb.accounts):
        assert net_vec[idx, 0] == acc_summary.net_dare_ducati

    # Close nominal accounts -> Pro e Danno -> Cavedal -> Bilancio del libro
    # Gain 50 ducats on ginger minus 6.5 ducats brokerage = 43.5 = 87/2 ducats net profit
    net_profit = ledger.close_to_bilancio()
    assert net_profit == sp.Rational(87, 2)

    closed_tb = ledger.trial_balance()
    assert closed_tb.is_balanced
    assert closed_tb.summa_dare_ducati == closed_tb.summa_avere_ducati
    for acc_summary in closed_tb.accounts:
        assert acc_summary.net_dare_ducati == sp.Integer(0)


def test_cassa_creditor_detection_and_validation() -> None:
    """Verify Cap. 12 Cassa non-negativity check (fol. 201r) and self-loop rejection."""
    ledger = QuadernoLedger()
    ledger.register_account("Cassa", kind="cassa")
    ledger.register_account("Cavedal", kind="capitale")

    with pytest.raises(ValueError):
        ledger.post("1493-11-08", "Cassa", "Cassa", VenetianAmount.from_ducati(10), "Invalid")

    # Overdraw Cassa on purpose -> Pacioli calls this an accounting error on fol. 201r!
    ledger.post("1493-11-09", "Cavedal", "Cassa", VenetianAmount.from_ducati(25), "Impossible cash credit")
    tb = ledger.trial_balance()
    assert tb.is_balanced
    assert not tb.cassa_non_negative


def test_problem_of_points_balla_and_balestrare_fol_197() -> None:
    """Verify Pacioli's 1494 division vs. Pascal–Fermat 1654 expectation on fol. 197r–197v."""
    # Classic 2-player balla at (5, 3) playing to 6 for 10 ducats
    balla = compare_problem_of_points(target_rounds=6, current_scores=(5, 3), total_stake_ducati=10)
    assert balla.pacioli_shares == (sp.Rational(25, 4), sp.Rational(15, 4))
    assert balla.pascal_fermat_probabilities == (sp.Rational(7, 8), sp.Rational(1, 8))
    assert balla.pascal_fermat_shares == (sp.Rational(35, 4), sp.Rational(5, 4))
    assert sum(balla.pacioli_shares) == sp.Integer(10)
    assert sum(balla.pascal_fermat_shares) == sp.Integer(10)
    assert sum(balla.discrepancies) == sp.Integer(0)

    # Problem 51 on fol. 197v: 3 crossbowmen (balestrare) at (4, 3, 2) playing to 6 for 10 ducats
    balestrare = compare_problem_of_points(
        target_rounds=6,
        current_scores=(4, 3, 2),
        total_stake_ducati=10,
    )
    assert balestrare.pacioli_shares == (
        sp.Rational(40, 9),
        sp.Rational(30, 9),
        sp.Rational(20, 9),
    )
    assert sum(balestrare.pascal_fermat_probabilities) == sp.Integer(1)
    assert sum(balestrare.pascal_fermat_shares) == sp.Integer(10)
    assert balestrare.pascal_fermat_shares[0] > balestrare.pacioli_shares[0]
