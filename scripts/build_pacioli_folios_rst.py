#!/usr/bin/env python3
"""Generate clean diplomatic RST files (0001.rst..0318.rst) for all 318 folios
of the 1509 Paganini edition of Fra Luca Pacioli's De Divina Proportione.

Each folio RST file in paganini_1509/ contains strictly the original 1509 Venice witness
text (Italian/Latin) and woodcut graphics (.. picture::), while separate language RST
files (Italian, German, English, and Notes) are generated in docsrc/.

Reads:
  resources/de_divina_proportione/paganini_1509/concordance.json
Writes:
  resources/de_divina_proportione/paganini_1509/0001.rst .. 0318.rst
  resources/de_divina_proportione/volume_I -> paganini_1509 (symlink)
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parent.parent
RES_DIR = ROOT / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"


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


def make_heading(text: str, char: str = "=") -> str:
    line = char * max(len(text), 4)
    return f"{text}\n{line}\n"


def build_folio_rst(
    fstr: str,
    finfo: Dict[str, Any],
    comp_map: Dict[int, Dict[str, Any]],
    arch_map: Dict[int, Dict[str, Any]],
) -> str:
    fnum = finfo["page_num"]
    side = finfo["side"]
    orig_folio = finfo["original_folio"]
    book_title = finfo["book"]
    title = finfo["title"]
    chapters = finfo.get("chapters", [])
    graphics = finfo.get("graphics", [])

    chap_summary = ", ".join(
        f"{c['part']}/{c['slug']} ({'Cap. ' + c['roman'] if c['chapter'] > 0 else 'Prohemio'})"
        for c in chapters
    ) or "None"
    gfx_summary = ", ".join(g["file"] for g in graphics) or "None"

    lines: List[str] = [
        f":folio: {fstr}",
        f":page_num: {fnum}",
        f":side: {side}",
        f":original_folio: {orig_folio}",
        f":book: {book_title}",
        f":chapters: {chap_summary}",
        f":graphics: {gfx_summary}",
        "",
        make_heading(f"Folio {fstr} ({orig_folio}) — {title}", "="),
    ]

    # 1. Woodcut Initials & Marginal Diagrams / Full-Page Plates
    if graphics:
        lines.append(make_heading("Woodcut Graphics & Illuminated Initials", "-"))
        for g in graphics:
            gfile = g["file"]
            gcap = g.get("caption", "")
            gtype = g.get("type", "diagram")
            lines.append(f".. picture:: {gfile}")
            lines.append("")
            if gcap:
                lines.append(f"   **{g['id']} ({gtype})**: {gcap}")
                lines.append("")

    # 2. Original 1509 Paganini Textual Content (Italian / Latin)
    if fnum <= 4 or fnum in (83, 84, 136) or fnum >= 312:
        lines.append(make_heading("Folio Description", "-"))
        lines.append(
            f"Blank leaf / flyleaf ({orig_folio}) in the 1509 Venice witness "
            f"(*Paganinus de Paganinis de Brixia*)."
        )
        lines.append("")
    elif 5 <= fnum <= 16:
        if "text_la" in finfo:
            lines.append(make_heading("Testo Latino (Paganini 1509)", "-"))
            lines.append(finfo["text_la"].strip())
            lines.append("")
        if "text_it" in finfo and finfo["text_it"].strip():
            lines.append(make_heading("Testo Originale (Paganini 1509)", "-"))
            lines.append(finfo["text_it"].strip())
            lines.append("")
    elif 17 <= fnum <= 82:
        lines.append(make_heading("Testo Italiano (Paganini 1509 / Winterberg 1889)", "-"))
        for ch_ref in chapters:
            cnum = ch_ref["chapter"]
            part = ch_ref["part"]
            ch_full = comp_map[cnum] if part == "compendio" else arch_map[cnum]
            hdr_label = (
                f"Cap. {ch_full['roman']}: {ch_full['title_it']}"
                if cnum > 0
                else f"Tractato de l'Architectura — Prohemio: {ch_full['title_it']}"
            )
            if not ch_ref.get("starts_on_folio", True):
                hdr_label += " (continuatio)"
            lines.append(make_heading(hdr_label, "~"))
            slices_it = ch_full.get("folio_slices_it", {}).get(fstr, [])
            if slices_it:
                for p in slices_it:
                    lines.append(p.strip())
                    lines.append("")
            else:
                for p in ch_full.get("paragraphs_it", []):
                    lines.append(p.strip())
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
            lines.append(make_heading("Testo Originale (Paganini 1509)", "-"))
            lines.append(finfo["text_it"].strip())
            lines.append("")
        if fnum % 2 == 0 and 138 <= fnum <= 310:
            lines.append(make_heading("Verso", "-"))
            lines.append(
                f"Carta bianca (verso della tavola {fnum - 1:04d}) nell'edizione Paganini 1509."
            )
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    conc_path = PAG_DIR / "concordance.json"
    conc = json.loads(conc_path.read_text(encoding="utf-8"))

    comp_map = {c["chapter"]: c for c in conc["chapters"]["compendio"]}
    arch_map = {c["chapter"]: c for c in conc["chapters"]["architectura"]}
    folios_conc = conc["folios"]

    count = 0
    for fnum in range(1, 319):
        fstr = f"{fnum:04d}"
        finfo = folios_conc[fstr]
        rst_content = build_folio_rst(fstr, finfo, comp_map, arch_map)
        rst_path = PAG_DIR / f"{fstr}.rst"
        rst_path.write_text(rst_content, encoding="utf-8")
        count += 1

    # Ensure volume_I symlink exists in resources/de_divina_proportione/ for FolioScanner compatibility
    sym_path = RES_DIR / "volume_I"
    if sym_path.is_symlink() or sym_path.exists():
        if sym_path.is_symlink():
            sym_path.unlink()
    os.symlink("paganini_1509", sym_path)

    print(f"Generated {count} single-language folio RST files (0001.rst..0318.rst) in {PAG_DIR}")


if __name__ == "__main__":
    main()
