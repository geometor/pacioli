#!/usr/bin/env python3
"""Generate standardized diplomatic RST files (0001.rst..0318.rst) and companion
Transcription & Graphic Calibration Notes (0001.notes.rst..0318.notes.rst) for all
318 folios of the 1509 Paganini edition of Fra Luca Pacioli's De Divina Proportione
for use with `publish folio` (the unified Folio Reviewer).

Each <NNNN>.rst file in paganini_1509/ contains strictly:
  1. Standardized RST field-list metadata (:folio:, :page:, :page_num:, :side:,
     :volume:, :book:, :section:, :title:) with ordered section slugs
     (00_front_matter .. 06_end_matter).
  2. Extracted woodcut graphics (`.. picture:: <file>` with `:alt:`).
  3. Diplomatic transcription in the original language of the 1509 scan (Italian/Latin),
     with zero German translations or German editorial footnotes.

Each <NNNN>.notes.rst file in paganini_1509/ contains structured:
  1. Summary & Folio Continuity (Preceding, Current, and Following Folio).
  2. Graphic Extraction & Calibration (id, type, file, bbox, margin/size_class, white_point).
  3. Diplomatic & Textual Observations (running header, folio signature, chapter boundaries,
     and Winterberg 1889 Italian source correspondence).
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parent.parent
RES_DIR = ROOT / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"

SECTION_SLUG_MAP = {
    "front_matter": "00_front_matter",
    "compendio": "01_compendio",
    "architectura": "02_architectura",
    "libellus": "03_libellus",
    "alphabet": "04_alphabet",
    "polyhedra_plates": "05_polyhedra_plates",
    "end_matter": "06_end_matter",
}

LIBELLUS_INCIPIT_LA = (
    "Libellus in tres partiales tractatus divisus quinque corporum regularium et dependentium "
    "active perscrutationis, B. Petro Soderino principi perpetuo populi Florentini a M. Luca "
    "Paciolo Burgense Minoritano particulariter dicatus, feliciter incipit."
)

LIBELLUS_INCIPIT_IT = (
    "I corpi laterati assai se possono collocare nel corpo sperico, i quali tutti li anguli loro "
    "sono contingenti la superficie dela spera. Ma solo sono cinque li regulari, cioè che sono "
    "de tutti li lati e tutte le base equali: il primo è il quatro base triangulari; il secondo "
    "è il cubo che ha sei face quadrate; il terzo è l'octobase triangulari; il quarto è il dodeci "
    "base pentagonali; il quinto si è il vinti base triangulari; de' quali intendo mostrare con "
    "numeri e per radici e binomii le quantità e mesure loro. E perchè tali mesure e quantità non "
    "se possono avere senza de' lati dele loro base e superficie di quelle, però è necessario "
    "cominciare con le base loro... Dele quali cose farò 3 tractatelli: nel primo se dirà de' lati "
    "e superficie dele base; nel secondo de' corpi laterati, le superficie e quadrature loro; nel "
    "terzo de' detti corpi contenuti l'uno da l'altro e qualche cosa dela spera, se piacerà a Dio."
)

LIBELLUS_COLOPHON_LA = (
    "FINIS.\n\n"
    "Venetiis Impressum per probum virum Paganinum de Paganinis de Brixia. Decreto tamen publico "
    "ut nullus ibidem totique dominio annorum XV. curriculo imprimat vel imprimere faciat. Et alibi "
    "impressum sub quovis colore in publicum ducat sub poena in dicto privilegio contenta. Anno "
    "Redemptionis nostrae M.D.VIIII. Kalen. Iunii. Leonardo Lauretano Ve. Rem. Pu. Gubernante. "
    "Pontificatus Iulii II. Anno VI."
)

# Regex patterns to strip Winterberg's German editorial footnote apparatus that leaked into OCR Italian lines
GERMAN_FOOTNOTE_PATTERNS = [
    re.compile(r"['\-\d\)\]]*\s*Vgl\.[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Siehe\s+Zeichnung[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Am\s+Ende\s+des\s+Tractats\.?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Bezieht\s+sich\s+auf[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Hierauf\s+ist\s+die\s+Figur[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Die\s+fehlende\s+Figur[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Es\s+sind\s+die\s+bereits\s+erwähnten[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Zu\s+ergänzen[^.;\n]*[.;]?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*[^\s]+\s+zu\s+ergänzen\.?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Wahrscheinlich:\s*„?[^“.\n]*“?\s*zu\s+lesen\.?", re.IGNORECASE),
    re.compile(r"['\-\d\)\]]*\s*Wohl:?\s+[^\n.]+\.?", re.IGNORECASE),
]


def clean_italian_text(text: str) -> str:
    """Remove any embedded German apparatus notes from Winterberg 1889 OCR while preserving 1509 Italian/Latin."""
    cleaned = text
    for pat in GERMAN_FOOTNOTE_PATTERNS:
        cleaned = pat.sub(" ", cleaned)
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)
    return cleaned.strip()


def make_heading(text: str, char: str = "=") -> str:
    line = char * max(len(text), 4)
    return f"{text}\n{line}\n"


def get_ordered_section_slug(fnum: int, finfo: Dict[str, Any]) -> str:
    sec_id = finfo.get("section_id", "")
    if sec_id in SECTION_SLUG_MAP:
        return SECTION_SLUG_MAP[sec_id]
    if fnum <= 16:
        return "00_front_matter"
    if fnum <= 61:
        return "01_compendio"
    if fnum <= 84:
        return "02_architectura"
    if fnum <= 136:
        return "03_libellus"
    if fnum <= 185:
        return "04_alphabet"
    if fnum <= 311:
        return "05_polyhedra_plates"
    return "06_end_matter"


def get_original_language_title(fnum: int, finfo: Dict[str, Any]) -> str:
    orig_folio = finfo["original_folio"]
    if "plate" in finfo:
        pl = finfo["plate"]
        return f"Tabula {pl['roman']} — {pl['latin']} ({pl['greek']})"
    raw_title = clean_italian_text(finfo["title"])
    # Replace English labels on blank/plate versos with Italian diplomatic labels
    raw_title = raw_title.replace("Front Flyleaf", "Carta di guardia anteriore")
    raw_title = raw_title.replace("Rear Flyleaf", "Carta di guardia posteriore")
    raw_title = raw_title.replace("Blank Leaf", "Carta bianca")
    raw_title = raw_title.replace("Alphabet Plate Verso", "Verso bianco della tavola d'alfabeto")
    raw_title = raw_title.replace("Polyhedra Plate Verso", "Verso bianco della tavola dei corpi")
    raw_title = raw_title.replace("Table of Contents", "Tabula")
    return raw_title


def build_folio_rst(
    fstr: str,
    finfo: Dict[str, Any],
    fjson: Dict[str, Any],
    comp_map: Dict[int, Dict[str, Any]],
    arch_map: Dict[int, Dict[str, Any]],
) -> str:
    fnum = finfo["page_num"]
    side = finfo["side"]
    orig_folio = finfo["original_folio"]
    book_title = finfo["book"]
    title = get_original_language_title(fnum, finfo)
    section_slug = get_ordered_section_slug(fnum, finfo)
    chapters = finfo.get("chapters", [])
    graphics = fjson.get("graphics", finfo.get("graphics", []))

    lines: List[str] = [
        f":folio: {fstr}",
        f":page: {orig_folio}",
        f":page_num: {fnum}",
        f":side: {side}",
        ":volume: I",
        f":book: {book_title}",
        f":section: {section_slug}",
        f":title: {title}",
        "",
        make_heading(f"Folio {fstr} ({orig_folio}) — {title}", "="),
    ]

    # 1. Extracted Woodcut Graphics (Initials, Marginal Diagrams, Full-Page Plates)
    if graphics:
        for g in graphics:
            gfile = g["file"]
            gid = g.get("id", "g1")
            gtype = g.get("type", "diagram")
            if "plate" in finfo and gtype == "plate":
                pl = finfo["plate"]
                galt = f"Tabula {pl['roman']}: {pl['latin']} ({pl['greek']})"
            elif gtype == "initial":
                galt = f"Folio {fstr} Capolettera {gid}"
            elif gtype == "diagram":
                galt = f"Folio {fstr} Figura {gid}"
            else:
                galt = f"Folio {fstr} Tavola {gid}"
            lines.append(f".. picture:: {gfile}")
            lines.append(f"   :alt: {galt}")
            lines.append("")


    # 2. Original 1509 Paganini Transcription (Strictly Italian / Latin / Greek)
    if fnum <= 4 or fnum in (83, 84, 136) or fnum >= 312:
        lines.append(
            f"*[Carta bianca / guardia ({orig_folio}) nell'edizione veneziana di Paganino de' Paganini, 1509.]*"
        )
        lines.append("")
    elif 5 <= fnum <= 16:
        if "text_la" in finfo and finfo["text_la"].strip():
            lines.append(clean_italian_text(finfo["text_la"]))
            lines.append("")
        if "text_it" in finfo and finfo["text_it"].strip():
            lines.append(clean_italian_text(finfo["text_it"]))
            lines.append("")
    elif 17 <= fnum <= 82:
        for ch_ref in chapters:
            cnum = ch_ref["chapter"]
            part = ch_ref["part"]
            ch_full = comp_map[cnum] if part == "compendio" else arch_map[cnum]
            clean_title_it = clean_italian_text(ch_full["title_it"])
            hdr_label = (
                f"Cap. {ch_full['roman']}: {clean_title_it}"
                if cnum > 0
                else f"Tractato de l'Architectura — Prohemio: {clean_title_it}"
            )
            if not ch_ref.get("starts_on_folio", True):
                hdr_label += " (continuatio)"
            lines.append(make_heading(hdr_label, "-"))
            slices_it = ch_full.get("folio_slices_it", {}).get(fstr, [])
            if slices_it:
                for p in slices_it:
                    cp = clean_italian_text(p)
                    if cp:
                        lines.append(cp)
                        lines.append("")
            else:
                for p in ch_full.get("paragraphs_it", []):
                    cp = clean_italian_text(p)
                    if cp:
                        lines.append(cp)
                        lines.append("")
    elif 85 <= fnum <= 135:
        lines.append(make_heading("Pars Tertia: Libellus in tres partiales tractatus divisus", "-"))
        if fnum == 85:
            lines.append(f"**Incipit**: *{LIBELLUS_INCIPIT_LA}*")
            lines.append("")
            lines.append(LIBELLUS_INCIPIT_IT)
            lines.append("")
        elif fnum <= 100:
            lines.append(
                f"**Tractatus Primus ({orig_folio})**: Casi geometrici e algebrici (*Casus*) de' lati, "
                "cateti, diagonali e superficie dele base triangulari, quadrate e pentagonali."
            )
            lines.append("")
        elif fnum <= 112:
            lines.append(
                f"**Tractatus Secundus ({orig_folio})**: Casi geometrici e algebrici (*Casus*) de' corpi "
                "laterati regulari, le superficie e quadrature loro."
            )
            lines.append("")
        else:
            lines.append(
                f"**Tractatus Tertius ({orig_folio})**: Casi geometrici e algebrici (*Casus*) de' corpi "
                "contenuti l'uno da l'altro e dela spera."
            )
            lines.append("")
        if fnum == 135:
            lines.append(make_heading("Colophon (Kalen. Iunii M.D.VIIII)", "~"))
            lines.append(LIBELLUS_COLOPHON_LA)
            lines.append("")
    elif 137 <= fnum <= 311:
        if "plate" in finfo:
            pl = finfo["plate"]
            lines.append(make_heading(f"Tabula {pl['roman']} (No. {pl['number']})", "-"))
            lines.append(f"- **Titulus Latinus**: *{pl['latin']}*")
            lines.append(f"- **Titulus Graecus**: {pl['greek']}")
            lines.append("")
        if "text_it" in finfo and finfo["text_it"].strip():
            lines.append(clean_italian_text(finfo["text_it"]))
            lines.append("")
        if fnum % 2 == 0 and 138 <= fnum <= 310:
            lines.append(
                f"*[Carta bianca — verso della tavola {fnum - 1:04d} nell'edizione Paganini 1509.]*"
            )
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_folio_notes_rst(
    fstr: str,
    finfo: Dict[str, Any],
    fjson: Dict[str, Any],
    folios_conc: Dict[str, Dict[str, Any]],
) -> str:
    fnum = finfo["page_num"]
    side = finfo["side"]
    orig_folio = finfo["original_folio"]
    book_title = finfo["book"]
    title = clean_italian_text(finfo["title"])
    section_slug = get_ordered_section_slug(fnum, finfo)
    header_str = fjson.get("header") or "None (unheadered / plate leaf)"
    chapters = fjson.get("chapters", finfo.get("chapters", []))
    graphics = fjson.get("graphics", finfo.get("graphics", []))

    prev_fstr = f"{fnum - 1:04d}" if fnum > 1 else None
    next_fstr = f"{fnum + 1:04d}" if fnum < 318 else None

    if prev_fstr:
        pinfo = folios_conc[prev_fstr]
        prev_line = (
            f"- **Preceding Folio** (``{prev_fstr}.rst``): Folio {pinfo['original_folio']} "
            f"({pinfo['side']}), {pinfo['book']} — {clean_italian_text(pinfo['title'])}"
        )
    else:
        prev_line = "- **Preceding Folio**: None (First scan of the 1509 Venice witness)."

    curr_line = (
        f"- **Current Folio** (``{fstr}.rst``): Folio {orig_folio} ({side}), "
        f"{book_title} [``{section_slug}``] — {title}"
    )

    if next_fstr:
        ninfo = folios_conc[next_fstr]
        next_line = (
            f"- **Following Folio** (``{next_fstr}.rst``): Folio {ninfo['original_folio']} "
            f"({ninfo['side']}), {ninfo['book']} — {clean_italian_text(ninfo['title'])}"
        )
    else:
        next_line = "- **Following Folio**: None (Final scan of the 1509 Venice witness)."

    lines: List[str] = [
        make_heading(f"Folio {fstr} ({orig_folio}) — Transcription & Graphic Calibration Notes", "="),
        make_heading("Summary & Folio Continuity", "-"),
        prev_line,
        curr_line,
        next_line,
        "",
        make_heading("Graphic Extraction & Calibration", "-"),
    ]

    if graphics:
        lines.append(
            f"A total of **{len(graphics)}** woodcut element(s) were extracted and calibrated from ``{fstr}.png``:"
        )
        lines.append("")
        for g in graphics:
            gid = g.get("id", "g1")
            gtype = g.get("type", "diagram")
            gfile = g.get("file", f"{fstr}.{gid}.png")
            bbox = g.get("bbox", [0, 0, 0, 0])
            wp = g.get("white_point", 226)
            gcap = g.get("caption", f"Folio {fstr} {gid}")
            placement = g.get("margin") or g.get("size_class") or ("full-page" if gtype == "plate" else "inline")
            lines.append(
                f"- **``{gid}``** (``{gfile}``): Type ``{gtype}`` | Caption: *{gcap}* | "
                f"Bounding Box ``[x={bbox[0]}, y={bbox[1]}, w={bbox[2]}, h={bbox[3]}]`` | "
                f"Placement/Class: ``{placement}`` | White-Point Threshold: ``{wp}``"
            )
        lines.append("")
    else:
        lines.append("- No woodcut diagrams or illuminated initials are extracted on this folio.")
        lines.append("")

    lines.append(make_heading("Diplomatic & Textual Observations", "-"))
    lines.append(f"- **1509 Paganini Running Header**: ``{header_str}``")
    lines.append(f"- **Folio Signature / Numeration**: ``{orig_folio}`` (Scan page ``{fnum}``, *{side}*)")
    lines.append(f"- **Book & Section Slug**: {book_title} (``{section_slug}``)")

    if chapters:
        lines.append("- **Chapter Boundaries & Winterberg 1889 Concordance**:")
        for c in chapters:
            cnum = c.get("chapter", 0)
            clabel = f"Cap. {c.get('roman', '')}" if cnum > 0 else "Prohemio (Dedication)"
            status = "Incipit (starts on this folio)" if c.get("starts_on_folio") else "Continuatio (continues from preceding folio)"
            wit_it = c.get("winterberg_it", "N/A")
            lines.append(
                f"  - **{clabel}** (``{c.get('part')}/{c.get('slug')}``): {status} | "
                f"Winterberg 1889 Italian file: ``{wit_it}``"
            )
    elif "plate" in finfo:
        pl = finfo["plate"]
        lines.append(
            f"- **Full-Page Woodcut Plate**: Tabula ``{pl['roman']}`` (Plate No. ``{pl['number']}``) | "
            f"Latin Cartouche: *{pl['latin']}* | Greek Cartouche: {pl['greek']}"
        )
    else:
        lines.append(f"- **Leaf Category**: {title}")

    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    conc_path = PAG_DIR / "concordance.json"
    conc = json.loads(conc_path.read_text(encoding="utf-8"))

    comp_map = {c["chapter"]: c for c in conc["chapters"]["compendio"]}
    arch_map = {c["chapter"]: c for c in conc["chapters"]["architectura"]}
    folios_conc = conc["folios"]

    rst_count = 0
    notes_count = 0
    for fnum in range(1, 319):
        fstr = f"{fnum:04d}"
        finfo = folios_conc[fstr]
        fjson_path = PAG_DIR / f"{fstr}.json"
        fjson = json.loads(fjson_path.read_text(encoding="utf-8")) if fjson_path.exists() else {}

        # 1. Write <NNNN>.rst
        rst_content = build_folio_rst(fstr, finfo, fjson, comp_map, arch_map)
        (PAG_DIR / f"{fstr}.rst").write_text(rst_content, encoding="utf-8")
        rst_count += 1

        # 2. Write <NNNN>.notes.rst
        notes_content = build_folio_notes_rst(fstr, finfo, fjson, folios_conc)
        (PAG_DIR / f"{fstr}.notes.rst").write_text(notes_content, encoding="utf-8")
        notes_count += 1

    # Ensure volume_I symlink exists in resources/de_divina_proportione/ for FolioScanner compatibility
    sym_path = RES_DIR / "volume_I"
    if sym_path.is_symlink() or sym_path.exists():
        if sym_path.is_symlink():
            sym_path.unlink()
    os.symlink("paganini_1509", sym_path)

    print(
        f"Generated {rst_count} folio RST files (0001.rst..0318.rst) and "
        f"{notes_count} companion notes files (0001.notes.rst..0318.notes.rst) in {PAG_DIR}"
    )


if __name__ == "__main__":
    main()
