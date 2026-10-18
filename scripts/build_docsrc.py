#!/usr/bin/env python3
"""Build the complete multi-track Sphinx/publish RST documentation in docsrc/
with separate RST files for each language (Italian, German, English, and Notes).

Structure generated:
  docsrc/
    index.rst
    compendio/
      index.rst
      cap_01/ .. cap_71/
        index.rst
        cap_NN_it.rst
        cap_NN_de.rst
        cap_NN_en.rst
        cap_NN_notes.rst
        <folio>.<gid>.png (copied woodcut diagrams/initials)
    architectura/
      index.rst
      dedication/
        index.rst
        dedication_it.rst
        dedication_de.rst
        dedication_en.rst
        dedication_notes.rst
      cap_01/ .. cap_20/
        index.rst
        cap_NN_it.rst
        cap_NN_de.rst
        cap_NN_en.rst
        cap_NN_notes.rst
    plates/
      index.rst
      alphabet_it.rst
      alphabet_de.rst
      alphabet_en.rst
      architectural_it.rst
      architectural_de.rst
      architectural_en.rst
      polyhedra_la.rst
      polyhedra_en.rst
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple

from translations_1_23 import CHAPTERS_1_TO_23
from translations_24_55 import CHAPTERS_24_TO_55
from translations_56_71 import CHAPTERS_56_TO_71
from translations_architectura import ARCHITECTURA_CHAPTERS

COMPENDIO_TRANSLATIONS: Dict[int, Dict[str, str]] = {
    **CHAPTERS_1_TO_23,
    **CHAPTERS_24_TO_55,
    **CHAPTERS_56_TO_71,
}


ROOT = Path(__file__).resolve().parent.parent
RES_DIR = ROOT / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"
DOCSRC = ROOT / "docsrc"


ALPHABET_EN = {
    "A": "This letter A is drawn from the circle and its square: the right leg must be one-ninth of the height in thickness. The left leg must be half the thickness of the thick leg. The middle crossbar must be one-third the thickness of the thick leg. The width of the said letter is determined by each leg passing through the intersection of the diagonals, the middle crossbar lying slightly lower, as you see here by the marked diameters.",
    "B": "This letter B is composed of two circles, of which the lower is the larger by one-ninth—that is, its diameter must be five-ninths of the total height, and the upper circle four-ninths in diameter, as is proportionally presented to your eyes above.",
    "C": "This letter C is drawn from the circle and its square, thickening the curve by a quarter-part on the outside and inside. The upper head terminates above the intersection of the diagonal and circumference; the lower passes beyond the intersection by half a ninth toward the corner of the square, as appears in the figure, and is hollowed out like an O.",
    "D": "This letter D is drawn from the circle and the square. The straight vertical leg lies between the diagonal intersections with a thickness of one-ninth; the curved body thickens like the other circular letters. The upper join is one-third the thickness of the thick leg, and the lower one-quarter or one-third.",
    "E": "This letter E is drawn from the circle and its square. The thick vertical stem is one-ninth of the height. The upper horizontal arm is half the thickness of the thick stem, and the lower arm likewise; the middle arm is one-third the thickness of the thick stem, like the crossbar of the A; and the said letter is half its square in width, and thus will be most perfect.",
    "F": "This letter F is formed in the exact same manner as the letter E, neither more nor less, except that F lacks the third [lowest] arm, as you had at length in the place of the said E with all its proportions; wherefore let that suffice here.",
    "G": "This letter G is formed like the C from its circle and square. The upright lower stem is one-third of its square in height, and one-ninth of the height of its square in thickness.",
    "H": "This letter H is drawn from the circle and its square. Its two thick vertical stems are formed through the intersections where the circumference of the circle and the diagonals of the square cross. The thickness of the said stems is one-ninth of the height, and the crossbar is drawn along the horizontal diameter with a thickness equal to one-third of the thick stem, like the crossbar of the A.",
    "I": "This letter I is drawn from the circle and the square; its thickness is one-ninth of the height, so that its formation is the easiest among the others.",
    "K": "This letter K is drawn from the circle and its square by drawing a diagonal of the square, upon which the two oblique branches meet and terminate at the middle of the thick stem. The lower branch is one-ninth in thickness like the other thick stems; the upper branch is half as thick, like the left leg of the A. The lower branch extends to or slightly beyond the diagonal intersection; the upper remains within the intersection.",
    "L": "This letter L is drawn from the circle and its square. Its vertical stem is one-ninth of the height in thickness, and its width is half the square with the small circles shown above. The thin lower arm is half the thickness of the vertical stem, like that of the E and the F.",
    "M": "This letter M is drawn from the circle and its square. The thin legs are half the thickness of the thick legs, like the left leg of the A. The outer legs stand slightly inside the square, and the middle strokes meet at the intersection of the diameters; their thick and thin strokes correspond to those of the A, as you may clearly understand from the figure above.",
    "N": "This letter N is drawn from its circle and square. The first vertical leg stands outside the intersection of the diagonals; the middle diagonal stroke is one-ninth in thickness taken diametrically; the third leg stands outside the intersection. The first and last vertical legs are half the thickness of the thick diagonal stroke, namely half a head [one-eighteenth of the square].",
    "O1": "This O is most perfect (*Questo O è perfectissimo*).",
    "O2": "This letter O is drawn from the circle and its square, divided into four parts crosswise by the four central lines. Its body is one-ninth in thickness; its upper part is half the thickness of its thick belly. One of its bellies inclines upward and the other downward; the thin part of the body is one-third of its belly. And because there are two opinions concerning it, I have set another one before you that is most perfect according to my judgment; take whichever pleases you, and from them you will form the Q, as you will understand below in its place.",
    "P": "This letter P is drawn from the circle and its square. Its thick stem is one-ninth in thickness. The form of the bowl is as large as the lower bowl of the B, and the thickness of its belly equals the thick stem; and the said letter begins at the intersections of the diagonals of the great circle, and thus will be most perfect.",
    "Q": "This letter Q, as I said above, is drawn from the O, terminating its tail three heads [three-ninths] of its height below the square, guiding the opposing thick bellies and thin strokes exactly as was told for the O. Its tail is nine heads long—that is, equal to the side of its right-angled square—and its tip rises one-ninth of the height at the end, following the curve of the pen with the tapering of its thickness.",
    "R": "This letter R is derived from the letter B; its upper bowl extends half a stem-width below the center. The whole letter remains within the diagonal intersections except for the curved tail, which extends beyond the intersections to the corner of the square, having a thickness of one-ninth and tapering to a fine point at the angle of the square in curved lines, as is manifest here in the example.",
    "S": "This letter S is drawn from eight circles, and this is its law of construction as appears here in the example: finding their centers by means of their parallel lines, you will find the lower circles to be larger than the upper by one-third of a ninth [one twenty-seventh] of its square. The middle belly is exactly one-ninth of the height in thickness, and the thin curves one-third of that thickness, terminating the heads with due grace.",
    "T": "This letter T is drawn from its square and circle. The thick vertical stem is formed exactly as was said for the I. The horizontal crossbar is half the thickness of the vertical stem, like the upper arms of E and F, and terminates half a head [one-eighteenth] inside each side of its square, making it most pleasing to the sight.",
    "V": "This letter V requires its entire square. The left leg is one-ninth of its square in thickness taken diametrically, like the right leg of the A and the diagonal of the N. The right leg is half the thickness of the thick leg, likewise taken diametrically like the left leg of the A, and terminates in a point at the base of the square at the end of the vertical diameter of the circle.",
    "X": "This letter X requires its entire square, crossing its legs at the central intersection of the diagonals. One leg is one-ninth of the height in thickness, and the other half as thick, taken diametrically, terminating its legs with due grace according to the curvature of the small circles.",
    "Y": "This letter Y requires the entire square; the right and left upper branches have the same thickness and proportion as those of the V, except that they meet at the central intersection of the diameters, and from there downward their junction is drawn vertically to the base of the square with a thickness of one-ninth of the square; the upper heads terminate on their small circles, as you see.",
}


def make_heading(text: str, char: str = "=") -> str:
    line = char * max(len(text), 4)
    return f"{text}\n{line}\n"


def clean_draft_en(raw_en: str) -> List[str]:
    """Extract clean paragraphs from an existing draft English file in winterberg_en/."""
    lines = raw_en.splitlines()
    paras: List[str] = []
    cur: List[str] = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("#"):
            continue
        if re.match(r"^(Cap|Gap|Ca)[\.,\s]+[IVXLCDM0-9]+", s, re.IGNORECASE):
            continue
        if not s:
            if cur:
                paras.append(" ".join(cur))
                cur = []
        else:
            cur.append(s)
    if cur:
        paras.append(" ".join(cur))
    return paras


def collect_chapter_graphics(
    ch: Dict[str, Any],
    folios_conc: Dict[str, Dict[str, Any]],
    dest_dir: Path,
) -> Tuple[str, List[Dict[str, str]]]:
    """Copy marginal diagrams and woodcut initials for a chapter into dest_dir and return
    (folio_banner_str, copied_diagrams_list).
    """
    folios = ch["folios"]
    start_f = ch["start_folio"]
    end_f = ch["end_folio"]
    orig_start = folios_conc[start_f]["original_folio"]
    orig_end = folios_conc[end_f]["original_folio"]
    folio_range_label = (
        f"{start_f} ({orig_start})"
        if start_f == end_f
        else f"{start_f}–{end_f} ({orig_start}–{orig_end})"
    )

    initial_file = None
    diagrams: List[Dict[str, str]] = []
    seen_files = set()

    for fstr in folios:
        finfo = folios_conc.get(fstr, {})
        for g in finfo.get("graphics", []):
            gfile = g["file"]
            src_p = PAG_DIR / gfile
            if not src_p.exists() or gfile in seen_files:
                continue
            if g["type"] == "initial":
                # Attach initial if chapter starts on this folio and we don't have one yet
                if fstr == start_f and initial_file is None:
                    shutil.copy2(src_p, dest_dir / gfile)
                    initial_file = gfile
                    seen_files.add(gfile)
            else:
                shutil.copy2(src_p, dest_dir / gfile)
                diagrams.append({
                    "file": gfile,
                    "caption": g.get("caption", f"Folio {fstr} {g['id']}"),
                    "type": g.get("type", "diagram"),
                })
                seen_files.add(gfile)

    folio_lines = [f".. folio:: {folio_range_label}"]
    if initial_file:
        folio_lines.append(f"   :initial: {initial_file}")
    folio_lines.append("")
    return "\n".join(folio_lines), diagrams


def build_track_nav(
    part_prefix: str,
    slug: str,
    active_track: str,
    prev_slug: str | None,
    next_slug: str | None,
    index_ref: str,
) -> str:
    """Create a Hoenen-style track-nav bar linking Italian, German, English, and Notes."""
    tracks = [
        ("en", "English", f"{part_prefix}-{slug}-en"),
        ("it", "Italiano (1509)", f"{part_prefix}-{slug}-it"),
        ("de", "Deutsch (1889)", f"{part_prefix}-{slug}-de"),
        ("notes", "Notes", f"{part_prefix}-{slug}-notes"),
    ]
    t_parts = []
    for tk, label, ref_id in tracks:
        if tk == active_track:
            t_parts.append(f"**{label}**")
        else:
            t_parts.append(f":ref:`{label} <{ref_id}>`")

    nav_parts = [f":ref:`Conspectus <{index_ref}>`"]
    if prev_slug:
        nav_parts.append(f":ref:`← Prev <{part_prefix}-{prev_slug}-{active_track}>`")
    if next_slug:
        nav_parts.append(f":ref:`Next → <{part_prefix}-{next_slug}-{active_track}>`")

    return (
        ".. container:: track-nav\n\n"
        f"   {' · '.join(t_parts)} | {' · '.join(nav_parts)}\n"
    )


def write_chapter_files(
    part_dir: Path,
    part_prefix: str,
    index_ref: str,
    ch: Dict[str, Any],
    prev_slug: str | None,
    next_slug: str | None,
    folios_conc: Dict[str, Dict[str, Any]],
) -> Dict[str, str]:
    """Generate separate RST files (index.rst, <slug>_it.rst, <slug>_de.rst, <slug>_en.rst, <slug>_notes.rst)
    for a chapter in Compendio or Architectura.
    """
    slug = ch["slug"]
    cnum = ch["chapter"]
    roman = ch["roman"]
    ch_dir = part_dir / slug
    ch_dir.mkdir(parents=True, exist_ok=True)

    folio_banner, diagrams = collect_chapter_graphics(ch, folios_conc, ch_dir)
    cap_label = f"CAPITOLO {roman}" if cnum > 0 else "PROHEMIO"
    cap_label_en = f"CHAPTER {roman}" if cnum > 0 else "DEDICATION"
    cap_label_de = f"CAPITEL {roman}" if cnum > 0 else "WIDMUNG"

    title_it = ch["title_it"] or cap_label
    title_de = ch["title_de"] or cap_label_de

    # Determine English title, body, and notes from the scholarly translation modules
    if part_prefix == "compendio":
        t_data = COMPENDIO_TRANSLATIONS[cnum]
    else:
        t_data = ARCHITECTURA_CHAPTERS[cnum]

    title_en = t_data["title_en"]
    body_en = t_data["body_en"]
    philological_footer = (
        "\n\nPhilological and Folio Apparatus\n"
        "--------------------------------\n\n"
        f"- **1509 Paganini Witness Folios**: {', '.join(ch['folios'])} "
        f"({folios_conc[ch['start_folio']]['original_folio']}–{folios_conc[ch['end_folio']]['original_folio']})\n"
        f"- **Winterberg 1889 Italian Source**: ``{ch.get('winterberg_it', 'N/A')}``\n"
        f"- **Winterberg 1889 German Source**: ``{ch.get('winterberg_de', 'N/A')}``\n"
        f"- **Marginal Woodcut Diagrams**: {len(diagrams)} figure(s) extracted from the 1509 Venice witness.\n"
    )
    notes_body = t_data["notes"] + philological_footer

    # Format marginal diagrams block if any
    diag_block = ""
    if diagrams:
        d_lines = ["", make_heading("Marginal Woodcut Diagrams (Paganini 1509)", "-")]
        for d in diagrams:
            d_lines.append(f".. figure:: {d['file']}")
            d_lines.append("   :align: center")
            d_lines.append("")
            d_lines.append(f"   {d['caption']}")
            d_lines.append("")
        diag_block = "\n".join(d_lines)

    # 1. Write <slug>_it.rst (Standalone Italian File)
    it_rst = "\n".join([
        ":layout: book",
        "",
        f".. _{part_prefix}-{slug}-it:",
        "",
        make_heading(f"{cap_label} (Italiano — 1509)", "="),
        f".. rubric:: {title_it}",
        "",
        build_track_nav(part_prefix, slug, "it", prev_slug, next_slug, index_ref),
        folio_banner,
        "\n\n".join(ch.get("paragraphs_it", [])),
        diag_block,
    ]).rstrip() + "\n"
    (ch_dir / f"{slug}_it.rst").write_text(it_rst, encoding="utf-8")

    # 2. Write <slug>_de.rst (Standalone German File)
    de_rst = "\n".join([
        ":layout: book",
        "",
        f".. _{part_prefix}-{slug}-de:",
        "",
        make_heading(f"{cap_label_de} (Deutsch — Winterberg 1889)", "="),
        f".. rubric:: {title_de}",
        "",
        build_track_nav(part_prefix, slug, "de", prev_slug, next_slug, index_ref),
        folio_banner,
        "\n\n".join(ch.get("paragraphs_de", [])),
        diag_block,
    ]).rstrip() + "\n"
    (ch_dir / f"{slug}_de.rst").write_text(de_rst, encoding="utf-8")

    # 3. Write <slug>_en.rst (Standalone English File)
    en_rst = "\n".join([
        ":layout: book",
        "",
        f".. _{part_prefix}-{slug}-en:",
        "",
        make_heading(f"{cap_label_en} (English)", "="),
        f".. rubric:: {title_en}",
        "",
        build_track_nav(part_prefix, slug, "en", prev_slug, next_slug, index_ref),
        folio_banner,
        body_en,
        diag_block,
    ]).rstrip() + "\n"
    (ch_dir / f"{slug}_en.rst").write_text(en_rst, encoding="utf-8")

    # 4. Write <slug>_notes.rst (Standalone Notes & Commentary File)
    notes_rst = "\n".join([
        ":layout: book",
        "",
        f".. _{part_prefix}-{slug}-notes:",
        "",
        make_heading(f"{cap_label_en} — Critical Commentary & Notes", "="),
        f".. rubric:: {title_en}",
        "",
        build_track_nav(part_prefix, slug, "notes", prev_slug, next_slug, index_ref),
        notes_body,
    ]).rstrip() + "\n"
    (ch_dir / f"{slug}_notes.rst").write_text(notes_rst, encoding="utf-8")

    # 5. Write index.rst in chapter folder (links separate language files via toctree)
    idx_rst = "\n".join([
        f".. _{part_prefix}-{slug}:",
        "",
        make_heading(f"{cap_label_en}: {title_en[:80]}", "="),
        f"- **Original Italian Title (1509)**: *{title_it}*",
        f"- **German Edition Title (1889)**: *{title_de}*",
        f"- **1509 Paganini Folios**: {', '.join(ch['folios'])} ({folios_conc[ch['start_folio']]['original_folio']}–{folios_conc[ch['end_folio']]['original_folio']})",
        "",
        "**Language Editions & Apparatus**:",
        f":ref:`English <{part_prefix}-{slug}-en>` · "
        f":ref:`Italiano (1509) <{part_prefix}-{slug}-it>` · "
        f":ref:`Deutsch (1889) <{part_prefix}-{slug}-de>` · "
        f":ref:`Notes & Commentary <{part_prefix}-{slug}-notes>`",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
        f"   {slug}_en",
        f"   {slug}_it",
        f"   {slug}_de",
        f"   {slug}_notes",
        "",
    ])
    (ch_dir / "index.rst").write_text(idx_rst, encoding="utf-8")

    return {
        "slug": slug,
        "roman": roman,
        "chapter": cnum,
        "title_en": title_en,
        "title_it": title_it,
        "title_de": title_de,
        "folios_label": f"{ch['start_folio']} ({folios_conc[ch['start_folio']]['original_folio']})",
    }


def build_plates_section(conc: Dict[str, Any]) -> None:
    """Create separate language RST files in docsrc/plates/ for Alphabet, Architectural, and Polyhedra plates."""
    plates_dir = DOCSRC / "plates"
    plates_dir.mkdir(parents=True, exist_ok=True)

    # Copy all plate graphics (g1..gN on 137..311) to docsrc/plates/
    folios_conc = conc["folios"]
    for fnum in range(137, 312):
        fstr = f"{fnum:04d}"
        for g in folios_conc.get(fstr, {}).get("graphics", []):
            src_p = PAG_DIR / g["file"]
            if src_p.exists():
                shutil.copy2(src_p, plates_dir / g["file"])

    # 1. Alphabet Plates: alphabet_it.rst, alphabet_de.rst, alphabet_en.rst
    alpha_list = conc["plates"]["alphabet"]
    it_lines = [
        ":layout: book",
        "",
        ".. _plates-alphabet-it:",
        "",
        make_heading("Appendice I: L'Alfabeto Geometrico Romano (Italiano — 1509)", "="),
        ".. container:: track-nav",
        "",
        "   :ref:`English <plates-alphabet-en>` · **Italiano (1509)** · :ref:`Deutsch (1889) <plates-alphabet-de>` | :ref:`← Plates Index <plates-index>`",
        "",
    ]
    de_lines = [
        ":layout: book",
        "",
        ".. _plates-alphabet-de:",
        "",
        make_heading("Anhang I: Das Geometrische Römische Alphabet (Deutsch — 1889)", "="),
        ".. container:: track-nav",
        "",
        "   :ref:`English <plates-alphabet-en>` · :ref:`Italiano (1509) <plates-alphabet-it>` · **Deutsch (1889)** | :ref:`← Plates Index <plates-index>`",
        "",
    ]
    en_lines = [
        ":layout: book",
        "",
        ".. _plates-alphabet-en:",
        "",
        make_heading("Appendix I: The Roman Geometric Alphabet (English)", "="),
        ".. container:: track-nav",
        "",
        "   **English** · :ref:`Italiano (1509) <plates-alphabet-it>` · :ref:`Deutsch (1889) <plates-alphabet-de>` | :ref:`← Plates Index <plates-index>`",
        "",
    ]

    for item in alpha_list:
        fstr = item["folio"]
        let_id = item["letter"]
        title = item["title"]
        gfx = folios_conc[fstr]["graphics"]
        gfile = gfx[0]["file"] if gfx else f"{fstr}.g1.png"

        for target_lines, txt in [
            (it_lines, item["text_it"]),
            (de_lines, item["text_de"]),
            (en_lines, ALPHABET_EN.get(let_id, item["text_it"])),
        ]:
            target_lines.append(make_heading(f"{title} (Folio {fstr})", "-"))
            target_lines.append(f".. folio:: {fstr}")
            target_lines.append("")
            target_lines.append(f".. figure:: {gfile}")
            target_lines.append("   :align: center")
            target_lines.append("")
            target_lines.append(f"   {title} (Folio {fstr})")
            target_lines.append("")
            target_lines.append(txt)
            target_lines.append("")

    (plates_dir / "alphabet_it.rst").write_text("\n".join(it_lines), encoding="utf-8")
    (plates_dir / "alphabet_de.rst").write_text("\n".join(de_lines), encoding="utf-8")
    (plates_dir / "alphabet_en.rst").write_text("\n".join(en_lines), encoding="utf-8")

    # 2. Architectural Plates: architectural_it.rst, architectural_de.rst, architectural_en.rst
    arch_plates = conc["plates"]["architectural"]
    arch_en_texts = {
        "0137": "Divina Proportio: Proportional profile of the human head inscribed in the equilateral triangle and square grid (Tractato de l'Architectura, Cap. I–II).",
        "0185": "PORTA TEMPLI DOMINI DICTA SPECIOSA (The Gate of the Lord's Temple Called Beautiful): In the present figure of the gate called Speciosa, the two parts adduced here—namely the round column with its capital, base, stylobate, and stereobate, and the epistyle with its frieze (zophorus) and cornice—are duly presented to your discerning eye.",
        "0213": "Corinthian, Ionic, and Pulvinated Column with Stylobate (Pedestal) and Stereobate: Column called Corinthian with respect to its capital, abacus, and cymatium, and Ionic and pulvinated with respect to its base and capital, as Vitruvius explains in full, alongside modern columns in the Cathedral of Pisa and in Santo Spirito and San Lorenzo in Florence under the patronage of the House of Medici.",
        "0215": "Epistyle (Architrave), Zophorus (Frieze), and Cornice: The entire assembly below the frieze is called Epistylium by the Ancients and Architrave by the Moderns, and the assembly above it is called Cornice (with lettered mouldings a, c, e = Fascia; f = Echinus/Ovolo; g = Scotia/Gola; k = Cymatium; l = Dentils; m = Corona/Dripstone; o = Acroterium/Reglet).",
        "0311": "ARBOR PROPORTIO ET PROPORTIONALITAS (Tree of Ratio and Proportionality): Above all it pertains to the geometer to treat completely of proportions; for the arithmetician does not find the measure of ratio in all numbers, since there are infinitely many ratios which the nature of numbers does not admit, as is clear from Book V of Euclid's Elements. Just as unity is the head of number, so equality is the principle of proportions (Boethius, De institutione musica II, c. 15).",
    }
    for lang, suf, hdr_title in [
        ("it", "it", "Tavole d'Architettura e Arbor Proportionis (Italiano / Latino — 1509)"),
        ("de", "de", "Architekturtafeln und Arbor Proportionis (Deutsch — 1889)"),
        ("en", "en", "Architectural Plates and Arbor Proportionis (English)"),
    ]:
        alines = [
            ":layout: book",
            "",
            f".. _plates-architectural-{suf}:",
            "",
            make_heading(hdr_title, "="),
            ".. container:: track-nav",
            "",
            "   :ref:`English <plates-architectural-en>` · :ref:`Italiano (1509) <plates-architectural-it>` · :ref:`Deutsch (1889) <plates-architectural-de>` | :ref:`← Plates Index <plates-index>`",
            "",
        ]
        for fstr, info in sorted(arch_plates.items()):
            alines.append(make_heading(f"Folio {fstr}: {info['title']}", "-"))
            alines.append(f".. folio:: {fstr}")
            alines.append("")
            for g in folios_conc[fstr]["graphics"]:
                alines.append(f".. figure:: {g['file']}")
                alines.append("   :align: center")
                alines.append("")
                alines.append(f"   {g['caption']}")
                alines.append("")
            txt = arch_en_texts[fstr] if lang == "en" else info[lang]
            alines.append(txt)
            alines.append("")
        (plates_dir / f"architectural_{suf}.rst").write_text("\n".join(alines), encoding="utf-8")

    # 3. Polyhedra Plates: polyhedra_la.rst (Latin/Greek 1509 captions) and polyhedra_en.rst (English)
    poly_plates = conc["plates"]["polyhedra"]
    la_lines = [
        ":layout: book",
        "",
        ".. _plates-polyhedra-la:",
        "",
        make_heading("Appendix II: Tabulae Corporum Regularium et Dependentium (Latino / Graeco — 1509)", "="),
        ".. container:: track-nav",
        "",
        "   :ref:`English <plates-polyhedra-en>` · **Latino / Graeco (1509)** | :ref:`← Plates Index <plates-index>`",
        "",
        "Full-page woodcut plates designed by **Leonardo da Vinci** (*per mano del nostro Lionardo da Vinci Fiorentino*), "
        "carrying their original 1509 Latin and Greek cartouches.",
        "",
    ]
    pen_lines = [
        ":layout: book",
        "",
        ".. _plates-polyhedra-en:",
        "",
        make_heading("Appendix II: Polyhedra Plates by Leonardo da Vinci (English)", "="),
        ".. container:: track-nav",
        "",
        "   **English** · :ref:`Latino / Graeco (1509) <plates-polyhedra-la>` | :ref:`← Plates Index <plates-index>`",
        "",
        "Sixty full-page woodcut plates of the Five Regular Platonic Solids and their Truncated (*abscisa*), "
        "Elevated/Stellated (*elevata*), and Prismatic/Pyramidal/Spherical Dependent Bodies in Solid (*planum/solidum*) "
        "and Skeletal (*vacuum*) perspective views, drawn by **Leonardo da Vinci**.",
        "",
    ]
    for fstr, pinfo in sorted(poly_plates.items()):
        gfx = folios_conc[fstr]["graphics"]
        gfile = gfx[0]["file"] if gfx else f"{fstr}.g1.png"
        rom = pinfo["roman"]

        la_lines.append(make_heading(f"Tabula {rom} (Folio {fstr}) — {pinfo['latin']}", "-"))
        la_lines.append(f".. folio:: {fstr}")
        la_lines.append("")
        la_lines.append(f".. figure:: {gfile}")
        la_lines.append("   :align: center")
        la_lines.append("")
        la_lines.append(f"   *{pinfo['latin']}* ({pinfo['greek']})")
        la_lines.append("")

        pen_lines.append(make_heading(f"Plate {rom} (Folio {fstr}) — {pinfo['english']}", "-"))
        pen_lines.append(f".. folio:: {fstr}")
        pen_lines.append("")
        pen_lines.append(f".. figure:: {gfile}")
        pen_lines.append("   :align: center")
        pen_lines.append("")
        pen_lines.append(f"   **{pinfo['english']}** — *{pinfo['latin']}* ({pinfo['greek']})")
        pen_lines.append("")

    (plates_dir / "polyhedra_la.rst").write_text("\n".join(la_lines), encoding="utf-8")
    (plates_dir / "polyhedra_en.rst").write_text("\n".join(pen_lines), encoding="utf-8")

    # 4. plates/index.rst
    p_idx = "\n".join([
        ".. _plates-index:",
        "",
        make_heading("Appendices: Woodcut Plates of the 1509 Paganini Edition", "="),
        "1. **The Roman Geometric Alphabet (Folios 0139–0183)**:",
        "   :ref:`English <plates-alphabet-en>` · :ref:`Italiano (1509) <plates-alphabet-it>` · :ref:`Deutsch (1889) <plates-alphabet-de>`",
        "2. **Architectural Plates & Arbor Proportionis (Folios 0137, 0185, 0213, 0215, 0311)**:",
        "   :ref:`English <plates-architectural-en>` · :ref:`Italiano (1509) <plates-architectural-it>` · :ref:`Deutsch (1889) <plates-architectural-de>`",
        "3. **Polyhedra Plates by Leonardo da Vinci (Plates I–LIX, Folios 0187–0309)**:",
        "   :ref:`English <plates-polyhedra-en>` · :ref:`Latino / Graeco (1509) <plates-polyhedra-la>`",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Plates by Language",
        "",
        "   alphabet_en",
        "   alphabet_it",
        "   alphabet_de",
        "   architectural_en",
        "   architectural_it",
        "   architectural_de",
        "   polyhedra_en",
        "   polyhedra_la",
        "",
    ])
    (plates_dir / "index.rst").write_text(p_idx, encoding="utf-8")


def main() -> None:
    conc = json.loads((PAG_DIR / "concordance.json").read_text(encoding="utf-8"))
    folios_conc = conc["folios"]

    # Remove old broken docsrc/books directory if present
    old_books = DOCSRC / "books"
    if old_books.exists():
        shutil.rmtree(old_books)

    # 1. Build Part I: Compendio de Divina Proportione (cap_01..cap_71)
    comp_dir = DOCSRC / "compendio"
    comp_dir.mkdir(parents=True, exist_ok=True)
    comp_chaps = conc["chapters"]["compendio"]
    comp_meta: List[Dict[str, str]] = []

    for idx, ch in enumerate(comp_chaps):
        prev_s = comp_chaps[idx - 1]["slug"] if idx > 0 else None
        next_s = comp_chaps[idx + 1]["slug"] if idx < len(comp_chaps) - 1 else None
        m = write_chapter_files(
            comp_dir, "compendio", "compendio-index", ch, prev_s, next_s, folios_conc
        )
        comp_meta.append(m)

    # Write docsrc/compendio/index.rst
    comp_idx_lines = [
        ".. _compendio-index:",
        "",
        make_heading("Part I: Compendio de Divina Proportione (Chapters I–LXXI)", "="),
        "Dedicated to **Ludovico Maria Sforza**, Duke of Milan (completed at Milan, December 14, 1498; "
        "printed at Venice by Paganino de' Paganini, June 1, 1509). Each chapter is presented in separate "
        "language files: **English**, **Italiano (1509)**, **Deutsch (Winterberg 1889)**, and **Critical Notes**.",
        "",
        make_heading("Conspectus Capitum (Part I)", "-"),
    ]
    for m in comp_meta:
        slug = m["slug"]
        rom = m["roman"]
        comp_idx_lines.append(
            f"- **Cap. {rom}** (*{m['folios_label']}*): {m['title_en'][:95]}\n"
            f"  [:ref:`English <compendio-{slug}-en>` · "
            f":ref:`Italiano <compendio-{slug}-it>` · "
            f":ref:`Deutsch <compendio-{slug}-de>` · "
            f":ref:`Notes <compendio-{slug}-notes>`]"
        )
    comp_idx_lines.extend([
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Chapters I–LXXI",
        "",
    ])
    for m in comp_meta:
        comp_idx_lines.append(f"   {m['slug']}/index")
    comp_idx_lines.append("")
    (comp_dir / "index.rst").write_text("\n".join(comp_idx_lines), encoding="utf-8")

    # 2. Build Part II: Tractato de l'Architectura (dedication + cap_01..cap_20)
    arch_dir = DOCSRC / "architectura"
    arch_dir.mkdir(parents=True, exist_ok=True)
    arch_chaps = conc["chapters"]["architectura"]
    arch_meta: List[Dict[str, str]] = []

    for idx, ch in enumerate(arch_chaps):
        prev_s = arch_chaps[idx - 1]["slug"] if idx > 0 else None
        next_s = arch_chaps[idx + 1]["slug"] if idx < len(arch_chaps) - 1 else None
        m = write_chapter_files(
            arch_dir, "architectura", "architectura-index", ch, prev_s, next_s, folios_conc
        )
        arch_meta.append(m)

    # Write docsrc/architectura/index.rst
    arch_idx_lines = [
        ".. _architectura-index:",
        "",
        make_heading("Part II: Tractato de l'Architectura (Prohemio & Chapters I–XX)", "="),
        "Dedicated to Pacioli's beloved disciples and pupils of Borgo Sansepolcro (1509 Paganini Folios "
        "0061–0082, ``f. 23r``–``f. 33v``). Each chapter is presented in separate language files: "
        "**English**, **Italiano (1509)**, **Deutsch (Winterberg 1889)**, and **Critical Notes**.",
        "",
        make_heading("Conspectus Capitum (Part II)", "-"),
    ]
    for m in arch_meta:
        slug = m["slug"]
        lbl = f"Cap. {m['roman']}" if m["chapter"] > 0 else "Prohemio (Dedication)"
        arch_idx_lines.append(
            f"- **{lbl}** (*{m['folios_label']}*): {m['title_en'][:95]}\n"
            f"  [:ref:`English <architectura-{slug}-en>` · "
            f":ref:`Italiano <architectura-{slug}-it>` · "
            f":ref:`Deutsch <architectura-{slug}-de>` · "
            f":ref:`Notes <architectura-{slug}-notes>`]"
        )
    arch_idx_lines.extend([
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Prohemio & Chapters I–XX",
        "",
    ])
    for m in arch_meta:
        arch_idx_lines.append(f"   {m['slug']}/index")
    arch_idx_lines.append("")
    (arch_dir / "index.rst").write_text("\n".join(arch_idx_lines), encoding="utf-8")

    # 3. Build Plates section
    build_plates_section(conc)

    # 4. Write master docsrc/index.rst
    root_idx_lines = [
        ":title: De Divina Proportione",
        ":author: Fra Luca Pacioli",
        ":publisher: Paganinus de Paganinis de Brixia (Venice, 1509) / Constantin Winterberg (Vienna, 1889)",
        ":year: 1509",
        "",
        ".. _pacioli-index:",
        "",
        make_heading("DE DIVINA PROPORTIONE", "="),
        ".. rubric:: Fra Luca Pacioli (Venice, 1509) — Critical Multi-Language Digital Edition",
        "",
        "A unified digital edition of Fra Luca Pacioli's *De Divina Proportione* (Venice: Paganino de' "
        "Paganini, June 1, 1509), integrating the 318 high-resolution folio scans and 510 extracted "
        "woodcuts (illuminated initials, marginal geometric diagrams, Roman geometric alphabet plates, "
        "architectural plates, and Leonardo da Vinci's sixty polyhedra plates) with separate, "
        "parallel language tracks:",
        "",
        "- **Italiano (1509 / 1889)**: Diplomatic Italian text from the 1509 Paganini edition and Constantin Winterberg's 1889 edition.",
        "- **Deutsch (1889)**: Constantin Winterberg's German critical translation (*Quellenschriften für Kunstgeschichte*, Vienna, 1889).",
        "- **English (GEOMETOR Edition)**: Complete, unabridged scholarly English translation and Euclidean dependency markup (`:just:`, `:g:`, `.. enunciation::`, `.. assertion::`, `.. qed::`, `.. folio::`) across the entire work: **Part I (*Compendio de Divina Proportione*, Chapters I–LXXI)**, **Part II (*Tractato de l'Architectura*, Dedication & Chapters I–XX)**, and **Appendices (Roman Alphabet, Architectural Plates, and Leonardo da Vinci's Sixty Polyhedra Plates)**.",
        "- **Critical Commentary & Notes**: Historical, prosopographical, architectural, and mathematical apparatus for every chapter.",
        "",
        make_heading("Complete Structure of the Work", "-"),
        "- :ref:`Part I: Compendio de Divina Proportione (Chapters I–LXXI, Folios 0017–0061) <compendio-index>`",
        "  - **Section 1 (Cap. I–VI)**: Dedicatory Epistle, Eulogy of Mathematics, Definition of the Divine Proportion, and Its Five Divine Attributes",
        "  - **Section 2 (Cap. VII–XXIII)**: The Thirteen Marvelous Effects of the Divine Proportion in Lines and Regular Polygons (:just:`XIII.1`–:just:`XIII.12`, :just:`X.73`, :just:`X.76`)",
        "  - **Section 3 (Cap. XXIV–LV)**: The Five Regular Platonic Solids, Proof of Their Uniqueness (:just:`XI.21`), Constructions (:just:`XIII.13`–:just:`XIII.18`), Proportions (Book XIV), Twelve Mutual Inscriptions (Book XV), and Truncated/Elevated Dependent Bodies (Plates I–XL)",
        "  - **Section 4 (Cap. LVI–LXXI)**: The Sphere, Oblong Bodies (Columns and Pyramids), Mensuration, Panegyric to Ludovico Sforza, Concordance of Leonardo's Plates, and Mathematical Glossary (Plates XLI–LIX)",
        "- :ref:`Part II: Tractato de l'Architectura (Prohemio & Chapters I–XX, Folios 0061–0082) <architectura-index>`",
        "  - **Prohemio**: Dedication to the Stonemasons of Borgo Sansepolcro, Promise of Piero della Francesca's Perspective, and Roll of Honor of the Captains of Sansepolcro",
        "  - **Chapters I–III**: Vitruvian Human Proportions, the Head in the Equilateral Triangle (:just:`I.1`), the Painter's Net (*Rete*), and the Perfect Numbers 6, 10, and 16 (:just:`IX.36`)",
        "  - **Chapters IV–XX**: The Classical Orders (Ionic, Doric, Corinthian), Bases, Stylobates, Stereobates, Survey of Columns Across Italy, Epistyles, Friezes, Cornices, the *Porta Speciosa*, Polyhedra in Architecture, and Superimposed Columns",
        "- :ref:`Appendices: Roman Alphabet, Architectural Plates, and Leonardo Polyhedra Plates (Folios 0137–0311) <plates-index>`",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :caption: Contents",
        "",
        "   compendio/index",
        "   architectura/index",
        "   plates/index",
        "",
    ]
    (DOCSRC / "index.rst").write_text("\n".join(root_idx_lines), encoding="utf-8")
    print(
        f"Built multi-language docsrc/ with {len(comp_meta)} Compendio chapters, "
        f"{len(arch_meta)} Architectura chapters, and Plates section."
    )


if __name__ == "__main__":
    main()
