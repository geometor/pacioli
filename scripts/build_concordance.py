#!/usr/bin/env python3
"""
scripts/build_concordance.py

Builds the complete, verified Paganini (1509) <-> Winterberg (1889) Folio-to-Chapter
and Plate Concordance (`resources/de_divina_proportione/paganini_1509/concordance.json`),
and updates `<folio>.json`, `pages.json`, `sections.json`, and `graphics_index.json`.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
RES_DIR = BASE_DIR / "resources" / "de_divina_proportione"
PAG_DIR = RES_DIR / "paganini_1509"
WB_DIR = RES_DIR / "winterberg"
WB_EN_DIR = RES_DIR / "winterberg_en"

ROMAN_NUMERALS = [
    "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
    "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
    "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
    "LI", "LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", "LX",
    "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX",
    "LXXI",
]


def norm(s: str) -> str:
    s = s.lower()
    s = s.replace("ſ", "s").replace("f", "s").replace("u", "v").replace("j", "i")
    return re.sub(r"[^a-z]", "", s)


def kmers(s: str, k: int = 5) -> set[str]:
    if len(s) < k:
        return {s} if s else set()
    return {s[i : i + k] for i in range(len(s) - k + 1)}


# Clean diplomatic transcriptions for Front Matter folios 0007 and 0008 (Latin)
FRONTMATTER_LATIN = {
    7: {
        "title": "Epistola ad Petrum Soderinum (1509)",
        "subtitle": "Excellentissimo Reipublicae Florentinae Principi Perpetuo D. Petro Soderino Frater Lucas Patiolus Burgensis Minoritanus et Sacrae Theologiae Professor. F. D.",
        "text_la": (
            "Excellentissimo Reipublicae Florentinae principi perpetuo D. Petro Soderino. "
            "Frater Lucas Patiolus Burgensis Minoritanus et sacrae Theologiae professor. F. D.\n\n"
            "Cum in his disciplinis: quas graeci Mathematicas appellant non minus utilitatis: "
            "quam voluptatis insit princeps patria ista clarissima Dignissime: quod tibi qui eas "
            "in primis calles: quod fratri Cardinali sapientissimo. Et patrono singulari meo: quod "
            "Ioanni Victorio I. V. eximio fratri optimo: quod Thomae: Ioanni baptistae nepoti "
            "tuis: quod Soderinae denique familiae omni: notissimum est: et quasi hereditario iure "
            "proprium: ut in hac videlicet facultate omnes excellatis. Ideo novum: hoc opus quod "
            "iampridem parturiebam tibi uni dicare constitui. Ut cum vobis omnibus semper carissimus "
            "vixerim habeam quo pacto satis faciam in parte omnibus haec igitur facultas: cum tanti "
            "fructus: tantaeque voluptatis sit: quantum et ipse agnoscis et probas: mirum dictu quam "
            "paucos patronos peritos sui habeat. Ego vero qui a teneris (ut aiunt) unguiculis "
            "pertinacissimo studio in his aliquem profectum assecutus multorum iudicio viderer. "
            "Iampridem opus illud emiseram: in quo omnem pene rationem huius disciplinae complexus "
            "fueram vernacula lingua quod Guidoni feltrio annis ab hinc aliquod dicatum a me: "
            "Venetiis impressum legitur. Accessit nunc ad eam curam: ut confluente studiosorum copia "
            "Megarensis Euclidis elementa lingua patria donare coactus sim: cessit id diis bene "
            "iuvantibus faelicissime. Nec vero multo post spe animos alentes libellum cui de divina "
            "proportione titulus est: Ludovico Sphorciae Duci mediolanensi nuncupavi. Tanto ardore ut "
            "schemata quoque sua Vincii nostri Leonardi manibus scalpta: quod opticen instructiorem "
            "reddere possent addiderim. Eum ego illi adhuc viventi: magnis ab eo donatus muneribus "
            "obtuleram. Fecerantque donationem illam nostram Iucundiorem Duo Romanae ecclesiae lumina: "
            "qui testes aderant Estensis. S. et sapientissimus frater tuus Cardinales Francisco pepo "
            "cive praestantissimo et tunc temporis cum fratre tuo oratore Clarissimo rem probante. "
            "Hunc vero tibi in praesentia: qui amissum labente Ludovici principatu libellum "
            "recuperasti: Iure tuo vendicabis in quo sepositis publicis curis animum interdum "
            "oblectes et nequid sine auctario veniat libellos duo velut appendices addidi alter "
            "veterum caracterum formam exactissimam quandam continet: in quo lineae curvae et rectae "
            "vis ostenditur. Alter quasi gradus nescio quos architectis struit: et marmorariis "
            "nostratibus: qui et ipsi libelli familiarium tuorum nomine: eorundemque municipis "
            "meorum circumferatur. Ut cum tibi omnia sua debeant: hac quoque in parte tibi non "
            "possint non debere. Caeterum tibi uni: Id totum nominatim inscribimus quo si vera "
            "fateri velim nihil habeant mathematicae disciplinae: vel sublimius: vel rarius: vel "
            "utilius. Hoc igitur opus veluti Thesaurum reconditum inclinante Iam aetate mea: "
            "posteritati invidere nolui. Cum praesertim tibi uni dicari posset. Qui praestantissimus "
            "omni virtutum genere his et vitae colore principes nostrae tempestatis facile excellas "
            "in hoc. n. finem ipsum quod ab omnibus expetitur assequere: cum activam partem ipsam "
            "in universum attingerit. Qui tibi scio tanto iucundior erit: quo et schemata ipsa Domi "
            "industria nostra habeas. Sed et res ipsa ingenii plena commendatiorem sese ipsa reddet. "
            "Nec vero vernacula haec et patria ipsa lingua te offendere debeat: cum tanto ampliorem "
            "fructum allaturus hic sit: quanto plures illum legent. Cum praesertim ingenium in his "
            "non eloquentiam requiras. Quod tu: Fraterque tuus Cardinalis Volaterranus: Cui vitam "
            "ipsam debeo: tam bene nostis: quam ego bene vobis semper opto. Vale et Salve. "
            "Venetiis. V. Idus Iunii. M.D.VIIII."
        ),
        "text_en": (
            "To the Most Excellent Perpetual Prince of the Florentine Republic, Lord Piero Soderini, "
            "Brother Luca Pacioli of Borgo Sansepolcro, of the Order of Minors and Professor of Sacred Theology, "
            "wishes utmost felicity.\n\n"
            "Since in those disciplines which the Greeks call Mathematical there resides no less utility than "
            "delight, Most Worthy Prince of that most illustrious commonwealth—a truth best known to you, who "
            "are yourself deeply versed in them, to your most wise brother the Cardinal and my singular patron "
            "[Francesco Soderini, Cardinal of Volterra], to your excellent brother Giovan Vittorio, Doctor of "
            "Both Laws, to your nephews Tommaso and Giovan Battista, and indeed to the entire Soderini family, "
            "as though it were yours by hereditary right to excel in this faculty—I have resolved to dedicate "
            "to you alone this new work, which I had long since brought forth. Having lived always on terms of "
            "the dearest affection with you all, I wished to have some means of repaying my debt in part to everyone. "
            "For although this science yields such great fruit and pleasure, as you yourself recognize and approve, "
            "it is marvelous to tell how few learned patrons it finds. As for myself, having from my tenderest "
            "youth (as the saying goes) pursued these studies with the most steadfast perseverance and achieved, "
            "in the judgment of many, some measure of success, I published some years ago that great work [the "
            "*Summa de Arithmetica, Geometria, Proportioni et Proportionalita*, 1494] in which I embraced nearly "
            "the whole method of this discipline in the vernacular tongue, dedicated by me to Guidobaldo da "
            "Montefeltro and printed in Venice. To that labor was recently added the charge—pressed upon me by a "
            "great concourse of scholars—of rendering the *Elements* of Euclid of Megara into our native tongue, "
            "which with the good help of heaven succeeded most happily. Not long prior, nourishing our spirits "
            "with hope, I had dedicated to Ludovico Sforza, Duke of Milan, a treatise entitled *De Divina "
            "Proportione*, with such ardor that I also added to it its geometric figures engraved by the hands "
            "of our Leonardo da Vinci, so that they might render the science of perspective more instructive. "
            "I presented that codex to the Duke while he still ruled, receiving generous gifts from him in return; "
            "and our presentation was made all the more joyous by the presence as witnesses of two great lights "
            "of the Roman Church, Cardinal Ippolito d'Este and your most wise brother the Cardinal, together with "
            "that most distinguished citizen Francesco Pepi, who was then serving alongside your brother as "
            "Florentine Ambassador. Now, however, you will rightfully claim this book as your own, since you "
            "recovered the manuscript after it had been lost during the fall of Ludovico's principate; in it you "
            "may from time to time refresh your mind when public cares are laid aside. And lest it come to you "
            "without an additional gift, I have appended two further treatises: one containing the most exact "
            "construction of the ancient Roman letters, demonstrating the power of curved and straight lines; "
            "the other laying out, as it were, steps for architects and for our fellow stonecutters and sculptors, "
            "which circulates under the names of members of your household and my fellow townsmen. Thus, since "
            "they owe all they have to you, in this part too they cannot but remain in your debt. Yet to you "
            "alone do we inscribe the whole work by name; for if I may speak the truth, the mathematical sciences "
            "possess nothing more sublime, more rare, or more useful. Now that my age is declining, I was "
            "unwilling to begrudge posterity this work, which is like a hidden treasure—especially as it could "
            "be dedicated to you alone, who by every kind of virtue and dignity of life easily excel the princes "
            "of our age, and who will attain the very end sought by all when you reach the active investigation "
            "of the regular bodies in their universality. I know this will be all the more delightful to you "
            "because you already possess inside your own home the physical models themselves, fashioned by our "
            "own industry. Nor should this vernacular and native tongue offend you, since the book will bring "
            "all the wider fruit the more numerous are its readers—especially as in these matters you seek "
            "scientific rigor rather than rhetorical ornament. All this you and your brother the Cardinal of "
            "Volterra, to whom I owe my very life, know as well as I ever wish you well. Farewell and prosper. "
            "Venice, the 9th of June, 1509."
        ),
    },
    8: {
        "title": "Danielis Caietani Epistolium ad Andream Mocenicum (1509)",
        "subtitle": "Magnifico et Clarissimo Andreae Mocenico Veneto Patricio ... Danielis Caietani Epistolium",
        "text_la": (
            "Magnifico et Clarissimo Andreae Mocenico Veneto patricio Viro Magnifici et generosissimi "
            "D. Leonardi olim Serenissimi philosopho insigni atque in omni genere doctrinae "
            "spectatissimo Danielis Caietani Epistolium.\n\n"
            "Delectat me nimis fortuna saeculi hodierni, Magnifice Andrea, nuper edito libro de "
            "divina proportione inscripto per Magistrum Lucam paciolum a burgo Sancti Sepulchri "
            "maximum minoritanae sectae ornamentum quoi ambigo an quempiam deinceps in arithmetice "
            "parem conspicaturi simus. Ecce cum primum affui (nanque ut frequentissime soleo illum "
            "domi forte salutaveram) offendi Circa repetitionem libri occupatum rogo nunquid me "
            "velit. Contra ille nihil nisi ut me ames et divinam proportionem meam cognoscas quam "
            "chalcographi nunc premunt. Gavissus sum ilico mirum in modum quod tanti tamque rari "
            "atque incogniti arcani thensauro Seculum nostrum donetur. In quo fama quidem authoris "
            "sed Scientia non minus Crescit aliena: adeo fideliter Subtiliter acute res altas atque "
            "aliorum Captu longe Sepositas tractat enucleat: ut quod nullus in id genus professione "
            "ad hanc usque diem aut comprehendere potuit aut scivit: hic Solus sui altissimi "
            "intellectus indagine Conquirit atque investigat. Dicitposite magna acrimonia maxima "
            "disciplina ad hanc materiam: ut qui in ea diutissime versati sunt non eant inficias "
            "Lucam paciolum esse alterum nostrae aetatis Nicomachum qui numeri et mensurae "
            "disciplinam difusissime scripsit. Itaque ut primum potui per occupationum mearum "
            "sequestram remissionem deliberavi impetum incredibilis laetitiae tibi Andrea vir "
            "rarissimae probitatis et scientiae hoc epistolio meo relaxare: magis tua causa haud "
            "sat scio qui semper extitisti rerum optimarum sitientissimus lector et iudex "
            "indubitatus quam ipsius materiae quae rara est arguta Callida atque argumentosa. "
            "Sed hoc praeclarissimum opus de divina proportione solius lucae pacioli magistri in "
            "sacrae theologiae adytis exquisitissimi atque in numeraria disciplina mirandi "
            "temporibus nostris sub tuae conscientiae contemplatione tuaeque doctrinae censura "
            "acerrima laudatissimum exit in manus atque in vulgatur a qua nihil unquam probatum "
            "fuit nisi quod laudatissimum esset haec una vel sola vel maxima mihi fuit scribendi "
            "Causa qua te scilicet a profundo rerum publicarum extractum ad capessendae tantae "
            "doctrinae studium incitarem: quod eo facilius me impetraturum confido quia tibi aevi "
            "animique vigor obtigit integer ex quo patavium ad illum meracissimum scientiae fontem "
            "laudabili aviditate profectus cum ingenti totius gymnasii applausu titulum veri atque "
            "absolutissimi philosophi reportasti. In hoc autem evigilatissimo tractatu non solum "
            "reperturus es ipse quod discas sed et relaturus fortasse quod doceas. Multa audisti "
            "multa per te ipse Conquisivisti mathematico auspicatu optimo atque physionomorum quos "
            "doctores miro studio aemulatus es. Sed ad hanc materiam nullum facile iudices "
            "extitisse ad praesens usque doctorem qui huic in hoc genere conferendus sit (pace "
            "aliorum dixerim). Ad hoc est illud quod subiectum certe formidandum tanta facilitate "
            "prosequitur ut a promptae et planae disputationis comunione ne idiotarum quidem aut "
            "imperitorum suscitatio repudietur: quemadmodum in Euclide cernere est quem de rhomano "
            "Vernaculum fecit nihil ab opinione Castigatissima domini Campani declinans quem "
            "summopere probat et sequitur. Sed tandem Epistolae manus extrema imponatur in qua "
            "pauca haec de intimis delibavi. Tu vero Censor maxime lege ut primum legeris "
            "Competenti praeconio extollenda iudicabis. Vale ex patavio. VII. Idus maias. M.D.VIIII."
        ),
        "text_en": (
            "Short Epistle of Daniele Gaetani of Cremona to the Magnificent and Most Illustrious "
            "Andrea Mocenigo, Venetian Patrician, son of the Magnificent and Most Noble Lord Leonardo "
            "(formerly Doge), distinguished philosopher and most accomplished in every branch of learning.\n\n"
            "I rejoice exceedingly in the fortune of our present age, Magnificent Andrea, now that the "
            "book entitled *De Divina Proportione* is being published by Master Luca Pacioli of Borgo "
            "Sansepolcro, the greatest ornament of the Minorite Order, whose equal in arithmetic I "
            "doubt we shall ever behold again. Behold, as soon as I arrived (having, as is my frequent "
            "custom, called upon him at home to greet him), I found him busily engaged in reviewing the "
            "proofs of his book. When I asked what he wished of me, he replied: 'Nothing, save that you "
            "love me and come to know my *Divina Proportione*, which the printers are now pressing.' "
            "I rejoiced at once in a marvelous way that our age is being gifted with the treasure of "
            "so great, so rare, and so previously unknown a mystery. In it not only the author's fame "
            "but universal science itself grows: so faithfully, subtly, and acutely does he treat and "
            "unfold lofty matters far removed from ordinary comprehension, that what no one in that "
            "profession up to this day was able either to grasp or to know, he alone by the inquiry of "
            "his most elevated intellect investigates and discovers. He sets forth this subject with "
            "great penetration and consummate mastery, so that those who have spent the longest time in "
            "these studies cannot deny that Luca Pacioli is a second Nicomachus of our age, who wrote "
            "most comprehensively on the science of number and measure. Therefore, as soon as a brief "
            "respite from my duties allowed, I resolved to share this burst of incredible joy with you, "
            "Andrea—a man of the rarest probity and learning—by means of this letter: no less for your "
            "own sake, as one who has ever been the most eager reader and unerring judge of the finest "
            "works, than for the sake of the subject matter itself, which is rare, acute, ingenious, "
            "and rich in demonstration. Thus this most illustrious work on the Divine Proportion—by "
            "Master Luca Pacioli alone, most accomplished in the inner sanctuaries of sacred theology "
            "and admirable in our times in the science of numbers—comes forth into the world under the "
            "contemplation of your judgment and the keen censorship of your learning, by which nothing "
            "was ever approved save what was most praiseworthy. And this possesses the further virtue "
            "that he treats a truly formidable subject with such lucidity and ease that not even "
            "uninitiated or lay readers are excluded from sharing in its clear and accessible exposition—"
            "just as may be seen in his edition of Euclid, which he rendered into the vernacular without "
            "departing from the most rigorous commentary of Campanus, whom he greatly approves and "
            "follows. Read it, then, Greatest of Critics, and as soon as you have read it you will judge "
            "it worthy of the highest praise. Farewell, from Padua, the 9th of May, 1509."
        ),
    },
}

# Alphabet plates mapping (folios 0139..0183 odd)
ALPHABET_PLATES = [
    (139, "A", "Lettera A"),
    (141, "B", "Lettera B"),
    (143, "C", "Lettera C"),
    (145, "D", "Lettera D"),
    (147, "E", "Lettera E"),
    (149, "F", "Lettera F"),
    (151, "G", "Lettera G"),
    (153, "H", "Lettera H"),
    (155, "I", "Lettera I / J"),
    (157, "K", "Lettera K"),
    (159, "L", "Lettera L"),
    (161, "M", "Lettera M"),
    (163, "N", "Lettera N"),
    (165, "O1", "Lettera O (primo modo perfectissimo)"),
    (167, "O2", "Lettera O (secondo modo)"),
    (169, "P", "Lettera P"),
    (171, "Q", "Lettera Q"),
    (173, "R", "Lettera R"),
    (175, "S", "Lettera S"),
    (177, "T", "Lettera T"),
    (179, "V", "Lettera V"),
    (181, "X", "Lettera X"),
    (183, "Y", "Lettera Y"),
]

# Polyhedra plates (folios 0187..0309 odd, with 0213 and 0215 architectural plates)
POLYHEDRA_PLATES = {
    187: ("I", 1, "Tetrahedron Planum Solidum", "Τετράεδρον ἐπίπεδον στερεόν", "Solid Regular Tetrahedron"),
    189: ("II", 2, "Tetrahedron Planum Vacuum", "Τετράεδρον ἐπίπεδον κενόν", "Hollow Regular Tetrahedron"),
    191: ("III", 3, "Tetrahedron Abscisum Solidum", "Τετράεδρον ἀποτετμημένον στερεόν", "Solid Truncated Tetrahedron"),
    193: ("IIII", 4, "Tetrahedron Abscisum Vacuum", "Τετράεδρον ἀποτετμημένον κενόν", "Hollow Truncated Tetrahedron"),
    195: ("V", 5, "Tetrahedron Elevatum Solidum", "Τετράεδρον ἐπηρμένον στερεόν", "Solid Stellated (Elevated) Tetrahedron"),
    197: ("VI", 6, "Tetrahedron Elevatum Vacuum", "Τετράεδρον ἐπηρμένον κενόν", "Hollow Stellated (Elevated) Tetrahedron"),
    199: ("VII", 7, "Exahedron sive Cubus Planum Solidum", "Ἑξάεδρον ἢ κύβος ἐπίπεδον στερεόν", "Solid Regular Hexahedron (Cube)"),
    201: ("VIII", 8, "Exahedron Planum Vacuum", "Ἑξάεδρον ἐπίπεδον κενόν", "Hollow Regular Hexahedron (Cube)"),
    203: ("VIIII", 9, "Exahedron Abscisum Solidum", "Ἑξάεδρον ἀποτετμημένον στερεόν", "Solid Truncated Hexahedron (Cuboctahedron)"),
    205: ("X", 10, "Exahedron Abscisum Vacuum", "Ἑξάεδρον ἀποτετμημένον κενόν", "Hollow Truncated Hexahedron (Cuboctahedron)"),
    207: ("XI", 11, "Exahedron Elevatum Solidum", "Ἑξάεδρον ἐπηρμένον στερεόν", "Solid Elevated Hexahedron"),
    209: ("XII", 12, "Exahedron Elevatum Vacuum", "Ἑξάεδρον ἐπηρμένον κενόν", "Hollow Elevated Hexahedron"),
    211: ("XIII", 13, "Exahedron Abscisum Elevatum Solidum", "Ἑξάεδρον ἀποτετμημένον ἐπηρμένον στερεόν", "Solid Elevated Truncated Hexahedron"),
    217: ("XIIII", 14, "Exahedron Abscisum Elevatum Vacuum", "Ἑξάεδρον ἀποτετμημένον ἐπηρμένον κενόν", "Hollow Elevated Truncated Hexahedron"),
    219: ("XV", 15, "Octahedron Planum Solidum", "Ὀκτάεδρον ἐπίπεδον στερεόν", "Solid Regular Octahedron"),
    221: ("XVI", 16, "Octahedron Planum Vacuum", "Ὀκτάεδρον ἐπίπεδον κενόν", "Hollow Regular Octahedron"),
    223: ("XVII", 17, "Octahedron Abscisum Solidum", "Ὀκτάεδρον ἀποτετμημένον στερεόν", "Solid Truncated Octahedron"),
    225: ("XVIII", 18, "Octahedron Abscisum Vacuum", "Ὀκτάεδρον ἀποτετμημένον κενόν", "Hollow Truncated Octahedron"),
    227: ("XIX", 19, "Octahedron Elevatum Solidum", "Ὀκτάεδρον ἐπηρμένον στερεόν", "Solid Elevated Octahedron (Stella Octangula)"),
    229: ("XX", 20, "Octahedron Elevatum Vacuum", "Ὀκτάεδρον ἐπηρμένον κενόν", "Hollow Elevated Octahedron (Stella Octangula)"),
    231: ("XXI", 21, "Icosahedron Planum Solidum", "Εἰκοσάεδρον ἐπίπεδον στερεόν", "Solid Regular Icosahedron"),
    233: ("XXII", 22, "Icosahedron Planum Vacuum", "Εἰκοσάεδρον ἐπίπεδον κενόν", "Hollow Regular Icosahedron"),
    235: ("XXIII", 23, "Icosahedron Abscisum Solidum", "Εἰκοσάεδρον ἀποτετμημένον στερεόν", "Solid Truncated Icosahedron"),
    237: ("XXIIII", 24, "Icosahedron Abscisum Vacuum", "Εἰκοσάεδρον ἀποτετμημένον κενόν", "Hollow Truncated Icosahedron"),
    239: ("XXV", 25, "Icosahedron Elevatum Solidum", "Εἰκοσάεδρον ἐπηρμένον στερεόν", "Solid Elevated Icosahedron"),
    241: ("XXVI", 26, "Icosahedron Elevatum Vacuum", "Εἰκοσάεδρον ἐπηρμένον κενόν", "Hollow Elevated Icosahedron"),
    243: ("XXVII", 27, "Dodecahedron Planum Solidum", "Δωδεκάεδρον ἐπίπεδον στερεόν", "Solid Regular Dodecahedron"),
    245: ("XXVIII", 28, "Dodecahedron Planum Vacuum", "Δωδεκάεδρον ἐπίπεδον κενόν", "Hollow Regular Dodecahedron"),
    247: ("XXIX", 29, "Dodecahedron Abscisum Solidum", "Δωδεκάεδρον ἀποτετμημένον στερεόν", "Solid Truncated Dodecahedron (Icosidodecahedron)"),
    249: ("XXX", 30, "Dodecahedron Abscisum Vacuum", "Δωδεκάεδρον ἀποτετμημένον κενόν", "Hollow Truncated Dodecahedron (Icosidodecahedron)"),
    251: ("XXXI", 31, "Dodecahedron Elevatum Solidum", "Δωδεκάεδρον ἐπηρμένον στερεόν", "Solid Elevated Dodecahedron"),
    253: ("XXXII", 32, "Dodecahedron Elevatum Vacuum", "Δωδεκάεδρον ἐπηρμένον κενόν", "Hollow Elevated Dodecahedron"),
    255: ("XXXIII", 33, "Dodecahedron Abscisum Elevatum Solidum", "Δωδεκάεδρον ἀποτετμημένον ἐπηρμένον στερεόν", "Solid Elevated Truncated Dodecahedron"),
    257: ("XXXIIII", 34, "Dodecahedron Abscisum Elevatum Vacuum", "Δωδεκάεδρον ἀποτετμημένον ἐπηρμένον κενόν", "Hollow Elevated Truncated Dodecahedron"),
    259: ("XXXV", 35, "Vigintisex Basium Planum Solidum", "Εἰκοσιεξάεδρον ἐπίπεδον στερεόν", "Solid 26-Base Body (Rhombicuboctahedron)"),
    261: ("XXXVI", 36, "Vigintisex Basium Planum Vacuum", "Εἰκοσιεξάεδρον ἐπίπεδον κενόν", "Hollow 26-Base Body (Rhombicuboctahedron)"),
    263: ("XXXVII", 37, "Vigintisex Basium Abscisum Elevatum Solidum", "Εἰκοσιεξάεδρον ἀποτετμημένον ἐπηρμένον στερεόν", "Solid Elevated 26-Base Body"),
    265: ("XXXVIII", 38, "Vigintisex Basium Abscisum Elevatum Vacuum", "Εἰκοσιεξάεδρον ἀποτετμημένον ἐπηρμένον κενόν", "Hollow Elevated 26-Base Body"),
    267: ("XXXIX", 39, "Septuaginta Duarum Basium Solidum", "Ἑβδομηκονταδισσάεδρον στερεόν", "Solid 72-Base Body"),
    269: ("XL", 40, "Septuaginta Duarum Basium Vacuum", "Ἑβδομηκονταδισσάεδρον κενόν", "Hollow 72-Base Body"),
    271: ("XLI", 41, "Columna Laterata Triangula Solida", "Κίων πλευρώδης τρίγωνος στερεός", "Solid Triangular Prism (Corpus Seratile)"),
    273: ("XLII", 42, "Columna Laterata Triangula Vacua", "Κίων πλευρώδης τρίγωνος κενός", "Hollow Triangular Prism"),
    275: ("XLIII", 43, "Pyramis Laterata Triangula Solida", "Πυραμὶς πλευρώδης τρίγωνος στερεά", "Solid Triangular Pyramid"),
    277: ("XLIIII", 44, "Pyramis Laterata Triangula Vacua", "Πυραμὶς πλευρώδης τρίγωνος κενή", "Hollow Triangular Pyramid"),
    279: ("XLV", 45, "Columna Laterata Quadrangula Solida", "Κίων πλευρώδης τετράγωνος στερεός", "Solid Quadrangular Prism"),
    281: ("XLVI", 46, "Columna Laterata Quadrangula Vacua", "Κίων πλευρώδης τετράγωνος κενός", "Hollow Quadrangular Prism"),
    283: ("XLVII", 47, "Pyramis Laterata Quadrangula Solida", "Πυραμὶς πλευρώδης τετράγωνος στερεά", "Solid Quadrangular Pyramid"),
    285: ("XLVII-bis", 47, "Pyramis Laterata Quadrangula Solida (bis)", "Πυραμὶς πλευρώδης τετράγωνος στερεά", "Solid Quadrangular Pyramid (Duplicate Scan in Witness)"),
    287: ("XLVIII", 48, "Pyramis Laterata Quadrangula Vacua", "Πυραμὶς πλευρώδης τετράγωνος κενή", "Hollow Quadrangular Pyramid"),
    289: ("XLIX", 49, "Columna Laterata Penthagona Solida", "Κίων πλευρώδης πεντάγωνος στερεός", "Solid Pentagonal Prism"),
    291: ("L", 50, "Columna Laterata Penthagona Vacua", "Κίων πλευρώδης πεντάγωνος κενός", "Hollow Pentagonal Prism"),
    293: ("LI", 51, "Pyramis Laterata Penthagona Solida", "Πυραμὶς πλευρώδης πεντάγωνος στερεά", "Solid Pentagonal Pyramid"),
    295: ("LII", 52, "Pyramis Laterata Penthagona Vacua", "Πυραμὶς πλευρώδης πεντάγωνος κενή", "Hollow Pentagonal Pyramid"),
    297: ("LIII", 53, "Columna Laterata Exagona Solida", "Κίων πλευρώδης ἑξάγωνος στερεός", "Solid Hexagonal Prism"),
    299: ("LIIII", 54, "Columna Laterata Exagona Vacua", "Κίων πλευρώδης ἑξάγωνος κενός", "Hollow Hexagonal Prism"),
    301: ("LV", 55, "Pyramis Laterata Triangula Inaequilatera Solida", "Πυραμὶς πλευρώδης τρίγωνος ἀνισόπλευρος στερεά", "Solid Scalene Triangular Pyramid"),
    303: ("LVI", 56, "Pyramis Laterata Triangula Inaequilatera Vacua", "Πυραμὶς πλευρώδης τρίγωνος ἀνισόπλευρος κενή", "Hollow Scalene Triangular Pyramid"),
    305: ("LVII", 57, "Columna Rotunda Solida", "Κίων στρογγύλος στερεός", "Solid Round Column (Cylinder)"),
    307: ("LVIII", 58, "Pyramis Rotunda Solida", "Πυραμὶς στρογγύλη στερεά", "Solid Round Pyramid (Cone)"),
    309: ("LIX (printed LXI)", 59, "Sphera Solida", "Σφαῖρα στερεά", "Solid Sphere"),
}


def parse_alphabet_texts() -> Dict[str, Dict[str, str]]:
    """Extract clean Italian and German descriptions for letters A..Y and architectural plates from 06_plates.txt."""
    plates_it = {
        "A": (
            "Questa letera A si cava del tondo e del suo quadro: la gamba da man drita vol esser grossa "
            "dele nove parti luna de lalteza. La gamba senistra vol esser la mita de la gamba grossa. "
            "La gamba de mezo vol esser la terza parte de la gamba grossa. La largheza de dita letera "
            "cadauna gamba per mezo de la crosiera, quella di mezo alquanto più bassa comme vedi qui "
            "per li diametri segnati."
        ),
        "B": (
            "Questa letera B si compone de doi tondi e quello desotto sie lo più grando de li nove parti "
            "luna cioè vol esser li cinque noni de la sua alteza per diametro. E quella desopra vol esser "
            "li quatro noni medesimamente per diametro comme qui desopra proportionatamente negliochi te sapresenta."
        ),
        "C": (
            "Questa lettera C se cava del tondo e del suo quadro ingrossando la quarta parte de fore e "
            "ancora de dentro. La testa desopra fenisci sopra la croci del diametro e circonferentia. "
            "Quella desotto passando la croci mezo nono apresso la costa del quadrato comme apare in la "
            "figura e cavasi comme uno O."
        ),
        "D": (
            "Questa letera D se cava del tondo e del quadro. La gamba derita vol esser de dentro le "
            "crosere grossa de nove parti luna; el corpo se ingrossa commo deli altri tondi. La apicatura "
            "desopra vol esser grossa el terzo de la gamba grossa et quella desotto el quarto over terzo."
        ),
        "E": (
            "Questa lettera E se cava del tondo e del suo quadro. La gamba grossa vol esser de le nove "
            "parti luna. La gamba desopra vol esser per la mita de la gamba grossa, quella de sotto per "
            "simile. Quella de mezo per terza parte de la gamba grossa comme quella de mezo del A, e la "
            "detta lettera vol esser larga meza del suo quadro et sic erit perfectissima."
        ),
        "F": (
            "Questa lettera F se forma a quel modo come la lettera E ne più ne mancho excepto che F si e "
            "senza la terza gamba: come denanci havesti diffusamente al luoco de ditto E cum tutte suo "
            "proportioni, pero qui quello te basti."
        ),
        "G": (
            "Questa letera G si forma commel C del suo tondo e quadro. La gamba deritta de sotto vol "
            "esser alta un terzo del suo quadro: e grossa de le nove parti luna de lalteza del suo quadrato."
        ),
        "H": (
            "Questa lettera H si cava del tondo e del suo quadro. Le sue gambe grosse si fanno per mezo "
            "le crosiere cioè dove se intersecano li diametri del tondo e suo quadro. La grosseza de "
            "ditte gambe vol esser de le nove parti una de lalteza. E quella de mezo se fa per mezo el "
            "diametro: la sua grosseza vol esser la terza parte de la gamba grossa commel traverso del A."
        ),
        "I": (
            "Questa lettera I se cava del tondo e del quadro; la sua grosseza vol esser de le nove parti "
            "luna che facil fia sua formatione fra laltre."
        ),
        "K": (
            "Questa lettera K se cava del tondo e del suo quadro tirando una linea per diametro del "
            "quadro; in questa linea se ferma e termina le due gambe per mezo la gamba grossa. La gamba "
            "de sotto vol esser grossa comme laltre gambe una parte de le nove. Quella de sopra la mita "
            "de la grossa comme la sinistra del A. Quella de sotto vol esser longa fin ala crociera over "
            "di fora. Quella de sopra dentro la crociera."
        ),
        "L": (
            "Questa lettera L se cava del tondo e del suo quadro. La sua grosseza vol esser de le nove "
            "parti una de laltezza. La sua largheza mezo quadro cum questi tondi soprascripti. La gamba "
            "sutile de sotto vol esser per la mita de la grossa comme quella del E et del F."
        ),
        "M": (
            "Questa lettera M se cava del tondo e del suo quadro. Le gambe suttili vogliano esser per "
            "mezo de le grosse comme la senistra del A. Le extreme gambe vogliano esser alquanto dentro "
            "al quadro; le medie fra quelle e le intersecationi de li diametri; lor grosseze grosse e "
            "sutili se referiscano a quelle del A comme disopra in figura aperto poi comprendere."
        ),
        "N": (
            "Questa lettera N se cava del suo tondo et etiam quadro. La prima gamba vol esser fora de la "
            "intersecatione de li diametri. La traversa de mezo vol esser grossa de le nove parti luna "
            "presa diametraliter. La terza gamba vol esser fora de la crociera. Prima gamba et ultima "
            "vogliano esser grosse la mita de la gamba grossa cioè duna testa."
        ),
        "O1": "Questo O è perfectissimo.",
        "O2": (
            "Questa lettera O si cava del tondo e del suo quadro. Se divide in quatro parti cioè in croce "
            "per mezo le quatro linee; el corpo suo vol esser grosso de le nove parti luna; el corpo suo "
            "de sopra vol esser per mezo del suo grosso. Le sue pance una vol pender in su laltra in giù; "
            "el sutile del corpo vol esser per la terza parte de la sua pancia. E perche di lui sonno doi "
            "opinioni pero te no posto un altro a mio piacere perfectissimo e tu prendi qual te pare e di "
            "loro formarai el Q comme disotto intenderai a suo luoco."
        ),
        "P": (
            "Questa lettera P si cava del tondo e del suo quadro. La sua gamba grossa vol esser de le "
            "nove parti luna. La forma del tondo vol esser grande comme quella del B da basso, e la sua "
            "grosseza de la pancia vol esser tanto quanto la gamba grossa e si vol principiar ditta "
            "lettera da le crociere del tondo grande cioè da le intersecationi de li diametri et sic "
            "erit perfectissima."
        ),
        "Q": (
            "Questa letera Q comme disopra dissi se cava del O, terminando sua gamba tre teste de sua "
            "altezza sotto el quadrato cioè de le nove parti le tre del suo quadrato overo diametro del "
            "suo tondo comme qui appare proportionata, guidando le pance grosse e sue sutili opposite a "
            "poncto comme del O fo dicto. E la sua gamba vol esser longa nove teste cioè quanto el suo "
            "quadrato a rectangulo, e la fine vol esser alta la poncta in su un nono de laltezza sequendo "
            "la curvita de la penna con la degradatione de la sua grosseza."
        ),
        "R": (
            "Questa lettera R se cava de la lettera B; el suo tondo sie de sotto dal centro una meza "
            "gamba. Tutta questa lettera vol esser dentro de le croci excepto la gamba storta vol uscir "
            "for de le croci fin al fin del quadro. Dicta gamba storta vol esser grossa de le nove parti "
            "luna terminata sutile in ponta nellangulo del quadro a modo de curve linee ut hic in exemplo patet."
        ),
        "S": (
            "Questa lettera S se cava de octo tondi et questa sie la sua ragione ut hic in exemplo "
            "apparet, li quali per le sue paralelle trovando lor centri troverai quelli de sotto esser "
            "magiori de li de sopra un terzo del nono del suo quadro. La pancia de mezzo vol esser grossa "
            "el nono aponto de lalteza. Le sutili un terzo de la grosseza terminando le teste con sua gratia."
        ),
        "T": (
            "Questa lettera T se cava del suo quadro e tondo. La gamba grossa vol esser a poncto comme "
            "del I fo detto. Quella traversa vol esser grossa per la mita de la grossa comme quelle "
            "disopra al E et F e vol terminare mezza testa per lato da le coste del suo quadro e fia ala "
            "vista gratissima."
        ),
        "V": (
            "Questa lettera V se cava del suo quadro tutto intero. La gamba senistra vol esser grossa el "
            "nono del suo quadro presa diametraliter comme la dextra del A e traversa del N. La dextra "
            "la mita de la grossa pur diametraliter presa comme la senistra del A e termina poncto nella "
            "basa del quadro in fin del diametro del tondo."
        ),
        "X": (
            "Questa lettera X vol tutto el suo quadro incrociando sue gambe nella intersecatione de li "
            "diametri. E luna vol esser grossa la nona parte de laltezza. Laltra la mita prese "
            "diametraliter terminando sue gambe con debita gratia secondo la forza de li tondi piccoli."
        ),
        "Y": (
            "Questa lettera Y vol tutto el quadro; le gambe dextra e senistra vogliano esser grosse comme "
            "la proportione de quelle del V, salvo che le terminano a poncto in su la intersecatione de "
            "li diametri, e da inde in giù si tira lor conjunctione ala basa del quadrato grossa el nono "
            "del quadrato; le teste de sopra finescano su li soi tondi comme vedi."
        ),
    }
    plates_de = {
        "A": (
            "Dieser Buchstabe A wird aus dem Kreise und seinem Quadrat entnommen. Das Bein zur Rechten "
            "muss einen der neun Theile der Höhe dick sein. Das linke Bein muss halb so dick sein als "
            "das dicke. Das mittlere (Quer-) Bein muss den dritten Theil des dicken Beines dick sein. "
            "Die Breite besagten Buchstabens bestimmt jedes Bein mittelst des Kreuzungspunktes der "
            "Diagonalen. Das mittlere liegt ein wenig tiefer, wie du hier mittelst der vorgezeichneten "
            "Durchmesser ersiehst."
        ),
        "B": (
            "Dieser Buchstabe B setzt sich aus zwei Kreisen zusammen und der untere ist der grössere: "
            "nämlich von den neun Theilen der Gesammthöhe muss er fünf zum Durchmesser haben, und der "
            "obere vier Neuntel, wie es sich dir hier oben im rechten Verhältniss den Augen darstellt."
        ),
        "C": (
            "Dieser Buchstabe C wird aus dem Kreise und seinem Quadrat entnommen, indem man den vierten "
            "Theil des Kreisbogens von aussen und innen her verdickt. Der Kopf oben endigt über dem "
            "Durchschnitt des Durchmessers und Kreisumfanges, der unten überschreitet den Kreuzungspunkt "
            "um ein halbes Neuntel nahe der Ecke des Quadrates, wie es in der Figur erhellt, und ergibt "
            "sich auf dieselbe Art wie ein O."
        ),
        "D": (
            "Dieser Buchstabe D wird aus dem Kreise und Quadrate entnommen. Das geradlinige Bein muss "
            "zwischen den Kreuzpunkten von Kreis und Diagonalen einen der neun Theile dick sein. Der "
            "runde Körper verdickt sich wie bei anderen Krümmungen. Das Verbindungsglied oben muss ein "
            "Drittel des dicken Beines dick sein, und das unten ein Viertel oder ein Drittel."
        ),
        "E": (
            "Dieser Buchstabe E leitet sich aus dem Kreise und seinem Vierseit her. Das dicke Bein muss "
            "einen der neun Theile, das obere die Hälfte des dicken Beines stark sein, das untere "
            "gleicherweise; das mittlere den dritten Theil des dicken Beines, wie das mittlere des A, "
            "und besagter Buchstabe muss so breit sein wie die halbe Seite seines Vierecks, und so wird "
            "er am vollkommensten sein."
        ),
        "F": (
            "Dieser Buchstabe F bildet sich auf die Art wie der Buchstabe E, weder mehr noch weniger, "
            "ausgenommen dass F ohne das dritte Bein ist, wie du es deutlich am Ort besagten E vor Augen "
            "gehabt hast mit allen seinen Proportionen. Darum möge hier dieses dir genügen."
        ),
        "G": (
            "Dieser Buchstabe G bildet sich wie das C aus seinem Kreise und Vierseit. Das untere gerade "
            "Bein muss ein Drittel seiner Quadratseite hoch und einen der neun Theile der Höhe seines "
            "Quadrats dick sein."
        ),
        "H": (
            "Dieser Buchstabe H wird aus dem Kreise und seinem Vierseit abgeleitet. Seine dicken Beine "
            "werden mittelst der Kreuzungspunkte gemacht, d. h. wo die Peripherie des Kreises und die "
            "Diagonalen des Quadrats sich schneiden. Die Dicke besagter Beine muss einen der neun Theile "
            "der Höhe betragen, und das mittlere wird mittelst des Durchmessers gemacht. Seine Dicke "
            "muss den dritten Theil des dicken Beines betragen, wie der Querbalken des A."
        ),
        "I": (
            "Dieser Buchstabe I (J) wird aus dem Kreise und Vierseit entnommen. Seine Dicke muss einen "
            "von den neun Theilen betragen, so dass seine Bildung vor den übrigen leicht ist."
        ),
        "K": (
            "Dieser Buchstabe K wird aus dem Kreise und seinem Vierseit entnommen, indem man eine Linie "
            "als Durchmesser des Vierseits zieht. In dieser Linie beschliessen und beendigen sich die "
            "beiden Beine in der Mitte des dicken Beines. Das untere Bein muss wie die übrigen Beine "
            "einen der neun Theile dick sein; das obere die Hälfte des dicken, wie das linke des A. Das "
            "untere muss bis zum Kreuzungspunkt oder darüber hinaus lang sein; das obere bleibt "
            "innerhalb des Kreuzungspunktes."
        ),
        "L": (
            "Dieser Buchstabe L wird aus dem Kreise und seinem Vierseit entnommen. Seine Dicke muss "
            "einen der neun Theile der Höhe betragen. Seine Breite die Hälfte der Quadratseite mit den "
            "darüber beschriebenen Rundungen. Das dünne Bein muss unten halb so dick sein wie das dicke, "
            "wie das des E und des F."
        ),
        "M": (
            "Dieser Buchstabe M wird aus dem Kreise und seinem Quadrat entnommen. Die dünnen Beine "
            "müssen halb so dick sein wie die dicken, wie das linke des A. Die äusseren Beine müssen "
            "ein wenig einwärts in das Quadrat treten; die mittleren liegen zwischen jenen und den "
            "Durchschnitten der Durchmesser. Ihre Dicken, dickere und dünnere, verhalten sich wie die "
            "des A, wie du aus der Figur deutlich verstehen kannst."
        ),
        "N": (
            "Dieser Buchstabe N wird aus seinem Kreise und aus dem Quadrat entnommen. Das erste Bein "
            "muss ausserhalb des Durchschnittes der Durchmesser liegen. Das mittlere Querbein muss einen "
            "der neun Theile, diametral genommen, dick sein. Das dritte Bein muss ausserhalb des "
            "Kreuzungspunktes liegen. Erstes und letztes Bein müssen halb so dick sein wie das dicke "
            "Bein, nämlich eine halbe Kopflänge (1/18 der Quadratseite)."
        ),
        "O1": "Dieses O ist sehr vollkommen.",
        "O2": (
            "Dieser Buchstabe O wird aus dem Kreise und seinem Quadrat entnommen. Es wird in vier Theile "
            "getheilt, d. h. kreuzweise mittelst der vier Mittellinien. Sein Körper muss einen der neun "
            "Theile dick sein, und sein Körper muss oben halb so dick sein als sein dicker Theil. Von "
            "seinen Bäuchen muss einer aufwärts, der andere abwärts hängen. Der dünne Theil des Körpers "
            "muss ein Drittel seines Bauches dick sein. Und weil darüber zwei Meinungen herrschen, so "
            "habe ich dir noch einen anderen hingesetzt, der nach meinem Gefallen sehr vollkommen ist, "
            "und du nimmst, welcher dir gut dünkt, und wirst aus ihnen das Q bilden."
        ),
        "P": (
            "Dieser Buchstabe P wird aus dem Kreise und seinem Vierseit entnommen. Sein dickes Bein muss "
            "einen der neun Theile betragen. Die Form des Runden muss so gross sein wie der untere des "
            "B und die Dicke des Bauches muss so gross sein wie das dicke Bein, und besagter Buchstabe "
            "muss an den Kreuzungspunkten des grossen Kreises beginnen, und so wird er sehr vollkommen sein."
        ),
        "Q": (
            "Dieser Buchstabe Q wird, wie ich oben sagte, aus dem O entnommen, indem sein Bein drei "
            "Kopflängen seiner Höhe unterhalb des Quadrats, d. h. drei von den neun Theilen seiner "
            "Quadratseite oder Durchmesser seines Kreises endet, wie es hier im rechten Verhältniss "
            "erscheint, indem man die dicken Bäuche und seine dünnen entgegengesetzten genau wie beim O "
            "gesagt worden führt. Und sein Bein muss neun Kopflängen, d. h. so lang wie sein "
            "rechtwinkeliges Vierseit sein, und das Ende muss am obersten Punkte ein Neuntel der Höhe "
            "hoch sein, indem man der Krümmung der Feder mit der Abnahme seiner Dicke folgt."
        ),
        "R": (
            "Dieser Buchstabe R wird aus dem Buchstaben B abgeleitet. Seine Rundung geht um eine halbe "
            "Beindicke unterhalb des Centrums. Dieser ganze Buchstabe muss innerhalb der Kreuzungspunkte "
            "liegen, ausgenommen das gebogene Bein, welches über die Kreuzpunkte hinaus bis ans Ende des "
            "Vierseits gehen muss. Besagtes gebogenes Bein muss einen der neun Theile dick sein, indem "
            "es dünn in eine Spitze am Ende des Vierseits nach Art von krummen Linien ausläuft."
        ),
        "S": (
            "Dieser Buchstabe S wird aus acht Kreisen entnommen und dieses ist sein Bildungsgesetz, wie "
            "hier im Beispiel erhellt. Nachdem du von diesen Kreisen mittelst ihrer Parallelen ihre "
            "Centra aufgefunden, so wirst du finden, dass die unteren um ein Drittel des Neuntels seines "
            "Quadrats grösser seien als die oberen. Der Bauch in der Mitte muss genau den neunten Theil "
            "der Höhe dick sein. Die dünneren Theile ein Drittel der Dicke, indem die Köpfe in "
            "anmuthiger Form endigen."
        ),
        "T": (
            "Dieser Buchstabe T wird aus dem Quadrat und Kreise entnommen. Das dicke Bein muss genau so "
            "sein, wie beim I gesagt worden. Das Querbein muss halb so dick sein wie das dicke, wie das "
            "obere beim E und F, und muss um eine halbe Kopflänge beiderseits von den Ecken seiner "
            "Quadratseite enden, und wird beim Anblick sehr anmuthig."
        ),
        "V": (
            "Dieser Buchstabe V wird aus seinem ganzen vollen Quadrat entnommen. Das linke Bein muss den "
            "neunten Theil seines Quadrats, diametral genommen, dick sein, wie das rechte des A und "
            "quere des N. Das rechte halb so dick als das dicke, ebenfalls diametral genommen wie das "
            "linke des A, und endigt in einem Punkte in der Basis des Quadrates am Ende des Kreisdurchmessers."
        ),
        "X": (
            "Dieser Buchstabe X bedarf seines ganzen Quadrats, indem sich seine Beine im Durchschnitt "
            "der Durchmesser kreuzen. Und das eine muss den neunten Theil der Höhe dick sein, das andere "
            "die Hälfte davon, beide diametral genommen, indem seine Beine mit erforderlicher Anmuth "
            "gemäss dem Zwange der kleinen Kreise endigen."
        ),
        "Y": (
            "Dieser Buchstabe Y erfordert das ganze Quadrat. Das rechte und linke Bein müssen so dick "
            "sein wie das Verhältniss derer des V aufweist, abgesehen dass sie genau im Durchschnitt der "
            "Durchmesser endigen. Und von da nach unten zieht man von ihrer Verbindung bis zur Basis "
            "eine ein Neuntel der Quadratseite dicke Linie. Die Spitzen oben endigen auf ihren Kreisen, "
            "wie du siehst."
        ),
    }
    res = {}
    for k in plates_it:
        res[k] = {"it": plates_it[k], "de": plates_de.get(k, "")}
    return res


ARCHITECTURAL_PLATES = {
    137: {
        "title": "Divina Proportio — Caput Humanum (Proportional Profile of the Human Head)",
        "it": "Divina Proportio. Figura del capo humano proportionato secondo il triangolo equilatero e il quadrato (Tractato de l'Architectura, Cap. I–II).",
        "de": "Divina Proportio. Proportionale Construction des menschlichen Kopfes im Dreieck- und Quadratnetz (Tractat über die Architektur, Cap. I–II).",
    },
    185: {
        "title": "Porta Templi Domini Dicta Speciosa",
        "it": (
            "PORTA TEMPLI DOMINI DICTA SPECIOSA.\n\n"
            "In la presente figura de la porta detta Speciosa le doi parti qui aducte cioè de la colonna "
            "rotonda con suo capitello, Basa, Stilobata et Steriobata, Epistilio cum suo Zophoro e "
            "Cornicione mi rendo certo Lectore che al intellecto debitamente lochio del tuo peregrino "
            "ingegno lo representa."
        ),
        "de": (
            "PORTA TEMPLI DOMINI DICTA SPECIOSA.\n\n"
            "Hinsichtlich der Figur des „Speciosa“ genannten Thores des Tempels Salomonis und der hier "
            "vorgeführten beiden Theile: nämlich der runden Säule mit ihrem Capitäl, Basis, Stilobat "
            "und Stereobat, Epistil mit seinem Zophoros und Karnies, bin ich sicher, Leser, dass das "
            "Auge deines bewanderten Geistes es in richtiger Weise dem Verständniss vorführe."
        ),
    },
    213: {
        "title": "Colonna Corinta, Jonica e Pulvinata con Stilobata e Steriobata",
        "it": (
            "Colonna detta Corinta respecto al Capitello, Abaco e Cimasa; Jonica e Pulvinata quanto ala "
            "Basa e in capitello come apieno nel suo libro Vitruvio expone de tutte.\n\n"
            "Per la importantia e varietà di questi nomi ala tavola ordinata nel principio del libro "
            "recorri e quella te mandara al suo capitulo. Dove apieno intenderai lor differentia antica "
            "e moderna etc.\n\n"
            "Benche tre sieno le sorti principali de le colonne dali antichi celebrate cioè Jonica, "
            "Dorica e Corinta: Non di meno molte altre più oltra speculando sonno dali pratici retrovate "
            "alochio vaghe e a li hedificii bastanti ale quali ancora non ben a pieno fia el nome "
            "assegnato cioè nel domo de Pisa e in Firence San Spirito e San Lorenzo digno patronato de "
            "la casa di Medici.\n\n"
            "Questo Vitruvio lo chiama Stillobata e da li Moderni fia detto Pilastrello overo basamento. "
            "El fundamento soto terra fin al suo piano largo quanto sua basa fia detto Steriobata."
        ),
        "de": (
            "Säule, korinthisch genannt, bezüglich des Capitäls, Abacus und Gesims; jonische und "
            "Polstersäule bezüglich der Basis und am Capitäl, wie Vitruv in seinem Buche vor Allem "
            "deutlich darlegt.\n\n"
            "Wegen der Wichtigkeit und Verschiedenheit dieser Namen geh' auf die am Anfange des Buches "
            "angeordnete Tafel zurück und diese wird dich auf das betreffende Capitel hinweisen, woraus "
            "du vollkommen ihre Unterschiede im Alterthum und jetzt verstehen wirst.\n\n"
            "Obwohl der Hauptsäulengattungen drei sind, welche von den Alten gepriesen, nämlich die "
            "dorische, jonische und korinthische, so sind nichtsdestoweniger viele andere darüber "
            "hinausspekulirend von den Praktikern aufgefunden, die für das Auge schön und für die "
            "Bauten genügend sind, nämlich im Dom zu Pisa und Florenz, S. Spirito und S. Lorenzo, dem "
            "würdigen Patronat des Hauses Medici.\n\n"
            "Dies nennt Vitruv Stilobat, und von den Modernen wird es Pilaster oder Basament genannt. "
            "Das Fundament unter der Erde bis zu seiner Grundebene, ebenso breit wie seine Basis, heisst Stereobat."
        ),
    },
    215: {
        "title": "Epistilio (Architrave), Zophoro (Fregio) e Cornicione",
        "it": (
            "Tutto el composto dal Zophoro in giù da li Antichi fia detto Epistilio e da li moderni "
            "Architrave, e tutto el composto sopra depso li Antichi cornice e moderni cornicione.\n\n"
            "- a = Fastigio over Fascia da li Antichi e moderni ut supra;\n"
            "- c = Fascia over Fastigio comme de sopra fo detto da cadauno;\n"
            "- e = Li antichi a questo dicano Fascia e a le volte Fastigio e cosi li moderni;\n"
            "- f = Questo da li antichi fia detto Echino e da li moderni Huovolo;\n"
            "- g = A questo li antichi dicano Scothia, li moderni gola de larchitrave;\n"
            "- k = Questo cadauno lo dice Cimacio del Fregio e Zophoro;\n"
            "- l = Li antichi li dicano Denticeli, li moderni denticelli e Rastro;\n"
            "- m = Li antichi li dicano Corona, li moderni la chiamano gociolatoro;\n"
            "- o = Li antichi a questo dicano Acrotherio, li moderni Regolo de la cornice.\n\n"
            "Quel che qui e posto de Colonna, Architrave e Cornicione solo acenno de lo intero exemplo "
            "fia facto perche apieno di loro non si po in breve dirne maxime per la gran varietà de "
            "proportioni e proportionalita che in sue debite dispositioni se ricercano. Il che tutto el "
            "rende chiaro el sublime volume del nostro degno Anticho Architecto Vitruvio Pollione. Dove "
            "ben monito de Arithmetica, Geometria e Quinto del perspicacissimo nostro Platonico e "
            "Megarense Phylosopho Euclide. Tal tutto Lectore te remetto senza la cui doctrina non e "
            "possibile in agibilibus Prathice e Theorice alcuna cosa bene exercitarse: cum omnia in "
            "numero, pondere et mensura disposuerit Altissimus et cetera."
        ),
        "de": (
            "Die ganze Zusammensetzung vom Zophoros abwärts wird von den Alten Epistyl und von den "
            "Modernen Architrav genannt, und die ganze Zusammensetzung oberhalb desselben von den Alten "
            "„Karnies“ und von den Modernen „Cornicione“.\n\n"
            "- a = Giebelabschluss oder Bündel von Alten und Modernen;\n"
            "- c = Bündel oder Giebelabschluss wie oben gesagt;\n"
            "- e = Die Alten sagen hiefür Bündel und zuweilen Giebelabschluss, und ebenso die Modernen;\n"
            "- f = Dies wird von den Alten Echinus und von den Modernen Eierstab genannt;\n"
            "- g = Hiefür sagen die Alten Scotia, die Modernen Kehle des Architravs;\n"
            "- k = Dieses nennen beide Gesimse des Frieses und Zophoros;\n"
            "- l = Die Alten sagen hier Zähne, die Modernen Zähnchen und „Rechen“;\n"
            "- m = Die Alten sagen hier Krone, die Modernen Dachtraufe;\n"
            "- o = Die Alten sagen dafür Akrotherion, die Modernen Stab des Karnieses.\n\n"
            "Das was hier über Säule, Architrav und Karnies beigebracht, ist nur als Skizze des "
            "vollständigen Beispiels dargestellt, weil man vollständig darüber in kurzen Worten nicht "
            "reden kann wegen der grossen Verschiedenheit der Verhältnisse und Proportionen. Alles das "
            "macht der erhabene Band unseres würdigen alten Architekten Vitruvius Pollio klar, worin "
            "über Arithmetik, Geometrie und das Fünfte (Perspective) unseres scharfsinnigen Platonikers "
            "und megaräischen Philosophen Euklid gut gehandelt worden: weil Alles nach Zahl, Gewicht "
            "und Mass der Höchste angeordnet hat."
        ),
    },
    311: {
        "title": "Arbor Proportio et Proportionalitas",
        "it": (
            "ARBOR PROPORTIO ET PROPORTIONALITAS.\n\n"
            "Maxime geometre interest de proportionibus totaliter disserere. Nam arithmeticus non "
            "invenit in omnibus numeris proportionis modum: infinite. n. sunt proportiones quas "
            "numerorum natura non patitur ut ex 5. elementorum E. clare habetur.\n\n"
            "Sicut numeri caput est unitas, ita proportionum aequalitatem esse principium. B. 2. musi. "
            "capi. 15. Amica. n. est similitudo.\n\n"
            "Et sic in infinitum in ultimis speciebus. Quae omnia et singula in Summa nostra "
            "arithmetice et geometrie theorice et pratice sigillatim declarata sunt distinctione 6. "
            "tractatu primo per totum. Ideo ibi recurras et contentaberis non immemor 5. Euclidis."
        ),
        "de": (
            "STAMMBAUM DER PROPORTION UND PROPORTIONALITÄT (ARBOR PROPORTIO ET PROPORTIONALITAS).\n\n"
            "Vor allem dem Geometer kommt es zu, vollständig über die Proportionen zu handeln; denn der "
            "Arithmetiker findet nicht in allen Zahlen das Mass des Verhältnisses, da es unendlich viele "
            "Proportionen gibt, welche die Natur der Zahlen nicht zulässt, wie aus dem V. Buche der "
            "Elemente Euklids klar hervorgeht.\n\n"
            "Wie die Einheit das Haupt der Zahl ist, so ist die Gleichheit der Ursprung der "
            "Proportionen (Boethius, De institutione musica II, c. 15).\n\n"
            "Und so bis ins Unendliche in den letzten Arten; welches alles im Einzelnen in unserer "
            "Summa de Arithmetica et Geometria (Distinctio VI, Tractatus I) erklärt ist."
        ),
    },
}


def clean_winterberg_lines(raw_text: str) -> Tuple[str, str, List[str]]:
    """Parse a Winterberg chapter file into (cap_header, title, clean_paragraphs)."""
    lines = raw_text.splitlines()
    cleaned_lines = []
    for ln in lines:
        s = ln.strip()
        # Skip OCR page markers or Winterberg running footers/page numbers
        if re.match(r"^##\s*p\.\s*\(#\d+\)", s):
            continue
        if re.match(r"^[0-9iIlL\s\.]{1,5}$", s):
            continue
        if "Quellenschriften f. Kunstgesch" in s:
            continue
        # Skip short editorial footnote lines like "1) l. da." or "^) I. siate."
        if re.match(r"^[\^1-9\*][\)\]]\s*(l\.|I\.|d\.\s*i\.|Soll\s)", s):
            continue
        cleaned_lines.append(s)

    # Extract header and title
    nonempty_idx = [i for i, l in enumerate(cleaned_lines) if l]
    if not nonempty_idx:
        return "", "", []

    first_i = nonempty_idx[0]
    first_line = cleaned_lines[first_i]
    cap_header = ""
    title = ""
    body_start_i = first_i + 1

    if re.match(r"^(Cap|Gap|Ca)[\.,\s]+[IVXLCDM0-9]+", first_line, re.IGNORECASE):
        cap_header = re.sub(r"^(Gap|Ca)\b", "Cap.", first_line).strip()
        if len(nonempty_idx) > 1:
            sec_i = nonempty_idx[1]
            title = cleaned_lines[sec_i]
            body_start_i = sec_i + 1
    else:
        # e.g. 001_dedication.txt where first paragraph is the epistola salutation
        cap_header = "Cap. I."
        # Collect first paragraph as title/salutation
        sal_parts = []
        idx = first_i
        while idx < len(cleaned_lines) and cleaned_lines[idx]:
            sal_parts.append(cleaned_lines[idx])
            idx += 1
        title = " ".join(sal_parts)
        body_start_i = idx

    # Reconstruct paragraphs from body_start_i
    paras = []
    cur = []
    for ln in cleaned_lines[body_start_i:]:
        if not ln:
            if cur:
                # Join hyphenated words across line breaks
                joined = ""
                for w_line in cur:
                    if joined.endswith("-") and w_line and w_line[0].islower():
                        joined = joined[:-1] + w_line
                    else:
                        joined = (joined + " " + w_line).strip()
                paras.append(joined)
                cur = []
        else:
            cur.append(ln)
    if cur:
        joined = ""
        for w_line in cur:
            if joined.endswith("-") and w_line and w_line[0].islower():
                joined = joined[:-1] + w_line
            else:
                joined = (joined + " " + w_line).strip()
        paras.append(joined)

    # Clean minor OCR artifacts in title and paragraphs
    def fix_ocr_typos(t: str) -> str:
        t = re.sub(r"\bGomme\b", "Comme", t)
        t = re.sub(r"\bGommo\b", "Commo", t)
        t = re.sub(r"\bGon\b", "Con", t)
        t = re.sub(r"\bGonciosia\b", "Conciosia", t)
        t = re.sub(r"\bGap\.", "Cap.", t)
        t = re.sub(r"\[\^[0-9]+\]|\^[0-9]*\)|[1-9]\)", "", t)
        t = re.sub(r"\s{2,}", " ", t).strip()
        return t

    title = fix_ocr_typos(title)
    paras = [fix_ocr_typos(p) for p in paras if fix_ocr_typos(p)]
    return cap_header, title, paras


def split_text_across_folios(
    full_text_lines: List[str],
    folios: List[int],
    folio_kmers: Dict[int, set[str]],
) -> Dict[int, List[str]]:
    """Split a list of lines/sentences across a contiguous range of folios using 5-gram overlap."""
    if not folios:
        return {}
    if len(folios) == 1 or not full_text_lines:
        return {folios[0]: full_text_lines}

    # If lines are long paragraphs, split into sentences so page breaks are fine-grained
    sentences: List[str] = []
    for p in full_text_lines:
        parts = re.split(r"(?<=[\.\:\;\?])\s+", p)
        for pt in parts:
            if pt.strip():
                sentences.append(pt.strip())

    if len(sentences) < len(folios):
        res = {f: [] for f in folios}
        for idx, s in enumerate(sentences):
            res[folios[min(idx, len(folios) - 1)]].append(s)
        return res

    # Dynamic programming or sequential binary split for k folios
    remaining = sentences
    result: Dict[int, List[str]] = {}
    for idx in range(len(folios) - 1):
        f_curr = folios[idx]
        f_next = folios[idx + 1]
        k_curr = folio_kmers.get(f_curr, set())
        k_next = folio_kmers.get(f_next, set())

        diffs = []
        for s in remaining:
            sk = kmers(norm(s), 5)
            sc_curr = len(sk & k_curr)
            sc_next = len(sk & k_next)
            diffs.append(sc_next - sc_curr)

        best_split = 1
        best_val = -1e9
        max_split = max(2, len(remaining) - (len(folios) - 1 - idx) + 1)
        for sp in range(1, max_split):
            val = sum(-x for x in diffs[:sp]) + sum(x for x in diffs[sp:])
            if val > best_val:
                best_val = val
                best_split = sp

        result[f_curr] = remaining[:best_split]
        remaining = remaining[best_split:]

    result[folios[-1]] = remaining
    return result


def main() -> None:
    # Load folio 5-grams from existing .txt files (or fallback to existing concordance.json if .txt files were already removed)
    conc_path = PAG_DIR / "concordance.json"
    existing_conc = json.loads(conc_path.read_text(encoding="utf-8")) if conc_path.exists() else None

    folio_kmers: Dict[int, set[str]] = {}
    folio_raw_txt: Dict[int, str] = {}
    has_txt = False
    for fnum in range(1, 319):
        txt_p = PAG_DIR / f"{fnum:04d}.txt"
        if txt_p.exists():
            has_txt = True
            raw = txt_p.read_text(encoding="utf-8", errors="ignore")
            folio_raw_txt[fnum] = raw
            folio_kmers[fnum] = kmers(norm(raw), 5)
        else:
            folio_raw_txt[fnum] = ""
            folio_kmers[fnum] = set()

    # 1. Process Part I (Compendio de Divina Proportione, Chapters 1..71)
    wb_it1_dir = WB_DIR / "01_divina_proportione_italian"
    wb_de1_dir = WB_DIR / "03_divina_proportione_german"
    wb_en1_dir = WB_EN_DIR / "01_divina_proportione_italian"
    wb_en2_dir = WB_EN_DIR / "divina_en_2"

    if not has_txt and existing_conc:
        compendio_chapters = existing_conc["chapters"]["compendio"]
        architectura_chapters = existing_conc["chapters"]["architectura"]
    else:
        compendio_chapters: List[Dict[str, Any]] = []
        cur_f = 17
        for cnum in range(1, 72):
            roman = ROMAN_NUMERALS[cnum]
            it_files = sorted(wb_it1_dir.glob(f"{cnum:03d}_*.txt"))
            de_files = sorted(wb_de1_dir.glob(f"{cnum:03d}_*.txt"))
            en1_files = sorted(wb_en1_dir.glob(f"{cnum:03d}_*.txt"))
            en2_files = sorted(wb_en2_dir.glob(f"{cnum:03d}_*.txt"))

            it_raw = it_files[0].read_text(encoding="utf-8", errors="ignore") if it_files else ""
            de_raw = de_files[0].read_text(encoding="utf-8", errors="ignore") if de_files else ""

            _, title_it, paras_it = clean_winterberg_lines(it_raw)
            _, title_de, paras_de = clean_winterberg_lines(de_raw)

            full_norm = norm(" ".join(paras_it))
            inc_k = kmers(full_norm[:220], 5)
            exc_k = kmers(full_norm[-220:], 5)

            best_s = cur_f
            best_sc = -1.0
            for fn in range(cur_f, min(62, cur_f + 5)):
                sc = len(inc_k & folio_kmers[fn]) / max(1, len(inc_k))
                if sc > best_sc:
                    best_sc = sc
                    best_s = fn
            cur_f = best_s

            best_e = best_s
            best_esc = -1.0
            for fn in range(best_s, min(62, best_s + 5)):
                sc = len(exc_k & folio_kmers[fn]) / max(1, len(exc_k))
                if sc > best_esc:
                    best_esc = sc
                    best_e = fn
            if best_e < best_s:
                best_e = best_s
            cur_f = best_e

            folios_spanned = list(range(best_s, best_e + 1))
            it_by_folio = split_text_across_folios(paras_it, folios_spanned, folio_kmers)
            de_by_folio: Dict[int, List[str]] = {}
            if len(folios_spanned) == 1:
                de_by_folio[folios_spanned[0]] = paras_de
            else:
                de_sents = []
                for p in paras_de:
                    for pt in re.split(r"(?<=[\.\:\;\?])\s+", p):
                        if pt.strip():
                            de_sents.append(pt.strip())
                total_it_chars = max(1, sum(len(" ".join(v)) for v in it_by_folio.values()))
                de_idx = 0
                for idx_f, fn in enumerate(folios_spanned):
                    if idx_f == len(folios_spanned) - 1:
                        de_by_folio[fn] = de_sents[de_idx:]
                    else:
                        frac = len(" ".join(it_by_folio[fn])) / total_it_chars
                        take = max(1, round(frac * len(de_sents)))
                        de_by_folio[fn] = de_sents[de_idx : de_idx + take]
                        de_idx += take

            compendio_chapters.append({
                "book": 1,
                "part": "compendio",
                "chapter": cnum,
                "roman": roman,
                "slug": f"cap_{cnum:02d}",
                "title_it": title_it,
                "title_de": title_de,
                "start_folio": f"{best_s:04d}",
                "end_folio": f"{best_e:04d}",
                "folios": [f"{fn:04d}" for fn in folios_spanned],
                "winterberg_it": f"winterberg/01_divina_proportione_italian/{it_files[0].name}" if it_files else None,
                "winterberg_de": f"winterberg/03_divina_proportione_german/{de_files[0].name}" if de_files else None,
                "draft_en_1": f"winterberg_en/01_divina_proportione_italian/{en1_files[0].name}" if en1_files else None,
                "draft_en_2": f"winterberg_en/divina_en_2/{en2_files[0].name}" if en2_files else None,
                "paragraphs_it": paras_it,
                "paragraphs_de": paras_de,
                "folio_slices_it": {f"{fn:04d}": [" ".join(it_by_folio[fn])] for fn in folios_spanned if it_by_folio.get(fn)},
                "folio_slices_de": {f"{fn:04d}": [" ".join(de_by_folio[fn])] for fn in folios_spanned if de_by_folio.get(fn)},
            })

        wb_it2_dir = WB_DIR / "02_architectura_italian"
        wb_de2_dir = WB_DIR / "04_architectura_german"
        wb_en2_de_dir = WB_EN_DIR / "04_architectura_german"

        arch_items_spec = [("dedication", 0, "Prohemio")] + [
            (f"cap_{c:02d}", c, ROMAN_NUMERALS[c]) for c in range(1, 21)
        ]

        architectura_chapters: List[Dict[str, Any]] = []
        cur_f = 61
        for slug, cnum, roman in arch_items_spec:
            if cnum == 0:
                it_files = [wb_it2_dir / "001_dedication.txt"]
                de_files = [wb_de2_dir / "001_dedication.txt"]
                en_files = [wb_en2_de_dir / "001_dedication.txt"]
            else:
                it_files = sorted(wb_it2_dir.glob(f"{cnum:03d}_cap_*.txt"))
                de_files = sorted(wb_de2_dir.glob(f"{cnum:03d}_cap_*.txt"))
                en_files = sorted(wb_en2_de_dir.glob(f"{cnum:03d}_cap_*.txt"))

            it_raw = it_files[0].read_text(encoding="utf-8", errors="ignore") if it_files and it_files[0].exists() else ""
            de_raw = de_files[0].read_text(encoding="utf-8", errors="ignore") if de_files and de_files[0].exists() else ""

            _, title_it, paras_it = clean_winterberg_lines(it_raw)
            _, title_de, paras_de = clean_winterberg_lines(de_raw)

            full_norm = norm(" ".join(paras_it))
            inc_k = kmers(full_norm[:220], 5)
            exc_k = kmers(full_norm[-220:], 5)

            best_s = cur_f
            best_sc = -1.0
            for fn in range(cur_f, min(83, cur_f + 5)):
                sc = len(inc_k & folio_kmers[fn]) / max(1, len(inc_k))
                if sc > best_sc:
                    best_sc = sc
                    best_s = fn
            cur_f = best_s

            best_e = best_s
            best_esc = -1.0
            for fn in range(best_s, min(83, best_s + 5)):
                sc = len(exc_k & folio_kmers[fn]) / max(1, len(exc_k))
                if sc > best_esc:
                    best_esc = sc
                    best_e = fn
            if best_e < best_s:
                best_e = best_s
            cur_f = best_e

            folios_spanned = list(range(best_s, best_e + 1))
            it_by_folio = split_text_across_folios(paras_it, folios_spanned, folio_kmers)
            de_by_folio = {}
            if len(folios_spanned) == 1:
                de_by_folio[folios_spanned[0]] = paras_de
            else:
                de_sents = []
                for p in paras_de:
                    for pt in re.split(r"(?<=[\.\:\;\?])\s+", p):
                        if pt.strip():
                            de_sents.append(pt.strip())
                total_it_chars = max(1, sum(len(" ".join(v)) for v in it_by_folio.values()))
                de_idx = 0
                for idx_f, fn in enumerate(folios_spanned):
                    if idx_f == len(folios_spanned) - 1:
                        de_by_folio[fn] = de_sents[de_idx:]
                    else:
                        frac = len(" ".join(it_by_folio[fn])) / total_it_chars
                        take = max(1, round(frac * len(de_sents)))
                        de_by_folio[fn] = de_sents[de_idx : de_idx + take]
                        de_idx += take

            architectura_chapters.append({
                "book": 2,
                "part": "architectura",
                "chapter": cnum,
                "roman": roman,
                "slug": slug,
                "title_it": title_it,
                "title_de": title_de,
                "start_folio": f"{best_s:04d}",
                "end_folio": f"{best_e:04d}",
                "folios": [f"{fn:04d}" for fn in folios_spanned],
                "winterberg_it": f"winterberg/02_architectura_italian/{it_files[0].name}" if it_files and it_files[0].exists() else None,
                "winterberg_de": f"winterberg/04_architectura_german/{de_files[0].name}" if de_files and de_files[0].exists() else None,
                "draft_en": f"winterberg_en/04_architectura_german/{en_files[0].name}" if en_files and en_files[0].exists() else None,
                "paragraphs_it": paras_it,
                "paragraphs_de": paras_de,
                "folio_slices_it": {f"{fn:04d}": [" ".join(it_by_folio[fn])] for fn in folios_spanned if it_by_folio.get(fn)},
                "folio_slices_de": {f"{fn:04d}": [" ".join(de_by_folio[fn])] for fn in folios_spanned if de_by_folio.get(fn)},
            })

    # 3. Parse Front Matter TOC (0005, 0006, 0009..0016) from 000_toc.txt
    toc_it_raw = (wb_it1_dir / "000_toc.txt").read_text(encoding="utf-8", errors="ignore")
    toc_de_raw = (wb_de1_dir / "000_toc.txt").read_text(encoding="utf-8", errors="ignore")
    toc_it_sections = [s.strip() for s in toc_it_raw.split("---") if s.strip()]

    # Split Tabula (toc_it_sections[4]) across folios 11..16
    tabula_it_lines = [l.strip() for l in toc_it_sections[4].splitlines() if l.strip()] if len(toc_it_sections) >= 5 else []
    if not has_txt and existing_conc:
        tabula_it_by_folio = {
            fn: [existing_conc["folios"].get(f"{fn:04d}", {}).get("text_it", "")]
            for fn in range(11, 17)
        }
    else:
        tabula_it_by_folio = split_text_across_folios(tabula_it_lines, [11, 12, 13, 14, 15, 16], folio_kmers)

    alpha_texts = parse_alphabet_texts()
    alpha_by_folio = {fnum: (let_id, let_title) for fnum, let_id, let_title in ALPHABET_PLATES}

    # 4. Build per-folio concordance entries for all 318 folios
    folios_concordance: Dict[str, Dict[str, Any]] = {}
    for fnum in range(1, 319):
        fstr = f"{fnum:04d}"
        side = "recto" if fnum % 2 == 1 else "verso"

        # Determine section and original 1509 foliation
        if fnum <= 4:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = f"Flyleaf {(fnum + 1)//2}{'r' if side == 'recto' else 'v'}"
            folio_title = f"Flyleaf ({orig_folio})"
        elif fnum == 5:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = "A1r"
            folio_title = "Title Page — Divina Proportione (1509)"
        elif fnum == 6:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = "A1v"
            folio_title = "Epigrams and Author's Sonnet (Cinque corpi in natura son producti)"
        elif fnum == 7:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = "A2r"
            folio_title = FRONTMATTER_LATIN[7]["title"]
        elif fnum == 8:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = "A2v"
            folio_title = FRONTMATTER_LATIN[8]["title"]
        elif fnum in (9, 10):
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            orig_folio = f"A3{'r' if fnum == 9 else 'v'}"
            folio_title = f"Nomina et Numerus Corporum ({orig_folio})"
        elif 11 <= fnum <= 16:
            sec_id = "front_matter"
            book_title = "Front Matter and Dedications"
            leaf_a = (fnum - 5) // 2 + 1
            orig_folio = f"A{leaf_a}{'r' if side == 'recto' else 'v'}"
            folio_title = f"Tabula — Table of Contents ({orig_folio})"
        elif 17 <= fnum <= 61:
            sec_id = "compendio"
            book_title = "Part I: Compendio de Divina Proportione"
            leaf_num = (fnum - 17) // 2 + 1
            orig_folio = f"f. {leaf_num}{'r' if side == 'recto' else 'v'}"
            folio_title = f"Compendio de Divina Proportione ({orig_folio})"
        elif 62 <= fnum <= 84:
            sec_id = "architectura"
            book_title = "Part II: Tractato de l'Architectura"
            leaf_num = (fnum - 17) // 2 + 1
            orig_folio = f"f. {leaf_num}{'r' if side == 'recto' else 'v'}"
            folio_title = (
                f"Tractato de l'Architectura ({orig_folio})"
                if fnum <= 82
                else f"Blank Leaf ({orig_folio})"
            )
        elif 85 <= fnum <= 136:
            sec_id = "libellus"
            book_title = "Part III: Libellus in tres partiales tractatus divisus"
            leaf_num = (fnum - 85) // 2 + 1
            orig_folio = f"Libellus f. {leaf_num}{'r' if side == 'recto' else 'v'}"
            if fnum <= 100:
                tr_name = "Tractatus Primus"
            elif fnum <= 112:
                tr_name = "Tractatus Secundus"
            elif fnum <= 135:
                tr_name = "Tractatus Tertius"
            else:
                tr_name = "Blank Verso"
            folio_title = f"Libellus — {tr_name} ({orig_folio})"
        elif 137 <= fnum <= 186:
            sec_id = "alphabet"
            book_title = "Appendix I: The Roman Geometric Alphabet"
            orig_folio = f"Plate Folio {fstr} ({side})"
            if fnum in ARCHITECTURAL_PLATES:
                folio_title = ARCHITECTURAL_PLATES[fnum]["title"]
            elif fnum in alpha_by_folio:
                let_id, let_title = alpha_by_folio[fnum]
                folio_title = f"Roman Geometric Alphabet — {let_title}"
            else:
                folio_title = f"Alphabet Plate Verso ({fstr})"
        elif 187 <= fnum <= 310:
            sec_id = "polyhedra_plates"
            book_title = "Appendix II: Polyhedra Plates by Leonardo da Vinci"
            orig_folio = f"Plate Folio {fstr} ({side})"
            if fnum in POLYHEDRA_PLATES:
                pl_rom, pl_num, pl_la, pl_gr, pl_en = POLYHEDRA_PLATES[fnum]
                folio_title = f"Plate {pl_rom} — {pl_la} ({pl_en})"
            elif fnum in ARCHITECTURAL_PLATES:
                folio_title = f"Architectural Plate — {ARCHITECTURAL_PLATES[fnum]['title']}"
            else:
                folio_title = f"Polyhedra Plate Verso ({fstr})"
        else:
            sec_id = "end_matter"
            book_title = "End Matter and Colophon"
            orig_folio = f"End Matter {fstr} ({side})"
            if fnum in ARCHITECTURAL_PLATES:
                folio_title = ARCHITECTURAL_PLATES[fnum]["title"]
            else:
                folio_title = f"Endleaf ({fstr})"

        # Find chapters spanning this folio
        chaps_on_folio: List[Dict[str, Any]] = []
        for ch in compendio_chapters:
            if fstr in ch["folios"]:
                chaps_on_folio.append({
                    "book": 1,
                    "part": "compendio",
                    "chapter": ch["chapter"],
                    "roman": ch["roman"],
                    "slug": ch["slug"],
                    "title_it": ch["title_it"],
                    "title_de": ch["title_de"],
                    "winterberg_it": ch["winterberg_it"],
                    "winterberg_de": ch["winterberg_de"],
                    "starts_on_folio": ch["start_folio"] == fstr,
                })
        for ch in architectura_chapters:
            if fstr in ch["folios"]:
                chaps_on_folio.append({
                    "book": 2,
                    "part": "architectura",
                    "chapter": ch["chapter"],
                    "roman": ch["roman"],
                    "slug": ch["slug"],
                    "title_it": ch["title_it"],
                    "title_de": ch["title_de"],
                    "winterberg_it": ch["winterberg_it"],
                    "winterberg_de": ch["winterberg_de"],
                    "starts_on_folio": ch["start_folio"] == fstr,
                })

        if chaps_on_folio and 17 <= fnum <= 82:
            chap_labels = [
                f"Cap. {c['roman']}" if c["chapter"] > 0 else "Prohemio (Architectura)"
                for c in chaps_on_folio
            ]
            first_t = chaps_on_folio[0]["title_it"][:55]
            folio_title = f"{', '.join(chap_labels)} ({orig_folio}) — {first_t}"

        # Load existing graphics from <folio>.json
        jf_path = PAG_DIR / f"{fstr}.json"
        jf_data = json.loads(jf_path.read_text(encoding="utf-8")) if jf_path.exists() else {}
        graphics = jf_data.get("graphics", [])

        # Enhance captions on plate graphics
        for g in graphics:
            if fnum in POLYHEDRA_PLATES and g["id"].startswith("g"):
                pl_rom, pl_num, pl_la, pl_gr, pl_en = POLYHEDRA_PLATES[fnum]
                g["type"] = "plate"
                g["caption"] = f"Plate {pl_rom}: {pl_la} ({pl_gr}) — {pl_en}"
                g["plate_number"] = pl_num
                g["plate_roman"] = pl_rom
                g["title_la"] = pl_la
                g["title_gr"] = pl_gr
                g["title_en"] = pl_en
            elif fnum in alpha_by_folio and g["id"].startswith("g"):
                let_id, let_title = alpha_by_folio[fnum]
                g["type"] = "plate"
                g["caption"] = f"Roman Geometric Alphabet — {let_title}"
                g["letter"] = let_id
            elif fnum in ARCHITECTURAL_PLATES and g["id"].startswith("g"):
                g["type"] = "plate"
                g["caption"] = ARCHITECTURAL_PLATES[fnum]["title"]

        # Update <folio>.json with verified chapters and section metadata
        jf_data["folio"] = fstr
        jf_data["page_num"] = fnum
        jf_data["side"] = side
        jf_data["original_folio"] = orig_folio
        jf_data["section_id"] = sec_id
        jf_data["section"] = book_title
        jf_data["title"] = folio_title
        if chaps_on_folio:
            jf_data["chapters"] = chaps_on_folio
        elif "chapters" in jf_data and fnum < 85:
            del jf_data["chapters"]
        jf_data["graphics"] = graphics

        jf_path.write_text(json.dumps(jf_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        folios_concordance[fstr] = {
            "folio": fstr,
            "page_num": fnum,
            "side": side,
            "original_folio": orig_folio,
            "section_id": sec_id,
            "book": book_title,
            "title": folio_title,
            "image": f"{fstr}.png",
            "rst": f"{fstr}.rst",
            "chapters": chaps_on_folio,
            "graphics": [
                {
                    "id": g["id"],
                    "type": g.get("type", "diagram"),
                    "file": g.get("file", f"{fstr}.{g['id']}.png"),
                    "caption": g.get("caption", ""),
                }
                for g in graphics
            ],
        }

        # Add frontmatter / plate texts to concordance entry so build_pacioli_folios_rst.py is self-contained
        if fnum == 5 and len(toc_it_sections) >= 1:
            folios_concordance[fstr]["text_it"] = toc_it_sections[0]
            folios_concordance[fstr]["text_de"] = "\n".join(toc_de_raw.splitlines()[:16]).strip()
        elif fnum == 6 and len(toc_it_sections) >= 2:
            folios_concordance[fstr]["text_it"] = toc_it_sections[1]
            folios_concordance[fstr]["text_de"] = "\n".join(toc_de_raw.splitlines()[16:77]).strip()
        elif fnum in FRONTMATTER_LATIN:
            folios_concordance[fstr]["text_la"] = FRONTMATTER_LATIN[fnum]["text_la"]
            folios_concordance[fstr]["text_en"] = FRONTMATTER_LATIN[fnum]["text_en"]
        elif fnum == 9 and len(toc_it_sections) >= 3:
            folios_concordance[fstr]["text_it"] = toc_it_sections[2]
        elif fnum == 10 and len(toc_it_sections) >= 4:
            folios_concordance[fstr]["text_it"] = toc_it_sections[3]
        elif 11 <= fnum <= 16:
            folios_concordance[fstr]["text_it"] = "\n\n".join(tabula_it_by_folio.get(fnum, []))
        elif fnum in alpha_by_folio:
            let_id, _ = alpha_by_folio[fnum]
            folios_concordance[fstr]["text_it"] = alpha_texts.get(let_id, {}).get("it", "")
            folios_concordance[fstr]["text_de"] = alpha_texts.get(let_id, {}).get("de", "")
        elif fnum in ARCHITECTURAL_PLATES:
            folios_concordance[fstr]["text_it"] = ARCHITECTURAL_PLATES[fnum]["it"]
            folios_concordance[fstr]["text_de"] = ARCHITECTURAL_PLATES[fnum]["de"]
        elif fnum in POLYHEDRA_PLATES:
            pl_rom, pl_num, pl_la, pl_gr, pl_en = POLYHEDRA_PLATES[fnum]
            folios_concordance[fstr]["plate"] = {
                "number": pl_num,
                "roman": pl_rom,
                "latin": pl_la,
                "greek": pl_gr,
                "english": pl_en,
            }

    # Save complete concordance.json
    concordance_data = {
        "work": "De Divina Proportione",
        "author": "Fra Luca Pacioli (with polyhedra woodcuts after Leonardo da Vinci)",
        "editions": {
            "paganini_1509": "Venetiis impressum per probum virum Paganinum de Paganinis de Brixia, M.D.IX.",
            "winterberg_1889": "Constantin Winterberg, Fra Luca Pacioli: Divina Proportione — Die Lehre vom Goldenen Schnitt (Wien: Carl Graeser, 1889).",
        },
        "total_folios": 318,
        "chapters": {
            "compendio": compendio_chapters,
            "architectura": architectura_chapters,
        },
        "plates": {
            "alphabet": [
                {
                    "folio": f"{fnum:04d}",
                    "letter": let_id,
                    "title": let_title,
                    "text_it": alpha_texts.get(let_id, {}).get("it", ""),
                    "text_de": alpha_texts.get(let_id, {}).get("de", ""),
                }
                for fnum, let_id, let_title in ALPHABET_PLATES
            ],
            "architectural": {
                f"{fnum:04d}": info for fnum, info in ARCHITECTURAL_PLATES.items()
            },
            "polyhedra": {
                f"{fnum:04d}": {
                    "roman": pl_rom,
                    "number": pl_num,
                    "latin": pl_la,
                    "greek": pl_gr,
                    "english": pl_en,
                }
                for fnum, (pl_rom, pl_num, pl_la, pl_gr, pl_en) in POLYHEDRA_PLATES.items()
            },
        },
        "folios": folios_concordance,
    }

    conc_path = PAG_DIR / "concordance.json"
    conc_path.write_text(json.dumps(concordance_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {conc_path} ({conc_path.stat().st_size} bytes)")

    # Update sections.json and pages.json to reference <folio>.rst instead of <folio>.txt
    sections_list = [
        {
            "id": "front_matter",
            "title": "Front Matter and Dedications",
            "start_page": 1,
            "end_page": 16,
            "description": "Title page, epigrams, dedication to Piero Soderini, Daniel Caietanus epistle, list of 61 bodies, and Tabula.",
        },
        {
            "id": "compendio",
            "title": "Part I: Compendio de Divina Proportione",
            "start_page": 17,
            "end_page": 61,
            "description": "Chapters I to LXXI: Dedication to Ludovico Sforza, 5 divine analogies, 13 miraculous effects of the golden ratio, Platonic & Archimedean solids, and measurements.",
        },
        {
            "id": "architectura",
            "title": "Part II: Tractato de l'Architectura",
            "start_page": 61,
            "end_page": 84,
            "description": "Dedication to Pacioli's disciples in Sansepolcro and Chapters I to XX on Vitruvian human proportion, columns, capitals, entablatures, and architecture.",
        },
        {
            "id": "libellus",
            "title": "Part III: Libellus in tres partiales tractatus divisus",
            "start_page": 85,
            "end_page": 136,
            "description": "Three mathematical treatises on the five regular bodies and dependent solids (vernacular translation of Piero della Francesca's Libellus).",
        },
        {
            "id": "alphabet",
            "title": "Appendix I: The Roman Geometric Alphabet",
            "start_page": 137,
            "end_page": 186,
            "description": "Proportional profile of the human head (Divina Proportio), geometric construction plates of classical Roman capital letters (A-Y), and Porta Speciosa.",
        },
        {
            "id": "polyhedra_plates",
            "title": "Appendix II: Polyhedra Plates by Leonardo da Vinci",
            "start_page": 187,
            "end_page": 310,
            "description": "Full-page woodcut illustrations designed by Leonardo da Vinci of regular, truncated, and elevated polyhedra in solid (planum) and skeletal (vacuum) forms (Plates I-LIX), plus architectural plates.",
        },
        {
            "id": "end_matter",
            "title": "End Matter and Arbor Proportionis",
            "start_page": 311,
            "end_page": 318,
            "description": "Arbor Proportio et Proportionalitas (Tree of Ratios and Proportions) and closing flyleaves.",
        },
    ]
    (PAG_DIR / "sections.json").write_text(json.dumps(sections_list, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    pages_list = []
    for fnum in range(1, 319):
        fstr = f"{fnum:04d}"
        finfo = folios_concordance[fstr]
        pages_list.append({
            "page_num": fnum,
            "folio": fstr,
            "original_folio": finfo["original_folio"],
            "section": finfo["section_id"],
            "title": finfo["title"],
            "image": f"{fstr}.png",
            "text": f"{fstr}.rst",
        })
    pages_manifest = {
        "work": "de_divina_proportione",
        "edition": "paganini_1509",
        "total_pages": 318,
        "pages": pages_list,
    }
    (PAG_DIR / "pages.json").write_text(json.dumps(pages_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Updated sections.json and pages.json (referencing <folio>.rst).")


if __name__ == "__main__":
    main()
