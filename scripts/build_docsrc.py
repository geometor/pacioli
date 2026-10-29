#!/usr/bin/env python3
"""Build the complete multi-track Sphinx/publish RST documentation in docsrc/
with separate RST files for each language (English, Italian, German, Latin, and Notes).

Structure generated:
  docsrc/
    index.rst (Project Portal)
    de_divina_proportione/
      index.rst (Book Codex Root)
      compendio/
        index.rst
        cap_01/ .. cap_71/
          cap_NN_en.rst
          cap_NN_it.rst
          cap_NN_de.rst
          cap_NN_notes.rst
          <folio>.<gid>.png (exact chapter woodcut diagrams/initial)
      architectura/
        index.rst
        dedication/
          dedication_en.rst
          dedication_it.rst
          dedication_de.rst
          dedication_notes.rst
        cap_01/ .. cap_20/
          cap_NN_en.rst
          cap_NN_it.rst
          cap_NN_de.rst
          cap_NN_notes.rst
      plates/
        index.rst
        alphabet_en.rst
        alphabet_it.rst
        alphabet_de.rst
        architectural_en.rst
        architectural_it.rst
        architectural_de.rst
        polyhedra_en.rst
        polyhedra_la.rst
      bibliography.rst
      persons.rst
      glossary.rst
"""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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
BOOK_DIR = DOCSRC / "de_divina_proportione"


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


LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s+")


def normalize_rst_lists(text: str) -> str:
    """Ensure blank lines before and after nested or mixed bullet/enumerated lists for valid Docutils RST."""
    lines = text.splitlines()
    out: List[str] = []
    active_list_state: Optional[Tuple[int, str]] = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            out.append(line)
            active_list_state = None
            continue

        m = LIST_ITEM_RE.match(line)
        if m:
            indent = len(m.group(1))
            kind = "enum" if m.group(2)[0].isdigit() else "bullet"
            cur_state = (indent, kind)
            if out and out[-1].strip() and (active_list_state is None or active_list_state != cur_state):
                out.append("")
            out.append(line)
            active_list_state = cur_state
        else:
            indent = len(line) - len(line.lstrip())
            if active_list_state is not None and indent <= active_list_state[0]:
                if out and out[-1].strip():
                    out.append("")
                active_list_state = None
            out.append(line)

    return "\n".join(out)


def sanitize_ocr_text(text: str) -> str:
    """Sanitize raw OCR symbols (|/, |, _, *) in diplomatic Italian and German paragraphs so Docutils does not treat them as broken inline markup."""
    res = text.replace("|/", "√")
    res = res.replace("|", r"\|")
    res = res.replace("_", "")
    res = res.replace("*", r"\*")
    return res



def build_chapter_graphic_assignments(
    folios_conc: Dict[str, Dict[str, Any]],
) -> Tuple[Dict[Tuple[str, int], Optional[str]], Dict[Tuple[str, int], List[Dict[str, Any]]]]:
    """Assign each woodcut initial (c1..c4) and marginal diagram (g1..g8) on folios 0017..0082
    to its exact (part, chapter) based on chapter start order and vertical y-position.
    """
    initial_map: Dict[Tuple[str, int], Optional[str]] = {}
    diagram_map: Dict[Tuple[str, int], List[Dict[str, Any]]] = defaultdict(list)

    for fnum in range(17, 83):
        fstr = f"{fnum:04d}"
        finfo = folios_conc.get(fstr, {})
        chaps = finfo.get("chapters", [])
        if not chaps:
            continue
        gfx = finfo.get("graphics", [])
        inits = sorted(
            [g for g in gfx if g.get("type") == "initial"],
            key=lambda g: g.get("bbox", [0, 0, 0, 0])[1],
        )
        diags = sorted(
            [g for g in gfx if g.get("type") != "initial"],
            key=lambda g: g.get("bbox", [0, 0, 0, 0])[1],
        )

        # Match chapters starting on this folio with woodcut initials from bottom to top
        starting_chaps = [
            (c["part"], int(c["chapter"])) for c in chaps if c.get("starts_on_folio")
        ]
        chap_start_y: Dict[Tuple[str, int], int] = {}
        for ch_key, init_g in zip(reversed(starting_chaps), reversed(inits)):
            if ch_key not in initial_map:
                initial_map[ch_key] = init_g["file"]
            chap_start_y[ch_key] = init_g.get("bbox", [0, 0, 0, 0])[1]

        # Explicit y-thresholds for the 2 folios where a chapter starts without a woodcut initial
        if fstr == "0032":
            chap_start_y[("compendio", 26)] = 360
        elif fstr == "0036":
            chap_start_y[("compendio", 30)] = 800

        # Build ordered vertical thresholds for all chapters present on this folio
        ordered_chaps: List[Tuple[Tuple[str, int], int]] = []
        for idx, c in enumerate(chaps):
            ckey = (c["part"], int(c["chapter"]))
            y_start = 0 if idx == 0 else chap_start_y.get(ckey, 0)
            ordered_chaps.append((ckey, y_start))

        # Assign each marginal diagram to the chapter whose y_start <= diagram vertical center
        for d in diags:
            bbox = d.get("bbox", [0, 0, 0, 0])
            yc = bbox[1] + bbox[3] / 2.0
            assigned_key = ordered_chaps[0][0]
            for ckey, y_start in ordered_chaps:
                if yc >= y_start - 20:
                    assigned_key = ckey
            diagram_map[assigned_key].append(
                {
                    "file": d["file"],
                    "caption": d.get("caption", f"Folio {fstr} {d['id']}"),
                    "type": d.get("type", "diagram"),
                    "folio": fstr,
                }
            )

    return initial_map, diagram_map


def collect_chapter_graphics(
    part_prefix: str,
    ch: Dict[str, Any],
    folios_conc: Dict[str, Dict[str, Any]],
    initial_map: Dict[Tuple[str, int], Optional[str]],
    diagram_map: Dict[Tuple[str, int], List[Dict[str, Any]]],
    dest_dir: Path,
) -> Tuple[str, str, List[Dict[str, str]]]:
    """Copy the exact woodcut initial and marginal diagrams for a chapter into dest_dir and return
    (folio_range_label, folio_banner_str, copied_diagrams_list).
    """
    cnum = int(ch["chapter"])
    ckey = (part_prefix, cnum)
    start_f = ch["start_folio"]
    end_f = ch["end_folio"]
    orig_start = folios_conc[start_f]["original_folio"]
    orig_end = folios_conc[end_f]["original_folio"]
    folio_range_label = (
        f"{start_f} ({orig_start})"
        if start_f == end_f
        else f"{start_f}–{end_f} ({orig_start}–{orig_end})"
    )

    # Remove any stale .png files in dest_dir from earlier builds
    for old_png in dest_dir.glob("*.png"):
        old_png.unlink()

    initial_file = initial_map.get(ckey)
    if initial_file:
        src_p = PAG_DIR / initial_file
        if src_p.exists():
            shutil.copy2(src_p, dest_dir / initial_file)
        else:
            initial_file = None

    diagrams: List[Dict[str, str]] = []
    for d in diagram_map.get(ckey, []):
        gfile = d["file"]
        src_p = PAG_DIR / gfile
        if src_p.exists():
            shutil.copy2(src_p, dest_dir / gfile)
            diagrams.append(
                {
                    "file": gfile,
                    "caption": d["caption"],
                    "type": d["type"],
                }
            )

    folio_lines = [f".. folio:: {folio_range_label}"]
    if initial_file:
        folio_lines.append(f"   :initial: {initial_file}")
    folio_lines.append("")
    return folio_range_label, "\n".join(folio_lines), diagrams


def write_chapter_files(
    part_dir: Path,
    part_prefix: str,
    ch: Dict[str, Any],
    folios_conc: Dict[str, Dict[str, Any]],
    initial_map: Dict[Tuple[str, int], Optional[str]],
    diagram_map: Dict[Tuple[str, int], List[Dict[str, Any]]],
) -> Dict[str, str]:
    """Generate separate RST files (<slug>_en.rst, <slug>_it.rst, <slug>_de.rst, <slug>_notes.rst)
    for a chapter in Compendio or Architectura.
    """
    slug = ch["slug"]
    cnum = int(ch["chapter"])
    roman = ch["roman"]
    ch_dir = part_dir / slug
    ch_dir.mkdir(parents=True, exist_ok=True)

    # Remove legacy dummy index.rst stub if present so the 4 tracks are clean
    legacy_idx = ch_dir / "index.rst"
    if legacy_idx.exists():
        legacy_idx.unlink()

    folio_range_label, folio_banner, diagrams = collect_chapter_graphics(
        part_prefix, ch, folios_conc, initial_map, diagram_map, ch_dir
    )
    cap_label_it = f"CAPITOLO {roman}" if cnum > 0 else "PROHEMIO"
    cap_label_en = f"CHAPTER {roman}" if cnum > 0 else "DEDICATION"
    cap_label_de = f"CAPITEL {roman}" if cnum > 0 else "WIDMUNG"
    canonical_id = (
        (f"Cap. {roman}" if part_prefix == "compendio" else f"Arch. Cap. {roman}")
        if cnum > 0
        else "Arch. Prohemio"
    )

    title_it = ch["title_it"] or cap_label_it
    title_de = ch["title_de"] or cap_label_de

    if part_prefix == "compendio":
        t_data = COMPENDIO_TRANSLATIONS[cnum]
    else:
        t_data = ARCHITECTURA_CHAPTERS[cnum]

    title_en = t_data["title_en"]
    body_en = normalize_rst_lists(t_data["body_en"])
    philological_footer = (
        "\n\nPhilological and Folio Apparatus\n"
        "--------------------------------\n\n"
        f"- **1509 Paganini Witness Folios**: {', '.join(ch['folios'])} "
        f"({folios_conc[ch['start_folio']]['original_folio']}–{folios_conc[ch['end_folio']]['original_folio']})\n"
        f"- **Winterberg 1889 Italian Source**: ``{ch.get('winterberg_it', 'N/A')}``\n"
        f"- **Winterberg 1889 German Source**: ``{ch.get('winterberg_de', 'N/A')}``\n"
        f"- **Marginal Woodcut Diagrams**: {len(diagrams)} figure(s) extracted from the 1509 Venice witness.\n"
    )
    notes_body = normalize_rst_lists(t_data["notes"] + philological_footer)

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

    common_meta = [
        ":layout: book",
        f":canonical_id: {canonical_id}",
        f":folio: {folio_range_label}",
    ]

    # 1. Write <slug>_en.rst (Primary English Track)
    en_rst = "\n".join(
        [
            *common_meta,
            "",
            f".. _{part_prefix}-{slug}:",
            f".. _{part_prefix}-{slug}-en:",
            "",
            make_heading(cap_label_en, "="),
            f".. rubric:: {title_en}",
            "",
            folio_banner,
            body_en,
            diag_block,
        ]
    ).rstrip() + "\n"
    (ch_dir / f"{slug}_en.rst").write_text(en_rst, encoding="utf-8")

    # 2. Write <slug>_it.rst (Diplomatic 1509 Italian Track)
    it_rst = "\n".join(
        [
            *common_meta,
            "",
            f".. _{part_prefix}-{slug}-it:",
            "",
            make_heading(cap_label_it, "="),
            f".. rubric:: {title_it}",
            "",
            folio_banner,
            "\n\n".join(sanitize_ocr_text(p) for p in ch.get("paragraphs_it", [])),
            diag_block,
        ]
    ).rstrip() + "\n"
    (ch_dir / f"{slug}_it.rst").write_text(it_rst, encoding="utf-8")

    # 3. Write <slug>_de.rst (Winterberg 1889 German Track)
    de_rst = "\n".join(
        [
            *common_meta,
            "",
            f".. _{part_prefix}-{slug}-de:",
            "",
            make_heading(cap_label_de, "="),
            f".. rubric:: {title_de}",
            "",
            folio_banner,
            "\n\n".join(sanitize_ocr_text(p) for p in ch.get("paragraphs_de", [])),
            diag_block,
        ]
    ).rstrip() + "\n"
    (ch_dir / f"{slug}_de.rst").write_text(de_rst, encoding="utf-8")

    # 4. Write <slug>_notes.rst (Critical Commentary & Notes Track)
    notes_rst = "\n".join(
        [
            *common_meta,
            "",
            f".. _{part_prefix}-{slug}-notes:",
            "",
            make_heading(f"{cap_label_en} — Critical Commentary & Notes", "="),
            f".. rubric:: {title_en}",
            "",
            notes_body,
        ]
    ).rstrip() + "\n"
    (ch_dir / f"{slug}_notes.rst").write_text(notes_rst, encoding="utf-8")

    return {
        "slug": slug,
        "roman": roman,
        "chapter": cnum,
        "title_en": title_en,
        "title_it": title_it,
        "title_de": title_de,
        "folios_label": folio_range_label,
    }


def build_plates_section(conc: Dict[str, Any]) -> None:
    """Create separate language RST files in docsrc/de_divina_proportione/plates/
    for Alphabet, Architectural, and Polyhedra plates.
    """
    plates_dir = BOOK_DIR / "plates"
    plates_dir.mkdir(parents=True, exist_ok=True)

    for old_png in plates_dir.glob("*.png"):
        old_png.unlink()

    # Copy all plate graphics (g1..gN on 137..311) to docsrc/de_divina_proportione/plates/
    folios_conc = conc["folios"]
    for fnum in range(137, 312):
        fstr = f"{fnum:04d}"
        for g in folios_conc.get(fstr, {}).get("graphics", []):
            src_p = PAG_DIR / g["file"]
            if src_p.exists():
                shutil.copy2(src_p, plates_dir / g["file"])

    # 1. Alphabet Plates: alphabet_en.rst, alphabet_it.rst, alphabet_de.rst
    alpha_list = conc["plates"]["alphabet"]
    en_lines = [
        ":layout: book",
        ":canonical_id: Appendix I",
        ":folio: 0139–0183",
        "",
        ".. _plates-alphabet-en:",
        "",
        make_heading("Appendix I: The Roman Geometric Alphabet", "="),
        ".. rubric:: Constructive Proportions of the Twenty-Three Classical Capitals from the Circle and Square",
        "",
    ]
    it_lines = [
        ":layout: book",
        ":canonical_id: Appendix I",
        ":folio: 0139–0183",
        "",
        ".. _plates-alphabet-it:",
        "",
        make_heading("Appendice I: L'Alfabeto Geometrico Romano", "="),
        ".. rubric:: Proporzioni costruttive delle ventitré lettere maiuscole antiche dal cerchio e dal quadrato (1509)",
        "",
    ]
    de_lines = [
        ":layout: book",
        ":canonical_id: Appendix I",
        ":folio: 0139–0183",
        "",
        ".. _plates-alphabet-de:",
        "",
        make_heading("Anhang I: Das Geometrische Römische Alphabet", "="),
        ".. rubric:: Konstruktionsproportionen der dreiundzwanzig antiken Versalien aus Kreis und Quadrat (Winterberg 1889)",
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

    (plates_dir / "alphabet_en.rst").write_text("\n".join(en_lines), encoding="utf-8")
    (plates_dir / "alphabet_it.rst").write_text("\n".join(it_lines), encoding="utf-8")
    (plates_dir / "alphabet_de.rst").write_text("\n".join(de_lines), encoding="utf-8")

    # 2. Architectural Plates: architectural_en.rst, architectural_it.rst, architectural_de.rst
    arch_plates = conc["plates"]["architectural"]
    arch_en_texts = {
        "0137": "Divina Proportio: Proportional profile of the human head inscribed in the equilateral triangle and square grid (Tractato de l'Architectura, Cap. I–II).",
        "0185": "PORTA TEMPLI DOMINI DICTA SPECIOSA (The Gate of the Lord's Temple Called Beautiful): In the present figure of the gate called Speciosa, the two parts adduced here—namely the round column with its capital, base, stylobate, and stereobate, and the epistyle with its frieze (zophorus) and cornice—are duly presented to your discerning eye.",
        "0213": "Corinthian, Ionic, and Pulvinated Column with Stylobate (Pedestal) and Stereobate: Column called Corinthian with respect to its capital, abacus, and cymatium, and Ionic and pulvinated with respect to its base and capital, as Vitruvius explains in full, alongside modern columns in the Cathedral of Pisa and in Santo Spirito and San Lorenzo in Florence under the patronage of the House of Medici.",
        "0215": "Epistyle (Architrave), Zophorus (Frieze), and Cornice: The entire assembly below the frieze is called Epistylium by the Ancients and Architrave by the Moderns, and the assembly above it is called Cornice (with lettered mouldings a, c, e = Fascia; f = Echinus/Ovolo; g = Scotia/Gola; k = Cymatium; l = Dentils; m = Corona/Dripstone; o = Acroterium/Reglet).",
        "0311": "ARBOR PROPORTIO ET PROPORTIONALITAS (Tree of Ratio and Proportionality): Above all it pertains to the geometer to treat completely of proportions; for the arithmetician does not find the measure of ratio in all numbers, since there are infinitely many ratios which the nature of numbers does not admit, as is clear from Book V of Euclid's Elements. Just as unity is the head of number, so equality is the principle of proportions (Boethius, De institutione musica II, c. 15).",
    }
    for lang, suf, hdr_title, sub_rubric in [
        (
            "en",
            "en",
            "Appendix II: Architectural Plates & Arbor Proportionis",
            "Human Profile, Porta Speciosa, Corinthian/Ionic Column, Entablature, and the Tree of Proportions",
        ),
        (
            "it",
            "it",
            "Appendice II: Tavole d'Architettura e Arbor Proportionis",
            "Profilo umano, Porta Speciosa, Colonna Corinzia/Ionica, Trabeazione e Albero delle Proporzioni (1509)",
        ),
        (
            "de",
            "de",
            "Anhang II: Architekturtafeln und Arbor Proportionis",
            "Menschliches Profil, Porta Speciosa, Korinthisch-Ionische Säule, Gebälk und Stammbaum der Proportionen (1889)",
        ),
    ]:
        alines = [
            ":layout: book",
            ":canonical_id: Appendix II",
            ":folio: 0137, 0185, 0213, 0215, 0311",
            "",
            f".. _plates-architectural-{suf}:",
            "",
            make_heading(hdr_title, "="),
            f".. rubric:: {sub_rubric}",
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
        (plates_dir / f"architectural_{suf}.rst").write_text(
            "\n".join(alines), encoding="utf-8"
        )

    # 3. Polyhedra Plates: polyhedra_en.rst (English) and polyhedra_la.rst (Latin/Greek 1509 captions)
    poly_plates = conc["plates"]["polyhedra"]
    pen_lines = [
        ":layout: book",
        ":canonical_id: Appendix III",
        ":folio: 0187–0309",
        "",
        ".. _plates-polyhedra-en:",
        "",
        make_heading("Appendix III: Polyhedra Plates by Leonardo da Vinci", "="),
        ".. rubric:: Sixty Perspective Woodcuts of the Regular and Dependent Solids in Solid and Skeletal Views",
        "",
        "Sixty full-page woodcut plates of the Five Regular Platonic Solids and their Truncated (*abscisa*), "
        "Elevated/Stellated (*elevata*), and Prismatic/Pyramidal/Spherical Dependent Bodies in Solid (*planum/solidum*) "
        "and Skeletal (*vacuum*) perspective views, drawn by **Leonardo da Vinci**.",
        "",
    ]
    la_lines = [
        ":layout: book",
        ":canonical_id: Appendix III",
        ":folio: 0187–0309",
        "",
        ".. _plates-polyhedra-la:",
        "",
        make_heading("Appendix III: Tabulae Corporum Regularium et Dependentium", "="),
        ".. rubric:: Sexaginta Tabulae Corporum Geometricorum per Manum Leonardi Vincii Florentini (1509)",
        "",
        "Full-page woodcut plates designed by **Leonardo da Vinci** (*per mano del nostro Lionardo da Vinci Fiorentino*), "
        "carrying their original 1509 Latin and Greek cartouches.",
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

    (plates_dir / "polyhedra_en.rst").write_text("\n".join(pen_lines), encoding="utf-8")
    (plates_dir / "polyhedra_la.rst").write_text("\n".join(la_lines), encoding="utf-8")

    # 4. plates/index.rst
    p_idx = "\n".join(
        [
            ":layout: book",
            ":title: Appendices: Woodcut Plates (1509)",
            "",
            ".. _plates-index:",
            "",
            make_heading("Appendices: Woodcut Plates of the 1509 Paganini Edition", "="),
            ".. rubric:: Roman Geometric Alphabet, Architectural Plates, Arbor Proportionis, and Leonardo da Vinci's Sixty Polyhedra",
            "",
            "1. **Appendix I — The Roman Geometric Alphabet (Folios 0139–0183)**:\n"
            "   [:ref:`English <plates-alphabet-en>` · :ref:`Italiano (1509) <plates-alphabet-it>` · :ref:`Deutsch (1889) <plates-alphabet-de>`]",
            "2. **Appendix II — Architectural Plates & Arbor Proportionis (Folios 0137, 0185, 0213, 0215, 0311)**:\n"
            "   [:ref:`English <plates-architectural-en>` · :ref:`Italiano (1509) <plates-architectural-it>` · :ref:`Deutsch (1889) <plates-architectural-de>`]",
            "3. **Appendix III — Polyhedra Plates by Leonardo da Vinci (Plates I–LIX, Folios 0187–0309)**:\n"
            "   [:ref:`English <plates-polyhedra-en>` · :ref:`Latin / Greek (1509) <plates-polyhedra-la>`]",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Appendices (English Edition)",
            "",
            "   alphabet_en",
            "   architectural_en",
            "   polyhedra_en",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Companion Language Tracks",
            "",
            "   alphabet_it",
            "   alphabet_de",
            "   architectural_it",
            "   architectural_de",
            "   polyhedra_la",
            "",
        ]
    )
    (plates_dir / "index.rst").write_text(p_idx, encoding="utf-8")


def main() -> None:
    conc = json.loads((PAG_DIR / "concordance.json").read_text(encoding="utf-8"))
    folios_conc = conc["folios"]

    # Remove legacy top-level directories in docsrc/ so everything lives cleanly under docsrc/de_divina_proportione/
    for legacy_name in ("books", "compendio", "architectura", "plates", "glossary.rst"):
        legacy_p = DOCSRC / legacy_name
        if legacy_p.is_dir():
            shutil.rmtree(legacy_p)
        elif legacy_p.is_file():
            legacy_p.unlink()

    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    initial_map, diagram_map = build_chapter_graphic_assignments(folios_conc)

    # 1. Build Part I: Compendio de Divina Proportione (cap_01..cap_71)
    comp_dir = BOOK_DIR / "compendio"
    comp_dir.mkdir(parents=True, exist_ok=True)
    comp_chaps = conc["chapters"]["compendio"]
    comp_meta: List[Dict[str, str]] = []

    for ch in comp_chaps:
        m = write_chapter_files(
            comp_dir, "compendio", ch, folios_conc, initial_map, diagram_map
        )
        comp_meta.append(m)

    comp_idx_lines = [
        ":layout: book",
        ":title: Part I: Compendio de Divina Proportione",
        "",
        ".. _compendio-index:",
        "",
        make_heading("Part I: Compendio de Divina Proportione (Chapters I–LXXI)", "="),
        ".. rubric:: Dedicated to Ludovico Maria Sforza, Duke of Milan (Milan, 1498 / Venice, 1509)",
        "",
        "Dedicated to **Ludovico Maria Sforza**, Duke of Milan (completed at Milan, December 14, 1498; "
        "printed at Venice by Paganino de' Paganini, June 1, 1509). Each chapter is presented in four "
        "synchronized companion tracks: **English**, **Italiano (1509)**, **Deutsch (Winterberg 1889)**, and **Critical Notes**.",
        "",
        make_heading("Conspectus Capitum (Part I)", "-"),
    ]
    for m in comp_meta:
        slug = m["slug"]
        rom = m["roman"]
        comp_idx_lines.append(
            f"- **Cap. {rom}** (*Folio {m['folios_label']}*): {m['title_en']}\n"
            f"  [:ref:`English <compendio-{slug}-en>` · "
            f":ref:`Italiano <compendio-{slug}-it>` · "
            f":ref:`Deutsch <compendio-{slug}-de>` · "
            f":ref:`Notes <compendio-{slug}-notes>`]"
        )
    comp_idx_lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Chapters I–LXXI (English)",
            "",
        ]
    )
    for m in comp_meta:
        comp_idx_lines.append(f"   {m['slug']}/{m['slug']}_en")

    for suf, cap_hdr in [
        ("it", "Capitoli I–LXXI (Italiano 1509)"),
        ("de", "Capitel I–LXXI (Deutsch 1889)"),
        ("notes", "Chapters I–LXXI (Critical Notes)"),
    ]:
        comp_idx_lines.extend(
            [
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                "   :hidden:",
                f"   :caption: {cap_hdr}",
                "",
            ]
        )
        for m in comp_meta:
            comp_idx_lines.append(f"   {m['slug']}/{m['slug']}_{suf}")

    comp_idx_lines.append("")
    (comp_dir / "index.rst").write_text("\n".join(comp_idx_lines), encoding="utf-8")

    # 2. Build Part II: Tractato de l'Architectura (dedication + cap_01..cap_20)
    arch_dir = BOOK_DIR / "architectura"
    arch_dir.mkdir(parents=True, exist_ok=True)
    arch_chaps = conc["chapters"]["architectura"]
    arch_meta: List[Dict[str, str]] = []

    for ch in arch_chaps:
        m = write_chapter_files(
            arch_dir, "architectura", ch, folios_conc, initial_map, diagram_map
        )
        arch_meta.append(m)

    arch_idx_lines = [
        ":layout: book",
        ":title: Part II: Tractato de l'Architectura",
        "",
        ".. _architectura-index:",
        "",
        make_heading("Part II: Tractato de l'Architectura (Prohemio & Chapters I–XX)", "="),
        ".. rubric:: Dedicated to the Stonemasons, Sculptors, and Disciples of Borgo Sansepolcro (1509)",
        "",
        "Dedicated to Pacioli's beloved disciples and pupils of Borgo Sansepolcro (1509 Paganini Folios "
        "0061–0082, ``f. 23r``–``f. 33v``). Each chapter is presented in four synchronized companion "
        "tracks: **English**, **Italiano (1509)**, **Deutsch (Winterberg 1889)**, and **Critical Notes**.",
        "",
        make_heading("Conspectus Capitum (Part II)", "-"),
    ]
    for m in arch_meta:
        slug = m["slug"]
        lbl = f"Cap. {m['roman']}" if m["chapter"] > 0 else "Prohemio (Dedication)"
        arch_idx_lines.append(
            f"- **{lbl}** (*Folio {m['folios_label']}*): {m['title_en']}\n"
            f"  [:ref:`English <architectura-{slug}-en>` · "
            f":ref:`Italiano <architectura-{slug}-it>` · "
            f":ref:`Deutsch <architectura-{slug}-de>` · "
            f":ref:`Notes <architectura-{slug}-notes>`]"
        )
    arch_idx_lines.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Prohemio & Chapters I–XX (English)",
            "",
        ]
    )
    for m in arch_meta:
        arch_idx_lines.append(f"   {m['slug']}/{m['slug']}_en")

    for suf, cap_hdr in [
        ("it", "Prohemio & Capitoli I–XX (Italiano 1509)"),
        ("de", "Widmung & Capitel I–XX (Deutsch 1889)"),
        ("notes", "Prohemio & Chapters I–XX (Critical Notes)"),
    ]:
        arch_idx_lines.extend(
            [
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                "   :hidden:",
                f"   :caption: {cap_hdr}",
                "",
            ]
        )
        for m in arch_meta:
            arch_idx_lines.append(f"   {m['slug']}/{m['slug']}_{suf}")

    arch_idx_lines.append("")
    (arch_dir / "index.rst").write_text("\n".join(arch_idx_lines), encoding="utf-8")

    # 3. Build Plates section
    build_plates_section(conc)

    # 4. Write Book Codex root docsrc/de_divina_proportione/index.rst
    book_idx_lines = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        ":book_title: De Divina Proportione",
        ":book_subtitle: Fra Luca Pacioli • Venice 1509 / Vienna 1889",
        ":author: Fra Luca Pacioli",
        ":publisher: Paganinus de Paganinis de Brixia (Venice, 1509) / Constantin Winterberg (Vienna, 1889)",
        ":year: 1509",
        "",
        ".. _de-divina-proportione-index:",
        ".. _pacioli-index:",
        "",
        make_heading("DE DIVINA PROPORTIONE", "="),
        ".. rubric:: Fra Luca Pacioli (Venice, 1509) — Critical Multi-Language Digital Edition",
        "",
        "A unified digital edition of Fra Luca Pacioli's *De Divina Proportione* (Venice: Paganino de' "
        "Paganini, June 1, 1509), integrating the 318 high-resolution folio scans and 482 recalibrated "
        "woodcuts (214 illuminated initials, 180 marginal geometric diagrams, 23 Roman geometric alphabet "
        "plates, 5 architectural and *Arbor Proportionis* plates, and Leonardo da Vinci's 60 polyhedra "
        "plates) with four synchronized companion tracks:",
        "",
        "- **English (GEOMETOR Edition)**: Unabridged scholarly English translation with Euclidean dependency markup (``:just:``, ``:g:``, ``.. enunciation::``, ``.. assertion::``, ``.. qed::``, ``.. folio::``) across all chapters and plates.",
        "- **Italiano (1509 / 1889)**: Diplomatic Italian text from the 1509 Venice Paganini edition and Constantin Winterberg's 1889 Vienna edition.",
        "- **Deutsch (1889)**: Constantin Winterberg's German critical translation (*Quellenschriften für Kunstgeschichte*, Vienna, 1889).",
        "- **Notes & Commentary**: Historical, prosopographical, architectural, and mathematical apparatus for every chapter.",
        "",
        make_heading("Conspectus Totius Operis", "-"),
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
        "- **Scholarly Apparatus**: :ref:`Bibliography & Cited Works <bibliography>` · :ref:`Index of Persons <persons>` · :ref:`Technical Glossary <glossary>`",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :caption: Contents",
        "",
        "   compendio/index",
        "   architectura/index",
        "   plates/index",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Scholarly Apparatus",
        "",
        "   bibliography",
        "   persons",
        "   glossary",
        "",
    ]
    (BOOK_DIR / "index.rst").write_text("\n".join(book_idx_lines), encoding="utf-8")

    # 5. Write Project Portal docsrc/index.rst
    portal_lines = [
        ":title: GEOMETOR • pacioli",
        "",
        "Pacioli",
        "=======",
        "",
        ".. rubric:: Mathematical, Architectural & Proportional Works of Fra Luca Pacioli (c. 1447–1517)",
        "",
        "Digital critical editions, multi-language parallel translations, recalibrated 1509 woodcut graphics, "
        "and Euclidean dependency apparatus for the treatises of **Fra Luca Pacioli of Borgo Sansepolcro, O.F.M.**, "
        "illustrated by **Leonardo da Vinci**.",
        "",
        "----",
        "",
        "Works (*Opera*)",
        "---------------",
        "",
        ":doc:`De Divina Proportione (Venice, 1509 / Vienna, 1889) <de_divina_proportione/index>`",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "",
        "*Venetiis: Impressum per probum virum Paganinum de Paganinis de Brixia, Kalen. Iunii M.D.VIIII (1509) "
        "/ Quellenschriften für Kunstgeschichte, ed. Constantin Winterberg, Vienna, 1889.*",
        "",
        "Pacioli's foundational Renaissance treatise on the Golden Ratio (*proportione avente el mezzo e doi extremi*), "
        "the Thirteen Marvelous Effects of Euclid's Book XIII, the Five Platonic and Archimedean Solids drawn in "
        "perspective by **Leonardo da Vinci**, Vitruvian architecture, and the geometric construction of the Roman alphabet.",
        "",
        "* **Edition Parts**: :ref:`Conspectus Operis <de-divina-proportione-index>` · "
        ":ref:`Part I: Compendio (Cap. I–LXXI) <compendio-index>` · "
        ":ref:`Part II: Architectura (Prohemio & Cap. I–XX) <architectura-index>` · "
        ":ref:`Appendices: Woodcut Plates (Alphabet, Architecture, Polyhedra) <plates-index>`",
        "* **Language Tracks**: Synchronized **English**, **Italiano (1509)**, **Deutsch (1889)**, **Latin / Greek (1509)**, and **Critical Notes** with track-preserving navigation.",
        "* **Scholarly Apparatus**: :ref:`Bibliography & Cited Works <bibliography>` · "
        ":ref:`Index of Persons <persons>` · :ref:`Technical Glossary <glossary>`",
        "",
    ]
    (DOCSRC / "index.rst").write_text("\n".join(portal_lines), encoding="utf-8")

    print(
        f"Built multi-language Book Codex in {BOOK_DIR} with {len(comp_meta)} Compendio chapters, "
        f"{len(arch_meta)} Architectura chapters, and Plates section."
    )


if __name__ == "__main__":
    main()
