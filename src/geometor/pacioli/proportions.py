r"""Exact symbolic proportion theory and Cossic algebra from Pacioli's *Summa* (1494).

Formalizes three pillars of Part I of Fra Luca Pacioli's *Summa de arithmetica,
geometria, proportioni et proportionalita* (Venice, 1494):

1. **Boethian Ratio Taxonomy & Six Euclidean Modes** (*Part I, Distinctio VI*,
   fols. 68v–98r): Exact classification of rational ratios into the five Boethian
   genera of greater and lesser inequality (*multiplex*, *superparticularis*,
   *superpartiens*, *multiplex superparticularis*, *multiplex superpartiens*),
   compound ratios (*proportioni composte*), and the six Euclidean *modi arguendi*
   on fol. 74r (*conversa*, *permutata*, *congionta*, *disgiunta*, *eversa*, *equa*).
2. **Semicircle Construction of the Three Classical Means & Golden Section**:
   Targeted ``geometor.model`` straightedge-and-compass constructions proving
   :math:`A \ge G \ge H` and :math:`G^2 = A \cdot H`, harmonic cross-ratio :math:`-1`,
   and Euclidean division of :math:`10` in extreme and mean ratio into
   :math:`\sqrt{125} - 5` and :math:`15 - \sqrt{125}` (*Summa* Dist. VI & *Compendio* Cap. VII–X).
3. **Six Canonical Cossic Quadratics** (*Part I, Distinctio VIII*, fols. 145r–150r):
   Symbolic solver and gnomon completion-of-the-square parameters matching Pacioli's
   *Primi/Secundi/Tertii canonis versus* and marginal woodcuts on fol. 146r.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    cross_ratio,
    is_harmonic,
    proposition,
    quadrance,
    zero_test,
)

__all__ = [
    "BoethianClassification",
    "CossicQuadraticResult",
    "ExtremeMeanResult",
    "SixModesResult",
    "ThreeMeansResult",
    "apply_six_euclidean_modes",
    "classify_boethian_ratio",
    "compound_ratios",
    "construct_extreme_and_mean_ratio",
    "construct_three_means",
    "solve_cossic_quadratic",
]

_MULTIPLES: dict[int, str] = {
    2: "dupla",
    3: "tripla",
    4: "quadrupla",
    5: "quintupla",
    6: "sextupla",
    7: "septupla",
    8: "octupla",
    9: "nonupla",
    10: "decupla",
}

_ORDINALS_FEM_SG: dict[int, str] = {
    2: "altera",
    3: "tertia",
    4: "quarta",
    5: "quinta",
    6: "sexta",
    7: "septima",
    8: "octava",
    9: "nona",
    10: "decima",
    12: "duodecima",
}

_ORDINALS_FEM_ACC_PL: dict[int, str] = {
    3: "tertias",
    4: "quartas",
    5: "quintas",
    6: "sextas",
    7: "septimas",
    8: "octavas",
    9: "nonas",
    10: "decimas",
}

_CARDINAL_PREFIX: dict[int, str] = {
    2: "bi",
    3: "tri",
    4: "quadri",
    5: "quinque",
    6: "sex",
    7: "septem",
    8: "octo",
    9: "novem",
}


@dataclass(frozen=True)
class BoethianClassification:
    """Exact Boethian classification of a positive rational ratio :math:`p : q`."""

    antecedent: sp.Integer
    consequent: sp.Integer
    reduced_ratio: sp.Rational
    inequality: str
    genus: str
    latin_species: str
    quotient: sp.Integer
    remainder: sp.Integer
    denominator: sp.Integer


@dataclass(frozen=True)
class SixModesResult:
    """The six Euclidean *modi arguendi* (Book V / *Summa* fol. 74r) on :math:`a : b = c : d`."""

    original: tuple[sp.Rational, sp.Rational]
    conversa: tuple[sp.Rational, sp.Rational]
    permutata: tuple[sp.Rational, sp.Rational]
    congionta: tuple[sp.Rational, sp.Rational]
    disgiunta: tuple[sp.Rational, sp.Rational] | None
    eversa: tuple[sp.Rational, sp.Rational] | None
    equa: tuple[sp.Rational, sp.Rational] | None


@dataclass(frozen=True)
class ThreeMeansResult:
    """Exact symbolic outputs of the semicircle construction of the three classical means."""

    model: Model
    a: sp.Expr
    b: sp.Expr
    arithmetic_mean: sp.Expr
    geometric_mean: sp.Expr
    harmonic_mean: sp.Expr
    harmonic_conjugate_point: spg.Point


@dataclass(frozen=True)
class ExtremeMeanResult:
    """Exact symbolic outputs of dividing a segment in extreme and mean ratio."""

    model: Model
    whole: sp.Expr
    major_part: sp.Expr
    minor_part: sp.Expr
    cut_point: spg.Point
    phi_ratio: sp.Expr


@dataclass(frozen=True)
class CossicQuadraticResult:
    """Symbolic solution and geometric gnomon invariants for Pacioli's 6 canonical equations."""

    canon_number: int
    canon_kind: str
    cossic_statement: str
    positive_roots: tuple[sp.Expr, ...]
    half_cose: sp.Expr
    half_cose_squared: sp.Expr
    completed_square_area: sp.Expr


def _multiple_word(q_int: int) -> str:
    return _MULTIPLES.get(q_int, f"{q_int}-upla")


def _superparticular_word(den: int) -> str:
    ord_sg = _ORDINALS_FEM_SG.get(den, f"{den}a")
    return f"sesqui{ord_sg}"


def _superpartient_word(rem: int, den: int) -> str:
    card = _CARDINAL_PREFIX.get(rem, f"{rem}-")
    ord_pl = _ORDINALS_FEM_ACC_PL.get(den, f"{den}as")
    return f"super{card}partiens {ord_pl}"


def classify_boethian_ratio(p: int | sp.Expr, q: int | sp.Expr) -> BoethianClassification:
    """Classify a positive rational ratio :math:`p : q` according to *Summa* Dist. VI.

    Implements Severinus Boethius's and Pacioli's fivefold taxonomy of greater
    (*maior inaequalitas*) and lesser (*minor inaequalitas*, prefixed ``sub-``)
    inequality on fols. 70r–83r.

    Args:
        p: Positive rational or integer antecedent.
        q: Positive rational or integer consequent.

    Returns:
        Exact :class:`BoethianClassification` record with reduced integers and species name.

    Raises:
        ValueError: If ``p`` or ``q`` is non-positive or non-rational.
    """
    p_sym = sp.sympify(p)
    q_sym = sp.sympify(q)
    if not (p_sym.is_rational and q_sym.is_rational):
        raise ValueError(f"Boethian ratios require rational terms; got {p!r} : {q!r}.")
    if p_sym <= 0 or q_sym <= 0:
        raise ValueError(f"Boethian terms must be strictly positive; got {p!r} : {q!r}.")

    ratio = sp.Rational(p_sym, q_sym)
    num = sp.Integer(ratio.p)
    den = sp.Integer(ratio.q)

    if num == den:
        return BoethianClassification(
            antecedent=sp.Integer(1),
            consequent=sp.Integer(1),
            reduced_ratio=sp.Rational(1, 1),
            inequality="aequalitas",
            genus="aequalis",
            latin_species="aequalis",
            quotient=sp.Integer(1),
            remainder=sp.Integer(0),
            denominator=sp.Integer(1),
        )

    is_greater = num > den
    big = int(num if is_greater else den)
    small = int(den if is_greater else num)
    quot, rem = divmod(big, small)

    if rem == 0:
        base_genus = "multiplex"
        base_species = _multiple_word(quot)
    elif quot == 1 and rem == 1:
        base_genus = "superparticularis"
        base_species = _superparticular_word(small)
    elif quot == 1 and rem > 1:
        base_genus = "superpartiens"
        base_species = _superpartient_word(rem, small)
    elif quot >= 2 and rem == 1:
        base_genus = "multiplex superparticularis"
        base_species = f"{_multiple_word(quot)} {_superparticular_word(small)}"
    else:
        base_genus = "multiplex superpartiens"
        base_species = f"{_multiple_word(quot)} {_superpartient_word(rem, small)}"

    if is_greater:
        inequality = "maior inaequalitas"
        genus = base_genus
        species = base_species
    else:
        inequality = "minor inaequalitas"
        genus = f"sub{base_genus}"
        species = f"sub{base_species}"

    return BoethianClassification(
        antecedent=num,
        consequent=den,
        reduced_ratio=ratio,
        inequality=inequality,
        genus=genus,
        latin_species=species,
        quotient=sp.Integer(quot),
        remainder=sp.Integer(rem),
        denominator=sp.Integer(small),
    )


def compound_ratios(ratios: list[tuple[int | sp.Expr, int | sp.Expr]]) -> BoethianClassification:
    """Compound a sequence of rational ratios (*proportioni composte*, *Summa* fol. 83r).

    For example, compounding musical *sesquialtera* (:math:`3:2`) and *sesquitertia*
    (:math:`4:3`) yields the octave *dupla* (:math:`2:1`).

    Args:
        ratios: Non-empty list of ``(antecedent, consequent)`` pairs.

    Returns:
        The :class:`BoethianClassification` of the compounded product ratio.
    """
    if not ratios:
        raise ValueError("compound_ratios requires at least one ratio.")
    prod = sp.Integer(1)
    for num, den in ratios:
        prod *= sp.Rational(sp.sympify(num), sp.sympify(den))
    return classify_boethian_ratio(prod.p, prod.q)


def apply_six_euclidean_modes(
    a: int | sp.Expr,
    b: int | sp.Expr,
    c: int | sp.Expr,
    d: int | sp.Expr,
    e: int | sp.Expr | None = None,
    f: int | sp.Expr | None = None,
) -> SixModesResult:
    """Verify and transform :math:`a:b = c:d` under Pacioli's six modes (*Summa* fol. 74r).

    On fol. 74r (*De sex speciebus sive modis arguendi proportionalitatum*), Pacioli
    enumerates: *conversa* (:math:`b:a = d:c`), *permutata* (:math:`a:c = b:d`),
    *congionta* (:math:`(a+b):b = (c+d):d`), *disgiunta* (:math:`(a-b):b = (c-d):d`),
    *eversa* (:math:`a:(a-b) = c:(c-d)`), and *equa* (:math:`a:e = c:f` when :math:`b:e = d:f`).

    Args:
        a: First antecedent.
        b: First consequent.
        c: Second antecedent.
        d: Second consequent.
        e: Optional third term for *proportione equa* (Euclid V.22).
        f: Optional sixth term for *proportione equa* (Euclid V.22).

    Returns:
        Exact :class:`SixModesResult` verifying equality of both sides in every valid mode.
    """
    ra, rb, rc, rd = (sp.Rational(sp.sympify(x)) for x in (a, b, c, d))
    if ra * rd != rb * rc:
        raise ValueError(f"Terms ({a}, {b}, {c}, {d}) are not in proportion: {ra/rb} != {rc/rd}.")

    orig = (sp.Rational(ra, rb), sp.Rational(rc, rd))
    conv = (sp.Rational(rb, ra), sp.Rational(rd, rc))
    perm = (sp.Rational(ra, rc), sp.Rational(rb, rd))
    cong = (sp.Rational(ra + rb, rb), sp.Rational(rc + rd, rd))

    disg = None
    ever = None
    if ra != rb and rc != rd:
        disg = (sp.Rational(ra - rb, rb), sp.Rational(rc - rd, rd))
        ever = (sp.Rational(ra, ra - rb), sp.Rational(rc, rc - rd))

    equa = None
    if e is not None and f is not None:
        re_val = sp.Rational(sp.sympify(e))
        rf_val = sp.Rational(sp.sympify(f))
        if rb * rf_val != rd * re_val:
            raise ValueError(f"Auxiliary terms ({e}, {f}) do not satisfy b:e = d:f.")
        equa = (sp.Rational(ra, re_val), sp.Rational(rc, rf_val))

    return SixModesResult(
        original=orig,
        conversa=conv,
        permutata=perm,
        congionta=cong,
        disgiunta=disg,
        eversa=ever,
        equa=equa,
    )


@proposition(
    "Summa.I.VI.Means",
    kind="theorem",
    title="Semicircle Construction of Arithmetic, Geometric, and Harmonic Means",
    hide_guides=False,
)
def _build_three_means_in_model(
    model: Model,
    pt_a: spg.Point,
    pt_p: spg.Point,
    pt_b: spg.Point,
) -> tuple[spg.Point, spg.Point, spg.Point]:
    """Construct midpoint M, altitude vertex Q, and projection N inside a Model."""
    line_ab = model.construct_line(pt_a, pt_b, classes=["given"], ID="l_AB", by="Post.1")

    with model.subconstruction("I.10_midpoint_AB", hide_guides=True) as scope:
        c_ab = model.construct_circle(pt_a, pt_b, by="Post.3")
        c_ba = model.construct_circle(pt_b, pt_a, by="Post.3")
        u1 = model.intersect(c_ab, c_ba, side_of=(pt_a, pt_b, 1), ID="U1", by="I.1")
        u2 = model.intersect(c_ab, c_ba, side_of=(pt_a, pt_b, -1), ID="U2", by="I.1")
        perp_mid = model.construct_line(u1, u2, by="Post.1")
        pt_m = model.intersect(line_ab, perp_mid, ID="M", classes=["result"], by="I.10")
        scope.keep(pt_m)

    semi = model.construct_circle(pt_m, pt_b, classes=["auxiliary"], ID="c_semi", by="Post.3")

    with model.subconstruction("I.11_perp_at_P", hide_guides=True) as scope:
        c_pa = model.construct_circle(pt_p, pt_a, by="Post.3")
        pt_p_opp = model.intersect(line_ab, c_pa, other_than=pt_a, ID="P_opp", by="Post.3")
        c1 = model.construct_circle(pt_a, pt_p_opp, by="Post.3")
        c2 = model.construct_circle(pt_p_opp, pt_a, by="Post.3")
        v1 = model.intersect(c1, c2, side_of=(pt_a, pt_b, 1), ID="V1", by="I.11")
        v2 = model.intersect(c1, c2, side_of=(pt_a, pt_b, -1), ID="V2", by="I.11")
        perp_p = model.construct_line(v1, v2, ID="l_PQ", by="Post.1")
        pt_q = model.intersect(semi, perp_p, side_of=(pt_a, pt_b, 1), ID="Q", classes=["result"], by="VI.13")
        scope.keep([perp_p, pt_q])

    rad_mq = model.construct_line(pt_m, pt_q, classes=["auxiliary"], ID="l_MQ", by="Post.1")

    with model.subconstruction("I.12_foot_P_on_MQ", hide_guides=True) as scope:
        c_pq = model.construct_circle(pt_p, pt_q, by="Post.3")
        pt_q2 = model.intersect(rad_mq, c_pq, other_than=pt_q, ID="Q_ref", by="Post.3")
        k1 = model.construct_circle(pt_q, pt_q2, by="Post.3")
        k2 = model.construct_circle(pt_q2, pt_q, by="Post.3")
        w1 = model.intersect(k1, k2, index=0, ID="W1", by="I.12")
        w2 = model.intersect(k1, k2, index=1, ID="W2", by="I.12")
        perp_pn = model.construct_line(w1, w2, ID="l_PN", by="Post.1")
        pt_n = model.intersect(rad_mq, perp_pn, ID="N", classes=["result"], by="I.12")
        scope.keep([perp_pn, pt_n])

    # Deductive verification: PQ _|_ AB, PN _|_ MQ, and MQ = MB (Arithmetic mean)
    model.assert_perpendicular((pt_p, pt_q), (pt_a, pt_b), by="I.11")
    model.assert_perpendicular((pt_p, pt_n), (pt_m, pt_q), by="I.12")
    model.assert_equal((pt_m, pt_q), (pt_m, pt_b), by="I.def.15")
    model.conclude([pt_m, pt_q, pt_n], by="VI.8.Porism", label="G^2 = A * H")
    return pt_m, pt_q, pt_n


def construct_three_means(a: int | sp.Expr = 9, b: int | sp.Expr = 4) -> ThreeMeansResult:
    r"""Construct Arithmetic, Geometric, and Harmonic means of :math:`a` and :math:`b` in ``Model``.

    Places collinear points :math:`A=(0,0)`, :math:`P=(a,0)`, :math:`B=(a+b,0)`. In the
    semicircle on diameter :math:`AB` with center :math:`M`:

    - Radius :math:`MQ = (a+b)/2 = A` (Arithmetic mean),
    - Altitude :math:`PQ = \sqrt{ab} = G` (Geometric mean, Euclid ``VI.13``),
    - Leg :math:`QN = 2ab/(a+b) = H` on radius :math:`MQ` where :math:`PN \perp MQ` (Harmonic mean),
      satisfying :math:`PQ^2 = MQ \cdot QN \iff G^2 = A \cdot H`.

    Also constructs the collinear harmonic range :math:`(A, C_H; P, D_H)` with cross-ratio :math:`-1`.

    Args:
        a: First positive exact length (default ``9``, matching *Summa* / *Compendio* ratios).
        b: Second positive exact length (default ``4``).

    Returns:
        Exact :class:`ThreeMeansResult` with proven ``Model`` and exact symbolic means.
    """
    a_val = sp.sympify(a)
    b_val = sp.sympify(b)
    if a_val.has(sp.Float) or b_val.has(sp.Float):
        raise TypeError("construct_three_means forbids floating-point inputs.")
    if a_val <= 0 or b_val <= 0 or a_val == b_val:
        raise ValueError("Provide distinct positive lengths a != b for the three means.")

    model = Model("pacioli_three_means", logger=False, auto_intersect=False)
    pt_a = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="A")
    pt_p = model.set_point(a_val, sp.Integer(0), classes=["given"], ID="P")
    pt_b = model.set_point(a_val + b_val, sp.Integer(0), classes=["given"], ID="B")

    pt_m, pt_q, pt_n = _build_three_means_in_model(model, pt_a, pt_p, pt_b)

    arith = sp.simplify(sp.sqrt(quadrance(pt_m, pt_q)))
    geom = sp.simplify(sp.sqrt(quadrance(pt_p, pt_q)))
    harm = sp.simplify(sp.sqrt(quadrance(pt_q, pt_n)))

    if not zero_test(geom**2 - arith * harm):
        raise AssertionError(f"G^2 != A * H: {geom**2} vs {arith * harm}")

    # Collinear harmonic conjugate on [A, P]: A=(0,0), X_H=(H_seg, 0), B_seg=(a,0), M_inf
    # For segments a and b from origin: O=(0,0), P_b=(b,0), P_h=(2ab/(a+b), 0), P_a=(a,0)
    pt_pb = model.set_point(b_val, sp.Integer(0), classes=["auxiliary"], ID="P_b")
    pt_ph = model.set_point(harm, sp.Integer(0), classes=["result"], ID="H_pt")
    cr = cross_ratio(pt_a, pt_ph, pt_pb, pt_p)
    # Check harmonic cross-ratio of (P_b, P_a; P_h, A) -> (b, a; 2ab/(a+b), 0) = -1!
    if not is_harmonic(pt_pb, pt_p, pt_ph, pt_a):
        raise AssertionError(f"Expected harmonic range, got cross_ratio={cr}")

    return ThreeMeansResult(
        model=model,
        a=a_val,
        b=b_val,
        arithmetic_mean=arith,
        geometric_mean=geom,
        harmonic_mean=harm,
        harmonic_conjugate_point=pt_ph,
    )


@proposition(
    "II.11",
    g_id="G.120",
    kind="problem",
    title="Divide a Given Straight Line in Extreme and Mean Ratio",
    hide_guides=False,
)
def _divide_extreme_mean_in_model(
    model: Model,
    pt_a: spg.Point,
    pt_b: spg.Point,
) -> spg.Point:
    """Euclidean II.11 / VI.30 compass-and-straightedge golden cut of segment AB."""
    line_ab = model.construct_line(pt_a, pt_b, classes=["given"], ID="l_AB", by="Post.1")

    # Perpendicular at A of length AB -> D
    with model.subconstruction("I.11_perp_at_A", hide_guides=True) as scope:
        c_ab_a = model.construct_circle(pt_a, pt_b, ID="c_AB", by="Post.3")
        pt_b_opp = model.intersect(line_ab, c_ab_a, other_than=pt_b, ID="B_opp", by="Post.3")
        k1 = model.construct_circle(pt_b, pt_b_opp, by="Post.3")
        k2 = model.construct_circle(pt_b_opp, pt_b, by="Post.3")
        v1 = model.intersect(k1, k2, side_of=(pt_a, pt_b, 1), ID="V_up", by="I.11")
        v2 = model.intersect(k1, k2, side_of=(pt_a, pt_b, -1), ID="V_dn", by="I.11")
        line_ad = model.construct_line(v1, v2, ID="l_AD", by="Post.1")
        pt_d = model.intersect(line_ad, c_ab_a, side_of=(pt_a, pt_b, 1), ID="D", classes=["auxiliary"], by="I.46")
        scope.keep([line_ad, pt_d])

    # Bisect AD at E (so AE = AB / 2; for AB = 10, AE = 5, EB = sqrt(125))
    with model.subconstruction("I.10_midpoint_AD", hide_guides=True) as scope:
        m1 = model.construct_circle(pt_a, pt_d, by="Post.3")
        m2 = model.construct_circle(pt_d, pt_a, by="Post.3")
        p1 = model.intersect(m1, m2, index=0, ID="M1", by="I.1")
        p2 = model.intersect(m1, m2, index=1, ID="M2", by="I.1")
        bis_ad = model.construct_line(p1, p2, by="Post.1")
        pt_e = model.intersect(line_ad, bis_ad, ID="E", classes=["auxiliary"], by="I.10")
        scope.keep(pt_e)

    # Circle (E, B) meets ray DA beyond A at F (AF = EB - EA = sqrt(125) - 5)
    model.construct_line(pt_e, pt_b, classes=["auxiliary"], ID="l_EB", by="Post.1")
    c_eb = model.construct_circle(pt_e, pt_b, classes=["auxiliary"], ID="c_EB", by="Post.3")
    pt_f = model.intersect(line_ad, c_eb, beyond=(pt_d, pt_a), ID="F", classes=["auxiliary"], by="II.6")

    # Transfer AF onto segment AB via circle (A, F) -> cut point C
    c_af = model.construct_circle(pt_a, pt_f, classes=["auxiliary"], ID="c_AF", by="Post.3")
    pt_c = model.intersect(line_ab, c_af, between=(pt_a, pt_b), ID="C", classes=["result"], by="II.11")

    model.assert_perpendicular((pt_a, pt_d), (pt_a, pt_b), by="I.11")
    model.assert_equal((pt_a, pt_f), (pt_a, pt_c), by="I.def.15")
    model.conclude([pt_c], by="II.11", label="AB * CB = AC^2")
    return pt_c


def construct_extreme_and_mean_ratio(length: int | sp.Expr = 10) -> ExtremeMeanResult:
    r"""Divide a line of given ``length`` (default ``10``) in extreme and mean ratio.

    Reproduces Pacioli's canonical numerical archetype (*Summa* Dist. VI & Part II Dist. VIII;
    *De Divina Proportione* Cap. VIII–X): for :math:`AB = 10`, the major segment is
    :math:`AC = \sqrt{125} - 5 = 5(\sqrt{5} - 1)` and the minor segment is
    :math:`CB = 15 - \sqrt{125} = 5(3 - \sqrt{5})`, satisfying
    :math:`AB \cdot CB = AC^2 = 150 - 10\sqrt{125}` and Euclid ``XIII.1``
    :math:`(AC + 5)^2 = 125 = 5 \cdot 5^2`.

    Args:
        length: Positive exact length of segment :math:`AB` (default ``10``).

    Returns:
        Exact :class:`ExtremeMeanResult` with proven ``Model`` and closed-form algebraic parts.
    """
    len_sym = sp.sympify(length)
    if len_sym.has(sp.Float):
        raise TypeError("construct_extreme_and_mean_ratio forbids floating-point inputs.")
    if len_sym <= 0:
        raise ValueError("Segment length must be strictly positive.")

    model = Model("pacioli_extreme_mean", logger=False, auto_intersect=False)
    pt_a = model.set_point(sp.Integer(0), sp.Integer(0), classes=["given"], ID="A")
    pt_b = model.set_point(len_sym, sp.Integer(0), classes=["given"], ID="B")
    pt_c = _divide_extreme_mean_in_model(model, pt_a, pt_b)

    major = sp.simplify(pt_c.x - pt_a.x)
    minor = sp.simplify(pt_b.x - pt_c.x)
    if not zero_test(len_sym * minor - major**2):
        raise AssertionError("Failed II.11 identity: AB * CB != AC^2.")
    if not zero_test((major + len_sym / 2) ** 2 - 5 * (len_sym / 2) ** 2):
        raise AssertionError("Failed XIII.1 First Effect identity.")

    phi_val = sp.simplify(major / minor)
    return ExtremeMeanResult(
        model=model,
        whole=len_sym,
        major_part=major,
        minor_part=minor,
        cut_point=pt_c,
        phi_ratio=phi_val,
    )


def solve_cossic_quadratic(
    canon_number: int,
    a_censi: int | sp.Expr,
    b_cose: int | sp.Expr,
    c_numero: int | sp.Expr,
) -> CossicQuadraticResult:
    """Solve one of Pacioli's six canonical Cossic equations (*Summa* fols. 145r–146r).

    On fol. 145r, Pacioli classifies positive-coefficient equations into three simple
    (*capitoli semplici*, 1–3) and three compound (*capitoli composti*, 4–6) canons:

    1. ``a .ce. = b .co.`` (:math:`a x^2 = b x`)
    2. ``a .ce. = c`` (:math:`a x^2 = c`)
    3. ``b .co. = c`` (:math:`b x = c`)
    4. ``a .ce. p̄ b .co. = c`` (:math:`a x^2 + b x = c` — *Primi canonis versus*:
       *Si res et census numero coaequantur...*)
    5. ``a .ce. p̄ c = b .co.`` (:math:`a x^2 + c = b x` — *Secundi canonis versus*:
       two positive roots when :math:`(b/(2a))^2 > c/a`)
    6. ``b .co. p̄ c = a .ce.`` (:math:`b x + c = a x^2` — *Tertii canonis versus*)

    Args:
        canon_number: Integer ``1`` through ``6`` selecting Pacioli's canon.
        a_censi: Coefficient of *censo* (:math:`x^2`), positive for canons 1, 2, 4, 5, 6.
        b_cose: Coefficient of *cosa* (:math:`x`), positive for canons 1, 3, 4, 5, 6.
        c_numero: Constant *numero*, positive for canons 2, 3, 4, 5, 6.

    Returns:
        Exact :class:`CossicQuadraticResult` with Cossic statement, positive root(s),
        and completion-of-the-square gnomon invariants.
    """
    a = sp.Rational(sp.sympify(a_censi)) if sp.sympify(a_censi).is_rational else sp.sympify(a_censi)
    b = sp.Rational(sp.sympify(b_cose)) if sp.sympify(b_cose).is_rational else sp.sympify(b_cose)
    c = sp.Rational(sp.sympify(c_numero)) if sp.sympify(c_numero).is_rational else sp.sympify(c_numero)

    if canon_number == 1:
        if a <= 0 or b <= 0:
            raise ValueError("Canon 1 requires positive censi and cose.")
        roots = (sp.simplify(b / a),)
        return CossicQuadraticResult(
            canon_number=1,
            canon_kind="semplice",
            cossic_statement=f"{a}.ce. eqle a {b}.co.",
            positive_roots=roots,
            half_cose=sp.Integer(0),
            half_cose_squared=sp.Integer(0),
            completed_square_area=sp.Integer(0),
        )

    if canon_number == 2:
        if a <= 0 or c <= 0:
            raise ValueError("Canon 2 requires positive censi and numero.")
        roots = (sp.simplify(sp.sqrt(c / a)),)
        return CossicQuadraticResult(
            canon_number=2,
            canon_kind="semplice",
            cossic_statement=f"{a}.ce. eqle a {c}",
            positive_roots=roots,
            half_cose=sp.Integer(0),
            half_cose_squared=sp.Integer(0),
            completed_square_area=sp.simplify(c / a),
        )

    if canon_number == 3:
        if b <= 0 or c <= 0:
            raise ValueError("Canon 3 requires positive cose and numero.")
        roots = (sp.simplify(c / b),)
        return CossicQuadraticResult(
            canon_number=3,
            canon_kind="semplice",
            cossic_statement=f"{b}.co. eqle a {c}",
            positive_roots=roots,
            half_cose=sp.Integer(0),
            half_cose_squared=sp.Integer(0),
            completed_square_area=sp.Integer(0),
        )

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Compound canons 4–6 require strictly positive coefficients.")

    p_norm = sp.simplify(b / a)
    q_norm = sp.simplify(c / a)
    half = sp.simplify(p_norm / 2)
    half_sq = sp.simplify(half**2)

    if canon_number == 4:
        comp_area = sp.simplify(half_sq + q_norm)
        root = sp.simplify(sp.sqrt(comp_area) - half)
        return CossicQuadraticResult(
            canon_number=4,
            canon_kind="composto (primi canonis)",
            cossic_statement=f"{a}.ce. p̄ {b}.co. eqle a {c}",
            positive_roots=(root,),
            half_cose=half,
            half_cose_squared=half_sq,
            completed_square_area=comp_area,
        )

    if canon_number == 5:
        comp_area = sp.simplify(half_sq - q_norm)
        if comp_area < 0:
            return CossicQuadraticResult(
                canon_number=5,
                canon_kind="composto (secundi canonis — impossibile)",
                cossic_statement=f"{a}.ce. p̄ {c} eqle a {b}.co.",
                positive_roots=(),
                half_cose=half,
                half_cose_squared=half_sq,
                completed_square_area=comp_area,
            )
        rt = sp.sqrt(comp_area)
        r1 = sp.simplify(half - rt)
        r2 = sp.simplify(half + rt)
        roots = (r1,) if zero_test(r1 - r2) else (r1, r2)
        return CossicQuadraticResult(
            canon_number=5,
            canon_kind="composto (secundi canonis)",
            cossic_statement=f"{a}.ce. p̄ {c} eqle a {b}.co.",
            positive_roots=roots,
            half_cose=half,
            half_cose_squared=half_sq,
            completed_square_area=comp_area,
        )

    if canon_number == 6:
        comp_area = sp.simplify(half_sq + q_norm)
        root = sp.simplify(sp.sqrt(comp_area) + half)
        return CossicQuadraticResult(
            canon_number=6,
            canon_kind="composto (tertii canonis)",
            cossic_statement=f"{b}.co. p̄ {c} eqle a {a}.ce.",
            positive_roots=(root,),
            half_cose=half,
            half_cose_squared=half_sq,
            completed_square_area=comp_area,
        )

    raise ValueError(f"Unknown canon_number {canon_number!r}; expected 1..6.")
