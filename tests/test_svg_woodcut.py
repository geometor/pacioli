"""Structural XML and `.euclid-graphic` contract tests for :mod:`geometor.pacioli.svg_woodcut`."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.pacioli.svg_woodcut import generate_all_summa_svgs

_SVG_NS = "{http://www.w3.org/2000/svg}"


def test_generate_all_summa_svgs_contract(tmp_path: Path) -> None:
    """Verify all 9 generated SVGs parse cleanly and satisfy the `.euclid-graphic` contract."""
    specs = generate_all_summa_svgs(tmp_path)
    assert len(specs) == 9

    expected_units = {
        "unit_01_dedication_arithmetica",
        "unit_02_algebra_cosa",
        "unit_03_proportioni",
        "unit_04_computis_quaderno",
        "unit_05_tractatus_geometriae",
    }
    assert {spec.unit_dir for spec in specs} == expected_units

    for spec in specs:
        assert spec.path.is_file(), f"Missing generated SVG {spec.path}"
        raw = spec.path.read_text(encoding="utf-8")
        root = ET.fromstring(raw)

        assert root.attrib.get("class") == "euclid-graphic"
        assert root.attrib.get("data-proposition") == spec.proposition

        # Five canonical layer groups in exact z-order
        top_groups = [el.attrib.get("id") for el in root.findall(f"{_SVG_NS}g")]
        assert top_groups == ["elements", "graphics", "highlights", "points", "labels"]

        # Defs must declare congruence tick markers
        defs = root.find(f"{_SVG_NS}defs")
        assert defs is not None
        marker_ids = {m.attrib.get("id") for m in defs.findall(f"{_SVG_NS}marker")}
        assert {"geom-tick-1", "geom-tick-2", "geom-tick-3"}.issubset(marker_ids)

        # Every straight segment path in #elements and #highlights must use 3-vertex midpoint d="M ... L ... L ..."
        for layer_id in ("elements", "highlights"):
            layer = next(el for el in root.findall(f"{_SVG_NS}g") if el.attrib.get("id") == layer_id)
            for path_el in layer.findall(f"{_SVG_NS}path"):
                d_attr = path_el.attrib.get("d", "")
                if " A " in d_attr or d_attr.endswith(" Z"):
                    continue
                assert d_attr.count(" L ") == 2, (
                    f"Segment path in {spec.filename} must have 3 vertices for marker-mid: {d_attr}"
                )
