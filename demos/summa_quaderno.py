"""Runnable CLI demonstration of Pacioli's Venetian *Quaderno* & *Problem of Points* (1494).

Displays Rich tables verifying:
1. Chronological Venetian *Giornale* entries (``Per // A``) in ``l. s. g. p.`` money of account,
2. Pre-closing *Summa summarum* trial balance and skew-symmetric conservation ``F + F^T = 0``,
3. Cap. 27 & Cap. 34 closing cycle (*Pro e Danno* -> *Cavedal* -> *Bilancio del libro*),
4. Pacioli's 1494 *Problem of Points* (*balla* & *balestrare*, fol. 197r–197v) vs. Pascal–Fermat.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pacioli.ledger_conservation import (  # noqa: E402
    build_venetian_merchant_quaderno_1493,
    compare_problem_of_points,
)


def run_demo() -> None:
    """Execute and print the Venetian *Quaderno* and *Problem of Points* showcase."""
    console = Console()
    console.rule("[bold gold1]Fra Luca Pacioli • Summa Dist. IX (1494) — De Computis et Scripturis")

    ledger = build_venetian_merchant_quaderno_1493()

    giornale_table = Table(title="Venetian Giornale (Nov. 1493, al modo de Vinegia, fol. 201v)")
    giornale_table.add_column("#", justify="right", style="cyan")
    giornale_table.add_column("Date", style="white")
    giornale_table.add_column("Per (Dare / Debtor)", style="green")
    giornale_table.add_column("A (Avere / Creditor)", style="yellow")
    giornale_table.add_column("l. s. g. p.", justify="right", style="bold white")

    for ent in ledger.entries:
        giornale_table.add_row(
            str(ent.entry_no),
            ent.date,
            ent.debit_account,
            ent.credit_account,
            ent.amount.format_venetian(),
        )
    console.print(giornale_table)

    tb = ledger.trial_balance()
    mat_b = ledger.incidence_matrix()
    flow_f = ledger.skew_symmetric_flow_matrix()
    is_skew = flow_f + flow_f.T == sp.zeros(flow_f.rows, flow_f.cols)

    quaderno_table = Table(title="Pre-Closing Quaderno Grande — Summa Summarum (Ducati a oro)")
    quaderno_table.add_column("Carta", justify="right", style="cyan")
    quaderno_table.add_column("Account", style="white")
    quaderno_table.add_column("Dare", justify="right", style="green")
    quaderno_table.add_column("Avere", justify="right", style="yellow")
    quaderno_table.add_column("Net Dare", justify="right", style="magenta")

    for acc in tb.accounts:
        quaderno_table.add_row(
            str(acc.folio),
            acc.name,
            str(acc.dare_ducati),
            str(acc.avere_ducati),
            str(acc.net_dare_ducati),
        )
    quaderno_table.add_section()
    quaderno_table.add_row(
        "Σ",
        "SUMMA SUMMARUM",
        f"[bold]{tb.summa_dare_ducati}[/bold]",
        f"[bold]{tb.summa_avere_ducati}[/bold]",
        f"[bold]{tb.net_conservation_sum}[/bold]",
    )
    console.print(quaderno_table)

    net_profit = ledger.close_to_bilancio()
    closed_tb = ledger.trial_balance()
    console.print(
        f"[bold]Conservation Laws Verified:[/bold] "
        f"Incidence B shape={mat_b.shape}, Fᵀ = -F is [green]{is_skew}[/green], "
        f"Cassa non-negative is [green]{tb.cassa_non_negative}[/green], "
        f"Net Profit to Cavedal = [yellow]{net_profit} ducati[/yellow], "
        f"Post-Bilancio Summa = {closed_tb.summa_dare_ducati} = {closed_tb.summa_avere_ducati}\n"
    )

    points_table = Table(
        title="Fol. 197r–197v: Problem of Points — Pacioli (1494) vs. Pascal–Fermat (1654)"
    )
    points_table.add_column("Contest (Target = 6, Stake = 10 ducats)", style="cyan")
    points_table.add_column("Pacioli 1494 Shares", style="yellow")
    points_table.add_column("Pascal–Fermat Shares", style="bold green")
    points_table.add_column("Discrepancy (PF - Pacioli)", style="magenta")

    for label, scores in [("Balla 2-player (5, 3)", (5, 3)), ("Balestrare 3-player (4, 3, 2)", (4, 3, 2))]:
        cmp = compare_problem_of_points(6, scores, 10)
        points_table.add_row(
            label,
            ", ".join(str(x) for x in cmp.pacioli_shares),
            ", ".join(str(x) for x in cmp.pascal_fermat_shares),
            ", ".join(str(x) for x in cmp.discrepancies),
        )
    console.print(points_table)


if __name__ == "__main__":
    run_demo()
