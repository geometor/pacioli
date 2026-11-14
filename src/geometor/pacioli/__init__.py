"""Symbolic modeling, digital codex tools, and conservation algebra for Fra Luca Pacioli.

Provides tools and exact ``SymPy`` / ``geometor.model`` modules spanning both of
Fra Luca Pacioli's Venetian folio masterpieces printed by Paganino de' Paganini:

- **Summa de arithmetica, geometria, proportioni et proportionalita (Venice, 1494)**:

  - :mod:`geometor.pacioli.proportions`: Boethian ratio taxonomy, Euclidean *modi arguendi*,
    semicircle construction of the three classical means, golden section of ``10``, and
    Pacioli's six canonical Cossic quadratic equations.
  - :mod:`geometor.pacioli.tractatus_geometriae`: Heron's ``(13, 14, 15)`` triangle
    construction, *De divisione superficierum* proportional cuts, and inscribed Platonic
    and Archimedean solids in the sphere of diameter ``6``.
  - :mod:`geometor.pacioli.ledger_conservation`: Venetian ``l. s. g. p.`` money of account,
    skew-symmetric conservation algebra of the *Quaderno*, and the *Problem of Points*.
  - :mod:`geometor.pacioli.svg_woodcut`: Deterministic ``.euclid-graphic`` SVG generator.

- **De Divina Proportione (Venice, 1509 / Vienna, 1889)**:

  - :class:`PacioliParser`, folio extraction, and woodcut graphic calibration utilities.
"""

from __future__ import annotations

from .extraction import extract_all
from .graphics import (
    build_graphics_index,
    clean_image,
    detect_graphics_cv,
    detect_initials,
    detect_margin_figures,
    extract_from_json,
)
from .ledger_conservation import (
    AccountSummary,
    JournalEntry,
    ProblemOfPointsResult,
    QuadernoLedger,
    TrialBalanceReport,
    VenetianAmount,
    build_venetian_merchant_quaderno_1493,
    compare_problem_of_points,
)
from .parser import PacioliParser
from .proportions import (
    BoethianClassification,
    CossicQuadraticResult,
    ExtremeMeanResult,
    SixModesResult,
    ThreeMeansResult,
    apply_six_euclidean_modes,
    classify_boethian_ratio,
    compound_ratios,
    construct_extreme_and_mean_ratio,
    construct_three_means,
    solve_cossic_quadratic,
)
from .svg_woodcut import (
    EuclidGraphicCanvas,
    SVGSpec,
    generate_all_summa_svgs,
)
from .tractatus_geometriae import (
    DodecahedronAxis48Result,
    HeronTriangleResult,
    InscribedPolyhedronSpec,
    TriangleDivisionResult,
    construct_heron_13_14_15,
    construct_triangle_division_cevian,
    construct_triangle_division_parallel,
    dodecahedron_in_sphere_sqrt48,
    inscribed_polyhedra_sphere_table,
)

__all__ = [
    "AccountSummary",
    "BoethianClassification",
    "CossicQuadraticResult",
    "DodecahedronAxis48Result",
    "EuclidGraphicCanvas",
    "ExtremeMeanResult",
    "HeronTriangleResult",
    "InscribedPolyhedronSpec",
    "JournalEntry",
    "PacioliParser",
    "ProblemOfPointsResult",
    "QuadernoLedger",
    "SVGSpec",
    "SixModesResult",
    "ThreeMeansResult",
    "TrialBalanceReport",
    "TriangleDivisionResult",
    "VenetianAmount",
    "apply_six_euclidean_modes",
    "build_graphics_index",
    "build_venetian_merchant_quaderno_1493",
    "classify_boethian_ratio",
    "clean_image",
    "compare_problem_of_points",
    "compound_ratios",
    "construct_extreme_and_mean_ratio",
    "construct_heron_13_14_15",
    "construct_three_means",
    "construct_triangle_division_cevian",
    "construct_triangle_division_parallel",
    "detect_graphics_cv",
    "detect_initials",
    "detect_margin_figures",
    "dodecahedron_in_sphere_sqrt48",
    "extract_all",
    "extract_from_json",
    "generate_all_summa_svgs",
    "inscribed_polyhedra_sphere_table",
    "solve_cossic_quadratic",
]
__version__ = "0.4.3"
