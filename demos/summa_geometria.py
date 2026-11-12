"""Runnable CLI demonstration of Pacioli's *Summa* Part II (*Tractatus Geometriae*, 1494).

Displays Rich summaries and tables verifying:
1. Heron's ``(13, 14, 15)`` triangle construction on Part II, fol. 9v,
2. Proportional division of triangles (*De divisione superficierum*, Part II, Dist. IV),
3. Inscribed Platonic & Archimedean solids in the sphere of diameter ``D = 6`` (fols. 68v–70r),
4. Dodecahedron of edge ``sqrt(20) - 2`` in the sphere of squared axis ``48`` (fol. 70r, prob. 21).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pacioli.tractatus_geometriae import (  # noqa: E402
    construct_heron_13_14_15,
    construct_triangle_division_cevian,
    construct_triangle_division_parallel,
    dodecahedron_in_sphere_sqrt48,
    inscribed_polyhedra_sphere_table,
)


def run_demo() -> None:
    """Execute and print the *Tractatus Geometriae* (Part II, 1494) symbolic showcase."""
    console = Console()
    console.rule("[bold gold1]Fra Luca Pacioli • Summa Part II (1494) — Tractatus Geometriae")

    heron = construct_heron_13_14_15()
    console.print(
        f"[bold]Heron's (13, 14, 15) Triangle (Part II, fol. 9v):[/bold]\n"
        f"  Vertices: G={heron.pt_g}, B={heron.pt_b}, A={heron.pt_a}, Foot D={heron.pt_d}\n"
        f"  Semiperimeter s = {heron.semiperimeter}, Excesses = {heron.excesses}, "
        f"Radicand = {heron.heron_radicand} ⇒ Area = √{heron.heron_radicand} = [green]{heron.area}[/green]\n"
        f"  Cathetus AD = {heron.altitude}, Segments = {heron.base_segments}, "
        f"Incenter I = {heron.incenter} (r = {heron.inradius}), "
        f"Circumcenter O = {heron.circumcenter} (R = {heron.circumradius})\n"
    )

    cev = construct_triangle_division_cevian(1, 2)
    par = construct_triangle_division_parallel(1, 1)
    console.print(
        f"[bold]De divisione superficierum (Part II, Dist. IV):[/bold]\n"
        f"  Vertex Cevian (1:2): K = {cev.cut_points[0]} ⇒ Areas {cev.part_1_area} & {cev.part_2_area}\n"
        f"  Parallel Cut (1:1):  U = {par.cut_points[0]}, V = {par.cut_points[1]} "
        f"⇒ Areas {par.part_1_area} & {par.part_2_area}\n"
    )

    solids_table = Table(
        title="Part II, Dist. VIII (fols. 68v–70r): Regular & Archimedean Solids in Sphere D = 6"
    )
    solids_table.add_column("Solid (1494 Volgare)", style="cyan")
    solids_table.add_column("Faces", style="white")
    solids_table.add_column("Edge² (Possanza)", style="yellow")
    solids_table.add_column("Exact Edge", style="bold green")
    solids_table.add_column("Exact Volume", style="magenta")

    for spec in inscribed_polyhedra_sphere_table(6).values():
        solids_table.add_row(
            spec.italian_name,
            spec.faces_description,
            str(spec.edge_squared),
            str(spec.edge),
            str(spec.volume),
        )
    console.print(solids_table)

    dod48 = dodecahedron_in_sphere_sqrt48()
    console.print(
        f"\n[bold]Problem 21 (Part II, fol. 70r — Sphere Axis² = {dod48.sphere_axis_squared}):[/bold] "
        f"Cube edge = {dod48.inscribed_cube_edge}, "
        f"Dodecahedron edge = [yellow]{dod48.dodecahedron_edge}[/yellow], "
        f"Minor golden segment = {dod48.extreme_mean_minor_part}"
    )


if __name__ == "__main__":
    run_demo()
