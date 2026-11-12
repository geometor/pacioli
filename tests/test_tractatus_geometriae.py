"""Exact symbolic unit tests for :mod:`geometor.pacioli.tractatus_geometriae`."""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, zero_test

from geometor.pacioli.tractatus_geometriae import (
    construct_heron_13_14_15,
    construct_triangle_division_cevian,
    construct_triangle_division_parallel,
    dodecahedron_in_sphere_sqrt48,
    inscribed_polyhedra_sphere_table,
)


def _assert_zero_floats_in_model(model: Model) -> None:
    """Assert that no geometric entity in ``model`` contains any ``sp.Float`` atom."""
    for elem in model:
        assert not elem.has(sp.Float), f"Found floating-point contamination in {elem!r}"
        if isinstance(elem, spg.Point2D):
            assert not elem.x.has(sp.Float)
            assert not elem.y.has(sp.Float)


def test_construct_heron_13_14_15_fol_9v() -> None:
    """Verify Pacioli's (13, 14, 15) triangle construction and invariants on Part II, fol. 9v."""
    res = construct_heron_13_14_15()
    _assert_zero_floats_in_model(res.model)

    assert res.pt_a == spg.Point2D(5, 12)
    assert res.pt_d == spg.Point2D(5, 0)
    assert res.incenter == spg.Point2D(6, 4)
    assert res.circumcenter == spg.Point2D(7, sp.Rational(33, 8))

    assert res.perimeter == sp.Integer(42)
    assert res.semiperimeter == sp.Integer(21)
    assert res.excesses == (sp.Integer(6), sp.Integer(7), sp.Integer(8))
    assert res.heron_radicand == sp.Integer(7056)
    assert res.area == sp.Integer(84)
    assert res.altitude == sp.Integer(12)
    assert res.base_segments == (sp.Integer(5), sp.Integer(9))
    assert res.inradius == sp.Integer(4)
    assert res.circumradius == sp.Rational(65, 8)
    assert len(res.model.steps) >= 5


def test_triangle_division_cevian_and_parallel() -> None:
    """Verify *De divisione superficierum* (Part II, Dist. IV) cevian and parallel cuts."""
    cev = construct_triangle_division_cevian(1, 2)
    _assert_zero_floats_in_model(cev.model)
    assert cev.total_area == sp.Integer(84)
    assert cev.part_1_area == sp.Integer(28)
    assert cev.part_2_area == sp.Integer(56)
    assert cev.cut_points[0] == spg.Point2D(sp.Rational(14, 3), 0)

    par = construct_triangle_division_parallel(1, 1)
    _assert_zero_floats_in_model(par.model)
    assert par.total_area == sp.Integer(84)
    assert zero_test(par.part_1_area - 42)
    assert zero_test(par.part_2_area - 42)
    pt_u, pt_v = par.cut_points
    assert zero_test(pt_u.x - 7 * sp.sqrt(2))
    assert pt_u.y == 0
    # Verify UV / GB = 1 / sqrt(2) => Q(G, U) / Q(G, B) = 1 / 2
    assert zero_test(quadrance(spg.Point2D(0, 0), pt_u) - sp.Rational(1, 2) * 196)
    assert zero_test(quadrance(spg.Point2D(0, 0), pt_v) - sp.Rational(1, 2) * 169)


def test_inscribed_polyhedra_sphere_diameter_6() -> None:
    """Verify regular and Archimedean solids in sphere D = 6 (Part II, fols. 68v–70r)."""
    table = inscribed_polyhedra_sphere_table(6)
    assert set(table.keys()) == {
        "tetrahedron",
        "cube",
        "octahedron",
        "icosahedron",
        "dodecahedron",
        "truncated_tetrahedron",
        "cuboctahedron",
    }

    assert table["tetrahedron"].edge_squared == sp.Integer(24)
    assert table["cube"].edge_squared == sp.Integer(12)
    assert table["octahedron"].edge_squared == sp.Integer(18)

    # Euclid XIII.18 fundamental identity: e_tet^2 = (4/3) e_oct^2 = 2 e_cube^2
    assert zero_test(table["tetrahedron"].edge_squared - 2 * table["cube"].edge_squared)

    # Euclid XIII.18: e_ico^2 + e_dod^2 vs sphere and golden identity
    # Truncated tetrahedron on fol. 69v (prob. 15–16): e^2 = 72/11 = 6 6/11
    assert table["truncated_tetrahedron"].edge_squared == sp.Rational(72, 11)

    # Cuboctahedron on fol. 69v–70r (prob. 17–19): edge = 3 = R
    assert table["cuboctahedron"].edge == sp.Integer(3)
    assert table["cuboctahedron"].edge_squared == sp.Integer(9)


def test_dodecahedron_in_sphere_sqrt48_fol_70r() -> None:
    """Verify Problem 21 on Part II, fol. 70r: sphere axis sqrt(48), dodecahedron sqrt(20)-2."""
    res = dodecahedron_in_sphere_sqrt48()
    assert res.sphere_axis_squared == sp.Integer(48)
    assert res.inscribed_cube_edge == sp.Integer(4)
    assert zero_test(res.dodecahedron_edge - (sp.sqrt(20) - 2))
    assert zero_test(res.extreme_mean_minor_part - (6 - sp.sqrt(20)))
    assert zero_test(res.inscribed_cube_edge * res.extreme_mean_minor_part - res.dodecahedron_edge**2)
