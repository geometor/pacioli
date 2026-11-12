r"""Exact symbolic constructions from Part II (*Tractatus Geometriae*) of *Summa* (1494).

Models three landmark geometric treatises from Part II of Fra Luca Pacioli's
*Summa de arithmetica, geometria, proportioni et proportionalita* (Venice, Nov. 10, 1494):

1. **Heron's Formula & the ``(13, 14, 15)`` Triangle** (*Part II, Distinctio I, Cap. 8*,
   fol. 9v): Pure straightedge-and-compass ``geometor.model.Model`` construction of
   :math:`\triangle G B A` with sides :math:`GA=13, GB=14, AB=15`, cathetus :math:`AD=12`,
   base segments :math:`GD=5, DB=9`, Heron product :math:`6 \cdot 7 \cdot 8 \cdot 21 = 7056`,
   area :math:`\sqrt{7056} = 84`, rational incenter :math:`I=(6,4)` (:math:`r=4`), and
   rational circumcenter :math:`O=(7, 33/8)` (:math:`R=65/8`).
2. **Proportional Division of Triangles** (*Part II, Distinctio IV: De divisione
   superficierum*, after Leonardo Pisano's *Practica Geometriae*): Exact Euclidean division
   of :math:`\triangle G B A` in ratio :math:`p : q` both through a vertex cevian (``VI.1``)
   and by a line parallel to the base constructed via the semicircle geometric mean
   (``VI.13``, ``VI.19``).
3. **Regular & Archimedean Polyhedra Inscribed in the Sphere** (*Part II, Distinctio VIII:
   De corporibus regularibus*, fols. 68v–70r): Exact closed-form edge lengths, squared edges
   (*possanze*), surface areas, and volumes over :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}, \phi)`
   for a sphere of diameter :math:`D = 6` (including the truncated tetrahedron of edge
   :math:`\sqrt{72/11} = \sqrt{6\frac{6}{11}}` and cuboctahedron of edge :math:`3` on fol. 69v,
   and the dodecahedron of edge :math:`\sqrt{20}-2` in the sphere of axis :math:`\sqrt{48}` on fol. 70r).
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    proposition,
    quadrance,
    zero_test,
)
from geometor.model.invariants import polygon_area2

__all__ = [
    "DodecahedronAxis48Result",
    "HeronTriangleResult",
    "InscribedPolyhedronSpec",
    "TriangleDivisionResult",
    "construct_heron_13_14_15",
    "construct_triangle_division_cevian",
    "construct_triangle_division_parallel",
    "dodecahedron_in_sphere_sqrt48",
    "inscribed_polyhedra_sphere_table",
]


@dataclass(frozen=True)
class HeronTriangleResult:
    """Exact symbolic invariants of Pacioli's ``(13, 14, 15)`` triangle (Part II, fol. 9v)."""

    model: Model
    pt_g: spg.Point
    pt_b: spg.Point
    pt_a: spg.Point
    pt_d: spg.Point
    incenter: spg.Point
    circumcenter: spg.Point
    sides: tuple[sp.Integer, sp.Integer, sp.Integer]
    perimeter: sp.Integer
    semiperimeter: sp.Integer
    excesses: tuple[sp.Integer, sp.Integer, sp.Integer]
    heron_radicand: sp.Integer
    area: sp.Integer
    altitude: sp.Integer
    base_segments: tuple[sp.Integer, sp.Integer]
    inradius: sp.Integer
    circumradius: sp.Rational


@dataclass(frozen=True)
class TriangleDivisionResult:
    """Exact symbolic outputs for dividing a triangle's area in ratio ``p : q``."""

    model: Model
    method: str
    ratio_p: sp.Integer
    ratio_q: sp.Integer
    total_area: sp.Expr
    part_1_area: sp.Expr
    part_2_area: sp.Expr
    cut_points: tuple[spg.Point, ...]


@dataclass(frozen=True)
class InscribedPolyhedronSpec:
    """Exact symbolic metrics of a regular or Archimedean solid in a sphere of diameter ``D``."""

    key: str
    italian_name: str
    faces_description: str
    sphere_diameter: sp.Expr
    edge_squared: sp.Expr
    edge: sp.Expr
    surface_area: sp.Expr
    volume: sp.Expr
    folio_citation: str


@dataclass(frozen=True)
class DodecahedronAxis48Result:
    """Exact symbolic metrics for Problem 21 on Part II, fol. 70r (sphere axis ``sqrt(48)``)."""

    sphere_axis_squared: sp.Integer
    sphere_axis: sp.Expr
    inscribed_cube_edge_squared: sp.Integer
    inscribed_cube_edge: sp.Integer
    dodecahedron_edge: sp.Expr
    extreme_mean_minor_part: sp.Expr


def _bisect_segment(
    model: Model,
    pt_1: spg.Point,
    pt_2: spg.Point,
    line_12: spg.Line,
    mid_id: str,
    perp_id: str,
) -> tuple[spg.Point, spg.Line]:
    """Construct midpoint and perpendicular bisector of segment [pt_1, pt_2] via Euclid I.10."""
    with model.subconstruction(f"I.10_{mid_id}", hide_guides=True) as scope:
        c1 = model.construct_circle(pt_1, pt_2, by="Post.3")
        c2 = model.construct_circle(pt_2, pt_1, by="Post.3")
        p_up = model.intersect(c1, c2, side_of=(pt_1, pt_2, 1), ID=f"{mid_id}_u", by="I.1")
        p_dn = model.intersect(c1, c2, side_of=(pt_1, pt_2, -1), ID=f"{mid_id}_d", by="I.1")
        perp = model.construct_line(p_up, p_dn, ID=perp_id, by="Post.1")
        mid = model.intersect(line_12, perp, ID=mid_id, by="I.10")
        scope.keep([mid, perp])
    return mid, perp


def _bisect_angle(
    model: Model,
    vertex: spg.Point,
    arm_1: spg.Point,
    arm_2: spg.Point,
    line_1: spg.Line,
    line_2: spg.Line,
    bis_id: str,
) -> spg.Line:
    """Construct internal angle bisector at ``vertex`` between rays to ``arm_1`` and ``arm_2`` (I.9)."""
    with model.subconstruction(f"I.9_{bis_id}", hide_guides=True) as scope:
        c_v = model.construct_circle(vertex, arm_1, by="Post.3")
        q2 = model.intersect(line_2, c_v, on_ray=(vertex, arm_2), ID=f"{bis_id}_q2", by="Post.3")
        k1 = model.construct_circle(arm_1, q2, by="Post.3")
        k2 = model.construct_circle(q2, arm_1, by="Post.3")
        cands = [
            model.intersect(k1, k2, index=0, ID=f"{bis_id}_t0", by="I.1"),
            model.intersect(k1, k2, index=1, ID=f"{bis_id}_t1", by="I.1"),
        ]
        q_diff = sp.simplify(quadrance(vertex, cands[0]) - quadrance(vertex, cands[1]))
        chosen = cands[0] if bool(q_diff >= 0) else cands[1]
        bis_line = model.construct_line(vertex, chosen, ID=bis_id, by="I.9")
        scope.keep(bis_line)
    return bis_line


@proposition(
    "Summa.II.I.8",
    kind="theorem",
    title="Heron's (13, 14, 15) Triangle, Cathetus, Incircle, and Circumcircle",
    hide_guides=False,
)
def _build_heron_model(
    model: Model,
    pt_g: spg.Point,
    pt_b: spg.Point,
    pt_r13: spg.Point,
    pt_r15: spg.Point,
) -> tuple[spg.Point, spg.Point, spg.Point, spg.Point]:
    """Construct A=(5,12), cathetus foot D=(5,0), incenter I=(6,4), circumcenter O=(7,33/8)."""
    line_gb = model.construct_line(pt_g, pt_b, classes=["given"], ID="l_GB", by="Post.1")

    # Euclid I.22 triangle from side lengths GA = 13, GB = 14, BA = 15
    c_g13 = model.construct_circle(pt_g, pt_r13, classes=["auxiliary"], ID="c_G13", by="Post.3")
    c_b15 = model.construct_circle(pt_b, pt_r15, classes=["auxiliary"], ID="c_B15", by="Post.3")
    pt_a = model.intersect(c_g13, c_b15, side_of=(pt_g, pt_b, 1), ID="A", classes=["result"], by="I.22")

    line_ga = model.construct_line(pt_g, pt_a, classes=["result"], ID="l_GA", by="Post.1")
    line_ba = model.construct_line(pt_b, pt_a, classes=["result"], ID="l_BA", by="Post.1")

    # Euclid I.12 cathetus AD perpendicular to GB
    with model.subconstruction("I.12_cathetus_AD", hide_guides=True) as scope:
        c_ag = model.construct_circle(pt_a, pt_g, by="Post.3")
        pt_g_ref = model.intersect(line_gb, c_ag, other_than=pt_g, by="Post.3")
        pt_d, line_ad = _bisect_segment(model, pt_g, pt_g_ref, line_gb, "D", "l_AD")
        model[pt_d].classes["result"] = ""
        model[line_ad].classes["auxiliary"] = ""
        scope.keep([pt_d, line_ad])

    # Incenter I via angle bisectors at G and B (Euclid IV.4)
    bis_g = _bisect_angle(model, pt_g, pt_b, pt_a, line_gb, line_ga, "l_bisG")
    bis_b = _bisect_angle(model, pt_b, pt_g, pt_a, line_gb, line_ba, "l_bisB")
    pt_i = model.intersect(bis_g, bis_b, ID="I", classes=["result"], by="IV.4")

    # Incircle tangent foot T on GB via I.12
    with model.subconstruction("I.12_inradius_IT", hide_guides=True) as scope:
        c_ig = model.construct_circle(pt_i, pt_g, by="Post.3")
        pt_g2 = model.intersect(line_gb, c_ig, other_than=pt_g, by="Post.3")
        pt_t, _ = _bisect_segment(model, pt_g, pt_g2, line_gb, "T", "l_IT")
        scope.keep(pt_t)
    model.construct_circle(pt_i, pt_t, classes=["result"], ID="c_in", by="IV.4")

    # Circumcenter O via perpendicular bisectors of GB and GA (Euclid IV.5)
    _, perp_gb = _bisect_segment(model, pt_g, pt_b, line_gb, "M_GB", "l_perpGB")
    _, perp_ga = _bisect_segment(model, pt_g, pt_a, line_ga, "M_GA", "l_perpGA")
    pt_o = model.intersect(perp_gb, perp_ga, ID="O", classes=["auxiliary"], by="IV.5")

    # Exact ProofMixin verifications
    model.assert_perpendicular((pt_a, pt_d), (pt_g, pt_b), by="I.12")
    model.assert_perpendicular((pt_i, pt_t), (pt_g, pt_b), by="IV.4")
    model.assert_equal((pt_o, pt_g), (pt_o, pt_b), by="IV.5")
    model.assert_equal((pt_o, pt_g), (pt_o, pt_a), by="IV.5")
    model.conclude([pt_a, pt_d, pt_i, pt_o], by="Summa.II.I.8", label="Area(ABG) = 84, AD = 12, r = 4")
    return pt_a, pt_d, pt_i, pt_o


def construct_heron_13_14_15() -> HeronTriangleResult:
    r"""Construct and verify Pacioli's ``(13, 14, 15)`` Heron triangle (Part II, fol. 9v).

    On Part II, fol. 9v (*Distinctio prima, Capitulum octavum*), Pacioli computes for
    :math:`\triangle ABG` with :math:`AG=13`, :math:`BG=14`, :math:`AB=15`:

    - Perimeter :math:`13 + 14 + 15 = 42`, semiperimeter :math:`s = 21`,
    - Excesses :math:`(s - 15, s - 14, s - 13) = (6, 7, 8)`,
    - Product :math:`6 \cdot 7 \cdot 8 = 336`, and :math:`336 \cdot 21 = 7056`,
    - Area :math:`\sqrt{7056} = 84` *braccia quadre*, cathetus :math:`AD = 12`, segments :math:`5, 9`.

    Returns:
        Exact :class:`HeronTriangleResult` containing the proven ``Model`` and invariants.
    """
    model = Model("pacioli_heron_13_14_15", logger=False, auto_intersect=False)
    pt_g = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="G")
    pt_b = model.set_point(sp.Integer(14), sp.Integer(0), classes=["given"], ID="B")
    pt_r13 = model.set_point(sp.Integer(13), sp.Integer(0), guide=True, ID="R13")
    pt_r15 = model.set_point(sp.Integer(-1), sp.Integer(0), guide=True, ID="R15")

    pt_a, pt_d, pt_i, pt_o = _build_heron_model(model, pt_g, pt_b, pt_r13, pt_r15)

    a_len = sp.Integer(13)
    b_len = sp.Integer(14)
    c_len = sp.Integer(15)
    perim = sp.Integer(a_len + b_len + c_len)
    semi = sp.Integer(perim // 2)
    exc = (sp.Integer(semi - c_len), sp.Integer(semi - b_len), sp.Integer(semi - a_len))
    radicand = sp.Integer(exc[0] * exc[1] * exc[2] * semi)
    heron_area = sp.Integer(sp.sqrt(radicand))

    poly_area = sp.Rational(polygon_area2([pt_g, pt_b, pt_a]), 2)
    if not zero_test(heron_area - poly_area):
        raise AssertionError(f"Heron area {heron_area} != coordinate area {poly_area}")

    alt = sp.Integer(sp.sqrt(quadrance(pt_a, pt_d)))
    seg_gd = sp.Integer(sp.sqrt(quadrance(pt_g, pt_d)))
    seg_db = sp.Integer(sp.sqrt(quadrance(pt_d, pt_b)))
    inrad = sp.Integer(pt_i.y)
    circumrad = sp.Rational(sp.sqrt(quadrance(pt_o, pt_g)))

    return HeronTriangleResult(
        model=model,
        pt_g=pt_g,
        pt_b=pt_b,
        pt_a=pt_a,
        pt_d=pt_d,
        incenter=pt_i,
        circumcenter=pt_o,
        sides=(a_len, b_len, c_len),
        perimeter=perim,
        semiperimeter=semi,
        excesses=exc,
        heron_radicand=radicand,
        area=heron_area,
        altitude=alt,
        base_segments=(seg_gd, seg_db),
        inradius=inrad,
        circumradius=circumrad,
    )


def construct_triangle_division_cevian(
    ratio_p: int = 1,
    ratio_q: int = 2,
) -> TriangleDivisionResult:
    r"""Divide :math:`\triangle GBA` (``13, 14, 15``) in ratio ``p : q`` by a vertex cevian.

    Implements the first problem of *Part II, Distinctio IV: De divisione superficierum*
    (following Euclid ``VI.1`` and Leonardo Pisano's *Practica Geometriae*): dividing base
    :math:`GB` at :math:`K` in ratio :math:`p : q` via Thales's intercept construction (``VI.10``)
    so :math:`\text{Area}(\triangle GAK) : \text{Area}(\triangle KAB) = p : q`.

    Args:
        ratio_p: Positive integer share adjacent to ``G`` (default ``1``).
        ratio_q: Positive integer share adjacent to ``B`` (default ``2``).

    Returns:
        Exact :class:`TriangleDivisionResult` with verified polygonal areas.
    """
    if ratio_p <= 0 or ratio_q <= 0:
        raise ValueError("Division shares p and q must be positive integers.")
    p_int = sp.Integer(ratio_p)
    q_int = sp.Integer(ratio_q)

    model = Model("pacioli_division_cevian", logger=False, auto_intersect=False)
    pt_g = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="G")
    pt_b = model.set_point(sp.Integer(14), sp.Integer(0), classes=["given"], ID="B")
    pt_a = model.set_point(sp.Integer(5), sp.Integer(12), classes=["given"], ID="A")
    line_gb = model.construct_line(pt_g, pt_b, classes=["given"], ID="l_GB", by="Post.1")
    model.construct_line(pt_g, pt_a, classes=["given"], ID="l_GA", by="Post.1")
    model.construct_line(pt_b, pt_a, classes=["given"], ID="l_BA", by="Post.1")

    # Euclid VI.10 auxiliary ray from G through (p, -p) and (p+q, -(p+q))
    with model.subconstruction("VI.10_divide_base", hide_guides=True) as scope:
        pt_u_p = model.set_point(p_int, -p_int, ID="U_p")
        pt_u_tot = model.set_point(p_int + q_int, -(p_int + q_int), ID="U_tot")
        model.construct_line(pt_g, pt_u_tot, by="Post.1")
        line_join = model.construct_line(pt_u_tot, pt_b, by="Post.1")
        # Parallel through U_p to line(U_tot, B) via direction offset
        dx = pt_b.x - pt_u_tot.x
        dy = pt_b.y - pt_u_tot.y
        pt_u_dir = model.set_point(pt_u_p.x + dx, pt_u_p.y + dy, ID="U_dir")
        line_par = model.construct_line(pt_u_p, pt_u_dir, by="I.31")
        model.assert_parallel(line_par, line_join, by="I.31")
        pt_k = model.intersect(line_gb, line_par, ID="K", classes=["result"], by="VI.10")
        scope.keep(pt_k)

    model.construct_line(pt_a, pt_k, classes=["result"], ID="l_AK", by="Post.1")

    tot_area = sp.Rational(polygon_area2([pt_g, pt_b, pt_a]), 2)
    area_1 = sp.Rational(polygon_area2([pt_g, pt_k, pt_a]), 2)
    area_2 = sp.Rational(polygon_area2([pt_k, pt_b, pt_a]), 2)
    if not zero_test(area_1 * q_int - area_2 * p_int):
        raise AssertionError(f"Cevian areas {area_1} : {area_2} do not match {p_int} : {q_int}.")
    model.conclude([pt_k], by="VI.1", label=f"Area(GAK):Area(KAB) = {p_int}:{q_int}")

    return TriangleDivisionResult(
        model=model,
        method="vertex_cevian",
        ratio_p=p_int,
        ratio_q=q_int,
        total_area=tot_area,
        part_1_area=area_1,
        part_2_area=area_2,
        cut_points=(pt_k,),
    )


def construct_triangle_division_parallel(
    ratio_p: int = 1,
    ratio_q: int = 1,
) -> TriangleDivisionResult:
    r"""Divide :math:`\triangle GBA` in ratio ``p : q`` by a cut parallel to side ``BA``.

    Implements Pacioli's *De divisione superficierum* (*Part II, Distinctio IV*, Euclid
    ``VI.13`` + ``VI.19``): to cut off :math:`\triangle GUV \sim \triangle GBA` with
    :math:`\text{Area}(\triangle GUV) / \text{Area}(\triangle GBA) = p / (p + q)`, first divide
    :math:`GB` at :math:`K` with :math:`GK / GB = p / (p+q)`, then construct the geometric mean
    :math:`GU = \sqrt{GB \cdot GK}` via a semicircle on :math:`GB` and draw :math:`UV \parallel BA`.

    Args:
        ratio_p: Positive integer share for sub-triangle ``GUV`` (default ``1``, bisecting area).
        ratio_q: Positive integer share for trapezoid ``UBAV`` (default ``1``).

    Returns:
        Exact :class:`TriangleDivisionResult` with verified radical cut coordinates and rational areas.
    """
    if ratio_p <= 0 or ratio_q <= 0:
        raise ValueError("Division shares p and q must be positive integers.")
    p_int = sp.Integer(ratio_p)
    q_int = sp.Integer(ratio_q)

    model = Model("pacioli_division_parallel", logger=False, auto_intersect=False)
    pt_g = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="G")
    pt_b = model.set_point(sp.Integer(14), sp.Integer(0), classes=["given"], ID="B")
    pt_a = model.set_point(sp.Integer(5), sp.Integer(12), classes=["given"], ID="A")
    line_gb = model.construct_line(pt_g, pt_b, classes=["given"], ID="l_GB", by="Post.1")
    line_ga = model.construct_line(pt_g, pt_a, classes=["given"], ID="l_GA", by="Post.1")
    line_ba = model.construct_line(pt_b, pt_a, classes=["given"], ID="l_BA", by="Post.1")

    # Semicircle on GB (center M = (7, 0))
    pt_m, perp_m = _bisect_segment(model, pt_g, pt_b, line_gb, "M", "l_perpM")
    c_semi = model.construct_circle(pt_m, pt_b, classes=["auxiliary"], ID="c_semi", by="Post.3")

    x_k = sp.Rational(14 * p_int, p_int + q_int)
    if x_k == sp.Integer(7):
        perp_k = perp_m
        pt_s = model.intersect(c_semi, perp_k, side_of=(pt_g, pt_b, 1), ID="S", classes=["auxiliary"], by="VI.13")
    else:
        pt_k = model.set_point(x_k, sp.Integer(0), classes=["auxiliary"], ID="K")
        with model.subconstruction("I.11_perp_at_K", hide_guides=True) as scope:
            c_kg = model.construct_circle(pt_k, pt_g, by="Post.3")
            pt_k_opp = model.intersect(line_gb, c_kg, other_than=pt_g, by="Post.3")
            _, perp_k = _bisect_segment(model, pt_g, pt_k_opp, line_gb, "K_chk", "l_perpK")
            pt_s = model.intersect(c_semi, perp_k, side_of=(pt_g, pt_b, 1), ID="S", classes=["auxiliary"], by="VI.13")
            scope.keep([perp_k, pt_s])

    # Transfer chord GS onto base GB via circle (G, S) -> U on [G, B]
    c_gs = model.construct_circle(pt_g, pt_s, classes=["auxiliary"], ID="c_GS", by="Post.3")
    pt_u = model.intersect(line_gb, c_gs, between=(pt_g, pt_b), ID="U", classes=["result"], by="Post.3")

    # Draw UV parallel to BA meeting GA at V
    pt_u_shift = model.set_point(
        pt_u.x + (pt_a.x - pt_b.x),
        pt_u.y + (pt_a.y - pt_b.y),
        guide=True,
        ID="U_dir",
    )
    line_uv = model.construct_line(pt_u, pt_u_shift, classes=["result"], ID="l_UV", by="I.31")
    pt_v = model.intersect(line_ga, line_uv, ID="V", classes=["result"], by="VI.2")

    model.assert_parallel(line_uv, line_ba, by="I.31")
    model.assert_equal((pt_g, pt_s), (pt_g, pt_u), by="I.def.15")

    tot_area = sp.simplify(sp.Rational(1, 2) * polygon_area2([pt_g, pt_b, pt_a]))
    area_1 = sp.simplify(sp.Rational(1, 2) * polygon_area2([pt_g, pt_u, pt_v]))
    area_2 = sp.simplify(tot_area - area_1)

    if not zero_test(area_1 * (p_int + q_int) - tot_area * p_int):
        raise AssertionError(f"Parallel cut area {area_1} != {p_int}/{p_int+q_int} * {tot_area}.")
    model.conclude([pt_u, pt_v], by="VI.19", label=f"Area(GUV):Area(UBAV) = {p_int}:{q_int}")

    return TriangleDivisionResult(
        model=model,
        method="parallel_cut",
        ratio_p=p_int,
        ratio_q=q_int,
        total_area=tot_area,
        part_1_area=area_1,
        part_2_area=area_2,
        cut_points=(pt_u, pt_v),
    )


def inscribed_polyhedra_sphere_table(
    diameter: int | sp.Expr = 6,
) -> dict[str, InscribedPolyhedronSpec]:
    r"""Compute exact symbolic metrics for regular & Archimedean solids in a sphere of diameter ``D``.

    Defaults to ``diameter = 6`` (*Summa* Part II, *Distinctio VIII: De corporibus regularibus*,
    fol. 69v–70r), reproducing both Euclid Book XIII's five regular solids and Pacioli's
    dependent Archimedean solids inherited from Piero della Francesca:

    - ``truncated_tetrahedron`` (fol. 69v, prob. 15–16): :math:`e^2 = \frac{2}{11} D^2`
      (:math:`= \frac{72}{11} = 6\frac{6}{11}` for :math:`D=6`, matching Pacioli's ``℞.6 6/11``!).
    - ``cuboctahedron`` (fol. 69v–70r, prob. 17–19): :math:`e = \frac{1}{2} D`
      (:math:`= 3` *braccia* for :math:`D=6`).

    Args:
        diameter: Exact positive sphere diameter ``D`` (default ``6``).

    Returns:
        Dictionary mapping solid keys to :class:`InscribedPolyhedronSpec`.
    """
    d_sym = sp.sympify(diameter)
    if d_sym.has(sp.Float):
        raise TypeError("inscribed_polyhedra_sphere_table forbids floating-point inputs.")
    if d_sym <= 0:
        raise ValueError("Sphere diameter must be positive.")

    d2 = d_sym**2
    sqrt2 = sp.sqrt(2)
    sqrt3 = sp.sqrt(3)
    sqrt5 = sp.sqrt(5)

    # 1. Tetrahedron (Euclid XIII.13): e^2 = (2/3) D^2
    e2_tet = sp.simplify(sp.Rational(2, 3) * d2)
    e_tet = sp.simplify(sp.sqrt(e2_tet))
    s_tet = sp.simplify(sqrt3 * e2_tet)
    v_tet = sp.simplify(sqrt2 / 12 * e_tet**3)

    # 2. Hexahedron / Cube (Euclid XIII.15): e^2 = (1/3) D^2
    e2_cub = sp.simplify(sp.Rational(1, 3) * d2)
    e_cub = sp.simplify(sp.sqrt(e2_cub))
    s_cub = sp.simplify(6 * e2_cub)
    v_cub = sp.simplify(e_cub**3)

    # 3. Octahedron (Euclid XIII.14): e^2 = (1/2) D^2
    e2_oct = sp.simplify(sp.Rational(1, 2) * d2)
    e_oct = sp.simplify(sp.sqrt(e2_oct))
    s_oct = sp.simplify(2 * sqrt3 * e2_oct)
    v_oct = sp.simplify(sqrt2 / 3 * e_oct**3)

    # 4. Icosahedron (Euclid XIII.16): e^2 = ((5 - sqrt(5)) / 10) D^2
    e2_ico = sp.simplify((5 - sqrt5) / 10 * d2)
    e_ico = sp.simplify(sp.sqrt(e2_ico))
    s_ico = sp.simplify(5 * sqrt3 * e2_ico)
    v_ico = sp.simplify(sp.Rational(5, 12) * (3 + sqrt5) * e_ico**3)

    # 5. Dodecahedron (Euclid XIII.17 / XIV.18): e = e_cube / phi = ((sqrt(5)-1)/(2*sqrt(3))) D
    e2_dod = sp.simplify((3 - sqrt5) / 6 * d2)
    e_dod = sp.simplify((sqrt5 - 1) / (2 * sqrt3) * d_sym)
    s_dod = sp.simplify(3 * sp.sqrt(25 + 10 * sqrt5) * e2_dod)
    v_dod = sp.simplify(sp.Rational(1, 4) * (15 + 7 * sqrt5) * e_dod**3)

    # 6. Truncated Tetrahedron (Summa Part II, fol. 69v, prob. 15–16): R^2 = (11/8) e^2 => e^2 = (2/11) D^2
    e2_ttet = sp.simplify(sp.Rational(2, 11) * d2)
    e_ttet = sp.simplify(sp.sqrt(e2_ttet))
    s_ttet = sp.simplify(7 * sqrt3 * e2_ttet)
    v_ttet = sp.simplify(sp.Rational(23, 12) * sqrt2 * e_ttet**3)

    # 7. Cuboctahedron (Summa Part II, fol. 69v–70r, prob. 17–19): R = e => e = D / 2
    e2_coct = sp.simplify(sp.Rational(1, 4) * d2)
    e_coct = sp.simplify(d_sym / 2)
    s_coct = sp.simplify((6 + 2 * sqrt3) * e2_coct)
    v_coct = sp.simplify(sp.Rational(5, 3) * sqrt2 * e_coct**3)

    return {
        "tetrahedron": InscribedPolyhedronSpec(
            key="tetrahedron",
            italian_name="Corpo de 4 base triangolari (Tetracedron)",
            faces_description="4 equilateral triangles",
            sphere_diameter=d_sym,
            edge_squared=e2_tet,
            edge=e_tet,
            surface_area=s_tet,
            volume=v_tet,
            folio_citation="Part II, Dist. VIII, fol. 69r (prob. 14); Euclid XIII.13",
        ),
        "cube": InscribedPolyhedronSpec(
            key="cube",
            italian_name="Cubo (Exacedron)",
            faces_description="6 squares",
            sphere_diameter=d_sym,
            edge_squared=e2_cub,
            edge=e_cub,
            surface_area=s_cub,
            volume=v_cub,
            folio_citation="Part II, Dist. VIII, fol. 69r (prob. 14); Euclid XIII.15",
        ),
        "octahedron": InscribedPolyhedronSpec(
            key="octahedron",
            italian_name="Corpo de 8 base triangolari (Octocedron)",
            faces_description="8 equilateral triangles",
            sphere_diameter=d_sym,
            edge_squared=e2_oct,
            edge=e_oct,
            surface_area=s_oct,
            volume=v_oct,
            folio_citation="Part II, Dist. VIII, fol. 68v; Euclid XIII.14",
        ),
        "icosahedron": InscribedPolyhedronSpec(
            key="icosahedron",
            italian_name="Corpo de 20 base triangolari (Ycocedron)",
            faces_description="20 equilateral triangles",
            sphere_diameter=d_sym,
            edge_squared=e2_ico,
            edge=e_ico,
            surface_area=s_ico,
            volume=v_ico,
            folio_citation="Part II, Dist. VIII, fol. 70v; Euclid XIII.16",
        ),
        "dodecahedron": InscribedPolyhedronSpec(
            key="dodecahedron",
            italian_name="Corpo de 12 base pentagonali (Dodecaedron)",
            faces_description="12 regular pentagons",
            sphere_diameter=d_sym,
            edge_squared=e2_dod,
            edge=e_dod,
            surface_area=s_dod,
            volume=v_dod,
            folio_citation="Part II, Dist. VIII, fol. 70r (prob. 21–22); Euclid XIII.17",
        ),
        "truncated_tetrahedron": InscribedPolyhedronSpec(
            key="truncated_tetrahedron",
            italian_name="Corpo de 4 triangoli e 4 exagoni (Tetracedron abscisum)",
            faces_description="4 equilateral triangles + 4 regular hexagons",
            sphere_diameter=d_sym,
            edge_squared=e2_ttet,
            edge=e_ttet,
            surface_area=s_ttet,
            volume=v_ttet,
            folio_citation="Part II, Dist. VIII, fol. 69v (prob. 15–16, edge = sqrt(6 6/11))",
        ),
        "cuboctahedron": InscribedPolyhedronSpec(
            key="cuboctahedron",
            italian_name="Corpo de 14 base: 6 quadrati e 8 triangoli (Exacedron abscisum)",
            faces_description="6 squares + 8 equilateral triangles",
            sphere_diameter=d_sym,
            edge_squared=e2_coct,
            edge=e_coct,
            surface_area=s_coct,
            volume=v_coct,
            folio_citation="Part II, Dist. VIII, fol. 69v–70r (prob. 17–19, edge = 3)",
        ),
    }


def dodecahedron_in_sphere_sqrt48() -> DodecahedronAxis48Result:
    """Reproduce Problem 21 on Part II, fol. 70r (dodecahedron in sphere of axis ``sqrt(48)``).

    On fol. 70r, Pacioli takes a sphere whose axis has squared length (*possanza*) ``48``:
    by Euclid ``XIII.15``, the inscribed cube has squared edge ``48 / 3 = 16``, so edge ``4``;
    dividing ``4`` in extreme and mean ratio (Campanus ``XIV.18`` / Euclid ``XIII.17`` corollary)
    yields major part ``sqrt(20) - 2`` (the dodecahedron edge) and minor part ``6 - sqrt(20)``.

    Returns:
        Exact :class:`DodecahedronAxis48Result` verified against :func:`inscribed_polyhedra_sphere_table`.
    """
    axis_sq = sp.Integer(48)
    axis = sp.sqrt(axis_sq)
    cube_sq = sp.Integer(16)
    cube_edge = sp.Integer(4)
    dod_edge = sp.sqrt(20) - 2
    minor = 6 - sp.sqrt(20)

    table = inscribed_polyhedra_sphere_table(axis)
    if not zero_test(table["dodecahedron"].edge - dod_edge):
        raise AssertionError("Dodecahedron edge mismatch on axis = sqrt(48).")
    if not zero_test(cube_edge * minor - dod_edge**2):
        raise AssertionError("Extreme-and-mean identity failed for cube edge 4.")

    return DodecahedronAxis48Result(
        sphere_axis_squared=axis_sq,
        sphere_axis=axis,
        inscribed_cube_edge_squared=cube_sq,
        inscribed_cube_edge=cube_edge,
        dodecahedron_edge=dod_edge,
        extreme_mean_minor_part=minor,
    )
