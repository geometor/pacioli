"""Exact symbolic unit tests for :mod:`geometor.pacioli.proportions`."""

from __future__ import annotations

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, is_harmonic, zero_test

from geometor.pacioli.proportions import (
    apply_six_euclidean_modes,
    classify_boethian_ratio,
    compound_ratios,
    construct_extreme_and_mean_ratio,
    construct_three_means,
    solve_cossic_quadratic,
)


def _assert_zero_floats_in_model(model: Model) -> None:
    """Assert that no geometric entity in ``model`` contains any ``sp.Float`` atom."""
    for elem in model:
        assert not elem.has(sp.Float), f"Found floating-point contamination in {elem!r}"
        if isinstance(elem, spg.Point2D):
            assert not elem.x.has(sp.Float)
            assert not elem.y.has(sp.Float)


def test_boethian_five_genera_and_sub_genera() -> None:
    """Verify Boethian ratio classification across all 5 genera and lesser inequalities."""
    eq = classify_boethian_ratio(6, 6)
    assert eq.inequality == "aequalitas"
    assert eq.genus == "aequalis"
    assert eq.latin_species == "aequalis"
    assert eq.reduced_ratio == sp.Rational(1, 1)

    mult = classify_boethian_ratio(12, 4)
    assert mult.inequality == "maior inaequalitas"
    assert mult.genus == "multiplex"
    assert mult.latin_species == "tripla"

    sup_part = classify_boethian_ratio(9, 6)
    assert sup_part.genus == "superparticularis"
    assert sup_part.latin_species == "sesquialtera"
    assert (sup_part.antecedent, sup_part.consequent) == (sp.Integer(3), sp.Integer(2))

    sup_partiens = classify_boethian_ratio(5, 3)
    assert sup_partiens.genus == "superpartiens"
    assert sup_partiens.latin_species == "superbipartiens tertias"

    mult_sp = classify_boethian_ratio(5, 2)
    assert mult_sp.genus == "multiplex superparticularis"
    assert mult_sp.latin_species == "dupla sesquialtera"

    mult_spt = classify_boethian_ratio(11, 4)
    assert mult_spt.genus == "multiplex superpartiens"
    assert mult_spt.latin_species == "dupla supertripartiens quartas"

    sub_sp = classify_boethian_ratio(3, 4)
    assert sub_sp.inequality == "minor inaequalitas"
    assert sub_sp.genus == "subsuperparticularis"
    assert sub_sp.latin_species == "subsesquitertia"

    with pytest.raises(ValueError):
        classify_boethian_ratio(-3, 2)


def test_compound_ratios_musical_octave() -> None:
    """Verify compounding sesquialtera (3:2) and sesquitertia (4:3) yields dupla (2:1)."""
    comp = compound_ratios([(3, 2), (4, 3)])
    assert comp.reduced_ratio == sp.Rational(2, 1)
    assert comp.latin_species == "dupla"

    major_tone = compound_ratios([(3, 2), (3, 4)])
    assert major_tone.reduced_ratio == sp.Rational(9, 8)
    assert major_tone.latin_species == "sesquioctava"


def test_six_euclidean_modes_fol_74r() -> None:
    """Verify all six Euclidean *modi arguendi* on *Summa* fol. 74r."""
    res = apply_six_euclidean_modes(12, 8, 9, 6, e=4, f=3)
    assert res.original[0] == res.original[1] == sp.Rational(3, 2)
    assert res.conversa == (sp.Rational(2, 3), sp.Rational(2, 3))
    assert res.permutata == (sp.Rational(4, 3), sp.Rational(4, 3))
    assert res.congionta == (sp.Rational(5, 2), sp.Rational(5, 2))
    assert res.disgiunta == (sp.Rational(1, 2), sp.Rational(1, 2))
    assert res.eversa == (sp.Rational(3, 1), sp.Rational(3, 1))
    assert res.equa == (sp.Rational(3, 1), sp.Rational(3, 1))

    with pytest.raises(ValueError):
        apply_six_euclidean_modes(5, 3, 7, 4)


def test_construct_three_means_semicircle() -> None:
    """Verify exact semicircle construction of arithmetic, geometric, and harmonic means."""
    res = construct_three_means(9, 4)
    _assert_zero_floats_in_model(res.model)

    assert res.arithmetic_mean == sp.Rational(13, 2)
    assert res.geometric_mean == sp.Integer(6)
    assert res.harmonic_mean == sp.Rational(72, 13)
    assert zero_test(res.geometric_mean**2 - res.arithmetic_mean * res.harmonic_mean)
    assert res.arithmetic_mean > res.geometric_mean > res.harmonic_mean

    pt_a = spg.Point(0, 0)
    pt_pb = spg.Point(4, 0)
    pt_pa = spg.Point(9, 0)
    assert is_harmonic(pt_pb, pt_pa, res.harmonic_conjugate_point, pt_a)
    assert len(res.model.steps) >= 4


def test_construct_extreme_and_mean_ratio_10() -> None:
    """Verify Pacioli's canonical golden section of 10 into sqrt(125)-5 and 15-sqrt(125)."""
    res = construct_extreme_and_mean_ratio(10)
    _assert_zero_floats_in_model(res.model)

    expected_major = sp.sqrt(125) - 5
    expected_minor = 15 - sp.sqrt(125)
    assert zero_test(res.major_part - expected_major)
    assert zero_test(res.minor_part - expected_minor)
    assert zero_test(res.whole * res.minor_part - res.major_part**2)
    assert zero_test((res.major_part + 5) ** 2 - 125)
    assert zero_test(res.phi_ratio - (1 + sp.sqrt(5)) / 2)
    assert len(res.model.steps) >= 3

    with pytest.raises(TypeError):
        construct_extreme_and_mean_ratio(10.0)


def test_solve_cossic_quadratic_six_canons() -> None:
    """Verify all six Cossic quadratic canons on *Summa* fols. 145r–146r."""
    c1 = solve_cossic_quadratic(1, 2, 10, 0)
    assert c1.positive_roots == (sp.Integer(5),)

    c2 = solve_cossic_quadratic(2, 3, 0, 27)
    assert c2.positive_roots == (sp.Integer(3),)

    c3 = solve_cossic_quadratic(3, 0, 4, 20)
    assert c3.positive_roots == (sp.Integer(5),)

    # Classic gnomon woodcut on fol. 146r: 1.ce. + 10.co. = 39 => cosa = 3
    c4 = solve_cossic_quadratic(4, 1, 10, 39)
    assert c4.positive_roots == (sp.Integer(3),)
    assert c4.half_cose == sp.Integer(5)
    assert c4.half_cose_squared == sp.Integer(25)
    assert c4.completed_square_area == sp.Integer(64)

    # Secundi canonis double positive root: 1.ce. + 21 = 10.co. => cose = (3, 7)
    c5 = solve_cossic_quadratic(5, 1, 10, 21)
    assert c5.positive_roots == (sp.Integer(3), sp.Integer(7))
    assert c5.completed_square_area == sp.Integer(4)

    # Impossibile case of Canon 5 when (b/2)^2 < c: 1.ce. + 30 = 10.co.
    c5_imp = solve_cossic_quadratic(5, 1, 10, 30)
    assert c5_imp.positive_roots == ()

    # Tertii canonis: 3.co. + 4 = 1.ce. => cosa = 4
    c6 = solve_cossic_quadratic(6, 1, 3, 4)
    assert c6.positive_roots == (sp.Integer(4),)

    # Malfatti-type 3-circle quadratic on Part II, fol. 57r: 5 3/4 censi + 16 cose = 48
    malfatti = solve_cossic_quadratic(4, sp.Rational(23, 4), 16, 48)
    r_val = malfatti.positive_roots[0]
    assert zero_test(sp.Rational(23, 4) * r_val**2 + 16 * r_val - 48)
