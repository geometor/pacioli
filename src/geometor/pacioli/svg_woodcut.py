"""Deterministic `.euclid-graphic` SVG generator for Pacioli's *Summa* (1494) codex.

Generates nine theme-adaptive, interactive ``.euclid-graphic`` SVGs directly from
exact ``SymPy`` and ``geometor.model`` coordinates (converting symbolic expressions
to pixel coordinates strictly at SVG serialization time). Every generated SVG adheres
to the ``photon-platform/publish`` five-layer contract (``#elements``, ``#graphics``,
``#highlights``, ``#points``, ``#labels``), 3-vertex midpoint segment paths for
congruence tick markers (``#geom-tick-1..3``), and canonical ``data-ref`` wiring for
``:g:`` and ``:eq:`` interactive highlighting.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from html import escape
from pathlib import Path

import sympy as sp

from geometor.pacioli.proportions import (
    construct_extreme_and_mean_ratio,
    construct_three_means,
)
from geometor.pacioli.tractatus_geometriae import (
    construct_heron_13_14_15,
    construct_triangle_division_parallel,
)

__all__ = [
    "EuclidGraphicCanvas",
    "SVGSpec",
    "generate_all_summa_svgs",
]

_STYLE_AND_DEFS = """  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #000000;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-point-stroke: #1e1e20;
        --geom-poly-fill: #d6cfc5;
        --geom-accent: #e8b85a;
        --geom-assert: #5ec27e;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-circle, .geom-curve {
      stroke: var(--geom-fg);
      stroke-width: 1.7;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc {
      stroke: var(--geom-fg);
      stroke-width: 1.6;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-dashed, .geom-aux {
      stroke: var(--geom-fg);
      stroke-width: 1.4;
      stroke-dasharray: 4, 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      opacity: 0.85;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-tick-mark {
      stroke: var(--geom-assert);
      stroke-width: 2;
      stroke-linecap: round;
      fill: none;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.05;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .geom-polygon-gnomon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.13;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-label {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sm {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 11px;
      font-weight: 600;
      fill: var(--geom-fg);
      opacity: 0.88;
      user-select: none;
    }
    .geom-overlay {
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.12s ease;
    }
    [data-ref]:hover, .highlight, .geom-highlight-active {
      opacity: 1 !important;
      stroke: var(--geom-accent) !important;
      cursor: pointer;
    }
    text[data-ref]:hover, text.highlight, text.geom-highlight-active {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
    .geom-polygon:hover, .geom-polygon.highlight, .geom-polygon-gnomon:hover, .geom-polygon-gnomon.highlight, polygon.geom-highlight-active {
      opacity: 1 !important;
      fill-opacity: 0.24 !important;
      fill: var(--geom-accent) !important;
      stroke: var(--geom-accent) !important;
    }
    .geom-point:hover, .geom-point.highlight, circle.geom-point.geom-highlight-active {
      opacity: 1 !important;
      fill: var(--geom-accent) !important;
      stroke: none !important;
    }
    .geom-assert-active {
      opacity: 1 !important;
      stroke: var(--geom-assert) !important;
    }
    text.geom-assert-active {
      opacity: 1 !important;
      fill: var(--geom-assert) !important;
      stroke: none !important;
    }
    polygon.geom-assert-active {
      opacity: 1 !important;
      fill-opacity: 0.22 !important;
      fill: var(--geom-assert) !important;
      stroke: var(--geom-assert) !important;
    }
    circle.geom-point.geom-assert-active {
      opacity: 1 !important;
      fill: var(--geom-assert) !important;
      stroke: none !important;
    }
    path.geom-assert-active.geom-tick-1 {
      marker-mid: url(#geom-tick-1);
    }
    path.geom-assert-active.geom-tick-2 {
      marker-mid: url(#geom-tick-2);
    }
    path.geom-assert-active.geom-tick-3 {
      marker-mid: url(#geom-tick-3);
    }
  </style>
  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" class="geom-tick-mark" />
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-3.2" y1="-4.5" x2="-3.2" y2="4.5" class="geom-tick-mark" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
      <line x1="3.2" y1="-4.5" x2="3.2" y2="4.5" class="geom-tick-mark" />
    </marker>
  </defs>"""


def _num(val: float | int | sp.Expr) -> float:
    if isinstance(val, (int, float)):
        return float(val)
    return float(sp.sympify(val).evalf())


def _fmt(val: float) -> str:
    rounded = round(val, 2)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.2f}".rstrip("0").rstrip(".")


@dataclass(frozen=True)
class SVGSpec:
    """Metadata describing a generated *Summa* ``.euclid-graphic`` SVG plate."""

    graphic_id: str
    unit_dir: str
    filename: str
    folio: str
    proposition: str
    path: Path


class EuclidGraphicCanvas:
    """Builder for standard 5-layer ``.euclid-graphic`` interactive SVGs."""

    def __init__(
        self,
        *,
        width: int,
        height: int,
        graphic_id: str,
        folio: str,
        proposition: str,
        scale: float = 1.0,
        origin_x: float = 0.0,
        origin_y: float = 0.0,
    ) -> None:
        """Initialize an SVG canvas mapping world ``(x, y)`` (y-up) to SVG pixels."""
        self.width = width
        self.height = height
        self.graphic_id = graphic_id
        self.folio = folio
        self.proposition = proposition
        self.scale = scale
        self.origin_x = origin_x
        self.origin_y = origin_y
        self._elements: list[str] = []
        self._graphics: list[str] = []
        self._highlights: list[str] = []
        self._points: list[str] = []
        self._labels: list[str] = []

    def to_px(self, x: float | int | sp.Expr, y: float | int | sp.Expr) -> tuple[float, float]:
        """Map exact mathematical ``(x, y)`` (y-up) to SVG screen coordinates (y-down)."""
        px = self.origin_x + _num(x) * self.scale
        py = self.origin_y - _num(y) * self.scale
        return (px, py)

    def add_circle(
        self,
        el_id: str,
        cx: float | int | sp.Expr,
        cy: float | int | sp.Expr,
        r: float | int | sp.Expr,
        *,
        data_ref: str = "",
        css_class: str = "geom-circle",
    ) -> None:
        """Add a circle to ``#elements`` and ``#highlights``."""
        px, py = self.to_px(cx, cy)
        pr = abs(_num(r) * self.scale)
        ref_attr = f' data-ref="{escape(data_ref)}"' if data_ref else ""
        self._elements.append(
            f'    <circle id="el-circle-{el_id}"{ref_attr} data-type="circle" '
            f'cx="{_fmt(px)}" cy="{_fmt(py)}" r="{_fmt(pr)}" class="{css_class}" />'
        )
        if data_ref:
            self._highlights.append(
                f'    <circle id="hl-circle-{el_id}"{ref_attr} '
                f'cx="{_fmt(px)}" cy="{_fmt(py)}" r="{_fmt(pr)}" class="{css_class} geom-overlay" />'
            )

    def add_arc(
        self,
        el_id: str,
        cx: float | int | sp.Expr,
        cy: float | int | sp.Expr,
        r: float | int | sp.Expr,
        deg_start: float,
        deg_end: float,
        *,
        data_ref: str = "",
        css_class: str = "geom-arc",
    ) -> None:
        """Add a circular arc (math degrees counter-clockwise from +x) to ``#elements``."""
        px_c, py_c = self.to_px(cx, cy)
        pr = abs(_num(r) * self.scale)
        rad1 = math.radians(deg_start)
        rad2 = math.radians(deg_end)
        x1 = px_c + pr * math.cos(rad1)
        y1 = py_c - pr * math.sin(rad1)
        x2 = px_c + pr * math.cos(rad2)
        y2 = py_c - pr * math.sin(rad2)
        span = (deg_end - deg_start) % 360.0
        large_arc = 1 if span > 180.0 else 0
        # Counter-clockwise in y-up math coordinates is sweep=0 in y-down SVG coordinates
        d_str = f"M {_fmt(x1)} {_fmt(y1)} A {_fmt(pr)} {_fmt(pr)} 0 {large_arc} 0 {_fmt(x2)} {_fmt(y2)}"
        ref_attr = f' data-ref="{escape(data_ref)}"' if data_ref else ""
        self._elements.append(
            f'    <path id="el-arc-{el_id}"{ref_attr} data-type="arc" class="{css_class}" d="{d_str}" />'
        )
        if data_ref:
            self._highlights.append(
                f'    <path id="hl-arc-{el_id}"{ref_attr} class="{css_class} geom-overlay" d="{d_str}" />'
            )

    def add_polygon(
        self,
        el_id: str,
        vertices: list[tuple[float | int | sp.Expr, float | int | sp.Expr]],
        *,
        data_ref: str = "",
        css_class: str = "geom-polygon",
    ) -> None:
        """Add a filled polygon to ``#graphics`` and ``#highlights``."""
        pts_str = " ".join(f"{_fmt(px)},{_fmt(py)}" for px, py in (self.to_px(x, y) for x, y in vertices))
        ref_attr = f' data-ref="{escape(data_ref)}"' if data_ref else ""
        self._graphics.append(
            f'    <polygon id="el-poly-{el_id}"{ref_attr} data-type="polygon" '
            f'points="{pts_str}" class="{css_class}" />'
        )
        if data_ref:
            self._highlights.append(
                f'    <polygon id="hl-poly-{el_id}"{ref_attr} '
                f'points="{pts_str}" class="{css_class} geom-overlay" />'
            )

    def add_segment(
        self,
        el_id: str,
        p1: tuple[float | int | sp.Expr, float | int | sp.Expr],
        p2: tuple[float | int | sp.Expr, float | int | sp.Expr],
        *,
        data_ref: str = "",
        css_class: str = "geom-line",
    ) -> None:
        """Add a 3-vertex midpoint segment path ``M x1 y1 L xm ym L x2 y2`` to ``#graphics``."""
        x1, y1 = self.to_px(p1[0], p1[1])
        x2, y2 = self.to_px(p2[0], p2[1])
        xm, ym = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        d_str = f"M {_fmt(x1)} {_fmt(y1)} L {_fmt(xm)} {_fmt(ym)} L {_fmt(x2)} {_fmt(y2)}"
        ref_attr = f' data-ref="{escape(data_ref)}"' if data_ref else ""
        self._graphics.append(
            f'    <path id="el-seg-{el_id}"{ref_attr} data-type="segment" class="{css_class}" d="{d_str}" />'
        )
        if data_ref:
            self._highlights.append(
                f'    <path id="hl-seg-{el_id}"{ref_attr} class="{css_class} geom-overlay" d="{d_str}" />'
            )

    def add_point(
        self,
        pt_id: str,
        x: float | int | sp.Expr,
        y: float | int | sp.Expr,
        *,
        label: str | None = None,
        dx: float = 0.0,
        dy: float = -10.0,
        anchor: str = "middle",
        radius: float = 3.4,
    ) -> None:
        """Add a point circle in ``#points`` and optional label in ``#labels``."""
        px, py = self.to_px(x, y)
        ref = escape(pt_id)
        self._points.append(
            f'    <circle id="el-pt-{ref}" data-ref="{ref}" data-type="point" '
            f'cx="{_fmt(px)}" cy="{_fmt(py)}" r="{_fmt(radius)}" class="geom-point" />'
        )
        lbl = pt_id if label is None else label
        if lbl:
            self._labels.append(
                f'    <text id="lbl-{ref}" data-ref="{ref}" x="{_fmt(px + dx)}" y="{_fmt(py + dy)}" '
                f'text-anchor="{anchor}" class="geom-label">{escape(lbl)}</text>'
            )

    def add_annotation(
        self,
        ann_id: str,
        x: float | int | sp.Expr,
        y: float | int | sp.Expr,
        text: str,
        *,
        anchor: str = "middle",
        data_ref: str = "",
    ) -> None:
        """Add a compact mathematical or woodcut caption inside ``#labels``."""
        px, py = self.to_px(x, y)
        ref_attr = f' data-ref="{escape(data_ref)}"' if data_ref else ""
        self._labels.append(
            f'    <text id="ann-{escape(ann_id)}"{ref_attr} x="{_fmt(px)}" y="{_fmt(py)}" '
            f'text-anchor="{anchor}" class="geom-label-sm">{escape(text)}</text>'
        )

    def render(self) -> str:
        """Serialize the complete 5-layer ``.euclid-graphic`` SVG XML string."""
        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}" class="euclid-graphic" '
            f'data-graphic-id="{escape(self.graphic_id)}" data-folio="{escape(self.folio)}" '
            f'data-graphic="g1" data-proposition="{escape(self.proposition)}">',
            _STYLE_AND_DEFS,
            '  <g id="elements">',
            *self._elements,
            "  </g>",
            '  <g id="graphics">',
            *self._graphics,
            "  </g>",
            '  <g id="highlights" style="pointer-events: none;">',
            *self._highlights,
            "  </g>",
            '  <g id="points">',
            *self._points,
            "  </g>",
            '  <g id="labels">',
            *self._labels,
            "  </g>",
            "</svg>",
            "",
        ]
        return "\n".join(lines)


def _svg_01_figurate_perfect() -> str:
    """Unit 1: Figurate polygonal numbers & Euclid IX.36 dyadic perfect-number lattice (fol. 8r)."""
    c = EuclidGraphicCanvas(
        width=460,
        height=230,
        graphic_id="summa.I.1.figurate",
        folio="fol. 8r",
        proposition="IX.36",
        scale=26.0,
        origin_x=42.0,
        origin_y=182.0,
    )
    # Left: Tetractys triangular number T_4 = 1 + 2 + 3 + 4 = 10
    tri_pts = [
        ("T1", 1.5, 4.2),
        ("T2", 1.0, 3.3),
        ("T3", 2.0, 3.3),
        ("T4", 0.5, 2.4),
        ("T5", 1.5, 2.4),
        ("T6", 2.5, 2.4),
        ("T7", 0.0, 1.5),
        ("T8", 1.0, 1.5),
        ("T9", 2.0, 1.5),
        ("T10", 3.0, 1.5),
    ]
    c.add_polygon("T4", [(0.0, 1.5), (3.0, 1.5), (1.5, 4.2)], data_ref="< A B C >")
    c.add_segment("AB", (0.0, 1.5), (3.0, 1.5), data_ref="/ A B /")
    c.add_segment("BC", (3.0, 1.5), (1.5, 4.2), data_ref="/ B C /")
    c.add_segment("CA", (1.5, 4.2), (0.0, 1.5), data_ref="/ C A /")
    for pid, x, y in tri_pts:
        c.add_point(pid, x, y, label="", radius=3.0)
    c.add_point("A", 0.0, 1.5, dx=-10, dy=6, anchor="end")
    c.add_point("B", 3.0, 1.5, dx=10, dy=6, anchor="start")
    c.add_point("C", 1.5, 4.2, dx=0, dy=-10)
    c.add_annotation("tri-cap", 1.5, 0.5, "Triangolare: 1+2+3+4 = 10")

    # Right: Euclid IX.36 dyadic gnomon rectangle 4 * 7 = 28 = 1 + 2 + 4 + 7 + 14
    x0, y0 = 6.2, 1.0
    w, h = 7.0, 4.0
    c.add_polygon("P28", [(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], data_ref="< D E F G >")
    # Dyadic subdivisions 1, 2, 4 along width 7
    c.add_polygon(
        "gnomon1",
        [(x0, y0), (x0 + 1.0, y0), (x0 + 1.0, y0 + h), (x0, y0 + h)],
        css_class="geom-polygon-gnomon",
        data_ref="< D H K G >",
    )
    for dx_cut in (1.0, 3.0):
        c.add_segment(f"cut-{int(dx_cut)}", (x0 + dx_cut, y0), (x0 + dx_cut, y0 + h), css_class="geom-dashed")
    c.add_segment("DE", (x0, y0), (x0 + w, y0), data_ref="/ D E /", css_class="geom-bold")
    c.add_segment("EF", (x0 + w, y0), (x0 + w, y0 + h), data_ref="/ E F /", css_class="geom-bold")
    c.add_segment("FG", (x0 + w, y0 + h), (x0, y0 + h), data_ref="/ F G /", css_class="geom-bold")
    c.add_segment("GD", (x0, y0 + h), (x0, y0), data_ref="/ G D /", css_class="geom-bold")
    c.add_point("D", x0, y0, dx=-9, dy=8, anchor="end")
    c.add_point("E", x0 + w, y0, dx=9, dy=8, anchor="start")
    c.add_point("F", x0 + w, y0 + h, dx=9, dy=-6, anchor="start")
    c.add_point("G", x0, y0 + h, dx=-9, dy=-6, anchor="end")
    c.add_annotation("p1", x0 + 0.5, y0 + 2.0, "1·4")
    c.add_annotation("p2", x0 + 2.0, y0 + 2.0, "2·4")
    c.add_annotation("p4", x0 + 5.0, y0 + 2.0, "4·4")
    c.add_annotation("perf-cap", x0 + 3.5, 0.2, "IX.36 Perfetto: (1+2+4)·4 = 7·4 = 28")
    return c.render()


def _svg_02_cossic_gnomon() -> str:
    """Unit 2: Pacioli's fol. 146r completion-of-the-square woodcut for 1.ce. + 10.co. = 39."""
    c = EuclidGraphicCanvas(
        width=360,
        height=300,
        graphic_id="summa.I.8.gnomon",
        folio="fol. 146r",
        proposition="II.4",
        scale=26.0,
        origin_x=76.0,
        origin_y=252.0,
    )
    # x = 3 (1.co.), p/2 = 5 => total side x + p/2 = 8, area = 39 + 25 = 64
    x_co = 3.0
    half_b = 5.0
    tot = x_co + half_b  # 8.0

    # Inner censo square A E F G (3 x 3 = 9)
    c.add_polygon("censo", [(0, 0), (x_co, 0), (x_co, x_co), (0, x_co)], data_ref="< A E F G >")
    # Two gnomon wings of 5.co. each: E B H F (5 x 3 = 15) and G F I D (3 x 5 = 15)
    c.add_polygon(
        "wing1",
        [(x_co, 0), (tot, 0), (tot, x_co), (x_co, x_co)],
        css_class="geom-polygon-gnomon",
        data_ref="< E B H F >",
    )
    c.add_polygon(
        "wing2",
        [(0, x_co), (x_co, x_co), (x_co, tot), (0, tot)],
        css_class="geom-polygon-gnomon",
        data_ref="< G F I D >",
    )
    # Completed square supplement F H C I (5 x 5 = 25)
    c.add_polygon("supp", [(x_co, x_co), (tot, x_co), (tot, tot), (x_co, tot)], data_ref="< F H C I >")

    c.add_segment("AB", (0, 0), (tot, 0), data_ref="/ A B /", css_class="geom-bold")
    c.add_segment("BC", (tot, 0), (tot, tot), data_ref="/ B C /", css_class="geom-bold")
    c.add_segment("CD", (tot, tot), (0, tot), data_ref="/ C D /", css_class="geom-bold")
    c.add_segment("DA", (0, tot), (0, 0), data_ref="/ D A /", css_class="geom-bold")
    c.add_segment("EI", (x_co, 0), (x_co, tot), data_ref="/ E I /")
    c.add_segment("GH", (0, x_co), (tot, x_co), data_ref="/ G H /")
    c.add_segment("AC", (0, 0), (tot, tot), data_ref="/ A C /", css_class="geom-dashed")

    c.add_point("A", 0, 0, dx=-10, dy=12, anchor="end")
    c.add_point("E", x_co, 0, dx=0, dy=15)
    c.add_point("B", tot, 0, dx=10, dy=12, anchor="start")
    c.add_point("G", 0, x_co, dx=-10, dy=4, anchor="end")
    c.add_point("F", x_co, x_co, dx=-8, dy=-6, anchor="end")
    c.add_point("H", tot, x_co, dx=10, dy=4, anchor="start")
    c.add_point("D", 0, tot, dx=-10, dy=-6, anchor="end")
    c.add_point("I", x_co, tot, dx=0, dy=-8)
    c.add_point("C", tot, tot, dx=10, dy=-6, anchor="start")

    c.add_annotation("ce-lbl", 1.5, 1.3, "1.ce. = 9")
    c.add_annotation("co1-lbl", 5.5, 1.3, "5.co. = 15")
    c.add_annotation("co2-lbl", 1.5, 5.4, "5.co. = 15")
    c.add_annotation("sq-lbl", 5.5, 5.4, "(5)² = 25")
    c.add_annotation("bot-lbl", 4.0, -0.95, "1.ce. p̄ 10.co. = 39  ⇒  (x + 5)² = 64  ⇒  x = 3")
    return c.render()


def _svg_03_book_x_binomial_apotome() -> str:
    """Unit 2: Euclid Book X binomial (a + sqrt(b)) & apotome/residuo (a - sqrt(b)) dissection."""
    c = EuclidGraphicCanvas(
        width=440,
        height=245,
        graphic_id="summa.I.8.surds",
        folio="fol. 118r",
        proposition="X.36",
        scale=28.0,
        origin_x=40.0,
        origin_y=198.0,
    )
    a_len = 3.0
    rt_b = float(sp.sqrt(5).evalf())  # ~2.236: Binomial 3 + sqrt(5), Residuo 3 - sqrt(5)
    tot = a_len + rt_b
    diff = a_len - rt_b

    # Left: Binomial segment A M B (AM = 3, MB = sqrt(5)) and square on AB = 14 + 6*sqrt(5)
    c.add_polygon("bin-a2", [(0, 0), (a_len, 0), (a_len, a_len), (0, a_len)], data_ref="< A M P Q >")
    c.add_polygon(
        "bin-ab1",
        [(a_len, 0), (tot, 0), (tot, a_len), (a_len, a_len)],
        css_class="geom-polygon-gnomon",
        data_ref="< M B R P >",
    )
    c.add_polygon(
        "bin-ab2",
        [(0, a_len), (a_len, a_len), (a_len, tot), (0, tot)],
        css_class="geom-polygon-gnomon",
    )
    c.add_polygon("bin-b", [(a_len, a_len), (tot, a_len), (tot, tot), (a_len, tot)])
    c.add_segment("AB", (0, 0), (tot, 0), data_ref="/ A B /", css_class="geom-bold")
    c.add_segment("BC", (tot, 0), (tot, tot), css_class="geom-line")
    c.add_segment("CD", (tot, tot), (0, tot), css_class="geom-line")
    c.add_segment("DA", (0, tot), (0, 0), css_class="geom-line")
    c.add_segment("MP", (a_len, 0), (a_len, tot), data_ref="/ M P /")
    c.add_segment("QR", (0, a_len), (tot, a_len), data_ref="/ Q R /")
    c.add_point("A", 0, 0, dx=-8, dy=12, anchor="end")
    c.add_point("M", a_len, 0, dx=0, dy=14)
    c.add_point("B", tot, 0, dx=8, dy=12, anchor="start")
    c.add_annotation("bin-1", 1.5, 1.4, "a² = 9")
    c.add_annotation("bin-2", a_len + rt_b / 2, 1.4, "3·℞.5")
    c.add_annotation("bin-3", a_len + rt_b / 2, a_len + rt_b / 2, "b = 5")
    c.add_annotation("bin-cap", tot / 2, -0.95, "Binomio: 3 p̄ ℞.5")

    # Right: Apotome / Residuo segment E N F where EF = 3, NF = sqrt(5), EN = 3 - sqrt(5)
    ox = 7.6
    c.add_polygon("apo-tot", [(ox, 0), (ox + a_len, 0), (ox + a_len, a_len), (ox, a_len)], data_ref="< E F G H >")
    c.add_polygon(
        "apo-res",
        [(ox, 0), (ox + diff, 0), (ox + diff, diff), (ox, diff)],
        css_class="geom-polygon-gnomon",
        data_ref="< E N K L >",
    )
    c.add_segment("EF", (ox, 0), (ox + a_len, 0), data_ref="/ E F /", css_class="geom-bold")
    c.add_segment("FG", (ox + a_len, 0), (ox + a_len, a_len), css_class="geom-line")
    c.add_segment("GH", (ox + a_len, a_len), (ox, a_len), css_class="geom-line")
    c.add_segment("HE", (ox, a_len), (ox, 0), css_class="geom-line")
    c.add_segment("NS", (ox + diff, 0), (ox + diff, a_len), data_ref="/ N S /", css_class="geom-dashed")
    c.add_segment("LT", (ox, diff), (ox + a_len, diff), data_ref="/ L T /", css_class="geom-dashed")
    c.add_point("E", ox, 0, dx=-8, dy=12, anchor="end")
    c.add_point("N", ox + diff, 0, dx=0, dy=14)
    c.add_point("F", ox + a_len, 0, dx=8, dy=12, anchor="start")
    c.add_annotation("apo-1", ox + 1.9, 1.9, "℞.5 · ℞.5 = 5")
    c.add_annotation("apo-cap", ox + a_len / 2, -0.95, "Residuo: 3 m̄ ℞.5")
    return c.render()


def _svg_04_three_means_semicircle() -> str:
    """Unit 3: Exact semicircle construction of Arithmetic A, Geometric G, and Harmonic H means."""
    res = construct_three_means(9, 4)
    pt_a = res.model.get_element_by_ID("A")
    pt_p = res.model.get_element_by_ID("P")
    pt_b = res.model.get_element_by_ID("B")
    pt_m = res.model.get_element_by_ID("M")
    pt_q = res.model.get_element_by_ID("Q")
    pt_n = res.model.get_element_by_ID("N")

    c = EuclidGraphicCanvas(
        width=440,
        height=255,
        graphic_id="summa.I.6.means",
        folio="fol. 73v",
        proposition="VI.13",
        scale=26.0,
        origin_x=50.0,
        origin_y=205.0,
    )
    c.add_arc("semi", pt_m.x, pt_m.y, sp.Rational(13, 2), 0.0, 180.0, data_ref="( M B )", css_class="geom-circle")
    c.add_polygon("MPQ", [(pt_m.x, pt_m.y), (pt_p.x, pt_p.y), (pt_q.x, pt_q.y)], data_ref="< M P Q >")
    c.add_polygon(
        "PQN",
        [(pt_p.x, pt_p.y), (pt_q.x, pt_q.y), (pt_n.x, pt_n.y)],
        css_class="geom-polygon-gnomon",
        data_ref="< P Q N >",
    )

    c.add_segment("AB", (pt_a.x, pt_a.y), (pt_b.x, pt_b.y), data_ref="/ A B /", css_class="geom-bold")
    c.add_segment("MQ", (pt_m.x, pt_m.y), (pt_q.x, pt_q.y), data_ref="/ M Q /", css_class="geom-line")
    c.add_segment("PQ", (pt_p.x, pt_p.y), (pt_q.x, pt_q.y), data_ref="/ P Q /", css_class="geom-bold")
    c.add_segment("PN", (pt_p.x, pt_p.y), (pt_n.x, pt_n.y), data_ref="/ P N /", css_class="geom-dashed")
    c.add_segment("QN", (pt_q.x, pt_q.y), (pt_n.x, pt_n.y), data_ref="/ Q N /", css_class="geom-bold")
    c.add_segment("AQ", (pt_a.x, pt_a.y), (pt_q.x, pt_q.y), data_ref="/ A Q /", css_class="geom-dashed")
    c.add_segment("BQ", (pt_b.x, pt_b.y), (pt_q.x, pt_q.y), data_ref="/ B Q /", css_class="geom-dashed")

    c.add_point("A", pt_a.x, pt_a.y, dx=-9, dy=12, anchor="end")
    c.add_point("M", pt_m.x, pt_m.y, dx=0, dy=15)
    c.add_point("P", pt_p.x, pt_p.y, dx=0, dy=15)
    c.add_point("B", pt_b.x, pt_b.y, dx=9, dy=12, anchor="start")
    c.add_point("Q", pt_q.x, pt_q.y, dx=6, dy=-9, anchor="start")
    c.add_point("N", pt_n.x, pt_n.y, dx=-10, dy=-4, anchor="end")

    c.add_annotation("lbl-A", 4.5, -0.95, "AP = 9, PB = 4  |  A = MQ = 6½,  G = PQ = 6,  H = QN = 5 7/13", anchor="start")
    return c.render()


def _svg_05_extreme_mean_10() -> str:
    """Unit 3: Euclidean II.11 / VI.30 division of AB = 10 into sqrt(125)-5 and 15-sqrt(125)."""
    res = construct_extreme_and_mean_ratio(10)
    m = res.model
    pt_a = m.get_element_by_ID("A")
    pt_b = m.get_element_by_ID("B")
    pt_d = m.get_element_by_ID("D")
    pt_e = m.get_element_by_ID("E")
    pt_f = m.get_element_by_ID("F")
    pt_c = m.get_element_by_ID("C")

    c = EuclidGraphicCanvas(
        width=420,
        height=340,
        graphic_id="summa.I.6.divina10",
        folio="fol. 78r",
        proposition="II.11",
        scale=16.5,
        origin_x=135.0,
        origin_y=195.0,
    )
    # Square on AB = 10: A(0,0), B(10,0), K(10,10), D(0,10)
    c.add_polygon("sqAB", [(0, 0), (10, 0), (10, 10), (0, 10)], data_ref="< A B K D >")
    # Rectangle on AF = AC = sqrt(125)-5: F(0, -ac), H(-ac, -ac), G(-ac, 0), A(0,0)
    ac = res.major_part
    c.add_polygon(
        "sqAC",
        [(0, 0), (ac, 0), (ac, -ac), (0, -ac)],
        css_class="geom-polygon-gnomon",
        data_ref="< A C H F >",
    )

    r_eb = sp.sqrt(125)
    c.add_arc("cEB", pt_e.x, pt_e.y, r_eb, 265.0, 340.0, data_ref="( E B )", css_class="geom-dashed")
    c.add_arc("cAF", pt_a.x, pt_a.y, ac, 270.0, 360.0, data_ref="( A F )", css_class="geom-arc")

    c.add_segment("AB", (pt_a.x, pt_a.y), (pt_b.x, pt_b.y), data_ref="/ A B /", css_class="geom-bold")
    c.add_segment("AC", (pt_a.x, pt_a.y), (pt_c.x, pt_c.y), data_ref="/ A C /", css_class="geom-bold")
    c.add_segment("CB", (pt_c.x, pt_c.y), (pt_b.x, pt_b.y), data_ref="/ C B /", css_class="geom-line")
    c.add_segment("DF", (pt_d.x, pt_d.y), (pt_f.x, pt_f.y), data_ref="/ D F /", css_class="geom-line")
    c.add_segment("BK", (10, 0), (10, 10), css_class="geom-line")
    c.add_segment("KD", (10, 10), (0, 10), css_class="geom-line")
    c.add_segment("EB", (pt_e.x, pt_e.y), (pt_b.x, pt_b.y), data_ref="/ E B /", css_class="geom-dashed")
    c.add_segment("CH", (ac, 0), (ac, -ac), css_class="geom-line")
    c.add_segment("HF", (ac, -ac), (0, -ac), css_class="geom-line")

    c.add_point("A", pt_a.x, pt_a.y, dx=-10, dy=-5, anchor="end")
    c.add_point("B", pt_b.x, pt_b.y, dx=10, dy=5, anchor="start")
    c.add_point("C", pt_c.x, pt_c.y, dx=4, dy=15, anchor="start")
    c.add_point("D", pt_d.x, pt_d.y, dx=-10, dy=4, anchor="end")
    c.add_point("E", pt_e.x, pt_e.y, dx=-10, dy=4, anchor="end")
    c.add_point("F", pt_f.x, pt_f.y, dx=-10, dy=5, anchor="end")

    c.add_annotation("eb-lbl", 5.3, 3.3, "EB = ℞.125")
    c.add_annotation("ac-lbl", 3.1, -3.1, "AC²")
    c.add_annotation("cap-10", 3.5, -7.6, "AB = 10  ⇒  AC = ℞.125 m̄ 5,  CB = 15 m̄ ℞.125")
    return c.render()


def _svg_06_quaderno_conservation() -> str:
    """Unit 4: Skew-symmetric directed conservation network of Pacioli's Venetian Quaderno."""
    c = EuclidGraphicCanvas(
        width=440,
        height=290,
        graphic_id="summa.I.9.quaderno",
        folio="fol. 202r",
        proposition="Summa.I.IX.14",
        scale=25.0,
        origin_x=220.0,
        origin_y=145.0,
    )
    r = 4.2
    c.add_circle("ring", 0.0, 0.0, r, data_ref="( O K )", css_class="geom-dashed")
    # Symmetry axis separating Dare (left, man sinistra) and Avere (right, man dextra)
    c.add_segment("axis", (0.0, -5.0), (0.0, 5.0), css_class="geom-dashed")

    nodes: list[tuple[str, str, float, str, float, float]] = [
        ("K", "K (Cavedal)", 90.0, "middle", 0.0, -10.0),
        ("S", "S (Cassa)", 150.0, "end", -10.0, 4.0),
        ("M", "M (Zenzer)", 210.0, "end", -10.0, 6.0),
        ("B", "B (Bilancio)", 270.0, "middle", 0.0, 16.0),
        ("P", "P (Pro e Danno)", 330.0, "start", 10.0, 6.0),
        ("D", "D (Martino)", 30.0, "start", 10.0, 4.0),
    ]
    coords: dict[str, tuple[float, float]] = {}
    for nid, _lbl, deg, _anc, _dx, _dy in nodes:
        rad = math.radians(deg)
        coords[nid] = (r * math.cos(rad), r * math.sin(rad))

    c.add_polygon(
        "cycle",
        [coords["K"], coords["S"], coords["M"], coords["D"], coords["P"]],
        data_ref="< K S M D P >",
    )

    chords = [
        ("KS", "K", "S", "/ K S /", "geom-bold"),
        ("SM", "S", "M", "/ S M /", "geom-line"),
        ("MD", "M", "D", "/ M D /", "geom-line"),
        ("DP", "D", "P", "/ D P /", "geom-line"),
        ("DS", "D", "S", "/ D S /", "geom-bold"),
        ("PK", "P", "K", "/ P K /", "geom-bold"),
        ("SB", "S", "B", "/ S B /", "geom-dashed"),
        ("KB", "K", "B", "/ K B /", "geom-dashed"),
    ]
    for eid, u, v, ref, cls in chords:
        c.add_segment(eid, coords[u], coords[v], data_ref=ref, css_class=cls)

    for nid, lbl, _deg, anc, dx, dy in nodes:
        x, y = coords[nid]
        c.add_point(nid, x, y, label=lbl, dx=dx, dy=dy, anchor=anc)

    c.add_annotation("dare-hdr", -4.8, 4.8, "DARE (Per · Sinistra)", anchor="start")
    c.add_annotation("avere-hdr", 4.8, 4.8, "AVERE (A · Dextra)", anchor="end")
    c.add_annotation("law", 0.0, -5.3, "1ᵀ · B = 0ᵀ  ⇔  Σ Dare = Σ Avere")
    return c.render()


def _svg_07_heron_13_14_15() -> str:
    """Unit 5: Exact Part II, fol. 9v Heron (13, 14, 15) triangle, cathetus AD=12, incircle r=4."""
    res = construct_heron_13_14_15()
    c = EuclidGraphicCanvas(
        width=420,
        height=295,
        graphic_id="summa.II.1.heron",
        folio="Part II, fol. 9v",
        proposition="Summa.II.I.8",
        scale=19.5,
        origin_x=72.0,
        origin_y=252.0,
    )
    g_pt = (res.pt_g.x, res.pt_g.y)
    b_pt = (res.pt_b.x, res.pt_b.y)
    a_pt = (res.pt_a.x, res.pt_a.y)
    d_pt = (res.pt_d.x, res.pt_d.y)
    i_pt = (res.incenter.x, res.incenter.y)
    t_pt = (res.incenter.x, sp.Integer(0))

    c.add_polygon("GBA", [g_pt, b_pt, a_pt], data_ref="< G B A >")
    c.add_polygon("GDA", [g_pt, d_pt, a_pt], css_class="geom-polygon-gnomon", data_ref="< G D A >")
    c.add_circle("incircle", i_pt[0], i_pt[1], res.inradius, data_ref="( I T )", css_class="geom-circle")

    c.add_segment("GB", g_pt, b_pt, data_ref="/ G B /", css_class="geom-bold")
    c.add_segment("GA", g_pt, a_pt, data_ref="/ G A /", css_class="geom-bold")
    c.add_segment("BA", b_pt, a_pt, data_ref="/ B A /", css_class="geom-bold")
    c.add_segment("AD", a_pt, d_pt, data_ref="/ A D /", css_class="geom-dashed")
    c.add_segment("IT", i_pt, t_pt, data_ref="/ I T /", css_class="geom-line")
    c.add_segment("GD", g_pt, d_pt, data_ref="/ G D /", css_class="geom-line")
    c.add_segment("DB", d_pt, b_pt, data_ref="/ D B /", css_class="geom-line")

    c.add_point("G", g_pt[0], g_pt[1], dx=-10, dy=12, anchor="end")
    c.add_point("D", d_pt[0], d_pt[1], dx=0, dy=15)
    c.add_point("T", t_pt[0], t_pt[1], dx=0, dy=15)
    c.add_point("B", b_pt[0], b_pt[1], dx=10, dy=12, anchor="start")
    c.add_point("A", a_pt[0], a_pt[1], dx=0, dy=-10)
    c.add_point("I", i_pt[0], i_pt[1], dx=10, dy=-4, anchor="start")

    c.add_annotation("lbl-13", 1.5, 6.6, "AG = 13")
    c.add_annotation("lbl-15", 10.6, 6.6, "AB = 15")
    c.add_annotation("lbl-12", 4.1, 6.2, "AD = 12", anchor="end")
    c.add_annotation("lbl-r4", 7.6, 2.0, "r = 4", anchor="start")
    c.add_annotation("heron-eq", 7.0, -1.55, "s = 21  |  ℞(6 · 7 · 8 · 21) = ℞.7056 = 84 braccia²")
    return c.render()


def _svg_08_divisione_superficierum() -> str:
    """Unit 5: Part II, Dist. IV De divisione superficierum parallel area bisection via VI.13/VI.19."""
    res = construct_triangle_division_parallel(1, 1)
    m = res.model
    pt_g = m.get_element_by_ID("G")
    pt_b = m.get_element_by_ID("B")
    pt_a = m.get_element_by_ID("A")
    pt_m = m.get_element_by_ID("M")
    pt_s = m.get_element_by_ID("S")
    pt_u, pt_v = res.cut_points

    c = EuclidGraphicCanvas(
        width=420,
        height=300,
        graphic_id="summa.II.4.divisione",
        folio="Part II, fol. 35r",
        proposition="VI.19",
        scale=19.0,
        origin_x=76.0,
        origin_y=248.0,
    )
    c.add_polygon("GBA", [(pt_g.x, pt_g.y), (pt_b.x, pt_b.y), (pt_a.x, pt_a.y)], data_ref="< G B A >")
    c.add_polygon(
        "GUV",
        [(pt_g.x, pt_g.y), (pt_u.x, pt_u.y), (pt_v.x, pt_v.y)],
        css_class="geom-polygon-gnomon",
        data_ref="< G U V >",
    )

    c.add_arc("semiGB", pt_m.x, pt_m.y, 7, 0.0, 180.0, data_ref="( M B )", css_class="geom-dashed")
    c.add_arc("arcGS", pt_g.x, pt_g.y, sp.sqrt(98), 0.0, 45.0, data_ref="( G S )", css_class="geom-arc")

    c.add_segment("GB", (pt_g.x, pt_g.y), (pt_b.x, pt_b.y), data_ref="/ G B /", css_class="geom-bold")
    c.add_segment("GA", (pt_g.x, pt_g.y), (pt_a.x, pt_a.y), data_ref="/ G A /", css_class="geom-bold")
    c.add_segment("BA", (pt_b.x, pt_b.y), (pt_a.x, pt_a.y), data_ref="/ B A /", css_class="geom-bold")
    c.add_segment("UV", (pt_u.x, pt_u.y), (pt_v.x, pt_v.y), data_ref="/ U V /", css_class="geom-bold")
    c.add_segment("MS", (pt_m.x, pt_m.y), (pt_s.x, pt_s.y), data_ref="/ M S /", css_class="geom-dashed")
    c.add_segment("GS", (pt_g.x, pt_g.y), (pt_s.x, pt_s.y), data_ref="/ G S /", css_class="geom-dashed")

    c.add_point("G", pt_g.x, pt_g.y, dx=-10, dy=12, anchor="end")
    c.add_point("M", pt_m.x, pt_m.y, dx=0, dy=15)
    c.add_point("U", pt_u.x, pt_u.y, dx=0, dy=15)
    c.add_point("B", pt_b.x, pt_b.y, dx=10, dy=12, anchor="start")
    c.add_point("A", pt_a.x, pt_a.y, dx=0, dy=-10)
    c.add_point("V", pt_v.x, pt_v.y, dx=-10, dy=-4, anchor="end")
    c.add_point("S", pt_s.x, pt_s.y, dx=8, dy=-6, anchor="start")

    c.add_annotation("div-lbl", 7.0, -1.65, "GU = GS = ℞(14·7) = ℞.98  ⇒  Area(GUV) = Area(UBAV) = 42")
    return c.render()


def _svg_09_inscribed_polyhedra() -> str:
    """Unit 5: Part II, fols. 69v–70r Sphere of diameter 6 with Cuboctahedron & Golden Rectangle."""
    c = EuclidGraphicCanvas(
        width=420,
        height=305,
        graphic_id="summa.II.8.corporibus",
        folio="Part II, fol. 69v",
        proposition="XIII.17",
        scale=36.0,
        origin_x=210.0,
        origin_y=150.0,
    )
    r_sph = sp.Integer(3)  # Sphere diameter D = 6 => R = 3
    c.add_circle("sphere", 0, 0, r_sph, data_ref="( O P )", css_class="geom-circle")

    # Great-circle hexagon of cuboctahedron of exact edge e = R = 3 (Part II, fol. 69v, prob. 17)
    hex_pts: list[tuple[sp.Expr, sp.Expr]] = [
        (sp.Integer(3), sp.Integer(0)),
        (sp.Rational(3, 2), sp.Rational(3, 2) * sp.sqrt(3)),
        (sp.Rational(-3, 2), sp.Rational(3, 2) * sp.sqrt(3)),
        (sp.Integer(-3), sp.Integer(0)),
        (sp.Rational(-3, 2), sp.Rational(-3, 2) * sp.sqrt(3)),
        (sp.Rational(3, 2), sp.Rational(-3, 2) * sp.sqrt(3)),
    ]
    c.add_polygon("cuboct", hex_pts, data_ref="< P Q R S T U >")
    names = ["P", "Q", "R", "S", "T", "U"]
    for idx in range(6):
        u_name = names[idx]
        v_name = names[(idx + 1) % 6]
        c.add_segment(
            f"{u_name}{v_name}",
            hex_pts[idx],
            hex_pts[(idx + 1) % 6],
            data_ref=f"/ {u_name} {v_name} /",
            css_class="geom-line",
        )
    # Internal triangular/square equatorial net of cuboctahedron
    c.add_segment("PS", hex_pts[0], hex_pts[3], data_ref="/ P S /", css_class="geom-dashed")
    c.add_segment("QT", hex_pts[1], hex_pts[4], data_ref="/ Q T /", css_class="geom-dashed")
    c.add_segment("RU", hex_pts[2], hex_pts[5], data_ref="/ R U /", css_class="geom-dashed")

    # Golden rectangle inscribed in the same sphere R = 3 (icosahedron skeleton):
    # half-sides a = 3 / sqrt(1 + phi^2) = 3 * sqrt((5 - sqrt(5))/10), b = phi * a
    phi = (sp.Integer(1) + sp.sqrt(5)) / 2
    a_half = sp.Integer(3) / sp.sqrt(1 + phi**2)
    b_half = sp.simplify(phi * a_half)
    g_rect = [
        (b_half, a_half),
        (-b_half, a_half),
        (-b_half, -a_half),
        (b_half, -a_half),
    ]
    c.add_polygon("golden-rect", g_rect, css_class="geom-polygon-gnomon", data_ref="< W X Y Z >")
    c.add_segment("WX", g_rect[0], g_rect[1], data_ref="/ W X /", css_class="geom-bold")
    c.add_segment("XY", g_rect[1], g_rect[2], data_ref="/ X Y /", css_class="geom-bold")
    c.add_segment("YZ", g_rect[2], g_rect[3], data_ref="/ Y Z /", css_class="geom-bold")
    c.add_segment("ZW", g_rect[3], g_rect[0], data_ref="/ Z W /", css_class="geom-bold")

    c.add_point("O", 0, 0, dx=8, dy=-6, anchor="start")
    offsets = [
        (11, 4, "start"),
        (8, -8, "start"),
        (-8, -8, "end"),
        (-11, 4, "end"),
        (-8, 14, "end"),
        (8, 14, "start"),
    ]
    for name, pt, (dx, dy, anc) in zip(names, hex_pts, offsets, strict=True):
        c.add_point(name, pt[0], pt[1], dx=dx, dy=dy, anchor=anc)
    for name, pt, (dx, dy, anc) in zip(
        ["W", "X", "Y", "Z"],
        g_rect,
        [(9, -5, "start"), (-9, -5, "end"), (-9, 13, "end"), (9, 13, "start")],
        strict=True,
    ):
        c.add_point(name, pt[0], pt[1], dx=dx, dy=dy, anchor=anc)

    c.add_annotation("sph-cap", 0.0, -3.75, "Spera D = 6 (R = 3)  |  Cuboctaedro lato = 3  |  Rettangolo aureo WXYZ")
    return c.render()


def generate_all_summa_svgs(summa_docsrc_dir: Path | str) -> list[SVGSpec]:
    """Generate and write all nine ``.euclid-graphic`` SVGs into ``docsrc/summa_1494/``.

    Args:
        summa_docsrc_dir: Target root directory (typically ``<repo>/docsrc/summa_1494``).

    Returns:
        Ordered list of :class:`SVGSpec` records written to disk.
    """
    base = Path(summa_docsrc_dir)
    manifest = [
        (
            "summa.I.1.figurate",
            "unit_01_dedication_arithmetica",
            "fig_01_figurate_perfect.svg",
            "fol. 8r",
            "IX.36",
            _svg_01_figurate_perfect,
        ),
        (
            "summa.I.8.gnomon",
            "unit_02_algebra_cosa",
            "fig_02_cossic_gnomon.svg",
            "fol. 146r",
            "II.4",
            _svg_02_cossic_gnomon,
        ),
        (
            "summa.I.8.surds",
            "unit_02_algebra_cosa",
            "fig_03_book_x_binomial_apotome.svg",
            "fol. 118r",
            "X.36",
            _svg_03_book_x_binomial_apotome,
        ),
        (
            "summa.I.6.means",
            "unit_03_proportioni",
            "fig_04_three_means_semicircle.svg",
            "fol. 73v",
            "VI.13",
            _svg_04_three_means_semicircle,
        ),
        (
            "summa.I.6.divina10",
            "unit_03_proportioni",
            "fig_05_extreme_mean_10.svg",
            "fol. 78r",
            "II.11",
            _svg_05_extreme_mean_10,
        ),
        (
            "summa.I.9.quaderno",
            "unit_04_computis_quaderno",
            "fig_06_quaderno_conservation.svg",
            "fol. 202r",
            "Summa.I.IX.14",
            _svg_06_quaderno_conservation,
        ),
        (
            "summa.II.1.heron",
            "unit_05_tractatus_geometriae",
            "fig_07_heron_13_14_15.svg",
            "Part II, fol. 9v",
            "Summa.II.I.8",
            _svg_07_heron_13_14_15,
        ),
        (
            "summa.II.4.divisione",
            "unit_05_tractatus_geometriae",
            "fig_08_divisione_superficierum.svg",
            "Part II, fol. 35r",
            "VI.19",
            _svg_08_divisione_superficierum,
        ),
        (
            "summa.II.8.corporibus",
            "unit_05_tractatus_geometriae",
            "fig_09_inscribed_polyhedra.svg",
            "Part II, fol. 69v",
            "XIII.17",
            _svg_09_inscribed_polyhedra,
        ),
    ]

    results: list[SVGSpec] = []
    for gid, unit_dir, fname, folio, prop, builder in manifest:
        out_dir = base / unit_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / fname
        out_path.write_text(builder(), encoding="utf-8")
        results.append(
            SVGSpec(
                graphic_id=gid,
                unit_dir=unit_dir,
                filename=fname,
                folio=folio,
                proposition=prop,
                path=out_path,
            )
        )
    return results
