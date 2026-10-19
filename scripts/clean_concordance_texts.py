#!/usr/bin/env python3
"""Clean OCR artifacts, leaked Winterberg footnotes, page numbers, broken hyphenations,
and paragraph breaks across `resources/de_divina_proportione/paganini_1509/concordance.json`.

Reads directly from `resources/de_divina_proportione/winterberg/` so it is 100% idempotent.
Also restores the complete 1509 Front Matter transcriptions for:
- 0005 (Title Page & Gaetani Epigram)
- 0006 (Author's Sonnet & Epigrams)
- 0007–0008 (Soderini & Gaetani Latin Epistles, split into readable paragraphs)
- 0009–0010 (Nomina et Numerus Corporum 1–61 in Latin and Polytonic Greek)
- 0011–0016 (Taula dela presente opera: Compendio Cap. I–LXXI & Architectura Cap. I–XX)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from build_concordance import FRONTMATTER_LATIN, clean_winterberg_lines

ROOT = Path(__file__).resolve().parent.parent
RES_DIR = ROOT / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"
WB_DIR = RES_DIR / "winterberg"


# Authentic Front Matter transcriptions for 0005, 0006, 0009, 0010
FOLIO_0005_TEXT = """Divina proportione: opera a tutti gl'ingegni perspicaci e curiosi necessaria, ove ciascun studioso di Philosophia, Perspectiva, Pictura, Sculptura, Architectura, Musica e altre Mathematiche, suavissima, sottile e admirabile doctrina conseguirà; e delectarassi, con varie questione de secretissima scientia.

M. Antonio Capella eruditissimo recensente: Venetiis impressum per probum virum Paganinum de Paganinis de Brixia, anno M.D.VIIII.

Danielis Caietani Cremonensis Epigramma
---------------------------------------

| Natura omnipotens produxit corpora quinque,
| Simplicia haec certo nomine dicta manent.
| Composito in numerum concurrunt addita cuique,
| Atque inter sese consociata vigent.
| Condita principio pura et sine labe fuere:
| Nomina sunt aër, coelum, aqua, flamma et humus.
| Foetibus innumeris voluit Plato maximus illa
| Esse, ubi est primum sumpta figura, dare.
| Sed quia naturae lex nil concedit inane
| (*In Coelo et Mundo* dixit Aristoteles),
| Quodque unum per se positum est, caret atque figura,
| Nulla subest oculi supposito species:
| Propterea Euclidae sublimius atque Platonis
| Ingenium excussit sphaerica quinque alia,
| Iocunda aspectu et multum irritantia sensum,
| Monstravere bases ut latus omne docet."""

FOLIO_0006_TEXT = """Sonetto de l'Auctore (Fra Luca Pacioli)
---------------------------------------

| Cinque corpi in natura son producti,
| Da' naturali semplici chiamati,
| Perchè a ciascun composito adunati
| Per ordine concorran fra lor tutti.
| Immixti, netti e puri fur constructi,
| Quattro elementi e ciel così nomati,
| Quale Platone vol che figurati
| L'esser dien a infiniti fructi.
| Ma perchè el vacuo la natura aborre,
| Aristotil in quel *De Celo e Mundo*
| Per sè non figurati volse porre.
| Però l'ingegno geometra profondo
| Di Plato e d'Euclide piacque exporre
| Cinqu'altri che in spera volgan tundo,
| Regolari d'aspecto iocundo,
| Comme vedi de lati e basi pare,
| E un altro sexto mai se pò formare.

Corpora ad Lectorem
-------------------

| El dolce fructo vago e sì dilecto
| Constrinse già i Philosophi cercare
| Causa de noi, che pasci l'intellecto.

Distichon ad Idem
-----------------

| Quaerere de nobis fructus dulcissimus egit
| Philosophos causam, mens ubi laeta manet.

Corpora Loquuntur
-----------------

| Qui cupitis rerum varias cognoscere causas,
| Discite nos: cunctis hac patet una via.

FINIS."""

FOLIO_0009_TEXT = """Nomina et Numerus Corporum (I–XXXIV)
------------------------------------

**Tetrahedron (Τετράεδρον)**

1. *Tetrahedron planum solidum* — Τετράεδρον ἐπίπεδον στερεόν
2. *Tetrahedron planum vacuum* — Τετράεδρον ἐπίπεδον κενόν
3. *Tetrahedron abscisum solidum* — Τετράεδρον ἀποτετμημένον στερεόν
4. *Tetrahedron abscisum vacuum* — Τετράεδρον ἀποτετμημένον κενόν
5. *Tetrahedron elevatum solidum* — Τετράεδρον ἐπηρμένον στερεόν
6. *Tetrahedron elevatum vacuum* — Τετράεδρον ἐπηρμένον κενόν

**Exahedron sive Cubus (Ἑξάεδρον ἢ κύβος)**

7. *Exahedron planum solidum* — Ἑξάεδρον ἐπίπεδον στερεόν
8. *Exahedron planum vacuum* — Ἑξάεδρον ἐπίπεδον κενόν
9. *Exahedron abscisum solidum* — Ἑξάεδρον ἀποτετμημένον στερεόν
10. *Exahedron abscisum vacuum* — Ἑξάεδρον ἀποτετμημένον κενόν
11. *Exahedron elevatum solidum* — Ἑξάεδρον ἐπηρμένον στερεόν
12. *Exahedron elevatum vacuum* — Ἑξάεδρον ἐπηρμένον κενόν
13. *Exahedron abscisum elevatum solidum* — Ἑξάεδρον ἀποτετμημένον ἐπηρμένον στερεόν
14. *Exahedron abscisum elevatum vacuum* — Ἑξάεδρον ἀποτετμημένον ἐπηρμένον κενόν

**Octahedron (Ὀκτάεδρον)**

15. *Octahedron planum solidum* — Ὀκτάεδρον ἐπίπεδον στερεόν
16. *Octahedron planum vacuum* — Ὀκτάεδρον ἐπίπεδον κενόν
17. *Octahedron abscisum solidum* — Ὀκτάεδρον ἀποτετμημένον στερεόν
18. *Octahedron abscisum vacuum* — Ὀκτάεδρον ἀποτετμημένον κενόν
19. *Octahedron elevatum solidum* — Ὀκτάεδρον ἐπηρμένον στερεόν
20. *Octahedron elevatum vacuum* — Ὀκτάεδρον ἐπηρμένον κενόν

**Icosahedron (Εἰκοσάεδρον)**

21. *Icosahedron planum solidum* — Εἰκοσάεδρον ἐπίπεδον στερεόν
22. *Icosahedron planum vacuum* — Εἰκοσάεδρον ἐπίπεδον κενόν
23. *Icosahedron abscisum solidum* — Εἰκοσάεδρον ἀποτετμημένον στερεόν
24. *Icosahedron abscisum vacuum* — Εἰκοσάεδρον ἀποτετμημένον κενόν
25. *Icosahedron elevatum solidum* — Εἰκοσάεδρον ἐπηρμένον στερεόν
26. *Icosahedron elevatum vacuum* — Εἰκοσάεδρον ἐπηρμένον κενόν

**Dodecahedron (Δωδεκάεδρον)**

27. *Dodecahedron planum solidum* — Δωδεκάεδρον ἐπίπεδον στερεόν
28. *Dodecahedron planum vacuum* — Δωδεκάεδρον ἐπίπεδον κενόν
29. *Dodecahedron abscisum solidum* — Δωδεκάεδρον ἀποτετμημένον στερεόν
30. *Dodecahedron abscisum vacuum* — Δωδεκάεδρον ἀποτετμημένον κενόν
31. *Dodecahedron elevatum solidum* — Δωδεκάεδρον ἐπηρμένον στερεόν
32. *Dodecahedron elevatum vacuum* — Δωδεκάεδρον ἐπηρμένον κενόν
33. *Dodecahedron abscisum elevatum solidum* — Δωδεκάεδρον ἀποτετμημένον ἐπηρμένον στερεόν
34. *Dodecahedron abscisum elevatum vacuum* — Δωδεκάεδρον ἀποτετμημένον ἐπηρμένον κενόν"""

FOLIO_0010_TEXT = """Nomina et Numerus Corporum (XXXV–LXI)
-------------------------------------

**Vigintisex Basium (Εἰκοσιεξάεδρον)**

35. *Vigintisex basium planum solidum* — Εἰκοσιεξάεδρον ἐπίπεδον στερεόν
36. *Vigintisex basium planum vacuum* — Εἰκοσιεξάεδρον ἐπίπεδον κενόν
37. *Vigintisex basium abscisum elevatum solidum* — Εἰκοσιεξάεδρον ἀποτετμημένον ἐπηρμένον στερεόν
38. *Vigintisex basium abscisum elevatum vacuum* — Εἰκοσιεξάεδρον ἀποτετμημένον ἐπηρμένον κενόν

**Septuaginta Duarum Basium (Ἑβδομηκονταδισσάεδρον)**

39. *Septuaginta duarum basium solidum* — Ἑβδομηκονταδισσάεδρον στερεόν
40. *Septuaginta duarum basium vacuum* — Ἑβδομηκονταδισσάεδρον κενόν

**Columnae et Pyramides Lateratae ac Rotundae**

41. *Columna laterata triangula solida seu corpus seratile* — Κίων πλευρώδης τρίγωνος στερεὸς ἢ σχῆμα πριστόν
42. *Columna laterata triangula vacua* — Κίων πλευρώδης τρίγωνος κενός
43. *Pyramis laterata triangula solida* — Πυραμὶς πλευρώδης τρίγωνος στερεά
44. *Pyramis laterata triangula vacua* — Πυραμὶς πλευρώδης τρίγωνος κενή
45. *Columna laterata quadrangula solida* — Κίων πλευρώδης τετράγωνος στερεός
46. *Columna laterata quadrangula vacua* — Κίων πλευρώδης τετράγωνος κενός
47. *Pyramis laterata quadrangula solida* — Πυραμὶς πλευρώδης τετράγωνος στερεά
48. *Pyramis laterata quadrangula vacua* — Πυραμὶς πλευρώδης τετράγωνος κενή
49. *Columna laterata penthagona solida* — Κίων πλευρώδης πεντάγωνος στερεός
50. *Columna laterata penthagona vacua* — Κίων πλευρώδης πεντάγωνος κενός
51. *Pyramis laterata penthagona solida* — Πυραμὶς πλευρώδης πεντάγωνος στερεά
52. *Pyramis laterata penthagona vacua* — Πυραμὶς πλευρώδης πεντάγωνος κενή
53. *Columna laterata exagona solida* — Κίων πλευρώδης ἑξάγωνος στερεός
54. *Columna laterata exagona vacua* — Κίων πλευρώδης ἑξάγωνος κενός
55. *Pyramis laterata triangula inaequilatera solida* — Πυραμὶς πλευρώδης τρίγωνος ἀνισόπλευρος στερεά
56. *Pyramis laterata triangula inaequilatera vacua* — Πυραμὶς πλευρώδης τρίγωνος ἀνισόπλευρος κενή
57. *Columna rotunda solida* — Κίων στρογγύλος στερεός
58. *Pyramis rotunda solida* — Πυραμὶς στρογγύλη στερεά
59. *Sphera solida* — Σφαῖρα στερεά
60. *Pyramis laterata exagona solida* — Πυραμὶς πλευρώδης ἑξάγωνος στερεά
61. *Pyramis laterata exagona vacua* — Πυραμὶς πλευρώδης ἑξάγωνος κενή

Avvertimento al Lectore (Errata Corrige, 1509)
----------------------------------------------

Lectore, le sequenti parole porrai formaliter nel Cap. L, al fin della colonna dove dici *absciso fo detto non è*, sequitano queste: *possibile che causino angulo solido, e formase dal precedente nella terza parte de ciascun suo lato uniforme tagliato etc. XIX, XX. L'octocedron elevato solido etc.* Poi sequita el principio della sequente colonna, videlicet *solido over vacuo*, fo per errore scorso.

Le sequenti videlicet: *superficie è 24 più R. 6912 e la quadratura è R. 8192*, porrai in fine del Caso 4 del 3° Tractato a carte 22, dove dici: *e tal corpo tutto è R. 40 e la* etc., sequita *superficie è 24* etc., e fia finito el caso; seque el principio de l'altra colonna."""


# Regex patterns identifying standalone Winterberg page numbers, signature marks, or editorial footnote paragraphs
STANDALONE_DROP_PATTERNS = [
    re.compile(r"^[\d\s\.\,\:\;\'\"\^\*\[\]\(\)iIlLqQoOäöüÌD\-]{1,9}$"),
    re.compile(r"^Quellenschrif", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*(?:Vgl\.|Vg\'\.|Siehe\s+Zeichnung|Am\s+Ende\s+des\s+Tractats|Bezieht\s+sich\s+auf|Hierauf\s+ist\s+die\s+Figur|Die\s+fehlende\s+Figur|Es\s+sind\s+die\s+bereits|Die\s+Ergänzung\s+der\s+im\s+Original|Die\s+römischen\s+Ziffern\s+beziehen|Die\s+vielfachen\s+sich\s+häufig|Das\s+ne\s+des\s+Textes|Fehlt\s+entsprechende\s+Bezeichnung|Verbum\s+zu\s+erzeugen|Durchgehends\s+fälschlich|Heute\s+versteht\s+man\s+darunter|Statt\s+des\s+Ausdrucks|Stati\s+,,körperlicher|Anmerkung\s+des\s+Textes|Es\s+sei\s+erlaubt,\s+hier|Der\s+Ausdruck\s+ist\s+hier|Unter\s+dieser\s+Bezeichnung\s+ist|Die\s+Ecken\s+des\s+Würfels|Dieser\s+Zusatz\s+ist\s+natürlich|Es\s+werden\s+hier\s+wie\s+im\s+Folgenden|Punkt\s+d,\s+welcher\s+in\s+der\s+Zeichnung|Das\s+Wortspiel\s+ist\s+in\s+der|simili\s*=\s*ähnlich|Das\s+im\s+Text\s+fehlende\s+Verbum|Des\s+Verständnisses\s+wegen|Es\s+mangelt\s+hiefür|Text\s+soll\s*;?\s*poco|romase\s+wohl\s+rimasi|Tygraphen\s*=\s*Tr[il]glyphen|Die\s+Worte\s+des\s+Textes|Hiür\s+ist\s+im\s+Text)", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*(?:lies\s*:|Soli\s+heissen|Wohl:?|Wahrscheinlich:?|Zu\s+ergänzen|cfr\.\s*Cap\.|vgl\.\s*(?:Fig|I\.\s*Fig|2\.\s*Fig|die\s+Fig)|cfr\.\s*2\.\s*Fig)", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*(?:1\.|I\.|l\.)\s+[A-Za-z0-9\s\.\,\-\']{1,35}$"),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*(?:seil[\.,]|scil[\.,])\s*.{1,180}$", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*D\.\s*h\.\s*(?:wie\s+der\s+Abstand|sein\s+Quadrat\s+ist\s+gleich|gerichtet\s+sein).*$", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*d\.\s*h\.\s*(?:vom\s+Ellbogengel|ihrer\s+zweiten\s+Potenz).*$", re.I),
    re.compile(r"^[\'\-\d\)\]\*■•\s]*(?:Quadrat\.\s*-\)\s*Biquadrat\.|Quadrat\.|Tractat\.|Gerade\s+Pyramide\.|3j\s+seil,\s+em\s+und\s+mp\.)$", re.I),
    re.compile(r"^(?:£-|/|\\|f,|Y\^|Kl|/\"\"\s*\^\s*,|1\^\s*\\|I\s*/\s*—\s*r~\s*1|r\s*4\s*2,|2\s*f\s*A\.|I\s*\\\s*I\s*1/\^\s*\\)$"),
    re.compile(r"^[^\w\n]*[che|a]\s+zu\s+ergänzen\.?$"),
    re.compile(r"^Wohl\s+anguli\s+statt\s+basi", re.I),
]


def is_garbage_or_footnote_para(p: str) -> bool:
    s = p.strip()
    if not s:
        return True
    for pat in STANDALONE_DROP_PATTERNS:
        if pat.match(s):
            return True
    return False


def clean_inline_it(text: str) -> str:
    """Clean OCR artifacts and inline German apparatus leaks from Italian prose."""
    t = text
    # Strip inline German footnote leaks
    t = re.sub(r"[\'\-\d\)\]]*\s*Vgl[\.\-][^.;\n]*[.;]?", " ", t, flags=re.I)
    t = re.sub(r"[\'\-\d\)\]]*\s*Siehe\s+Zeichnung[^.;\n]*[.;]?", " ", t, flags=re.I)
    t = re.sub(r"[\'\-\d\)\]]*\s*Am\s+Ende\s+des\s+Tractats\.?", " ", t, flags=re.I)
    t = re.sub(r"[\'\-\d\)\]]*\s*Wahrscheinlich:\s*„?[^“.\n]*“?\s*zu\s+lesen\.?", " ", t, flags=re.I)
    t = re.sub(r"[\'\-\d\)\]]*\s*Wohl:?\s+(?:rame|fanno|de\s+loctocedron|sa\s+lacomodare)[^.\n]*\.?", " ", t, flags=re.I)
    t = re.sub(r"[\'\-\d\)\]]*\s*Zu\s+ergänzen[^.\n]*\.?", " ", t, flags=re.I)

    # Specific OCR fixes in Italian
    replacements = [
        ("theo- logiae", "theologiae"),
        ("aeompagnata", "accompagnata"),
        ("solerlo imitatore", "solerto imitatore"),
        ("exiraii consultissimì", "eximii consultissimi"),
        ("cose none", "cose nove"),
        ("Sy^/j tanti", "37 4/5 tanti"),
        ("braccia 1 2", "braccia 12"),
        ("1 2 pentagon", "12 pentagoni"),
        ("loo grassi buoi", "100 grassi buoi"),
        ("defidia", "de Fidia"),
        ("CoUigiadro", "Col ligiadro"),
        ("denoto luogo", "devoto luogo"),
        ("penolegiato", "pennellegiato"),
        ("lacomo Andrea", "Iacomo Andrea"),
        ("lacomandrea", "Iacomandrea"),
        ("paroUe", "parolle"),
        ("matheraatici", "mathematici"),
        ("Exortation«", "Exortatione"),
        ("cornino anco", "commo anco"),
        ("Guido vbaldo dicala", "Guido Ubaldo dicata"),
        ("ornamemto", "ornamento"),
        ("diete forme", "dicte forme"),
        ("diete certezze", "dicte certezze"),
        ("diete sorti", "dicte sorti"),
        ("diete colonne", "dicte colonne"),
        ("diete laude", "dicte laude"),
        ("diete inscriptioni", "dicte inscriptioni"),
        ("diete corde", "dicte corde"),
        ("diete mathematici", "dicte mathematici"),
        ("diete discipline", "dicte discipline"),
        ("dieta proportione", "dicta proportione"),
        ("dieta pyramide", "dicta pyramide"),
        ("dieta opera", "dicta opera"),
        ("dieta summa", "dicta Summa"),
        ("dieta testa", "dicta testa"),
        ("fanciliari", "familiari"),
        ("anniline", "anili ne"),
        ("talse facetie", "false facetie"),
        ("vn fumé", "un fumo"),
        ("jtrimo grado", "primo grado"),
        ("introductioiic e aigumcnto", "introductione e argumento"),
        ("Ihomo", "l'homo"),
        ("Gioe", "Cioè"),
        ("c^oe", "cioè"),
        ("(.|ual", "qual"),
        ("«on che", "non che"),
        ("capitoli©", "Capitolio"),
        ("francese©", "Francesco"),
        ("sano^ì", "fanno"),
        ("ogibilibus-)", "agibilibus"),
        ("ho^ mo", "homo"),
        ("dal) ^he", "da μανθάνω che"),
        ("^daltro", "d'altro"),
        ("|Jo", "Io"),
        ("|in", "in"),
        ("|le", "le"),
        ("|scientie", "scientie"),
        ("georaetrice", "geometrice"),
        ("huraana", "humana"),
        ("ucla figura", "nela figura"),
        ("Jaltro", "l'altro"),
        ("eie medesime", "e le medesime"),
        ("eie sue", "e le sue"),
        ("3872", "38 1/2"),
        ("38^/2", "38 1/2"),
        ("2^/2", "2 1/2"),
        ("2Vj", "2 1/2"),
        ("3/^4", "3/4"),
        ("^Vi4", "11/14"),
        ("la Y2 el Y3 li ^4 ^i Vs ^^ cetera", "la 1/2, el 1/3, li 1/4, li 1/5 et cetera"),
        ("el Yj cioè", "el 1/3 cioè"),
        ("el y^ più", "el 1/4 più"),
        ("Poi li altri Y; se diuidano in 1 2 parti equali che cadauno sira el quartodecimo de dicti Y; e la fascia soprana neuolesser 5. cioè Y12 ^^ ^^'^^^ V7 ^^'^^ ^^ spacio e la-",
         "Poi li altri 6/7 se dividano in 12 parti equali, e la fascia soprana ne vol esser 5, cioè 5/12 de dicti 6/7; lo spacio"),
        ("do- - ^ . ^ ^ ^^£ b", "doverse così formare:"),
        ("''^ '", ""),
        ("j t ^", ""),
        ("-t \\", ""),
    ]
    for old, new in replacements:
        t = t.replace(old, new)

    t = re.sub(r"\beh'", "ch'", t)
    t = re.sub(r"\bGommo\b", "Commo", t)
    t = re.sub(r"\bGomme\b", "Comme", t)
    t = re.sub(r"\bGon\b", "Con", t)
    t = re.sub(r"\bGap[\.,]", "Cap.", t)
    t = re.sub(r"\bGhe\b", "Che", t)
    t = re.sub(r"[\^\[\]\\]+", "", t)
    t = re.sub(r"\s+([,.;:?!])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t.strip()


def clean_inline_de(text: str) -> str:
    """Clean OCR artifacts, leaked inline footnotes, and broken square roots in German prose."""
    t = text
    # Strip inline editorial notes that leaked into the middle or end of paragraphs
    t = re.sub(r"\s*Text\s+[1lI]\.\s*quanto\s+statt\s+quarto\.", "", t)
    t = re.sub(r"\s*seil[.,]\s*dem\s+Radius\s+bd\s+des\s+Kreises\s+gleich\.", ".", t)
    t = re.sub(r"\s*seil\.\s*72-Flächner\.", "", t)
    t = re.sub(r"\(seil\.\s*Ecke\)", "(scil. Ecke)", t)
    t = re.sub(r"\bseil,\s*", "scil. ", t)

    # Fix OCR hch -> lich in German words
    t = re.sub(r"([A-Za-zäöüÄÖÜ]+)hch([a-z]*)", r"\1lich\2", t)
    t = t.replace("unendHchen", "unendlichen").replace("wissenschaftHchen", "wissenschaftlichen")
    t = t.replace("nämHch", "nämlich").replace("heihge", "heilige").replace("AnbHck", "Anblick")
    t = t.replace("GHed", "Glied").replace("selb§t", "selbst").replace("Gonfusion", "Confusion")
    t = t.replace("Girkel", "Cirkel").replace("Girat", "Citat").replace("Gentram", "Centrum")
    t = t.replace("Gentrum", "Centrum").replace("Gharaktere", "Charaktere").replace("Gapitellen", "Capitellen")
    t = t.replace("Capiteli", "Capitell").replace("Gypern", "Cypern").replace("muhiplicirt", "multiplicirt")
    t = t.replace("riegeiförmig", "riegelförmig").replace("mögh'ch", "möglich")
    t = t.replace('W"ink', "Wink").replace("bewundernsund", "bewunderns- und")
    t = t.replace("Andernmittheile", "Andern mittheile").replace("Be- *kräftigung", "Bekräftigung")
    t = t.replace("Plimmel", "Himmel").replace("wue Etwas", "wie Etwas").replace("<ler nur in eineni", "der nur in einem")
    t = t.replace("uijd", "und").replace("i:usaramengestellt", "zusammengestellt")

    # Fix w^ / W^
    t = re.sub(r"([wW])\^", r"\1", t)
    t = t.replace("vv^ie", "wie").replace("vs^enn", "wenn").replace("bev^^ahren", "bewahren")
    t = t.replace("Aufzählun^", "Aufzählung").replace("^,leichseitigen", "gleichseitigen")
    t = t.replace("^der Fall", "der Fall")

    # Fix trailing ^ used for comma or footnote mark
    t = re.sub(r"([A-Za-zäöüÄÖÜ])\^(?=\s+[a-zäöü])", r"\1,", t)
    t = re.sub(r"\^[\'\d\)]*", "", t)
    t = re.sub(r"[\'\-\*1-3]\)|\[#?\d*\]", "", t)

    # Fix OCR square roots and fractions in German
    sqrt_repls = [
        ("SyYjmal", "37 4/5 mal"),
        ("Yj2", "1/12"),
        ("Y2, Y3, ^4, ^3", "1/2, 1/3, 1/4, 1/5"),
        ("Y2", "1/2"),
        ("Y3", "1/3"),
        ("Yg", "1/3"),
        ("Vg", "1/3"),
        ("1^3", "1 1/3"),
        ("i:iV2", "1 : 1 1/2"),
        ("3872", "38 1/2"),
        ("3 8 1/2", "38 1/2"),
        ("128Y3", "128 1/3"),
        ("^'/u", "11/14"),
        ("^Vi4", "11/14"),
        ("i5o9", "1509"),
        ("am i. Juni", "am 1. Juni"),
        ("1 5 Jahren", "15 Jahren"),
        ("i5 — ]/ i25", "15 − √125"),
        ("i5 — |/i23", "15 − √125"),
        ("i5 — i/i^S", "15 − √125"),
        ("i5 — ]X 1 25", "15 − √125"),
        ("5 — ]/ 12 5", "15 − √125"),
        ("18— |X 180", "18 − √180"),
        ("]/i25 — 5", "√125 − 5"),
        ("],/'i25 — 5", "√125 − 5"),
        ("'A/iiS — 5", "√125 − 5"),
        ("j/i25— =-5", "√125 − 5"),
        ("jXi25 — 5", "√125 − 5"),
        ("]/ 125 — 5", "√125 − 5"),
        ("y 12b — 5", "√125 − 5"),
        ("]/ 180 — 6", "√180 − 6"),
        ("[./ 180 — 6", "√180 − 6"),
        ("\\/iSo — 6", "√180 − 6"),
        ("]/ i25", "√125"),
        ("]/ 1 25", "√125"),
        ("]i 25", "√125"),
        ("j/^l25", "√125"),
        ("t5o — ]/i25oo", "150 − √12500"),
        ("i 25", "125"),
        ("2 5", "25"),
        ("3o", "30"),
        ("1 8", "18"),
        ("loo", "100"),
    ]
    for old, new in sqrt_repls:
        t = t.replace(old, new)

    # Clean remaining specific OCR square-root tokens (|/ or ]/ or ]X or |/ before digits) -> √
    t = re.sub(r"(?:■\s*)?(?:\|\/|\]\/|\[\/|\]X|\|X|j\/\^|1\/\^|\'\\\/)\s*(?=\d)", "√", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\s+([,.;:?!])", r"\1", t)
    return t.strip()


ABBREV_END_RE = re.compile(
    r"\b(?:heil|hl|d\.\s*h|z\.\s*B|u\.\s*s\.\s*w|cfr|vgl|scil|Cap|Fig|M|S|D|B|R|St|P|V|VI|VII|Nr)\.$",
    re.I,
)


def split_into_sentences_safe(text: str) -> List[str]:
    """Split paragraph into sentences without breaking after abbreviations like `heil.`, `S.`, `d. h.`."""
    raw_parts = re.split(r"(?<=[\.\!\?])\s+(?=[A-ZÄÖÜ«„\"\'])", text)
    if len(raw_parts) <= 1:
        return [text]
    sentences: List[str] = []
    for part in raw_parts:
        if sentences and (ABBREV_END_RE.search(sentences[-1]) or re.match(r"^[A-Z]\.\s+[a-z]", part)):
            sentences[-1] = sentences[-1] + " " + part
        else:
            sentences.append(part)
    return sentences


def merge_and_split_paragraphs(raw_paras: List[str], lang: str = "it", max_words: int = 125) -> List[str]:
    """Filter out footnote/page-number paragraphs, rejoin paragraphs broken across page breaks,
    and split overly long paragraphs at natural sentence boundaries.
    """
    cleaned: List[str] = []
    for p in raw_paras:
        if is_garbage_or_footnote_para(p):
            continue
        cp = clean_inline_it(p) if lang == "it" else clean_inline_de(p)
        if not cp or is_garbage_or_footnote_para(cp):
            continue
        cleaned.append(cp)

    # Rejoin paragraphs broken mid-word (ending with '-') or mid-sentence
    merged: List[str] = []
    for p in cleaned:
        if not merged:
            merged.append(p)
            continue
        prev = merged[-1]
        if prev.endswith("-"):
            # Hyphenated word split across page break
            if p and p[0].islower():
                merged[-1] = prev[:-1] + p
            else:
                merged[-1] = prev + p
        elif not re.search(r"[\.\!\?\:\;\"»”\)]$|\bFINIS\.?$", prev) or (p and p[0].islower()):
            merged[-1] = prev + " " + p
        else:
            merged.append(p)

    # Now split long paragraphs (> max_words) at sentence boundaries
    final_paras: List[str] = []
    for p in merged:
        words = p.split()
        if len(words) <= max_words:
            final_paras.append(p)
            continue
        sentences = split_into_sentences_safe(p)
        if len(sentences) <= 1:
            final_paras.append(p)
            continue
        cur_sents: List[str] = []
        cur_w = 0
        target_w = max(65, min(95, len(words) // ((len(words) // 90) + 1)))
        for s in sentences:
            sw = len(s.split())
            if cur_sents and (cur_w + sw > max_words or (cur_w >= target_w and sw >= 15)):
                final_paras.append(" ".join(cur_sents))
                cur_sents = [s]
                cur_w = sw
            else:
                cur_sents.append(s)
                cur_w += sw
        if cur_sents:
            final_paras.append(" ".join(cur_sents))

    return final_paras


def parse_clean_tabula_folios() -> Dict[int, str]:
    """Parse `toc_it_sections[5]` (lines 409–860 of 000_toc.txt) and split cleanly across folios 11..16."""
    toc_it_raw = (WB_DIR / "01_divina_proportione_italian" / "000_toc.txt").read_text(encoding="utf-8", errors="ignore")
    sections = [s.strip() for s in toc_it_raw.split("---") if s.strip()]
    tabula_raw = sections[5] if len(sections) >= 6 else sections[-1]

    # Reconstruct paragraphs from tabula_raw
    paras: List[str] = []
    cur: List[str] = []
    for ln in tabula_raw.splitlines():
        s = ln.strip()
        if not s:
            if cur:
                joined = ""
                for w in cur:
                    if joined.endswith("-") and w and w[0].islower():
                        joined = joined[:-1] + w
                    else:
                        joined = (joined + " " + w).strip()
                paras.append(clean_inline_it(joined))
                cur = []
        else:
            cur.append(s)
    if cur:
        joined = ""
        for w in cur:
            if joined.endswith("-") and w and w[0].islower():
                joined = joined[:-1] + w
            else:
                joined = (joined + " " + w).strip()
        paras.append(clean_inline_it(joined))

    # Fix specific OCR in Tabula paragraphs
    fixed_paras: List[str] = []
    for p in paras:
        p = p.replace("Cap. XI. Ghc cosa sia radice", "Cap. IX. Che cosa sia radice")
        p = p.replace("(^uuli sicnno le quantità rationaji e irrational!.", "Quali sienno le quantità rationali e irrationali.")
        p = p.replace("Cap. XVIII. Dela inclusione del tetracedron in lo duodecedron.", "Cap. XLIII. Dela inclusione del tetracedron in lo duodecedron.")
        p = p.replace("Cap. LUI.", "Cap. LIII.")
        p = p.replace("li 'y,, cioè", "li 11/14, cioè")
        p = p.replace("□ cosa cose. CU censo censi.", "co. cosa / cose; ce. censo / censi;")
        fixed_paras.append(p)

    # Distribute across folios 11..16 matching the 6 pages of the 1509 Tabula (A4r..A6v):
    buckets: Dict[int, List[str]] = {11: [], 12: [], 13: [], 14: [], 15: [], 16: []}
    cur_folio = 11
    for p in fixed_paras:
        if p.startswith("Cap. VI."):
            cur_folio = 12
        elif p.startswith("Cap. XXIV."):
            cur_folio = 13
        elif p.startswith("Cap. XLVIII."):
            cur_folio = 14
        elif p.startswith("Cap. LX."):
            cur_folio = 15
        elif p.startswith("Tabula del tractato de larchitectura"):
            cur_folio = 16
        buckets[cur_folio].append(p)

    return {fn: "\n\n".join(buckets[fn]) for fn in range(11, 17)}


def split_cleaned_paras_across_folios(
    cleaned_paras: List[str],
    folios: List[str],
    old_slices: Dict[str, List[str]],
    max_words: int = 115,
) -> Dict[str, List[str]]:
    """Split cleaned paragraphs (or their sentences) across `folios` proportionally to `old_slices`."""
    if not folios:
        return {}
    if len(folios) == 1:
        return {folios[0]: cleaned_paras}

    # Flatten cleaned_paras into sentences so folio boundaries stay accurate
    all_sents: List[str] = []
    for p in cleaned_paras:
        for s in split_into_sentences_safe(p):
            if s.strip():
                all_sents.append(s.strip())

    if not all_sents:
        return {f: [] for f in folios}

    weights = [max(1, len(" ".join(old_slices.get(f, [])))) for f in folios]
    tot_w = sum(weights)
    sent_idx = 0
    res: Dict[str, List[str]] = {}
    for idx, fstr in enumerate(folios):
        if idx == len(folios) - 1:
            f_sents = all_sents[sent_idx:]
        else:
            frac = weights[idx] / tot_w
            take = max(1, round(frac * len(all_sents)))
            f_sents = all_sents[sent_idx : sent_idx + take]
            sent_idx += take
        if f_sents:
            res[fstr] = merge_and_split_paragraphs([" ".join(f_sents)], lang="it", max_words=max_words)
        else:
            res[fstr] = []
    return res


def main() -> None:
    conc_path = PAG_DIR / "concordance.json"
    conc = json.loads(conc_path.read_text(encoding="utf-8"))

    # 1. Re-parse and clean chapters in compendio and architectura from raw Winterberg files
    for part in ("compendio", "architectura"):
        for ch in conc["chapters"][part]:
            wb_it_rel = ch.get("winterberg_it")
            wb_de_rel = ch.get("winterberg_de")
            if wb_it_rel and (RES_DIR / wb_it_rel).exists():
                it_raw = (RES_DIR / wb_it_rel).read_text(encoding="utf-8", errors="ignore")
                _, raw_title_it, raw_paras_it = clean_winterberg_lines(it_raw)
            else:
                raw_title_it = ch.get("title_it", "")
                raw_paras_it = ch.get("paragraphs_it", [])

            if wb_de_rel and (RES_DIR / wb_de_rel).exists():
                de_raw = (RES_DIR / wb_de_rel).read_text(encoding="utf-8", errors="ignore")
                _, raw_title_de, raw_paras_de = clean_winterberg_lines(de_raw)
            else:
                raw_title_de = ch.get("title_de", "")
                raw_paras_de = ch.get("paragraphs_de", [])

            ch["title_it"] = clean_inline_it(raw_title_it)
            ch["title_de"] = clean_inline_de(raw_title_de)
            ch["paragraphs_it"] = merge_and_split_paragraphs(raw_paras_it, lang="it", max_words=120)
            ch["paragraphs_de"] = merge_and_split_paragraphs(raw_paras_de, lang="de", max_words=120)

            ch["folio_slices_it"] = split_cleaned_paras_across_folios(
                ch["paragraphs_it"], ch.get("folios", []), ch.get("folio_slices_it", {}), max_words=115
            )
            ch["folio_slices_de"] = split_cleaned_paras_across_folios(
                ch["paragraphs_de"], ch.get("folios", []), ch.get("folio_slices_de", {}), max_words=115
            )

    # 2. Update Front Matter folios 0005, 0006, 0007, 0008, 0009, 0010, and 0011..0016 in concordance["folios"]
    folios = conc["folios"]
    folios["0005"]["text_it"] = FOLIO_0005_TEXT
    folios["0006"]["text_it"] = FOLIO_0006_TEXT
    for fnum, fstr in ((7, "0007"), (8, "0008")):
        raw_la = [p.strip() for p in FRONTMATTER_LATIN[fnum]["text_la"].split("\n\n") if p.strip()]
        if len(raw_la) >= 2:
            body_paras = merge_and_split_paragraphs(raw_la[1:], lang="it", max_words=105)
            folios[fstr]["text_la"] = "\n\n".join([raw_la[0]] + body_paras)
    folios["0009"]["text_it"] = FOLIO_0009_TEXT
    folios["0010"]["text_it"] = FOLIO_0010_TEXT

    tabula_by_folio = parse_clean_tabula_folios()
    for fn in range(11, 17):
        fstr = f"{fn:04d}"
        folios[fstr]["text_it"] = tabula_by_folio[fn]

    # Also update chapter titles stored inside folios[fstr]["chapters"]
    comp_by_num = {c["chapter"]: c for c in conc["chapters"]["compendio"]}
    arch_by_num = {c["chapter"]: c for c in conc["chapters"]["architectura"]}
    for fstr, finfo in folios.items():
        for ch_ref in finfo.get("chapters", []):
            src = comp_by_num[ch_ref["chapter"]] if ch_ref["part"] == "compendio" else arch_by_num[ch_ref["chapter"]]
            ch_ref["title_it"] = src["title_it"]
            ch_ref["title_de"] = src["title_de"]

    conc_path.write_text(json.dumps(conc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Successfully cleaned concordance.json from Winterberg sources!")


if __name__ == "__main__":
    main()
