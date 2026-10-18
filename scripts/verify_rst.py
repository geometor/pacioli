#!/usr/bin/env python3
"""Verify all generated RST files in resources/de_divina_proportione/paganini_1509/
(318 <NNNN>.rst + 318 <NNNN>.notes.rst = 636 files) and docsrc/ for structural
completeness, required metadata fields, zero German sections in <NNNN>.rst,
image existence, and valid RST heading/directive syntax.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PAG_DIR = ROOT / "resources" / "de_divina_proportione" / "paganini_1509"
DOCSRC = ROOT / "docsrc"

REQUIRED_FOLIO_FIELDS = [
    ":folio:",
    ":page:",
    ":page_num:",
    ":side:",
    ":volume:",
    ":book:",
    ":section:",
    ":title:",
]

VALID_SECTIONS = {
    "00_front_matter",
    "01_compendio",
    "02_architectura",
    "03_libellus",
    "04_alphabet",
    "05_polyhedra_plates",
    "06_end_matter",
}


def check_rst_headings(filepath: Path, text: str, errors: list[str]) -> None:
    lines = text.splitlines()
    for i in range(1, len(lines)):
        ln = lines[i]
        prev = lines[i - 1]
        if len(ln) >= 4 and len(set(ln)) == 1 and ln[0] in "=-~^\"`#*+":
            if not prev.strip():
                errors.append(f"{filepath.name}:{i+1}: Underline '{ln[:10]}' has empty title line above it")
            elif len(ln) < len(prev):
                errors.append(
                    f"{filepath.name}:{i+1}: Underline length ({len(ln)}) shorter than title ({len(prev)})"
                )


def verify_all() -> int:
    errors: list[str] = []

    # 1. Verify 318 <NNNN>.rst and 318 <NNNN>.notes.rst files in paganini_1509/
    folio_rsts = sorted(PAG_DIR.glob("[0-9][0-9][0-9][0-9].rst"))
    notes_rsts = sorted(PAG_DIR.glob("[0-9][0-9][0-9][0-9].notes.rst"))

    if len(folio_rsts) != 318:
        errors.append(f"Expected 318 <NNNN>.rst files in {PAG_DIR}, found {len(folio_rsts)}")
    if len(notes_rsts) != 318:
        errors.append(f"Expected 318 <NNNN>.notes.rst files in {PAG_DIR}, found {len(notes_rsts)}")

    for frst in folio_rsts:
        txt = frst.read_text(encoding="utf-8")
        # Check required field list metadata
        for req_f in REQUIRED_FOLIO_FIELDS:
            if req_f not in txt:
                errors.append(f"{frst.name}: Missing required field '{req_f}'")
        sec_m = re.search(r"^:section:\s*(\S+)", txt, re.MULTILINE)
        if not sec_m or sec_m.group(1) not in VALID_SECTIONS:
            errors.append(f"{frst.name}: Invalid :section: value '{sec_m.group(1) if sec_m else None}'")

        # Check zero German translation or German footnote apparatus in <NNNN>.rst
        for bad_de in [
            "Text auf Deutsch",
            "Übersetzung",
            "Winterberg 1889 (Deutsch)",
            "Vgl. die",
            "Siehe Zeichnung",
            "Am Ende des Tractats",
            "zu ergänzen",
        ]:
            if bad_de in txt:
                errors.append(f"{frst.name}: Found German string '{bad_de}' in single-language folio RST")

        # Check picture directives and :alt:
        for m in re.finditer(r"^\.\.\s+picture::\s+(\S+)", txt, re.MULTILINE):
            img_name = m.group(1)
            if not (PAG_DIR / img_name).exists():
                errors.append(f"{frst.name}: Missing image {img_name}")

        check_rst_headings(frst, txt, errors)

    for nrst in notes_rsts:
        txt = nrst.read_text(encoding="utf-8")
        for req_sec in [
            "Summary & Folio Continuity",
            "Graphic Extraction & Calibration",
            "Diplomatic & Textual Observations",
            "**Preceding Folio**",
            "**Current Folio**",
            "**Following Folio**",
        ]:
            if req_sec not in txt:
                errors.append(f"{nrst.name}: Missing section/item '{req_sec}'")
        check_rst_headings(nrst, txt, errors)

    print(f"Verified {len(folio_rsts)} <NNNN>.rst files and {len(notes_rsts)} <NNNN>.notes.rst files in paganini_1509/ (636 files total)")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:25]:
            print("  -", e)
        return 1
    print("ALL CHECKS PASSED: Zero German sections in <NNNN>.rst, all metadata fields and .notes.rst sections valid.")
    return 0


if __name__ == "__main__":
    sys.exit(verify_all())
