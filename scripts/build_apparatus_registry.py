#!/usr/bin/env python3
"""Enrich all 318 Paganini 1509 folio RST files (`resources/de_divina_proportione/paganini_1509/*.rst`
and `*.notes.rst`) and all book-track RST files (`docsrc/**/*.rst`) with `:person:`, `:term:`,
and `:cite:` roles, and generate the master apparatus registries (`citations.json`, `glossary.json`,
`persons.json`) in both:
  - `resources/de_divina_proportione/`
  - `resources/de_divina_proportione/paganini_1509/`

Idempotent: unwraps any previously applied `:person:`, `:term:`, or `:cite:` roles before
re-applying the canonical rules, and guarantees 0 Docutils errors or warnings.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Dict, List, Pattern, Tuple

from apparatus_catalogs import (
    AUTHOR_CATALOG,
    CITE_AUTHOR_TO_PERSONS,
    PERSON_CATALOG,
    TERM_CATALOG,
    WORK_TITLES,
)

ROOT = Path(__file__).resolve().parent.parent
RES_DIR = ROOT / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"
DOCSRC_DIR = ROOT / "docsrc"

HEADING_CHARS = set("=-~^\"'+*#`:._")

ROMAN_NUMERALS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
}

ITALIAN_BOOK_TO_ROMAN = {
    "primo": "I",
    "1°": "I",
    "secondo": "II",
    "2°": "II",
    "tertio": "III",
    "terzo": "III",
    "3°": "III",
    "quarto": "IV",
    "4°": "IV",
    "quinto": "V",
    "5°": "V",
    "sexto": "VI",
    "sesto": "VI",
    "6°": "VI",
    "septimo": "VII",
    "settimo": "VII",
    "7°": "VII",
    "octavo": "VIII",
    "ottavo": "VIII",
    "8°": "VIII",
    "nono": "IX",
    "9°": "IX",
    "decimo": "X",
    "10°": "X",
    "undecimo": "XI",
    "vndecimo": "XI",
    "l'undecimo": "XI",
    "11°": "XI",
    "duodecimo": "XII",
    "12°": "XII",
    "terzodecimo": "XIII",
    "decimo tertio": "XIII",
    "decimotertio": "XIII",
    "13°": "XIII",
    "quartodecimo": "XIV",
    "decimo quarto": "XIV",
    "decimoquarto": "XIV",
    "14°": "XIV",
    "quintodecimo": "XV",
    "decimo quinto": "XV",
    "decimoquinto": "XV",
    "15°": "XV",
}

ITALIAN_ORDINAL_TO_NUM = {
    "prima": "1",
    "1ª": "1",
    "seconda": "2",
    "seconsta": "2",
    "2ª": "2",
    "tertia": "3",
    "terza": "3",
    "3ª": "3",
    "quarta": "4",
    "4ª": "4",
    "quinta": "5",
    "5ª": "5",
    "sexta": "6",
    "sesta": "6",
    "6ª": "6",
    "septima": "7",
    "settima": "7",
    "7ª": "7",
    "octava": "8",
    "ottava": "8",
    "8ª": "8",
    "nona": "9",
    "9ª": "9",
    "decima": "10",
    "10ª": "10",
    "undecima": "11",
    "vndecima": "11",
    "11ª": "11",
    "duodecima": "12",
    "12ª": "12",
    "terzadecima": "13",
    "decimatertia": "13",
    "decimaterza": "13",
    "13ª": "13",
    "quartadecima": "14",
    "decimaquarta": "14",
    "14ª": "14",
    "quintadecima": "15",
    "decimaquinta": "15",
    "15ª": "15",
    "sextadecima": "16",
    "decimasexta": "16",
    "16ª": "16",
    "decimaseptima": "17",
    "17ª": "17",
    "decimaoctava": "18",
    "18ª": "18",
    "decimanona": "19",
    "19ª": "19",
    "vigesima": "20",
    "20ª": "20",
    "vigesimaprima": "21",
    "21ª": "21",
    "vigesimaseconda": "22",
    "vigesimaterza": "23",
    "vigesimaquarta": "24",
    "vigesimaquinta": "25",
    "vigesimasexta": "26",
    "vigesimaseptima": "27",
    "vigesimaoctava": "28",
    "vigesimanona": "29",
    "trigesima": "30",
    "30ª": "30",
    "trigesimaprima": "31",
    "trigesimaseconda": "32",
    "32ª": "32",
    "trigesimaterza": "33",
    "tregesimaterza": "33",
    "trigesimaquarta": "34",
    "trigesimaquinta": "35",
    "trigesimasexta": "36",
    "36ª": "36",
    "quadragesimaseptima": "47",
    "47ª": "47",
    "penultima": "47",
}

UNWRAP_ROLE_RE = re.compile(r":(?:person|term|cite):`([^`<>]+?)\s*<[^`<>]+>`")
JUST_ROLE_RE = re.compile(r":just:`([IVX]+\.[a-zA-Z0-9.–-]+)`")


def strip_existing_apparatus_roles(text: str) -> str:
    """Idempotently unwrap any previously inserted :person:, :term:, or :cite: roles."""
    prev = None
    cur = text
    while prev != cur:
        prev = cur
        cur = UNWRAP_ROLE_RE.sub(lambda m: m.group(1), cur)
    return cur


def is_heading_underline(line: str) -> bool:
    s = line.strip()
    return len(s) >= 3 and len(set(s)) == 1 and s[0] in HEADING_CHARS


# Protected spans in plain text: existing roles, inline code, links, math, and emphasis/strong spans
PROTECTED_SPAN_RE = re.compile(
    r"(?:"
    r":[a-zA-Z0-9_-]+:`[^`]+`"  # existing RST roles (:just:, :g:, :ref:, :doc:, :person:, :term:, :cite:)
    r"|``[^`]+``"  # inline literal
    r"|`[^`]+`_"  # RST hyperlink
    r"|\$[^$\n]+\$"  # inline math
    r"|\*\*[^*\n]+\*\*"  # bold span (handled atomically)
    r"|\*[^*\n]+\*"  # italic span (handled atomically)
    r")"
)


def build_citation_rules() -> List[Tuple[Pattern[str], Any]]:
    """Build regex rules for :cite:`display <target>`."""
    rules: List[Tuple[Pattern[str], Any]] = []

    # 1. Dynamic Italian Euclidean proposition citations: e.g. "per la 11ª del secondo", "per la penultima del primo", "per la 32 del primo"
    ord_keys = sorted(ITALIAN_ORDINAL_TO_NUM.keys(), key=len, reverse=True)
    book_keys = sorted(ITALIAN_BOOK_TO_ROMAN.keys(), key=len, reverse=True)
    ord_pat = "|".join(re.escape(k) for k in ord_keys) + r"|\d+ª|\d+"
    book_pat = "|".join(re.escape(k) for k in book_keys)

    def _it_euclid_prop(m: re.Match[str]) -> str:
        full = m.group(0)
        ord_raw = m.group("ord").lower()
        bk_raw = re.sub(r"\s+", " ", m.group("bk").lower().strip())
        pnum = ITALIAN_ORDINAL_TO_NUM.get(ord_raw)
        if not pnum:
            digits = re.sub(r"\D", "", ord_raw)
            pnum = digits or "1"
        brom = ITALIAN_BOOK_TO_ROMAN.get(bk_raw, "I")
        return f":cite:`{full} <euclid:elements:{brom}.{pnum}>`"

    rules.append(
        (
            re.compile(
                rf"\b(?:per la|la|nela|dela)\s+(?P<ord>{ord_pat})\s+(?:propositione\s+|conclusione\s+)?(?:del|de\s*l'|de\s+lo|dello)\s+(?:(?:dicto|ditto|detto|suo)\s+)?(?P<bk>{book_pat})\b",
                re.I,
            ),
            _it_euclid_prop,
        )
    )

    # 2. Dynamic Italian Euclidean book citations: e.g. "nel sexto libro", "nel terzodecimo libro"
    def _it_euclid_book(m: re.Match[str]) -> str:
        full = m.group(0)
        bk_raw = re.sub(r"\s+", " ", m.group("bk").lower().strip())
        brom = ITALIAN_BOOK_TO_ROMAN.get(bk_raw, "I")
        return f":cite:`{full} <euclid:elements:{brom}>`"

    rules.append(
        (
            re.compile(
                rf"\b(?:nel|del)\s+(?P<bk>{book_pat})\s+libro(?:\s+de\s+Euclide)?\b",
                re.I,
            ),
            _it_euclid_book,
        )
    )

    # 3. Dynamic German Euclidean proposition citations: e.g. "nach dem 11. Satze des 2. Buches", "nach dem 30. Satze des 6. Buches"
    def _de_euclid_prop(m: re.Match[str]) -> str:
        full = m.group(0)
        pnum = m.group("prop")
        bnum = int(m.group("bk"))
        brom = ROMAN_NUMERALS.get(bnum, str(bnum))
        return f":cite:`{full} <euclid:elements:{brom}.{pnum}>`"

    rules.append(
        (
            re.compile(
                r"\bnach\s+dem\s+(?P<prop>\d+)\.\s*Satze?\s+des\s+(?P<bk>\d+)\.\s*Buches\b",
                re.I,
            ),
            _de_euclid_prop,
        )
    )

    # 4. Dynamic English / German / Notes Euclidean locus citations: e.g. "Euclid XIII.1", "Euklid XIII.3", "Elements VI.def.3", "Campanus IX.16"
    def _en_euclid_prop(m: re.Match[str]) -> str:
        full = m.group(0)
        brom = m.group("bk")
        prop = m.group("prop")
        return f":cite:`{full} <euclid:elements:{brom}.{prop}>`"

    rules.append(
        (
            re.compile(
                r"\b(?:Euclid|Euklid|Elements|Elemente)\s+(?P<bk>I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV)\.(?P<prop>(?:def\.\d+|\d+(?:[–-]\d+)?))\b"
            ),
            _en_euclid_prop,
        )
    )

    def _en_euclid_book_named(m: re.Match[str]) -> str:
        full = m.group(0)
        brom = m.group("bk")
        return f":cite:`{full} <euclid:elements:{brom}>`"

    rules.append(
        (
            re.compile(
                r"\b(?:Euclid|Euklid),?\s+(?:Book\s+(?P<bk>I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV)|(?P<bk2>I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV)\.\s*Buch(?:es)?)\b"
            ),
            lambda m: f":cite:`{m.group(0)} <euclid:elements:{m.group('bk') or m.group('bk2')}>`",
        )
    )

    def _en_campanus_loc(m: re.Match[str]) -> str:
        full = m.group(0)
        bk = m.group("bk")
        prop = m.group("prop")
        return f":cite:`{full} <campanus:euclid:{bk}.{prop}>`"

    rules.append(
        (
            re.compile(
                r"\bCampanus\s+(?P<bk>I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV)\.(?P<prop>\d+(?:[–-]\d+)?)\b"
            ),
            _en_campanus_loc,
        )
    )

    def _en_vitruvius_loc(m: re.Match[str]) -> str:
        full = m.group(0)
        bk = m.group("bk")
        ch = m.group("ch")
        return f":cite:`{full} <vitruvius:de-arch:{bk}.{ch}>`"

    rules.append(
        (
            re.compile(
                r"\bVitruvius\s+(?P<bk>I|II|III|IV|V|VI|VII|VIII|IX|X)\.(?P<ch>\d+(?:[–-]\d+)?)\b"
            ),
            _en_vitruvius_loc,
        )
    )

    # 5. Static work & locus citations
    static_cites = [
        (r"\bnach dem vorletzten Satze des ersten Buches\b", "euclid:elements:I.47"),
        (r"\blibro de li Elementi\b", "euclid:elements"),
        (r"\blibri de li Elementi\b", "euclid:elements"),
        (r"\bBook XIV,\s*Proposition 2\b", "hypsicles:liber-xiv:2"),
        (r"\bXIV\.\s*Buch(?:es)?,\s*Satz\s*2\b", "hypsicles:liber-xiv:2"),
        (r"\bElementa Liber XIV\b", "hypsicles:liber-xiv"),
        (r"\bin primo gradu certitudinis\b", "averroes:met:II.16"),
        (r"\bQuam sine fictione didici, et sine invidia communico\b", "biblia:sapientia:7.13"),
        (r"\bquod ne sine figmento didici et sine inuidia libenter communico\b", "biblia:sapientia:7.13"),
        (r"\bWisdom 7:13\b", "biblia:sapientia:7.13"),
        (r"\bomnia in numero, pondere et mensura\b", "biblia:sapientia:11.21"),
        (r"\bWisdom 11:21\b", "biblia:sapientia:11.21"),
        (r"\bIn Coelo et Mundo\b", "aristotle:de-caelo:III.8"),
        (r"\bDe Celo e Mundo\b", "aristotle:de-caelo:III.8"),
        (r"\bDe Caelo et Mundo\b", "aristotle:de-caelo:III.8"),
        (r"\bDe Caelo\b", "aristotle:de-caelo:III.8"),
        (r"\bVom Himmel und der Welt\b", "aristotle:de-caelo:III.8"),
        (r"\bAnalytica Posteriora\b", "aristotle:anal-post:I.7"),
        (r"\bPosterior Analytics\b", "aristotle:anal-post:I.7"),
        (r"\bNicomachean Ethics\b", "aristotle:eth-nic:V.3"),
        (r"\bEthica Nicomachea\b", "aristotle:eth-nic:V.3"),
        (r"\bMetaphysica\b", "aristotle:met:II"),
        (r"\bMetaphysics\b", "aristotle:met:II"),
        (r"\bDe Anima\b", "aristotle:de-anima:II"),
        (r"\bMeteorologica\b", "aristotle:meteor:III"),
        (r"\bnel suo Timeo\b", "plato:timaeus:53c-56c"),
        (r"\bTimaeus\b", "plato:timaeus:53c-56c"),
        (r"\bTimeo\b", "plato:timaeus:53c-56c"),
        (r"\bTimäus\b", "plato:timaeus:53c-56c"),
        (r"\bSumma de Arithmetica, Geometria, Proportioni et Proportionalita\b", "pacioli:summa"),
        (r"\bSumma d[ei] [Aa]rithmetica\b", "pacioli:summa"),
        (r"\bnostra grande opera\b", "pacioli:summa"),
        (r"\bgrandopera nostra\b", "pacioli:summa"),
        (r"\bDivina Proportione:\s*Die Lehre vom Goldenen Schnitt\b", "winterberg:divina-proportione-1889"),
        (r"\bCompendio de Divina Proportione\b", "pacioli:divina-proportione"),
        (r"\bDe [Dd]ivina [Pp]roportione\b", "pacioli:divina-proportione"),
        (r"\bTractato de l'Architectura\b", "pacioli:architectura"),
        (r"\bLibellus,?\s+Tract(?:ate|\.)\s*II,?\s+Cas(?:e|\.)\s*20\b", "pacioli:libellus:II.20"),
        (r"\bLibellus de [Qq]uinque [Cc]orporibus [Rr]egularibus\b", "piero:libellus"),
        (r"\bTractatus de [Qq]uinque [Cc]orporibus [Rr]egularibus\b", "piero:libellus"),
        (r"\bDe [Qq]uinque [Cc]orporibus [Rr]egularibus\b", "piero:libellus"),
        (r"\bTractat über die fünf regelmässigen Körper\b", "piero:libellus"),
        (r"\bTreatise on the Five Regular Bodies\b", "piero:libellus"),
        (r"\bCod\.?\s*Vat\.?\s*Lat\.?\s*3129\b", "piero:cod-vat-lat-3129"),
        (r"\bVat\.?\s*Urb\.?\s*[Ll]at\.?\s*632\b", "piero:libellus"),
        (r"\bDe Prospectiva Pingendi\b", "piero:prospectiva"),
        (r"\bDe Re Aedificatoria\b", "alberti:de-re-aedificatoria"),
        (r"\bDe Architectura\b", "vitruvius:de-arch"),
        (r"\bElementa Euclidis cum Commentariis Campani\b", "campanus:euclid"),
        (r"\bDimensio Circuli\b", "archimedes:dimensio-circuli"),
        (r"\bDe Sphaera et Cylindro\b", "archimedes:sphaera"),
        (r"\bDe Institutione Musica\b", "boethius:musica:II.15"),
        (r"\bDe Institutione Arithmetica\b", "boethius:arithmetica"),
        (r"\bAlmagesto?\b", "ptolemy:almagest:I.9"),
        (r"\bCosmographia\b", "ptolemy:cosmographia"),
        (r"\bDe Civitate Dei\b", "augustine:de-civitate-dei:XVI.23"),
        (r"\bEtymologiae\b", "isidore:etymologiae:III"),
        (r"\bnel secondo dele Sententie\b", "scotus:sententiae:II"),
        (r"\bDe Natura Deorum\b", "cicero:de-natura-deorum:I.60"),
        (r"\bNaturalis Historia\b", "pliny:naturalis-historia:XXXVI"),
        (r"\bEpitoma Rei Militaris\b", "vegetius:de-re-militari"),
        (r"\bStrategemata\b", "frontinus:strategemata"),
        (r"\bStratagematon\b", "frontinus:strategemata"),
        (r"\bTeberina\b", "bartolus:tyberiadis"),
        (r"\bTyberiadis\b", "bartolus:tyberiadis"),
        (r"\blibro de pictura e mo[uv]imenti humani\b", "leonardo:pittura"),
        (r"\bTrattato della Pittura\b", "leonardo:pittura"),
        (r"\bBook of Painting\b", "leonardo:pittura"),
        (r"\bDas Malerbuch Lionardo da Vinci's\b", "winterberg:malerbuch-1887"),
        (r"\bJahrbücher der königlich preussischen Kunstsammlungen\b", "winterberg:malerbuch-1887"),
        (r"\bMalerbuch(?:es)?\b", "leonardo:pittura"),
        (r"\bDas Buch von der Malerei\b", "ludwig:buch-von-der-malerei"),
        (r"\bdel moto locale,? dele percussioni e pesi\b", "leonardo:moto-locale"),
        (r"\bQuellenschriften für Kunstgeschichte(?: und Kunsttechnik des Mittelalters und der Neuzeit)?\b", "eitelberger:quellenschriften"),
        (r"\bHistoire des sciences mathématiques en Italie\b", "libri:histoire:III"),
        (r"\bHist\.\s*des\s*sc\.\s*math\.", "libri:histoire:III"),
        (r"\bHistoire des mathématiques\b", "montucla:histoire"),
        (r"\bHist\.\s*des\s*math\.", "montucla:histoire"),
        (r"\b(?:Le\s+)?Vite(?:\s+de'\s+più\s+eccellenti\s+pittori,\s+scultori,\s+e\s+architettori)?\b", "vasari:vite"),
        (r"\b(?:I\s+)?Sette Libri dell'Architettura\b", "serlio:architettura"),
        (r"\bNeue Lehre von den Proportionen des menschlichen Körpers\b", "zeising:proportionen"),
        (r"\bDie männliche und weibliche Normalgestalt\b", "brocheneck:normalgestalt"),
        (r"\bLehrbuch der plastischen Anatomie\b", "harless:anatomie"),
        (r"\bDie Proportionslehre der menschlichen Gestalt\b", "carus:proportionslehre"),
        (r"\bProportionsschlüssel(?::\s*Neues System der Verhältnisse des menschlichen Körpers)?\b", "schmidt:proportionsschluessel"),
        (r"\bSur l'homme\b", "quetelet:anthropometrie"),
        (r"\bAnthropométrie\b", "quetelet:anthropometrie"),
        (r"\bDie Proportionslehre Dürer's(?:\s+nach ihren wesentlichen Bestimmungen in übersichtlicher Darstellung)?\b", "trost:proportionslehre"),
        (r"\bGeneral[ -]Trattato di (?:Numeri et Misure|Matematiche)\b", "tartaglia:general-trattato"),
        (r"\bM\.\s*Vitruvii per Iocundum solito castigatior factus\b", "giocondo:vitruvius"),
        (r"\bApologia(?: degli Accademici di Banchi di Roma)?\b", "caro:apologia"),
        (r"\bSynagoge\b", "pappus:synagoge:V"),
        (r"\bHarmonices Mundi\b", "kepler:harmonices-mundi"),
    ]
    for pat_str, target in static_cites:
        rules.append((re.compile(pat_str), target))

    return rules


def build_person_rules() -> List[Tuple[Pattern[str], str]]:
    """Build regex rules for :person:`display <slug>` across Italian, Latin, German, and English."""
    raw_patterns: List[Tuple[str, str]] = [
        # Authors & Philosophers (specific multi-word distinctions first)
        (r"\bEuclid\s+of\s+Megara\b", "euclid-of-megara"),
        (r"\bEuklid\s+von\s+Megara\b", "euclid-of-megara"),
        (r"\bEuclid\s+of\s+Alexandria\b", "euclid"),
        (r"\bEuklid\s+von\s+Alexandria\b", "euclid"),
        (r"\bEuclide\s+Megarense\b", "euclid"),
        (r"\bEuclidis\s+Megarensis\b", "euclid"),
        (r"\bEuclidae\b", "euclid"),
        (r"\bEuclide\b", "euclid"),
        (r"\bEuklid(?:'s|s|ischen|ische)?\b", "euclid"),
        (r"\bEuclid\b", "euclid"),
        (r"\bPlatone\b", "plato"),
        (r"\bPlatonis\b", "plato"),
        (r"\bPlaton(?:s)?\b", "plato"),
        (r"\bPlato\b", "plato"),
        (r"\bAristotile\b", "aristotle"),
        (r"\bAristotele\b", "aristotle"),
        (r"\bAristotil\b", "aristotle"),
        (r"\bAristoteles\b", "aristotle"),
        (r"\bAristotle\b", "aristotle"),
        (r"\bArchimede\s+Siracusano\b", "archimedes"),
        (r"\bArchimede\b", "archimedes"),
        (r"\bArchimedes\b", "archimedes"),
        (r"\bVi[ct]*ru[uv]io\b", "vitruvius"),
        (r"\bVitruv(?:'s|s)?\b", "vitruvius"),
        (r"\bVitruvius\b", "vitruvius"),
        (r"\bBoet(?:h)?io\b", "boethius"),
        (r"\bBoethius\b", "boethius"),
        (r"\bCampano\b", "campanus"),
        (r"\bCampanus(?:\s+of\s+Novara|\s+von\s+Novara)?\b", "campanus"),
        (r"\bPtolomeo\b", "ptolemy"),
        (r"\bTolomeo\b", "ptolemy"),
        (r"\bPtolemäus\b", "ptolemy"),
        (r"\bPtolemy\b", "ptolemy"),
        (r"\bPythagora\b", "pythagoras"),
        (r"\bPitagora\b", "pythagoras"),
        (r"\bPythagoras\b", "pythagoras"),
        (r"\bPietro\s+de\s+li\s+Franceschi\b", "piero-della-francesca"),
        (r"\bPiero\s+della\s+Francesca(?:'s)?\b", "piero-della-francesca"),
        (r"\bPietro\s+della\s+Francesca(?:'s)?\b", "piero-della-francesca"),
        (r"\bPietro\s+Franceschi\b", "piero-della-francesca"),
        (r"\bLeon\s*Ba[pt]*ista\s+de\s*li\s+Alberti\b", "alberti"),
        (r"\bLeon\s+Battista\s+Alberti\b", "alberti"),
        (r"\bL\.\s*B\.\s*Alberti(?:'s)?\b", "alberti"),
        (r"\bAlberti(?:'s|s)?\b", "alberti"),
        (r"\bL[eio]onardo\s+da\s+[Vv][ie]nci(?:\s+Fiorentino)?(?:'s)?\b", "leonardo"),
        (r"\bLeonardo\s+da\s+Vinci(?:'s)?\b", "leonardo"),
        (r"\bFra\s+Luca\s+Pacioli(?:'s)?\b", "pacioli"),
        (r"\bLuca\s+Pacioli(?:'s)?\b", "pacioli"),
        (r"\bLucas\s+Paciolus\b", "pacioli"),
        (r"\bPacioli(?:'schen|'sche|'s|s)?\b", "pacioli"),
        # Winterberg & 1889 Apparatus Authorities
        (r"\bConstantin\s+Winterberg\b", "winterberg"),
        (r"\bWinterberg(?:'s|s)?\b", "winterberg"),
        (r"\bRudolf\s+Eitelberger\s+von\s+Edelberg\b", "rudolf-von-eitelberger"),
        (r"\bRudolf\s+von\s+Eitelberger\b", "rudolf-von-eitelberger"),
        (r"\bHofrath\s+(?:von|v\.)\s+Eitelberger\b", "rudolf-von-eitelberger"),
        (r"\bR\.\s*v\.\s*Eitelberger\b", "rudolf-von-eitelberger"),
        (r"\bEitelberger\b", "rudolf-von-eitelberger"),
        (r"\bHeinrich\s+Ludwig\b", "heinrich-ludwig"),
        (r"\bH\.\s*Ludwig\b", "heinrich-ludwig"),
        (r"\bAlbert\s+Ilg\b", "albert-ilg"),
        (r"\bCarl\s+Graeser\b", "carl-graeser"),
        (r"\bCarl\s+Fromme\b", "carl-fromme"),
        (r"\bGuillaume\s+Libri\b", "guillaume-libri"),
        (r"\bLibri\b", "guillaume-libri"),
        (r"\bJean-Étienne\s+Montucla\b", "montucla"),
        (r"\bMontucla\b", "montucla"),
        (r"\bGiorgio\s+Vasari(?:'s)?\b", "vasari"),
        (r"\bVasari(?:'s|s)?\b", "vasari"),
        (r"\bSebastiano\s+Serlio\b", "serlio"),
        (r"\bSerlio\b", "serlio"),
        (r"\bAdolf\s+Zeising(?:'s)?\b", "adolf-zeising"),
        (r"\bA\.\s*Zeising(?:'s)?\b", "adolf-zeising"),
        (r"\bZeising(?:'s|s)?\b", "adolf-zeising"),
        (r"\bBrocheneck\b", "brocheneck"),
        (r"\bEmil\s+Harless\b", "emil-harless"),
        (r"\bE\.\s*Harless\b", "emil-harless"),
        (r"\bHarless\b", "emil-harless"),
        (r"\bCarl\s+Gustav\s+Carus\b", "carl-gustav-carus"),
        (r"\bC\.\s*G\.\s*Carus\b", "carl-gustav-carus"),
        (r"\bCarus\b", "carl-gustav-carus"),
        (r"\bCarl\s+Schmidt\b", "carl-schmidt"),
        (r"\bC\.\s*Schmidt\b", "carl-schmidt"),
        (r"\bAdolphe\s+Quetelet\b", "adolphe-quetelet"),
        (r"\bQuetelet\b", "adolphe-quetelet"),
        (r"\bJohann\s+Jacob\s+Trost\b", "j-j-trost"),
        (r"\bJ\.\s*J\.\s*Trost\b", "j-j-trost"),
        (r"\bTrost\b", "j-j-trost"),
        (r"\bNiccol[òo]\s+Tartaglia(?:'s)?\b", "niccolo-tartaglia"),
        (r"\bTartaglia(?:'s|s)?\b", "niccolo-tartaglia"),
        (r"\bFra\s+(?:Giovanni\s+)?Giocondo(?:\s+of\s+Verona|\s+von\s+Verona|\s+da\s+Verona)?\b", "fra-giocondo"),
        (r"\bGiovanni\s+Giocondo\b", "fra-giocondo"),
        (r"\bAnn?ibale\s+Caro(?:'s)?\b", "annibale-caro"),
        (r"\bJohannes\s+Kepler\b", "johannes-kepler"),
        (r"\bKepler\b", "johannes-kepler"),
        (r"\bSan\s+Rocco\b", "san-rocco"),
        (r"\bSaint\s+Roch\b", "san-rocco"),
        (r"\bSt\.\s+Roch(?:us)?\b", "san-rocco"),
        (r"\bheil(?:igen|\.)\s+Rochus\b", "san-rocco"),
        (r"\bKing\s+Ferrante(?:\s+of\s+Naples)?\b", "ferrante-of-naples"),
        (r"\bKönig\s+Ferrante\b", "ferrante-of-naples"),
        (r"\bRe\s+Ferrante\b", "ferrante-of-naples"),
        (r"\bFerdinand\s+I\s+of\s+Naples\b", "ferrante-of-naples"),
        (r"\bFerrante\b", "ferrante-of-naples"),
        # Renaissance Patrons & Interlocutors
        (r"\bLudo[uv]ico\s+Maria\s+Sforza(?:\s+Anglo)?\b", "ludovico-sforza"),
        (r"\bLudo[uv]ico\s+Sforza\b", "ludovico-sforza"),
        (r"\bLudovico\s+il\s+Moro\b", "ludovico-sforza"),
        (r"\bGaleazzo\s+(?:Sforza\s+VI\.\s+)?San\s*[Ss]e[uv]erino\b", "galeazzo-sanseverino"),
        (r"\bGaleazzo\s+da\s+San\s+Severino\b", "galeazzo-sanseverino"),
        (r"\bSan\s*[Ss]e[uv]erino\b", "galeazzo-sanseverino"),
        (r"\bFrancesco\s+Soderini\b", "francesco-soderini"),
        (r"\bCardinale\s+Volterrano\b", "francesco-soderini"),
        (r"\bVolaterranus\b", "francesco-soderini"),
        (r"\bTommaso\s+Soderini\b", "tommaso-soderini"),
        (r"\bThomas\s+Soderinus\b", "tommaso-soderini"),
        (r"\bGiovan\s+Battista\s+Soderini\b", "giovan-battista-soderini"),
        (r"\bGiovan\s+Vittorio\s+Soderini\b", "giovan-vittorio-soderini"),
        (r"\bIoannes\s+Victorius\s+Soderinus\b", "giovan-vittorio-soderini"),
        (r"\bPetro\s+Soderino\b", "piero-soderini"),
        (r"\bPiero\s+Soderini\b", "piero-soderini"),
        (r"\bSoderini\b", "piero-soderini"),
        (r"\bGuidobaldo(?:\s+da\s+Montefeltro)?\b", "guidobaldo"),
        (r"\bGuido\s+Ubaldo\b", "guidobaldo"),
        (r"\bFederico\s+da\s+Montefeltro\b", "federico-da-montefeltro"),
        (r"\bFederigo\s+da\s+Montefeltro\b", "federico-da-montefeltro"),
        (r"\bFeltrensis\b", "federico-da-montefeltro"),
        (r"\bFrancesco\s+Sforza\b", "francesco-sforza"),
        (r"\bDanielis\s+Caietani(?:\s+Cremonensis)?\b", "daniele-gaetani"),
        (r"\bDaniele\s+Gaetani\b", "daniele-gaetani"),
        (r"\bAntonio\s+Capella\b", "antonio-capella"),
        (r"\bPaganinum\s+de\s+Paganinis(?:\s+de\s+Brixia)?\b", "paganino-de-paganini"),
        (r"\bPaganino\s+de'\s+Paganini\b", "paganino-de-paganini"),
        (r"\bPaganino\s+de\s+Paganini\b", "paganino-de-paganini"),
        (r"\bAndrea\s+Mocenigo\b", "andrea-mocenigo"),
        (r"\bAndreas\s+Mocenigo\b", "andrea-mocenigo"),
        (r"\bLeonardo\s+Mocenigo\b", "leonardo-mocenigo"),
        (r"\bLeonardus\s+Mocenigo\b", "leonardo-mocenigo"),
        (r"\bLeonardo\s+Loredan\b", "leonardo-loredan"),
        (r"\bLeonardus\s+Lauredanus\b", "leonardo-loredan"),
        (r"\bFrancesco\s+Pepi\b", "francesco-pepi"),
        (r"\bFranciscus\s+Pepius\b", "francesco-pepi"),
        (r"\bFrancesco\s+Sansone\b", "francesco-sansone"),
        (r"\bFranciscus\s+Sanson\b", "francesco-sansone"),
        (r"\bGaleotto\s+(?:Franciotti\s+)?della\s+Rovere\b", "galeotto-della-rovere"),
        (r"\bGirolamo\s+Riario\b", "girolamo-riario"),
        (r"\bHieronymo\s+Riario\b", "girolamo-riario"),
        (r"\bMario\s+Mellini\b", "mario-mellini"),
        (r"\bMario\s+Melini\b", "mario-mellini"),
        (r"\bMelozzo(?:\s+da\s+Forlì)?\b", "melozzo-da-forli"),
        (r"\bGiulio\s+II\b", "julius-ii"),
        (r"\bJulius\s+II\b", "julius-ii"),
        (r"\bPaulo\s+II\b", "paul-ii"),
        (r"\bPaolo\s+II\b", "paul-ii"),
        (r"\bPaul\s+II\b", "paul-ii"),
        (r"\bSan\s+Francesco\b", "francis-of-assisi"),
        (r"\bFrancis\s+of\s+Assisi\b", "francis-of-assisi"),
        (r"\b(?:Magistro|Maestro|Magister)\s+Gometi(?:o|us)\b", "gometius"),
        (r"\bGomez\s+de\s+Lisboa\b", "gometius"),
        (r"\bGometi(?:o|us)\b", "gometius"),
        (r"\bDomenico\s+(?:per\s+cognomento\s+)?[Pp]onzone\b", "domenico-ponzone"),
        (r"\bPonzone\b", "domenico-ponzone"),
        (r"\bFrancesco\s+[Bb]usti\b", "francesco-busti"),
        (r"\bBusti\b", "francesco-busti"),
        (r"\bAmbrosio\s+da\s+Rosate\b", "ambrogio-da-rosate"),
        (r"\bAmbrogio\s+(?:Varese\s+)?da\s+Rosate\b", "ambrogio-da-rosate"),
        (r"\bAmbrogio\s+rosa\b", "ambrogio-da-rosate"),
        (r"\bAl[ou]isi(?:o)?\s+Marlian[io]\b", "aloisio-marliani"),
        (r"\bMarliani\b", "aloisio-marliani"),
        (r"\bGabriel(?:e)?\s+[Pp]iro[uv]ano\b", "gabriele-pirovano"),
        (r"\bPirovano\b", "gabriele-pirovano"),
        (r"\bNicol[òo]\s+Cusano\b", "nicolo-cusano"),
        (r"\bAndrea\s+(?:da\s+Novara|no[uv]arese)\b", "andrea-da-novara"),
        (r"\b(?:Giacomo|Iacomo)\s+Andrea\s+da\s+Fer+ara\b", "giacomo-andrea"),
        (r"\bJakob\s+Andrea\s+von\s+Ferrara\b", "giacomo-andrea"),
        (r"\bA[uv]erro(?:is|è|es)\b", "averroes"),
        (r"\bA[uv]icenna\b", "avicenna"),
        (r"\bGalieno\b", "galen"),
        (r"\bGaleno\b", "galen"),
        (r"\bGalen\b", "galen"),
        (r"\bYpocrate\b", "hippocrates"),
        (r"\bIppocrate\b", "hippocrates"),
        (r"\bHippokrates\b", "hippocrates"),
        (r"\bHippocrates\b", "hippocrates"),
        (r"\bSerapione\b", "serapion"),
        (r"\bSerapion\b", "serapion"),
        (r"\bAugustino\b", "augustine"),
        (r"\bAgostino\b", "augustine"),
        (r"\bAugustinus\b", "augustine"),
        (r"\bAugustine(?:\s+of\s+Hippo)?\b", "augustine"),
        (r"\bIsidoro\b", "isidore"),
        (r"\bIsidorus\b", "isidore"),
        (r"\bIsidore(?:\s+of\s+Seville)?\b", "isidore"),
        (r"\bGio(?:v)?anni\s+[Ss]coto\b", "duns-scotus"),
        (r"\bDuns\s+Scoto\b", "duns-scotus"),
        (r"\bDuns\s+Scotus\b", "duns-scotus"),
        (r"\bThoma\s+d'Aquino\b", "thomas-aquinas"),
        (r"\bThomas\s+von\s+Aquino?\b", "thomas-aquinas"),
        (r"\bThomas\s+Aquinas\b", "thomas-aquinas"),
        (r"\bAlberto\s+Magno\b", "albertus-magnus"),
        (r"\bAlbertus\s+Magnus\b", "albertus-magnus"),
        (r"\bDion[yi]sio\b", "dionysius"),
        (r"\bDionigi\b", "dionysius"),
        (r"\bDionysius\b", "dionysius"),
        (r"\bIesu\s+Christo\b", "jesus-christ"),
        (r"\bGesù\s+Cristo\b", "jesus-christ"),
        (r"\bJesus\s+Christ\b", "jesus-christ"),
        (r"\bPhidia\b", "phidias"),
        (r"\bFidias?\b", "phidias"),
        (r"\bPhidias\b", "phidias"),
        (r"\bPra[xs]itell?[eo]\b", "praxiteles"),
        (r"\bPrassitele\b", "praxiteles"),
        (r"\bPraxiteles\b", "praxiteles"),
        (r"\bApelle\b", "apelles"),
        (r"\bApelles\b", "apelles"),
        (r"\bParrhasio\b", "parrhasius"),
        (r"\bParrasio\b", "parrhasius"),
        (r"\bParrhasius\b", "parrhasius"),
        (r"\bMyrone\b", "myron"),
        (r"\bMirone\b", "myron"),
        (r"\bMyron\b", "myron"),
        (r"\bPol[yi]c[lr]eto\b", "polykleitos"),
        (r"\bPolykleitos\b", "polykleitos"),
        (r"\bPolyklet\b", "polykleitos"),
        (r"\bCallimacho\b", "callimachus"),
        (r"\bCallimaco\b", "callimachus"),
        (r"\bKallimachos\b", "callimachus"),
        (r"\bCallimachus\b", "callimachus"),
        (r"\bZeu[zs][eo]\b", "zeuxis"),
        (r"\bZeusi\b", "zeuxis"),
        (r"\bZeuxis\b", "zeuxis"),
        (r"\bDinocrate\b", "dinocrates"),
        (r"\bDinocrates\b", "dinocrates"),
        (r"\bDiogneto\b", "diognetus"),
        (r"\bDiognetus\b", "diognetus"),
        (r"\bEpimacho\b", "epimachus"),
        (r"\bEpimachus\b", "epimachus"),
        (r"\bCallia\b", "callias"),
        (r"\bCallias\b", "callias"),
        (r"\bChersiphron\b", "chersiphron"),
        (r"\bMetagenes\b", "metagenes"),
        (r"\bBramante\b", "bramante"),
        (r"\bAndrea\s+Mantegna\b", "andrea-mantegna"),
        (r"\bMantegna\b", "andrea-mantegna"),
        (r"\bIulio\s+Cesar[eo]\b", "julius-caesar"),
        (r"\bGiulio\s+Cesare\b", "julius-caesar"),
        (r"\bJulius\s+Cäsar\b", "julius-caesar"),
        (r"\bJulius\s+Caesar\b", "julius-caesar"),
        (r"\bOctaviano\b", "augustus"),
        (r"\bOttaviano\b", "augustus"),
        (r"\bAugustus\b", "augustus"),
        (r"\bNerone\b", "nero"),
        (r"\bNero\b", "nero"),
        (r"\bHierone\b", "hiero"),
        (r"\bGerone\b", "hiero"),
        (r"\bHiero\b", "hiero"),
        (r"\bIone\b", "ion"),
        (r"\bIon\b", "ion"),
        (r"\bAlexandro\s+Magno\b", "alexander-the-great"),
        (r"\bAlessandro\s+Magno\b", "alexander-the-great"),
        (r"\bAlexander\s+the\s+Great\b", "alexander-the-great"),
        (r"\bMarcell(?:o|us)\b", "marcellus"),
        (r"\bDemetrio\s+Poliorcete\b", "demetrius-poliorcetes"),
        (r"\bDemetrius\s+Poliorcetes\b", "demetrius-poliorcetes"),
        (r"\bDemetrio\b", "demetrius-poliorcetes"),
        (r"\bVegetio\b", "vegetius"),
        (r"\bVegetius\b", "vegetius"),
        (r"\b[Ff]rontino\b", "frontinus"),
        (r"\bFrontinus\b", "frontinus"),
        (r"\bRoberto\s+[Vv]alturr?i(?:o)?\b", "roberto-valturio"),
        (r"\bValturio\b", "roberto-valturio"),
        (r"\bSigismondo\s+(?:Pandolfo\s+)?Malatesta\b", "sigismondo-malatesta"),
        (r"\bTito\s+Li[uv]io\b", "livy"),
        (r"\bLivius\b", "livy"),
        (r"\bLivy\b", "livy"),
        (r"\bTullio\b", "cicero"),
        (r"\bCicerone\b", "cicero"),
        (r"\bCicero\b", "cicero"),
        (r"\bPlinio\b", "pliny"),
        (r"\bPlinius\b", "pliny"),
        (r"\bPliny\b", "pliny"),
        (r"\bStrabone\b", "strabo"),
        (r"\bStrabo\b", "strabo"),
        (r"\bMarino\b", "marinus-of-tyre"),
        (r"\bMarinus(?:\s+of\s+Tyre)?\b", "marinus-of-tyre"),
        (r"\bAlbumasar\b", "albumasar"),
        (r"\bAlfragan(?:us|o)\b", "alfraganus"),
        (r"\bGeber\b", "geber"),
        (r"\bAlfonso\s+X(?:\s+of\s+Castile)?\b", "alfonso-x"),
        (r"\bAlfonso\s+re\s+di\s+Spagna\b", "alfonso-x"),
        (r"\bGiovanni\s+Bianchini\b", "giovanni-bianchini"),
        (r"\bBianchini\b", "giovanni-bianchini"),
        (r"\bProsdocimo(?:\s+de'\s+Beldomandi)?\b", "prosdocimo-beldomandi"),
        (r"\bProdocimo\b", "prosdocimo-beldomandi"),
        (r"\bSimonide\b", "simonides"),
        (r"\bSimonides\b", "simonides"),
        (r"\bNicomach(?:o|um|us)\b", "nicomachus"),
        (r"\bC(?:h)?alcidio\b", "chalcidius"),
        (r"\bChalcidius\b", "chalcidius"),
        (r"\bApuleio\b", "apuleius"),
        (r"\bApuleius\b", "apuleius"),
        (r"\bMacrobio\b", "macrobius"),
        (r"\bMacrobius\b", "macrobius"),
        (r"\bBartolo\s+da\s+Sassoferrato\b", "bartolus"),
        (r"\bBartolus(?:\s+of\s+Sassoferrato)?\b", "bartolus"),
        (r"\bBartolo\b", "bartolus"),
        (r"\bAlfonso\s+d'Este\b", "alfonso-d-este"),
        (r"\bAlphonsus\s+Estensis\b", "alfonso-d-este"),
        (r"\bIppolito\s+d'Este\b", "ippolito-deste"),
        (r"\bHippolytus\s+Estensis\b", "ippolito-deste"),
        (r"\bGiuliano\s+da\s+Sangallo\b", "giuliano-da-sangallo"),
        (r"\bIuliano\s+da\s+San\s+Gallo\b", "giuliano-da-sangallo"),
        (r"\bAntonio\s+del\s+Pollaiuolo\b", "antonio-pollaiuolo"),
        (r"\bAntonio\s+Pollaiolo\b", "antonio-pollaiuolo"),
        (r"\bPollaiuolo\b", "antonio-pollaiuolo"),
        (r"\bDomenico\s+Ghirlandaio\b", "domenico-ghirlandaio"),
        (r"\bGhirlandaio\b", "domenico-ghirlandaio"),
        (r"\bSandro\s+Botticelli\b", "sandro-botticelli"),
        (r"\bSandro\s+di\s+Botticello\b", "sandro-botticelli"),
        (r"\bBotticelli\b", "sandro-botticelli"),
        (r"\bFilippino\s+Lippi\b", "filippino-lippi"),
        (r"\bAndrea\s+del\s+Verrocchio\b", "andrea-del-verrocchio"),
        (r"\bVerrocchio\b", "andrea-del-verrocchio"),
        (r"\bBenedetto\s+da\s+Maiano\b", "benedetto-da-maiano"),
        (r"\bBernardo\s+Rossellino\b", "bernardo-rossellino"),
        (r"\bLorenzo\s+Canozi(?:\s+da\s+Lendinara)?\b", "lorenzo-canozi"),
        (r"\bLorenzo\s+da\s+Lendinara\b", "lorenzo-canozi"),
        (r"\bGiovan\s+Marco\s+Canozi\b", "giovan-marco-canozi"),
        (r"\bGiovan\s+Marco\s+da\s+Lendinara\b", "giovan-marco-canozi"),
        (r"\bCamillo\s+Vitelli\b", "camillo-vitelli"),
        (r"\bGian\s+Giacomo\s+Trivulzio\b", "gian-giacomo-trivulzio"),
        (r"\bIacomo\s+Tri[uv]ultio\b", "gian-giacomo-trivulzio"),
        (r"\bGiovanni\s+(?:Gioviano\s+)?Pontano\b", "giovanni-pontano"),
        (r"\bPontano\b", "giovanni-pontano"),
        (r"\bPier\s+Vettori\b", "pier-vettori"),
        (r"\bPiero\s+del\s+Tovaglia\b", "piero-del-tovaglia"),
        (r"\bTovaglia\b", "piero-del-tovaglia"),
        (r"\bCatano\s+Catani\b", "catano-catani"),
        (r"\bCiriaco\s+[Pp]alamides\b", "ciriaco-palamides"),
        (r"\bPalamides\b", "ciriaco-palamides"),
        (r"\bSalomone\b", "solomon"),
        (r"\bSalomon\b", "solomon"),
        (r"\bSolomon\b", "solomon"),
        (r"\bHypsicles\b", "hypsicles"),
        (r"\bIpsicle\b", "hypsicles"),
        (r"\bTheaetetus\b", "theaetetus"),
        (r"\bTeeteto\b", "theaetetus"),
        (r"\bPappus(?:\s+of\s+Alexandria)?\b", "pappus"),
        (r"\bPappo\b", "pappus"),
        (r"\bFibonacci\b", "fibonacci"),
        (r"\bLeonardo\s+Pisano\b", "fibonacci"),
        # Short-name fallbacks (placed after all multi-word names sharing these given names)
        (r"\bL[ei]onardo(?:'s|s)?\b", "leonardo"),
        (r"\bPiero(?:'s)?\b", "piero-della-francesca"),
    ]
    return [(re.compile(pat), slug) for pat, slug in raw_patterns]


def build_term_rules() -> List[Tuple[Pattern[str], str]]:
    """Build regex rules for :term:`display <slug>` across Latin, Greek, Italian, German, and English."""
    raw_patterns: List[Tuple[str, str]] = [
        # Composite Polyhedra (Latin & Greek) - longer matches first
        (r"\bTetrahedron\s+abscisum\b", "tetrahedron-abscisum"),
        (r"\bΤετράεδρον\s+ἀποτετμημένον\b", "tetrahedron-abscisum"),
        (r"\bTetrahedron\s+elevatum\b", "tetrahedron-elevatum"),
        (r"\bΤετράεδρον\s+ἐπηρμένον\b", "tetrahedron-elevatum"),
        (r"\bExahedron\s+abscisum\s+elevatum\b", "exahedron-abscisum-elevatum"),
        (r"\bἙξάεδρον\s+ἀποτετμημένον\s+ἐπηρμένον\b", "exahedron-abscisum-elevatum"),
        (r"\bExahedron\s+abscisum\b", "exahedron-abscisum"),
        (r"\bἙξάεδρον\s+ἀποτετμημένον\b", "exahedron-abscisum"),
        (r"\bcuboctahedron\b", "exahedron-abscisum"),
        (r"\bExahedron\s+elevatum\b", "exahedron-elevatum"),
        (r"\bἙξάεδρον\s+ἐπηρμένον\b", "exahedron-elevatum"),
        (r"\bOctahedron\s+abscisum\b", "octahedron-abscisum"),
        (r"\bὈκτάεδρον\s+ἀποτετμημένον\b", "octahedron-abscisum"),
        (r"\bOctahedron\s+elevatum\b", "octahedron-elevatum"),
        (r"\bὈκτάεδρον\s+ἐπηρμένον\b", "octahedron-elevatum"),
        (r"\bStella\s+Octangula\b", "octahedron-elevatum"),
        (r"\bIcosahedron\s+abscisum\b", "icosahedron-abscisum"),
        (r"\bΕἰκοσάεδρον\s+ἀποτετμημένον\b", "icosahedron-abscisum"),
        (r"\bIcosahedron\s+elevatum\b", "icosahedron-elevatum"),
        (r"\bΕἰκοσάεδρον\s+ἐπηρμένον\b", "icosahedron-elevatum"),
        (r"\bDodecahedron\s+abscisum\s+elevatum\b", "dodecahedron-abscisum-elevatum"),
        (r"\bΔωδεκάεδρον\s+ἀποτετμημένον\s+ἐπηρμένον\b", "dodecahedron-abscisum-elevatum"),
        (r"\bDodecahedron\s+abscisum\b", "dodecahedron-abscisum"),
        (r"\bΔωδεκάεδρον\s+ἀποτετμημένον\b", "dodecahedron-abscisum"),
        (r"\bicosidodecahedron\b", "dodecahedron-abscisum"),
        (r"\bDodecahedron\s+elevatum\b", "dodecahedron-elevatum"),
        (r"\bΔωδεκάεδρον\s+ἐπηρμένον\b", "dodecahedron-elevatum"),
        (r"\bVigintisex\s+basium\s+elevatum\b", "vigintisex-basium-elevatum"),
        (r"\bΕἰκοσιεξάεδρον\s+ἐπηρμένον\b", "vigintisex-basium-elevatum"),
        (r"\bVigintisex\s+basium\b", "vigintisex-basium"),
        (r"\bΕἰκοσιεξάεδρον\b", "vigintisex-basium"),
        (r"\brhombicuboctahedron\b", "vigintisex-basium"),
        (r"\bcorpo\s+de\s+(?:26|vintisei)\s+basi\b", "vigintisex-basium"),
        (r"\bSeptuaginta\s+duarum\s+basium\b", "septuaginta-duarum-basium"),
        (r"\bἙβδομηκονταδισσάεδρον\b", "septuaginta-duarum-basium"),
        (r"\bcorpo\s+de\s+(?:72|settantadoi)\s+basi\b", "septuaginta-duarum-basium"),
        (r"\bColumna\s+laterata\s+triangula\b", "corpo-seratile"),
        (r"\bΚίων\s+πλευρώδης\s+τρίγωνος\b", "corpo-seratile"),
        (r"\bΣχῆμα\s+πριστόν\b", "corpo-seratile"),
        (r"\bcorpo\s+seratile\b", "corpo-seratile"),
        (r"\bcorpi\s+seratili\b", "corpo-seratile"),
        (r"\bColumna\s+laterata\s+quadrilatera\b", "colonna-quadrilatera"),
        (r"\bΚίων\s+πλευρώδης\s+τετράπλευρος\b", "colonna-quadrilatera"),
        (r"\bColumna\s+laterata\s+pentagona\b", "colonna-pentagona"),
        (r"\bΚίων\s+πλευρώδης\s+πεντάγωνος\b", "colonna-pentagona"),
        (r"\bColumna\s+laterata\s+exagona\b", "colonna-exagona"),
        (r"\bΚίων\s+πλευρώδης\s+ἑξάγωνος\b", "colonna-exagona"),
        (r"\bPyramis\s+laterata\s+triangula\b", "pyramide-triangula"),
        (r"\bΠυραμὶς\s+πλευρώδης\s+τρίγωνος\b", "pyramide-triangula"),
        (r"\bPyramis\s+laterata\s+quadrilatera\b", "pyramide-quadrilatera"),
        (r"\bΠυραμὶς\s+πλευρώδης\s+τετράπλευρος\b", "pyramide-quadrilatera"),
        (r"\bPyramis\s+laterata\s+pentagona\b", "pyramide-pentagona"),
        (r"\bΠυραμὶς\s+πλευρώδης\s+πεντάγωνος\b", "pyramide-pentagona"),
        (r"\bPyramis\s+laterata\s+exagona\b", "pyramide-exagona"),
        (r"\bΠυραμὶς\s+πλευρώδης\s+ἑξάγωνος\b", "pyramide-exagona"),
        (r"\bColumna\s+rotunda\b", "colonna-rotonda"),
        (r"\bΚίων\s+στρογγύλος\b", "colonna-rotonda"),
        (r"\bcolonne?\s+rotonde?\b", "colonna-rotonda"),
        (r"\bcolonne?\s+laterate?\b", "colonna-laterata"),
        (r"\bPyramis\s+rotunda\b", "pyramide-rotonda"),
        (r"\bΠυραμὶς\s+στρογγύλη\b", "pyramide-rotonda"),
        (r"\bpyramidi?\s+rotonde?\b", "pyramide-rotonda"),
        (r"\bpyramidi?\s+laterate?\b", "pyramide-laterata"),
        (r"\bpyramidi?\s+corte?\b", "pyramide-corta"),
        # Base Regular Solids & Modifiers
        (r"\bTetrahedron\b", "tetrahedron"),
        (r"\btetracedron\b", "tetrahedron"),
        (r"\bΤετράεδρον\b", "tetrahedron"),
        (r"\btetrahedron\b", "tetrahedron"),
        (r"\bTetraeder(?:s|n)?\b", "tetrahedron"),
        (r"\bExahedron\b", "exahedron"),
        (r"\bexacedron\b", "exahedron"),
        (r"\bἙξάεδρον\b", "exahedron"),
        (r"\bhexahedron\b", "exahedron"),
        (r"\bHexaeder(?:s|n)?\b", "exahedron"),
        (r"\bOctahedron\b", "octahedron"),
        (r"\boctocedron\b", "octahedron"),
        (r"\bὈκτάεδρον\b", "octahedron"),
        (r"\boctahedron\b", "octahedron"),
        (r"\bOktaeder(?:s|n)?\b", "octahedron"),
        (r"\bIcosahedron\b", "icosahedron"),
        (r"\bycocedron\b", "icosahedron"),
        (r"\bicocedron\b", "icosahedron"),
        (r"\bΕἰκοσάεδρον\b", "icosahedron"),
        (r"\bicosahedron\b", "icosahedron"),
        (r"\bIkosaeder(?:s|n)?\b", "icosahedron"),
        (r"\bDodecahedron\b", "dodecahedron"),
        (r"\bduodecedron\b", "dodecahedron"),
        (r"\bΔωδεκάεδρον\b", "dodecahedron"),
        (r"\bdodecahedron\b", "dodecahedron"),
        (r"\bDodekaeder(?:s|n)?\b", "dodecahedron"),
        (r"\bPlanum\b", "planum"),
        (r"\bplanum\b", "planum"),
        (r"\bἐπίπεδον\b", "planum"),
        (r"\bSolidum\b", "solidum"),
        (r"\bsolidum\b", "solidum"),
        (r"\bστερεόν\b", "solidum"),
        (r"\bVacuum\b", "vacuum"),
        (r"\bvacuum\b", "vacuum"),
        (r"\bκενόν\b", "vacuum"),
        (r"\bAbscisum\b", "abscisum"),
        (r"\babscisum\b", "abscisum"),
        (r"\bἀποτετμημένον\b", "abscisum"),
        (r"\babscisi\b", "abscisum"),
        (r"\bscapezzi\b", "abscisum"),
        (r"\bElevatum\b", "elevatum"),
        (r"\belevatum\b", "elevatum"),
        (r"\bἐπηρμένον\b", "elevatum"),
        (r"\bpontuti\b", "elevatum"),
        (r"\bSphaera\b", "spera"),
        (r"\bΣφαῖρα\b", "spera"),
        (r"\bspera\b", "spera"),
        # Core Proportion & Mathematical Terms
        (r"\bdivina\s+proportione\b", "divina-proportione"),
        (r"\bDivina\s+Proportione\b", "divina-proportione"),
        (r"\bProportione\s+divina\b", "divina-proportione"),
        (r"\bDivine\s+Proportion\b", "divina-proportione"),
        (r"\bgöttlichen?\s+Proportion\b", "divina-proportione"),
        (r"\bGoldene[nr]?\s+Schnitt(?:es|e|s)?\b", "goldener-schnitt"),
        (r"\bGolden\s+Section\b", "goldener-schnitt"),
        (r"\bPol\s+und\s+Polare\b", "pol-und-polare"),
        (r"\bpole\s+and\s+polar\b", "pol-und-polare"),
        (r"\breciproke[nr]?\s+Körper\b", "reciproke-koerper"),
        (r"\breciprocal\s+(?:solid\s+)?bodies\b", "reciproke-koerper"),
        (r"\bKanon(?:s)?\b", "kanon"),
        (r"\bin\s+agibilibus\b", "in-agibilibus"),
        (r"\bCeneraccio\b", "ceneraccio"),
        (r"\bproportione\s+avente\s+el\s+mezzo\s+e\s+doi\s+extremi\b", "extrema-et-media-ratio"),
        (r"\bextreme\s+and\s+mean\s+ratio\b", "extrema-et-media-ratio"),
        (r"\bproportione\s+continua\b", "proportione-continua"),
        (r"\bcontinuous\s+proportion\b", "proportione-continua"),
        (r"\bstetige[nr]?\s+Proportion\b", "proportione-continua"),
        (r"\bproportione\s+discontinua\b", "proportione-discontinua"),
        (r"\bArbor\s+Proportio\s+et\s+Proportionalitas\b", "arbor-proportionis"),
        (r"\bproportionalità\b", "proportionalitas"),
        (r"\bProportionalitas\b", "proportionalitas"),
        (r"\bsexquialtera\b", "sexquialtera"),
        (r"\bsesquialtera\b", "sexquialtera"),
        (r"\bsexquitertia\b", "sexquitertia"),
        (r"\bsesquitertia\b", "sexquitertia"),
        (r"\bsuperparticularis\b", "superparticularis"),
        (r"\bsuperparticolare\b", "superparticularis"),
        (r"\bsuperpartiens\b", "superpartiens"),
        (r"\bmultiplex\b", "multiplex"),
        (r"\bquinta\s+essentia\b", "quinta-essentia"),
        (r"\bfifth\s+essence\b", "quinta-essentia"),
        (r"\bquintessence\b", "quinta-essentia"),
        (r"\bcimento\s+e\s+copella\b", "cimento-e-copella"),
        (r"\btouchstone\s+and\s+assaying-cup\b", "cimento-e-copella"),
        (r"\bcorpi\s+regulari\b", "corpi-regulari"),
        (r"\bcorpora\s+regularia\b", "corpi-regulari"),
        (r"\bcorpi\s+dependenti\b", "corpi-dependenti"),
        (r"\bquantità\s+continua\b", "quantita-continua"),
        (r"\bquantità\s+discreta\b", "quantita-discreta"),
        (r"\bradice\s+universale\b", "radice-universale"),
        (r"\bradice\s+legata\b", "radice-universale"),
        (r"\balgebra\s+e\s+almucabala\b", "algebra-e-almucabala"),
        (r"\bregola\s+de\s+la\s+cosa\b", "algebra-e-almucabala"),
        (r"\bcenso\s+de\s+censo\b", "censo-de-censo"),
        (r"\blinea\s+minore\b", "linea-minore"),
        (r"\bresiduo\b", "residuo"),
        (r"\bapotome\b", "residuo"),
        (r"\bbinomio\b", "binomio"),
        (r"\bincommensurabil[ei]\b", "irrationale"),
        (r"\birrational[ei]\b", "irrationale"),
        (r"\bcommensurabil[ei]\b", "rationale"),
        (r"\bpotentia\b", "potentia"),
        (r"\bypothesi\b", "ypothesi"),
        (r"\bypotumissa\b", "ypotumissa"),
        (r"\bhypotenusa\b", "ypotumissa"),
        (r"\bcorausto\b", "corausto"),
        (r"\bcoraustus\b", "corausto"),
        (r"\bcono\s+dela\s+pyramide\b", "cono-pyramidale"),
        (r"\bcorda\s+pentagonica\b", "corda-pentagonica"),
        (r"\bcatheto\b", "catheto"),
        (r"\bcatheti\b", "catheto"),
        (r"\bperpendiculare\b", "catheto"),
        (r"\bdyametro\b", "dyametro"),
        (r"\bparalellogramo\b", "paralellogramo"),
        (r"\bparallelogram\b", "paralellogramo"),
        (r"\bdiagonale\b", "diagonale"),
        (r"\bsaetta\b", "saetta"),
        (r"\bsagitta\b", "saetta"),
        (r"\belmuhaym\b", "elmuhaym"),
        (r"\belmuariffe\b", "elmuariffe"),
        (r"\btetragono\s+longo\b", "tetragono-longo"),
        (r"\bangulo\s+solido\b", "angulo-solido"),
        (r"\bagnoli\s+solidi\b", "angulo-solido"),
        (r"\bsolid\s+angles?\b", "angulo-solido"),
        (r"\bangulo\s+dela\s+iustitia\b", "angulo-dela-iustitia"),
        (r"\bAngle\s+of\s+Justice\b", "angulo-dela-iustitia"),
        (r"\bangulo\s+recto\b", "angulo-recto"),
        (r"\bangulo\s+acuto\b", "angulo-acuto"),
        (r"\bangulo\s+obtuso\b", "angulo-obtuso"),
        (r"\bquadratura\s+del\s+cerchio\b", "quadratura-del-cerchio"),
        (r"\bgnomone\b", "gnomone"),
        (r"\bgnomon\b", "gnomone"),
        (r"\bisoscele\b", "isoscele"),
        (r"\bysopleuro\b", "equilatero"),
        (r"\bequilatero\b", "equilatero"),
        (r"\bscaleno\b", "scaleno"),
        (r"\borthogonio\b", "orthogonio"),
        (r"\bambliogonio\b", "ambliogonio"),
        (r"\boxigonio\b", "oxigonio"),
        (r"\bpentagono\b", "pentagono"),
        (r"\bexagono\b", "exagono"),
        (r"\bdecagono\b", "decagono"),
        (r"\boctagono\b", "octagono"),
        (r"\btetragono\b", "tetragono"),
        (r"\bsemicirculo\b", "semicirculo"),
        (r"\bcirconferentia\b", "circonferentia"),
        (r"\bquadrivio\b", "quadrivio"),
        (r"\bQuadrivium\b", "quadrivio"),
        (r"\bperspectiva\b", "perspectiva"),
        (r"\bprospectiva\b", "perspectiva"),
        (r"\barithmetica\b", "arithmetica"),
        (r"\bgeometria\b", "geometria"),
        (r"\bastronomia\b", "astronomia"),
        (r"\bcosmographia\b", "cosmographia"),
        # Architectural & Typographic Terms
        (r"\bPorta\s+Templi\s+Domini\s+dicta\s+Speciosa\b", "porta-speciosa"),
        (r"\bPorta\s+Speciosa\b", "porta-speciosa"),
        (r"\bepistilio\b", "epistilio"),
        (r"\barchitrave\b", "epistilio"),
        (r"\bzophoro\b", "zophoro"),
        (r"\bfregio\b", "zophoro"),
        (r"\bcornicione\b", "cornicione"),
        (r"\bstilobata\b", "stilobata"),
        (r"\bpilastrello\b", "stilobata"),
        (r"\bbasamento\b", "stilobata"),
        (r"\bsteriobata\b", "steriobata"),
        (r"\bstereobate\b", "steriobata"),
        (r"\bstylobate\b", "stilobata"),
        (r"\bcapitello\b", "capitello"),
        (r"\babaco\b", "abaco"),
        (r"\bechino\b", "echino"),
        (r"\bhuovolo\b", "echino"),
        (r"\bscothia\b", "scothia"),
        (r"\btrochilo\b", "scothia"),
        (r"\bdenticeli\b", "denticeli"),
        (r"\bgociolatoro\b", "corona"),
        (r"\btygraphi\b", "tygraphi"),
        (r"\btriglyphi\b", "tygraphi"),
        (r"\btriglyphs\b", "tygraphi"),
        (r"\bmetopa\b", "metopa"),
        (r"\bmetopes\b", "metopa"),
        (r"\bpulvinata\b", "pulvinata"),
        (r"\bcolonna\s+dorica\b", "colonna-dorica"),
        (r"\bcolonna\s+ionica\b", "colonna-ionica"),
        (r"\bcolonna\s+corinthia\b", "colonna-corinthia"),
        (r"\bimoscapo\b", "imoscapo"),
        (r"\bsommoscapo\b", "sommoscapo"),
        (r"\bastragalo\b", "astragalo"),
        (r"\btondino\b", "astragalo"),
        (r"\bplintho\b", "plintho"),
        (r"\bacroterio\b", "acroterio"),
        (r"\bfastigio\b", "fastigio"),
        (r"\bfrontespicio\b", "fastigio"),
        (r"\btimpano\b", "timpano"),
        (r"\bpilastro\b", "pilastro"),
        (r"\bcotozzo\b", "cotozzo"),
        (r"\btondo\s+e\s+quadro\b", "tondo-e-quadro"),
        (r"\bal\s+tondo\s+e\s+al\s+quadro\b", "homo-ad-circulum"),
        (r"\bcrosiera\b", "crosiera"),
        (r"\bgamba\s+grossa\b", "gamba-grossa"),
        (r"\bcircino\b", "circino"),
        (r"\bsquadra\b", "norma"),
        (r"\barchipendolo\b", "archipendolo"),
        (r"\bsimetria\b", "simetria"),
        (r"\bcommensuratione\b", "simetria"),
        (r"\bequestre\s+statua\b", "statua-equestre"),
        (r"\bequestrian\s+statue\b", "statua-equestre"),
        (r"\bsimulacro\b", "simulacro"),
        (r"\bLast\s+Supper\b", "simulacro"),
        (r"\bAbendmahl(?:e|s)?\b", "simulacro"),
        (r"\bCenacolo\b", "simulacro"),
        (r"\bla\s+Rotonda\b", "rotonda-pantheon"),
        (r"\bPantheon\b", "rotonda-pantheon"),
        (r"\bSanta\s+Maria\s+delle\s+Grazie\b", "santa-maria-delle-grazie"),
        (r"\bS\.\s+Maria\s+de\s+le\s+Gratie\b", "santa-maria-delle-grazie"),
        (r"\bBorgo\s+San\s*sepolcro\b", "san-sepolcro"),
        (r"\bBorgo\s+San\s+Sepolcro\b", "san-sepolcro"),
    ]
    return [(re.compile(pat, re.I), slug) for pat, slug in raw_patterns]


CITE_RULES = build_citation_rules()
PERSON_RULES = build_person_rules()
TERM_RULES = build_term_rules()


def try_wrap_entire_emphasis_span(span: str) -> str:
    """If an italic `*inner*` or bold `**inner**` span matches a citation, person, or term rule
    across the entire inner text (allowing optional German/English outer quotes `„...“`, `"..."`),
    wrap the emphasis span INSIDE the role:
    e.g. `*In Coelo et Mundo*` -> `:cite:`*In Coelo et Mundo* <aristotle:de-caelo:III.8>``
    and `*„Summa de arithmetica“*` -> `:cite:`*„Summa de arithmetica“* <pacioli:summa>``
    which is 100% valid Docutils and supported by `photon_platform.publish.roles.geometry`.
    """
    if span.startswith("**") and span.endswith("**") and len(span) > 4:
        delim = "**"
        inner = span[2:-2]
    elif span.startswith("*") and span.endswith("*") and len(span) > 2:
        delim = "*"
        inner = span[1:-1]
    else:
        return span

    # Do not touch spans that contain backticks or roles
    if "`" in inner or "<" in inner or ">" in inner:
        return span

    inner_unquoted = inner.strip('„“”"«»\'').strip()
    candidates = [inner] if inner_unquoted == inner else [inner, inner_unquoted]

    # 1. Check full-span match against CITE_RULES
    for cand in candidates:
        for pat, target in CITE_RULES:
            m = pat.fullmatch(cand)
            if m:
                if callable(target):
                    res = target(m)
                    return res.replace(f":cite:`{cand} <", f":cite:`{delim}{inner}{delim} <", 1)
                return f":cite:`{delim}{inner}{delim} <{target}>`"

    # 2. Check full-span match against PERSON_RULES
    for cand in candidates:
        for pat, slug in PERSON_RULES:
            if pat.fullmatch(cand):
                return f":person:`{delim}{inner}{delim} <{slug}>`"

    # 3. Check full-span match against TERM_RULES
    for cand in candidates:
        for pat, slug in TERM_RULES:
            if pat.fullmatch(cand):
                return f":term:`{delim}{inner}{delim} <{slug}>`"

    # 4. Special check for Latin polyhedra plate titles like `*Tetrahedron Planum Solidum*`:
    # match the longest polyhedron term prefix in `inner` only when `inner` has no nested markup/parens
    if re.fullmatch(r"[A-Za-zΑ-Ωα-ω\s\[\]]+", inner):
        for pat, slug in TERM_RULES:
            m = pat.match(inner)
            if m and slug in (
                "tetrahedron-abscisum",
                "tetrahedron-elevatum",
                "exahedron-abscisum-elevatum",
                "exahedron-abscisum",
                "exahedron-elevatum",
                "octahedron-abscisum",
                "octahedron-elevatum",
                "icosahedron-abscisum",
                "icosahedron-elevatum",
                "dodecahedron-abscisum-elevatum",
                "dodecahedron-abscisum",
                "dodecahedron-elevatum",
                "vigintisex-basium-elevatum",
                "vigintisex-basium",
                "septuaginta-duarum-basium",
                "corpo-seratile",
                "colonna-quadrilatera",
                "colonna-pentagona",
                "colonna-exagona",
                "pyramide-triangula",
                "pyramide-quadrilatera",
                "pyramide-pentagona",
                "pyramide-exagona",
                "colonna-rotonda",
                "pyramide-rotonda",
                "tetrahedron",
                "exahedron",
                "octahedron",
                "icosahedron",
                "dodecahedron",
                "spera",
            ):
                return f":term:`{delim}{inner}{delim} <{slug}>`"

    return span


def apply_rules_to_plain_chunk(chunk: str) -> str:
    """Apply CITE_RULES, PERSON_RULES, and TERM_RULES to a plain-text chunk (outside any roles or emphasis).
    Each newly inserted role is immediately protected from subsequent rules.
    """
    text = chunk

    def _sub_unprotected(text_in: str, role_name: str, pat: Pattern[str], target: Any) -> str:
        parts = PROTECTED_SPAN_RE.split(text_in)
        protected = PROTECTED_SPAN_RE.findall(text_in)
        out: List[str] = []
        for idx, part in enumerate(parts):
            if part:
                if callable(target):
                    part = pat.sub(target, part)
                else:
                    part = pat.sub(lambda m: f":{role_name}:`{m.group(0)} <{target}>`", part)
            out.append(part)
            if idx < len(protected):
                out.append(protected[idx])
        return "".join(out)

    for pat, target in CITE_RULES:
        text = _sub_unprotected(text, "cite", pat, target)

    for pat, slug in PERSON_RULES:
        text = _sub_unprotected(text, "person", pat, slug)

    for pat, slug in TERM_RULES:
        text = _sub_unprotected(text, "term", pat, slug)

    return text


def enrich_line(line: str) -> str:
    """Enrich a single non-heading, non-directive RST line with :cite:, :person:, and :term: roles."""
    stripped = line.strip()
    if not stripped:
        return line
    # Skip field list metadata, directives, comments, and toctree entries
    if (
        stripped.startswith(":")
        or stripped.startswith("..")
        or is_heading_underline(stripped)
        or re.match(r"^[a-z0-9_/-]+$", stripped)
    ):
        return line

    # Split by protected spans; for `*...*` and `**...**` spans try whole-span wrapping,
    # and for plain text chunks apply CITE_RULES, PERSON_RULES, and TERM_RULES.
    parts = PROTECTED_SPAN_RE.split(line)
    protected = PROTECTED_SPAN_RE.findall(line)
    out: List[str] = []
    for idx, part in enumerate(parts):
        if part:
            out.append(apply_rules_to_plain_chunk(part))
        if idx < len(protected):
            prot = protected[idx]
            if prot.startswith("*"):
                out.append(try_wrap_entire_emphasis_span(prot))
            else:
                out.append(prot)
    return "".join(out)


def enrich_rst_document(raw_text: str, convert_just_to_cite: bool = False) -> str:
    """Cleanly unwrap any prior apparatus roles and enrich all eligible body lines in an RST document."""
    cleaned = strip_existing_apparatus_roles(raw_text)
    if convert_just_to_cite:
        cleaned = JUST_ROLE_RE.sub(lambda m: f":cite:`Euclid {m.group(1)} <euclid:elements:{m.group(1)}>`", cleaned)
    lines = cleaned.splitlines()
    n = len(lines)
    out_lines: List[str] = []

    in_directive_block = False
    for i, line in enumerate(lines):
        s = line.strip()
        # Check if this line is a section title (next line is a heading underline)
        if i + 1 < n and s and is_heading_underline(lines[i + 1]):
            out_lines.append(line)
            continue
        # Check if this line is a heading underline or overline
        if is_heading_underline(s):
            out_lines.append(line)
            continue
        # Check directive blocks (like .. toctree::, .. figure::, .. picture::, .. folio::)
        if s.startswith(".. "):
            if any(
                s.startswith(d)
                for d in (
                    ".. toctree::",
                    ".. picture::",
                    ".. figure::",
                    ".. image::",
                    ".. folio::",
                    ".. math::",
                )
            ):
                in_directive_block = True
            else:
                in_directive_block = False
            out_lines.append(line)
            continue

        if in_directive_block:
            if not s or (not line.startswith(" ") and not line.startswith("\t")):
                if s and not line.startswith(" "):
                    in_directive_block = False
                else:
                    out_lines.append(line)
                    continue
            else:
                # Inside picture/figure/toctree options or caption: skip `:alt:`, `:align:`, etc.
                if s.startswith(":"):
                    out_lines.append(line)
                    continue
                # If it's a toctree entry path, skip
                if re.match(r"^[a-zA-Z0-9_/-]+$", s):
                    out_lines.append(line)
                    continue

        out_lines.append(enrich_line(line))

    return "\n".join(out_lines) + ("\n" if raw_text.endswith("\n") else "")


ROLE_EXTRACT_RE = re.compile(r":(?P<role>cite|term|person):`(?P<content>[^`]+)`")
TARGET_SPLIT_RE = re.compile(r"^(?P<display>.*?)\s*<(?P<target>[^>]+)>$")


def parse_role_content(content: str) -> Tuple[str, str]:
    m = TARGET_SPLIT_RE.match(content.strip())
    if m:
        disp = m.group("display").strip() or m.group("target").strip()
        target = m.group("target").strip()
    else:
        disp = content.strip()
        target = disp
    # Strip outer emphasis stars and outer quote marks for clean registry display strings
    clean_disp = disp.strip("*").strip('„“”"«»').strip()
    return clean_disp, target


def parse_folio_metadata(raw_rst: str, fstr: str) -> Dict[str, str]:
    meta = {
        "volume": "volume_I",
        "folio": fstr,
        "page": fstr,
        "book": "",
        "section": "",
    }
    for line in raw_rst.splitlines()[:15]:
        m = re.match(r"^:([a-z_]+):\s*(.+)$", line.strip())
        if m:
            k, v = m.group(1), m.group(2).strip()
            if k == "page":
                meta["page"] = v
            elif k == "book":
                meta["book"] = v
            elif k == "section":
                meta["section"] = v
    return meta


def parse_Cite_Key(key: str) -> Tuple[str, str, str]:
    parts = key.split(":")
    author_slug = parts[0]
    work_slug = parts[1] if len(parts) > 1 else ""
    locus = ":".join(parts[2:]) if len(parts) > 2 else ""
    return author_slug, work_slug, locus


def main() -> None:
    # 1. Enrich all 318 folio .rst and .notes.rst files in paganini_1509/
    folio_occ_cites: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    folio_occ_terms: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    folio_occ_persons: Dict[str, List[Dict[str, str]]] = defaultdict(list)

    for fnum in range(1, 319):
        fstr = f"{fnum:04d}"
        rst_path = PAG_DIR / f"{fstr}.rst"
        notes_path = PAG_DIR / f"{fstr}.notes.rst"

        if rst_path.exists():
            enriched_rst = enrich_rst_document(rst_path.read_text(encoding="utf-8"), convert_just_to_cite=False)
            rst_path.write_text(enriched_rst, encoding="utf-8")
        else:
            enriched_rst = ""

        if notes_path.exists():
            enriched_notes = enrich_rst_document(notes_path.read_text(encoding="utf-8"), convert_just_to_cite=True)
            notes_path.write_text(enriched_notes, encoding="utf-8")
        else:
            enriched_notes = ""

        meta = parse_folio_metadata(enriched_rst, fstr)
        combined = enriched_rst + "\n" + enriched_notes

        seen_cite_on_folio = set()
        seen_term_on_folio = set()
        seen_person_on_folio = set()

        for m in ROLE_EXTRACT_RE.finditer(combined):
            role = m.group("role")
            disp, target = parse_role_content(m.group("content"))
            occ_entry = {
                "volume": meta["volume"],
                "folio": meta["folio"],
                "page": meta["page"],
                "book": meta["book"],
                "section": meta["section"],
                "display": disp,
            }
            if role == "cite":
                if (target, disp) not in seen_cite_on_folio:
                    seen_cite_on_folio.add((target, disp))
                    folio_occ_cites[target].append(occ_entry)
                # Also credit the cited author in persons.json
                author_slug, _, _ = parse_Cite_Key(target)
                for pslug in CITE_AUTHOR_TO_PERSONS.get(author_slug, []):
                    if (pslug, disp) not in seen_person_on_folio:
                        seen_person_on_folio.add((pslug, disp))
                        folio_occ_persons[pslug].append(occ_entry)
            elif role == "term":
                tslug = target.lower()
                if (tslug, disp) not in seen_term_on_folio:
                    seen_term_on_folio.add((tslug, disp))
                    folio_occ_terms[tslug].append(occ_entry)
            elif role == "person":
                pslug = target.lower()
                if (pslug, disp) not in seen_person_on_folio:
                    seen_person_on_folio.add((pslug, disp))
                    folio_occ_persons[pslug].append(occ_entry)

    # 2. Enrich all RST files in docsrc/ and collect work_occurrences
    work_occ_cites: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    work_occ_terms: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    work_occ_persons: Dict[str, List[Dict[str, str]]] = defaultdict(list)

    for doc_path in sorted(DOCSRC_DIR.rglob("*.rst")):
        if doc_path.name in {"bibliography.rst", "persons.rst", "glossary.rst"}:
            continue
        rel_doc = doc_path.relative_to(DOCSRC_DIR).with_suffix("").as_posix()
        raw_doc = doc_path.read_text(encoding="utf-8")
        is_notes_doc = (
            doc_path.name.endswith("_notes.rst")
            or doc_path.name.startswith("intro_")
            or doc_path.name.startswith("anmerkungen_")
        )
        enriched_doc = enrich_rst_document(raw_doc, convert_just_to_cite=is_notes_doc)
        doc_path.write_text(enriched_doc, encoding="utf-8")

        # Extract document title from first heading
        doc_title = rel_doc
        dlines = enriched_doc.splitlines()
        for i, ln in enumerate(dlines[:-1]):
            if ln.strip() and is_heading_underline(dlines[i + 1].strip()):
                doc_title = ln.strip()
                break

        seen_w_cite = set()
        seen_w_term = set()
        seen_w_person = set()
        for m in ROLE_EXTRACT_RE.finditer(enriched_doc):
            role = m.group("role")
            disp, target = parse_role_content(m.group("content"))
            w_entry = {
                "work": "divina_proportione",
                "doc": rel_doc,
                "title": doc_title,
                "display": disp,
            }
            if role == "cite":
                if (target, rel_doc) not in seen_w_cite:
                    seen_w_cite.add((target, rel_doc))
                    work_occ_cites[target].append(w_entry)
                # Also credit the cited author in work_occ_persons
                author_slug, _, _ = parse_Cite_Key(target)
                for pslug in CITE_AUTHOR_TO_PERSONS.get(author_slug, []):
                    if (pslug, rel_doc) not in seen_w_person:
                        seen_w_person.add((pslug, rel_doc))
                        work_occ_persons[pslug].append(w_entry)
            elif role == "term":
                tslug = target.lower()
                if (tslug, rel_doc) not in seen_w_term:
                    seen_w_term.add((tslug, rel_doc))
                    work_occ_terms[tslug].append(w_entry)
            elif role == "person":
                pslug = target.lower()
                if (pslug, rel_doc) not in seen_w_person:
                    seen_w_person.add((pslug, rel_doc))
                    work_occ_persons[pslug].append(w_entry)

    # 3. Build citations.json
    all_cite_keys = sorted(set(folio_occ_cites.keys()) | set(work_occ_cites.keys()))
    citations_registry: Dict[str, Any] = {}
    for ckey in all_cite_keys:
        author_slug, work_slug, locus = parse_Cite_Key(ckey)
        ainfo = AUTHOR_CATALOG.get(
            author_slug,
            {
                "name": author_slug.replace("-", " ").title(),
                "bib_anchor": f"bib-{author_slug}",
                "work_default": work_slug.replace("-", " ").title(),
            },
        )
        wtitle = WORK_TITLES.get(f"{author_slug}:{work_slug}", ainfo["work_default"])
        citations_registry[ckey] = {
            "author": ainfo["name"],
            "author_slug": author_slug,
            "work": wtitle,
            "work_slug": work_slug,
            "locus": locus,
            "bib_anchor": ainfo["bib_anchor"],
            "occurrences": folio_occ_cites.get(ckey, []),
            "work_occurrences": work_occ_cites.get(ckey, []),
        }

    # 4. Build glossary.json (include all catalog terms + any dynamic terms)
    all_term_keys = sorted(set(TERM_CATALOG.keys()) | set(folio_occ_terms.keys()) | set(work_occ_terms.keys()))
    glossary_registry: Dict[str, Any] = {}
    for tslug in all_term_keys:
        tinfo = TERM_CATALOG.get(
            tslug,
            {
                "headword": tslug.replace("-", " "),
                "language": "Italian / Latin",
                "translation": tslug.replace("-", " ").title(),
                "definition": f"Technical geometric or architectural term ({tslug}) in Pacioli's De Divina Proportione.",
            },
        )
        glossary_registry[tslug] = {
            "headword": tinfo["headword"],
            "language": tinfo["language"],
            "translation": tinfo["translation"],
            "definition": tinfo["definition"],
            "occurrences": folio_occ_terms.get(tslug, []),
            "work_occurrences": work_occ_terms.get(tslug, []),
        }

    # 5. Build persons.json (include all catalog persons + any dynamic persons)
    all_person_keys = sorted(set(PERSON_CATALOG.keys()) | set(folio_occ_persons.keys()) | set(work_occ_persons.keys()))
    persons_registry: Dict[str, Any] = {}
    for pslug in all_person_keys:
        pinfo = PERSON_CATALOG.get(
            pslug,
            {
                "name": pslug.replace("-", " ").title(),
                "dates": "fl. 15th–16th century",
                "role": "Historical Authority / Interlocutor",
                "bio": f"Historical personage ({pslug}) referenced in Pacioli's De Divina Proportione.",
                "works": [],
                "bib_anchor": f"bib-{pslug}",
            },
        )
        persons_registry[pslug] = {
            "name": pinfo["name"],
            "dates": pinfo["dates"],
            "role": pinfo["role"],
            "bio": pinfo["bio"],
            "works": pinfo["works"],
            "bib_anchor": pinfo["bib_anchor"],
            "occurrences": folio_occ_persons.get(pslug, []),
            "work_occurrences": work_occ_persons.get(pslug, []),
        }

    # 6. Write citations.json, glossary.json, and persons.json to BOTH directories
    for out_dir in (RES_DIR, PAG_DIR):
        (out_dir / "citations.json").write_text(
            json.dumps(citations_registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (out_dir / "glossary.json").write_text(
            json.dumps(glossary_registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (out_dir / "persons.json").write_text(
            json.dumps(persons_registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    # 7. Write scholarly apparatus RST pages in docsrc/de_divina_proportione/
    write_apparatus_rst_pages(citations_registry, glossary_registry, persons_registry)

    tot_cite_occ = sum(len(v["occurrences"]) for v in citations_registry.values())
    tot_term_occ = sum(len(v["occurrences"]) for v in glossary_registry.values())
    tot_pers_occ = sum(len(v["occurrences"]) for v in persons_registry.values())
    print(
        f"Built Apparatus Registries & RST Pages:\n"
        f"  - citations.json: {len(citations_registry)} unique loci ({tot_cite_occ} folio occurrences)\n"
        f"  - glossary.json:  {len(glossary_registry)} technical terms ({tot_term_occ} folio occurrences)\n"
        f"  - persons.json:   {len(persons_registry)} historical persons ({tot_pers_occ} folio occurrences)"
    )


def _apparatus_slug(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


def _make_rst_heading(text: str, char: str = "-") -> str:
    line = char * max(len(text), 4)
    return f"{text}\n{line}"


def _format_work_occ_links(work_occs: List[Dict[str, str]], max_links: int = 24) -> str:
    """Format compact :doc: backlinks to chapters/plates in docsrc/de_divina_proportione/."""
    links: List[str] = []
    seen_docs = set()
    for w in work_occs:
        doc = w.get("doc", "")
        if not doc or not doc.startswith("de_divina_proportione/"):
            continue
        if doc in seen_docs:
            continue
        seen_docs.add(doc)
        parts = doc.split("/")
        # Build concise label (e.g. "Compendio Cap. III (EN)" or "Architectura Cap. I (IT)")
        lang_tag = ""
        for suf, lbl in (("_en", "EN"), ("_it", "IT"), ("_de", "DE"), ("_la", "LA"), ("_notes", "Notes")):
            if parts[-1].endswith(suf):
                lang_tag = f" ({lbl})"
                break
        if len(parts) >= 3 and parts[1] in ("compendio", "architectura"):
            sec_lbl = "Comp." if parts[1] == "compendio" else "Arch."
            ch_slug = parts[2]
            if ch_slug == "dedication":
                unit_lbl = f"{sec_lbl} Prohemio{lang_tag}"
            elif ch_slug.startswith("cap_"):
                cnum = int(ch_slug.split("_")[1])
                unit_lbl = f"{sec_lbl} Cap. {cnum}{lang_tag}"
            else:
                unit_lbl = f"{sec_lbl} {ch_slug}{lang_tag}"
        elif len(parts) >= 3 and parts[1] == "intro":
            unit_lbl = f"Winterberg Intro{lang_tag}"
        elif len(parts) >= 3 and parts[1] == "plates":
            stem = parts[-1].rsplit("_", 1)[0]
            if stem == "anmerkungen":
                unit_lbl = f"Winterberg Anmerkungen{lang_tag}"
            else:
                unit_lbl = f"Plates: {stem.title()}{lang_tag}"
        else:
            unit_lbl = w.get("title", parts[-1])
        links.append(f":doc:`{unit_lbl} </{doc}>`")

    if not links:
        return ""
    if len(links) > max_links:
        shown = ", ".join(links[:max_links])
        return f"{shown}, *...and {len(links) - max_links} more*"
    return ", ".join(links)


def write_apparatus_rst_pages(
    citations: Dict[str, Any],
    glossary: Dict[str, Any],
    persons: Dict[str, Any],
) -> None:
    """Generate bibliography.rst, persons.rst, and glossary.rst inside docsrc/de_divina_proportione/."""
    book_dir = DOCSRC_DIR / "de_divina_proportione"
    book_dir.mkdir(parents=True, exist_ok=True)

    # 1. Bibliography
    works_by_author: Dict[str, Dict[str, List[Tuple[str, Dict[str, Any]]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for ckey, cdata in citations.items():
        author_slug = cdata.get("author_slug") or ckey.split(":")[0]
        work_slug = cdata.get("work_slug") or (ckey.split(":")[1] if ":" in ckey else ckey)
        wkey = f"{author_slug}:{work_slug}"
        works_by_author[author_slug][wkey].append((ckey, cdata))

    bib_lines: List[str] = [
        ":order: 90",
        ":layout: book",
        ":type: apparatus",
        ":title: Bibliography & Cited Works",
        "",
        ".. _bibliography:",
        "",
        "==========================",
        "Bibliography & Cited Works",
        "==========================",
        "",
        ".. rubric:: Classical, Patristic, Scholastic & Renaissance Sources in *De Divina Proportione*",
        "",
        "Systematic register of classical treatises, Euclidean propositions, and philosophical works cited "
        "by Fra Luca Pacioli across *De Divina Proportione* (1509), with direct backlinks to every chapter occurrence.",
        "",
    ]

    emitted_cite_slugs = set()
    for author_slug in sorted(works_by_author.keys()):
        first_entry = next(iter(works_by_author[author_slug].values()))[0][1]
        author_name = first_entry.get("author", author_slug.replace("-", " ").title())
        bib_anchor = first_entry.get("bib_anchor", f"bib-{author_slug}")
        if bib_anchor not in emitted_cite_slugs:
            bib_lines.append(f".. _{bib_anchor}:")
            emitted_cite_slugs.add(bib_anchor)
        bib_lines.append("")
        bib_lines.append(_make_rst_heading(author_name, "-"))
        bib_lines.append("")
        for pslug in CITE_AUTHOR_TO_PERSONS.get(author_slug, []):
            if pslug in persons:
                pname = persons[pslug]["name"]
                bib_lines.append(f"See biographical entry: :ref:`{pname} <person-{_apparatus_slug(pslug)}>`.")
                bib_lines.append("")

        for wkey, loci_list in sorted(works_by_author[author_slug].items()):
            wtitle = loci_list[0][1].get("work", wkey)
            w_slug = _apparatus_slug(wkey)
            bib_lines.append(f".. _work-{w_slug}:")
            if w_slug not in emitted_cite_slugs:
                bib_lines.append(f".. _cite-{w_slug}:")
                emitted_cite_slugs.add(w_slug)
            bib_lines.append("")
            bib_lines.append(f"**{wtitle}** (``{wkey}``)")
            bib_lines.append("")

            for ckey, cdata in sorted(loci_list, key=lambda x: x[0]):
                c_slug = _apparatus_slug(ckey)
                if c_slug not in emitted_cite_slugs:
                    bib_lines.append(f".. _cite-{c_slug}:")
                    bib_lines.append("")
                    emitted_cite_slugs.add(c_slug)
                locus = cdata.get("locus") or "General reference"
                doc_links = _format_work_occ_links(cdata.get("work_occurrences", []))
                folios = sorted({o["folio"] for o in cdata.get("occurrences", []) if o.get("folio")})
                folio_str = f" [1509 Folios: {', '.join(folios[:10])}]" if folios else ""
                if doc_links:
                    bib_lines.append(f"- ``{locus}`` (``{ckey}``) — Cited in {doc_links}{folio_str}")
                else:
                    bib_lines.append(f"- ``{locus}`` (``{ckey}``){folio_str}")
                bib_lines.append("")

    (book_dir / "bibliography.rst").write_text("\n".join(bib_lines).rstrip() + "\n", encoding="utf-8")

    # 2. Persons
    persons_lines: List[str] = [
        ":order: 91",
        ":layout: book",
        ":type: apparatus",
        ":title: Index of Persons",
        "",
        ".. _persons:",
        "",
        "================",
        "Index of Persons",
        "================",
        "",
        ".. rubric:: Prosopographical Register of Mathematicians, Architects, Patrons & Philosophers",
        "",
        "Biographical register of ancient, medieval, and Renaissance authorities and contemporaries referenced "
        "in Fra Luca Pacioli's *De Divina Proportione* (1509).",
        "",
    ]

    for pslug, pdata in sorted(persons.items(), key=lambda kv: kv[1].get("name", kv[0]).lower()):
        p_anchor = _apparatus_slug(pslug)
        pname = pdata.get("name", pslug)
        pdates = pdata.get("dates", "")
        prole = pdata.get("role", "")
        pbio = pdata.get("bio", "")
        pworks = pdata.get("works", [])

        persons_lines.append(f".. _person-{p_anchor}:")
        persons_lines.append("")
        h_text = f"{pname} ({pdates})" if pdates else pname
        persons_lines.append(_make_rst_heading(h_text, "-"))
        persons_lines.append("")
        if prole:
            persons_lines.append(f"*{prole}*")
            persons_lines.append("")
        if pbio:
            persons_lines.append(pbio)
            persons_lines.append("")
        if pworks:
            persons_lines.append(f"**Principal Works:** {', '.join(f'*{w}*' for w in pworks)}")
            persons_lines.append("")
        doc_links = _format_work_occ_links(pdata.get("work_occurrences", []))
        if doc_links:
            persons_lines.append(f"**Occurrences:** {doc_links}")
            persons_lines.append("")

    (book_dir / "persons.rst").write_text("\n".join(persons_lines).rstrip() + "\n", encoding="utf-8")

    # 3. Glossary
    glossary_lines: List[str] = [
        ":order: 92",
        ":layout: book",
        ":type: apparatus",
        ":title: Technical Glossary",
        "",
        ".. _glossary:",
        "",
        "====================================================",
        "Glossary of Geometric, Architectural & Latin Terms",
        "====================================================",
        "",
        ".. rubric:: Multilingual Lexicon of Renaissance Mathematical & Architectural Terminology",
        "",
        "Technical terms in Italian, Latin, Greek, and German across Fra Luca Pacioli's *De Divina Proportione* (1509 / 1889).",
        "",
    ]

    for tslug, tdata in sorted(glossary.items(), key=lambda kv: kv[0].lower()):
        t_anchor = _apparatus_slug(tslug)
        headword = tdata.get("headword", tslug)
        lang = tdata.get("language", "")
        trans = tdata.get("translation", "")
        defn = tdata.get("definition", "")

        glossary_lines.append(f".. _term-{t_anchor}:")
        glossary_lines.append("")
        h_text = f"{headword} ({tslug})" if headword != tslug else headword
        glossary_lines.append(_make_rst_heading(h_text, "-"))
        glossary_lines.append("")
        meta_bits = []
        if lang:
            meta_bits.append(f"**Language:** {lang}")
        if trans:
            meta_bits.append(f"**Translation:** *{trans}*")
        if meta_bits:
            glossary_lines.append(" | ".join(meta_bits))
            glossary_lines.append("")
        if defn:
            glossary_lines.append(defn)
            glossary_lines.append("")
        doc_links = _format_work_occ_links(tdata.get("work_occurrences", []))
        if doc_links:
            glossary_lines.append(f"**Occurrences:** {doc_links}")
            glossary_lines.append("")

    (book_dir / "glossary.rst").write_text("\n".join(glossary_lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
