"""Runnable CLI demonstration of Pacioli's *Summa* (1494) proportions and Cossic algebra.

Displays Rich tables verifying:
1. Severinus Boethius's and Pacioli's five genera of rational inequality (*Summa* fols. 70r–83r),
2. The six Euclidean *modi arguendi* (*Summa* fol. 74r),
3. Exact ``geometor.model`` semicircle construction of the three classical means and the
   division of ``10`` in extreme and mean ratio,
4. Pacioli's six canonical Cossic quadratic equations (*Summa* fols. 145r–146r).
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

from geometor.pacioli.proportions import (  # noqa: E402
    apply_six_euclidean_modes,
    classify_boethian_ratio,
    compound_ratios,
    construct_extreme_and_mean_ratio,
    construct_three_means,
    solve_cossic_quadratic,
)


def run_demo() -> None:
    """Execute and print the *Summa* (1494) proportions and Cossic algebra showcase."""
    console = Console()
    console.rule("[bold gold1]Fra Luca Pacioli • Summa (1494) — Proportioni & Regola dela Cosa")

    boethian_table = Table(title="Part I, Dist. VI (fols. 70r–83r): Five Boethian Genera of Ratio")
    boethian_table.add_column("Terms (p : q)", style="cyan")
    boethian_table.add_column("Reduced", style="white")
    boethian_table.add_column("Inequality", style="magenta")
    boethian_table.add_column("Genus", style="green")
    boethian_table.add_column("Latin Species", style="bold yellow")

    sample_pairs = [(6, 6), (12, 4), (9, 6), (5, 3), (5, 2), (11, 4), (3, 4)]
    for p_val, q_val in sample_pairs:
        rec = classify_boethian_ratio(p_val, q_val)
        boethian_table.add_row(
            f"{p_val} : {q_val}",
            f"{rec.antecedent}:{rec.consequent}",
            rec.inequality,
            rec.genus,
            rec.latin_species,
        )
    console.print(boethian_table)

    octave = compound_ratios([(3, 2), (4, 3)])
    console.print(
        f"[bold]Compounded Musical Octave (fol. 83r):[/bold] "
        f"(3:2 sesquialtera) ⊗ (4:3 sesquitertia) = "
        f"[yellow]{octave.antecedent}:{octave.consequent} ({octave.latin_species})[/yellow]\n"
    )

    modes = apply_six_euclidean_modes(12, 8, 9, 6, e=4, f=3)
    console.print(
        f"[bold]Six Euclidean Modes on 12:8 = 9:6 (fol. 74r):[/bold] "
        f"conversa={modes.conversa[0]}, permutata={modes.permutata[0]}, "
        f"congionta={modes.congionta[0]}, disgiunta={modes.disgiunta[0] if modes.disgiunta else 'N/A'}, "
        f"eversa={modes.eversa[0] if modes.eversa else 'N/A'}, "
        f"equa={modes.equa[0] if modes.equa else 'N/A'}\n"
    )

    means = construct_three_means(9, 4)
    div10 = construct_extreme_and_mean_ratio(10)
    console.print(
        f"[bold]Semicircle Three Means for (9, 4) (fol. 73v):[/bold] "
        f"A = {means.arithmetic_mean}, G = {means.geometric_mean}, H = {means.harmonic_mean} "
        f"(G² = A·H = {means.geometric_mean**2}; Proof steps = {len(means.model.steps)})"
    )
    console.print(
        f"[bold]Divine Proportion of 10 (Dist. VI & Compendio Cap. VIII):[/bold] "
        f"Major = {div10.major_part}, Minor = {div10.minor_part}, "
        f"φ = {div10.phi_ratio} (Proof steps = {len(div10.model.steps)})\n"
    )

    cossic_table = Table(title="Part I, Dist. VIII (fols. 145r–146r): Six Canonical Cossic Equations")
    cossic_table.add_column("Canon", justify="right", style="cyan")
    cossic_table.add_column("Kind", style="magenta")
    cossic_table.add_column("1494 Cossic Statement", style="white")
    cossic_table.add_column("Positive Root(s)", style="bold green")
    cossic_table.add_column("Completed Square", style="yellow")

    cases = [
        (1, 2, 10, 0),
        (2, 3, 0, 27),
        (3, 0, 4, 20),
        (4, 1, 10, 39),
        (5, 1, 10, 21),
        (6, 1, 3, 4),
        (4, sp.Rational(23, 4), 16, 48),
    ]
    for canon_no, a_val, b_val, c_val in cases:
        sol = solve_cossic_quadratic(canon_no, a_val, b_val, c_val)
        roots_str = ", ".join(str(r) for r in sol.positive_roots)
        cossic_table.add_row(
            str(sol.canon_number),
            sol.canon_kind,
            sol.cossic_statement,
            roots_str,
            str(sol.completed_square_area),
        )
    console.print(cossic_table)


if __name__ == "__main__":
    run_demo()
