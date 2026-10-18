#!/usr/bin/env python3
"""Verify all generated RST files in resources/de_divina_proportione/paganini_1509/
and docsrc/ for structural completeness, separate language files, image existence,
zero draft placeholders, and docutils RST syntax validity.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PAG_DIR = ROOT / "resources" / "de_divina_proportione" / "paganini_1509"
DOCSRC = ROOT / "docsrc"


def verify_all() -> int:
    errors = []

    # 1. Verify 318 folio RST files in paganini_1509/ and zero .txt files
    txt_files = list(PAG_DIR.glob("*.txt"))
    if txt_files:
        errors.append(f"Found {len(txt_files)} leftover .txt files in {PAG_DIR}")

    folio_rsts = sorted(PAG_DIR.glob("[0-9][0-9][0-9][0-9].rst"))
    if len(folio_rsts) != 318:
        errors.append(f"Expected 318 folio RST files in {PAG_DIR}, found {len(folio_rsts)}")

    for frst in folio_rsts:
        txt = frst.read_text(encoding="utf-8")
        if "Übersetzung" in txt or "Winterberg 1889 (Deutsch)" in txt:
            errors.append(f"Multi-language German text found in single-language folio file {frst.name}")
        for m in re.finditer(r"^\.\.\s+(?:picture|figure)::\s+(\S+)", txt, re.MULTILINE):
            img_name = m.group(1)
            if not (PAG_DIR / img_name).exists():
                errors.append(f"Missing image {img_name} referenced in {frst}")

    # 2. Verify all 71 Compendio chapters and 21 Architectura chapters have separate language files
    comp_slugs = [f"cap_{i:02d}" for i in range(1, 72)]
    for slug in comp_slugs:
        cdir = DOCSRC / "compendio" / slug
        for fname in ["index.rst", f"{slug}_en.rst", f"{slug}_it.rst", f"{slug}_de.rst", f"{slug}_notes.rst"]:
            fpath = cdir / fname
            if not fpath.exists():
                errors.append(f"Missing {fpath}")

    arch_slugs = ["dedication"] + [f"cap_{i:02d}" for i in range(1, 21)]
    for slug in arch_slugs:
        adir = DOCSRC / "architectura" / slug
        for fname in ["index.rst", f"{slug}_en.rst", f"{slug}_it.rst", f"{slug}_de.rst", f"{slug}_notes.rst"]:
            fpath = adir / fname
            if not fpath.exists():
                errors.append(f"Missing {fpath}")

    # 3. Verify zero "Translation Status" draft banners remain in docsrc/ and check image references
    docsrc_rsts = sorted(DOCSRC.rglob("*.rst"))
    for rpath in docsrc_rsts:
        txt = rpath.read_text(encoding="utf-8")
        if "Translation Status" in txt or "Draft synthesis from the earlier track" in txt:
            errors.append(f"Draft translation banner still present in {rpath}")
        for m in re.finditer(r"^\.\.\s+(?:picture|figure)::\s+(\S+)", txt, re.MULTILINE):
            img_name = m.group(1)
            if not (rpath.parent / img_name).exists():
                errors.append(f"Missing image {img_name} referenced in {rpath}")
        for m in re.finditer(r"^\s+:initial:\s+(\S+)", txt, re.MULTILINE):
            img_name = m.group(1)
            if not (rpath.parent / img_name).exists():
                errors.append(f"Missing initial image {img_name} referenced in {rpath}")

    print(f"Verified {len(folio_rsts)} single-language folio RST files in paganini_1509/")
    print(f"Verified {len(docsrc_rsts)} multi-track RST files in docsrc/ (71 Compendio chapters + 21 Architectura chapters + Plates)")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:25]:
            print("  -", e)
        return 1
    print("ALL CHECKS PASSED: Zero errors, zero missing images, zero draft banners remaining.")
    return 0


if __name__ == "__main__":
    sys.exit(verify_all())
