"""Constantin Winterberg's 1889 Critical Commentary, Preface, Introduction, and
17 Substantive Mathematical Notes (*Sachliche Anmerkungen*, pp. III-V, 1-15, 338-352)
in synchronized English and German (with restored LaTeX mathematical notation).
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

WINTERBERG_INTRO_EN = """.. rubric:: Series Title Page (*Quellenschriften für Kunstgeschichte*, Vienna, 1889)

*Quellenschriften für Kunstgeschichte und Kunsttechnik des Mittelalters und der Neuzeit*, published with the support of the Imperial-Royal Austrian Ministry for Worship and Education, founded by **Rudolf Eitelberger von Edelberg**, continued by **Albert Ilg**. New Series, Volume II (*Neue Folge, II. Band*): **Fra Luca Pacioli**, *Divina Proportione: Die Lehre vom Goldenen Schnitt* (*The Doctrine of the Golden Section*), newly edited, translated, and elucidated from the Venice Edition of the year 1509 by **Constantin Winterberg** (Vienna: Published by **Carl Graeser**, printed by **Carl Fromme**, 1889).

----

.. rubric:: Preface (*Vorwort*, Karlsruhe, March 1889)

The efforts of modern scholarship have long been directed toward recovering the lost technical foundations that continually recur in the pictorial and architectural composition of the masterpieces of the Renaissance, so that they might once again exert a stimulating influence upon contemporary art. To have advanced the solution of this task through the careful publication of the written traditions of the foremost masters of that era is the great merit of the *Quellenschriften für Kunstgeschichte und Kunsttechnik des Mittelalters und der Neuzeit*.

Indeed, it is precisely the technical treatises that have suffered the undeserved fate of either mouldering unused and half-forgotten in the libraries of Italy, or—when published in earlier centuries—standing so far removed from modern habits of expression that only a few scholars undertake their study. This applies above all to Fra Luca Pacioli's treatises, *De Divina Proportione* and the *Libellus de Quinque Corporibus Regularibus*. Modest as purely abstract scientific works, their chief value lies rather in the fact that, having arisen in the closest connection with the needs of artistic practice, they cast a flood of light upon the manner in which mathematical disciplines were applied in the visual arts during the first great flowering of the Early Renaissance. The cumbersome, archaic mode of expression and the dense, nearly indecipherable scribal and typographical abbreviations that characterize the surviving early sixteenth-century edition (Venice, 1509) explain why these treatises have hitherto remained virtually inaccessible to practicing artists, quite apart from the extreme rarity of the printed volumes themselves.

To remedy this deficiency at least in part through the present new edition, to offer a fresh contribution to the understanding of the artistic creation of a great epoch, and to dedicate a tribute of gratitude to the memory of the late Councillor **Rudolf von Eitelberger**—who alongside his friend **Heinrich Ludwig** in Rome gave the first impetus to this undertaking—affords the editor special satisfaction.

*Karlsruhe i. B., March 1889 — Constantin Winterberg*

----

1. Pacioli, Piero della Francesca, and Leonardo da Vinci
--------------------------------------------------------

Among the few writings of the Early Renaissance that treat technical and mathematical disciplines in their direct relation to artistic practice, none deserves the attention of both the historian and the specialist more than the celebrated treatises of **Fra Luca Pacioli**. Even the greatest and most famous artistic compilation of that age, **Leonardo da Vinci**'s *Trattato della Pittura* (*Book of Painting* / *Malerbuch*), consists essentially of loosely connected notes extending across the auxiliary sciences of painting without a unified systematic architecture. It is otherwise with the writings of Pacioli, which—despite all stylistic defects—form a complete, systematically worked-out whole. Their interest is heightened by the fact that they arose in immediate response to the practical needs of Renaissance workshops; indeed, the companion treatise on the five regular bodies (*Libellus de Quinque Corporibus Regularibus*) derives its substantive authorship from **Piero della Francesca**, a practicing master of the highest rank. Only in reading these treatises does one gain a full view of the formidable difficulties that confronted Renaissance artists even in elementary problems of solid geometry, and one cannot sufficiently admire the energy and insight with which the foremost masters strove to solve the problems required for their art using the mathematical tools inherited from antiquity.

**Fra Luca Pacioli**, a friar of the Franciscan Order, was born (according to **Guillaume Libri**, *Histoire des sciences mathématiques en Italie*, Vol. III) at **Borgo Sansepolcro** in the Tuscan Apennines—the very same town where **Piero della Francesca** first saw the light of day. According to **Jean-Étienne Montucla** (*Histoire des mathématiques*), Pacioli undertook travels to the Orient at the command of his Franciscan superiors, where he may have become more closely acquainted with Arabic mathematical science. The fruits of Pacioli's mathematical studies were first gathered in his monumental *Summa de Arithmetica, Geometria, Proportioni et Proportionalita* (Venice, 1494), dedicated to **Guidobaldo da Montefeltro**, Duke of Urbino. Beside its algebraic treatise, the *Summa de Arithmetica* includes an extensive geometric section in which continuous proportions are accorded special practical utility, and in which the golden section already appears as a privileged case.

Throughout his career, as **Giorgio Vasari** reports in his *Vite*, Pacioli stood in close scientific intercourse with the foremost artists of his age:

- **Piero della Francesca**, his elder compatriot, instructed him in the mathematical and perspective disciplines; in the *Summa de Arithmetica* and in the *Tractato de l'Architectura* (Chapter XIX), Pacioli hails Piero as *"il monarca alli tempi nostri della pictura e architectura"* ("the monarch of painting and architecture in our times").
- **Leonardo da Vinci** designed the sixty perspective plates of the regular and dependent polyhedra for *De Divina Proportione* during their joint residence at the Sforza court in Milan (1496–1499). These same perspective drawings of solid (*solidum*) and skeletal (*vacuum*) polyhedra passed into almost all subsequent sixteenth-century treatises on perspective. In the text of *De Divina Proportione*, Pacioli repeatedly celebrates his friendship with Leonardo and records primary eyewitness accounts of Leonardo's *Last Supper* (*Il Cenacolo*) in Santa Maria delle Grazie and the colossal bronze equestrian monument to **Francesco Sforza**.

From this living exchange between theory and workshop practice, between science and art, emerged *De Divina Proportione*—completed in manuscript at Milan in 1498 for Duke **Ludovico Maria Sforza** (*il Moro*) and first printed at Venice by **Paganino de' Paganini** in June 1509.

2. The Golden Section, Vitruvian Harmonic Ratios, and Aesthetic Rhythm
----------------------------------------------------------------------

In his *Histoire des sciences mathématiques en Italie* (Vol. III), **Guillaume Libri** asserted that Pacioli sought in *De Divina Proportione* to establish the golden section as a universal morphological and aesthetic law governing the human figure, architecture, and even the construction of the Roman alphabet. Closer examination of the text shows that this claim requires careful qualification:

- What Pacioli sets forth in the *Tractato de l'Architectura* concerning the proportions of the human body (Chapters I–III) and the classical column orders (Chapters IV–XX) is substantially a faithful restatement of **Vitruvius** (*De Architectura*, Books III–V). In Vitruvius, as in Renaissance architects such as **Leon Battista Alberti** (*De Re Aedificatoria*) and **Sebastiano Serlio** (*Sette Libri dell'Architettura*), it is not the irrational golden section, but rather **rational harmonic ratios** ($1:2$, $2:3$, $3:4$, $3:4:5$) derived from musical consonances and aliquot body modules ($\\frac{1}{6}$, $\\frac{1}{8}$, $\\frac{1}{10}$, $\\frac{1}{12}$) that govern architectural commensuration.
- Likewise, the twenty-three capital letters of the **Roman Alphabet** (Appendix I) are constructed from rational subdivisions ($\\frac{1}{9}$, $\\frac{1}{2}$, $\\frac{1}{3}$, $\\frac{1}{4}$) of the square and inscribed circle.
- Nevertheless, within the domain of solid geometry, Pacioli shows that not only the five Platonic solids (above all the dodecahedron and icosahedron), but also their truncated and stellated derivatives, are governed directly or indirectly by the proportion having a mean and two extremes. In Chapter LIV (and Chapter XIX of the *Tractato de l'Architectura*), Pacioli even conceives the progressive truncation and subdivision of polyhedra (*in agibilibus*, misprinted *"in ogibilibus"* in the 1509 edition) as a geometric method of exhaustion—an anticipation of the differential calculus—approaching curved vaults and the sphere itself, and urges architects and sculptors to follow the example of **Phidias** in applying the regular solids.

As **Euclid** already knew in the *Elements*, all the mathematical theorems Pacioli adduces on the *Divina Proportione* follow as necessary consequences from its definition (:just:`VI.def.3`, :just:`II.11`, :just:`VI.30`, :just:`XIII.1`–:just:`XIII.18`). When in the mid-nineteenth century **Adolf Zeising** (*Neue Lehre von den Proportionen des menschlichen Körpers*, 1854) revived the golden section as a universal morphological and aesthetic canon (*Kanon*) of the human figure, empirical measurements and canonical systems—whether constructed geometrically after the golden section by **Adolf Zeising** and **Brocheneck** (*Die männliche und weibliche Normalgestalt*), derived from the module of the vertebral column (*Wirbelsäule*) by **Carl Gustav Carus** (*Die Proportionslehre der menschlichen Gestalt*), based on an arbitrary geometric key by **Carl Schmidt** (*Proportionsschlüssel*), or determined purely empirically by probability and mean values by **Adolphe Quetelet** (*Anthropométrie*) and after him **J. J. Trost** (*Die Proportionslehre Dürer's*)—showed that while human proportions approximate the golden ratio within modest tolerances, any continuous geometric division adjusted to empirical means yields comparable external approximations, as **Emil Harless** (*Lehrbuch der plastischen Anatomie*) rightly observed.

Where the golden section possesses a genuine and unique aesthetic preeminence, however, is in **visual perception and rhythmic articulation**:

1. For the eye to perceive lawful articulation (*gesetzmässige Gliederung*) across the parts of a whole without artificial measuring aids, the governing law must announce itself immediately as a **continuous rhythm**.
2. In an **arithmetic series** generated additively from two initial terms ($c = a + b$, $d = b + c$, $e = c + d$, $\\dots$), every term is the sum of its two predecessors—an organic law of growth (as shown in **Constantin Winterberg**'s study *"Das Malerbuch Lionardo da Vinci's"* in *Jahrbücher der königlich preussischen Kunstsammlungen*, 1887, and exemplified both in the branching of trees and in the parallelogram composition of resultant forces $c, c'$ meeting at an angle).
3. In a **discontinuous geometric proportion** $\\frac{a}{b} = \\frac{c}{d}$ among four segments, two terms remain independent, creating a perceptual gap as the eye passes from $b$ to $c$. Only when the proportion becomes **continuous**—so that each neighbor-ratio equals the preceding ratio, $\\frac{b}{a} = \\frac{c}{b}$—can the eye follow an unbroken rhythmic progression.
4. When we unite **both** requirements in a single three-term relation—demanding simultaneously the **continuous geometric proportion** $a : b = b : c$ and the **additive arithmetic relation** $a + b = c$—we obtain uniquely the **Golden Section** (*der goldene Schnitt*):

   .. math::

      \\frac{b}{a} = \\frac{a + b}{b} = \\varphi = \\frac{1 + \\sqrt{5}}{2}.

Because every triad of consecutive terms satisfies both the multiplicative ratio and the additive sum of parts into the whole, the eye apprehends the unity of the whole and its parts immediately and without auxiliary perspective grids.

3. Mathematical Structure of the Treatise & Critique of the Mutual Inscriptions
-------------------------------------------------------------------------------

According to its mathematical content, Part I (*Compendio de Divina Proportione*) divides into four principal groups:

1. **The Thirteen Effects of the Divine Proportion (Chapters I–XXIII)**: After the dedication to **Ludovico Sforza**, the defense of mathematics, and the five divine attributes of the proportion (Chapters I–VI), Pacioli presents thirteen theorems on lines cut in extreme and mean ratio and their application to the regular pentagon, decagon, and hexagon (Chapters VII–XXIII, following **Euclid**, *Elements* Books II, IV, VI, and :just:`XIII.1`–:just:`XIII.12`). Because Pacioli states several of these theorems primarily through numerical examples (with $a+b = 10$, $a = \\sqrt{125}-5$, $b = 15-\\sqrt{125}$), concise algebraic proofs are supplied in **Anmerkungen 1–9**.
2. **Construction, Sphere Inscription, and Uniqueness of the Five Regular Solids (Chapters XXIV–XXXIV)**: Using the theorem of **Pythagoras** (:just:`I.47`) and the chord and tangent theorems of the circle in **Euclid**, Pacioli demonstrates why at most five regular polyhedra can exist in nature (:just:`XI.21`), constructs each solid in the sphere (:just:`XIII.13`–:just:`XIII.18`), and determines the ratios of their edges, altitudes, and sphere diameters (**Anmerkungen 10–14**).
3. **The Twelve Mutual Inscriptions and the Truncated/Elevated Dependent Bodies (Chapters XXXV–LV)**:
   In Chapters XXXV–XLVI, Pacioli treats twelve problems of inscribing one regular solid inside another, following **Euclid** Book XV (:just:`XV.1`–:just:`XV.12`) and his medieval predecessor **Campanus of Novara** (*Elementa Euclidis cum Commentariis Campani*). Here Pacioli repeats an error already criticized by **Niccolò Tartaglia** in his *General Trattato di Numeri et Misure* (*General-Trattato di Matematiche*): not only does he omit several valid inscriptions (such as the icosahedron in the cube, which **Tartaglia** and **Piero della Francesca**'s *Libellus de Quinque Corporibus Regularibus* both treat), but in **Chapter XLVI** he explicitly attempts to prove—on **Plato**'s cosmological grounds (*Timaeus*)—that **the octahedron cannot be inscribed in the icosahedron**!
   As **Niccolò Tartaglia** proved by far clearer and shorter methods than Pacioli's, and as shown in **Anmerkung 15**, this claim is false: joining the midpoints of the three pairs of opposite parallel edges of the icosahedron yields three mutually perpendicular axes of equal length, whose six endpoints form a regular octahedron inscribed in the icosahedron. And as demonstrated in full in **Anmerkung 17**, the modern projective theory of **poles and polar planes with respect to a concentric sphere** ($R = \\sqrt{r\\rho}$) immediately resolves the complete system of **all 21 possible mutual inscriptions** of the five regular solids by pairing each direct inscription (vertices on vertices, faces, or edges) with its polar-reciprocal dual (faces on faces, vertices, or edges).
   Chapters XLVII–LV then describe the **truncated** (*abscisi*) and **elevated/stellated** (*elevati*) dependent bodies (**Anmerkung 16**) and the 26-base and 72-base solids.
4. **The Sphere, Oblong Prisms/Columns, Pyramids/Cones, and Practical Mensuration (Chapters LVI–LXXI)**: After demonstrating how all five regular solids are carved within the sphere (Chapter LVII), Pacioli treats prismatic columns and pyramids, proves that the pyramid is one-third of the prism of equal base and height (:just:`XII.7`), and concludes with the panegyric to **Ludovico Sforza**, the ordering of **Leonardo da Vinci**'s plates, and a glossary of mathematical terms, serving as a theoretical preparation for the problems in the *Libellus de Quinque Corporibus Regularibus*.

Already among his sixteenth-century contemporaries—most famously **Annibale Caro** (*Apologia*)—Pacioli's diffuse, half-Latinized vernacular prose style, mingling mathematical theorems with scholastic and theological digressions, was disparagingly dubbed *"Ceneraccio"* ("ash-lye" / *Aschenlauge, Schmutzbrühe*). Yet fairness requires recognizing that the Franciscan friar, addressing courtly audiences of princes, nobles, and artists in his public lectures at Florence, Milan, Rome, and Venice, deliberately wove historical and practical episodes into his discourse to sustain the interest of his listeners.

4. Editorial Principles and Sources (1509 Venice Print & Vatican Manuscript)
----------------------------------------------------------------------------

The primary purpose of this 1889 edition was first to render readable again the archaic text of the 1509 Venice edition—which had become almost unreadable through scribal and typographical abbreviations of every kind—while correcting obvious printing corruptions in the mathematical letters and numbers, and second to provide a critical German translation and mathematical commentary using the methods of modern geometry, so that **Leonardo da Vinci**'s polyhedral constructions may once again inspire contemporary artists, architects, and engineers.

The copy of the 1509 Venice edition (**Paganino de' Paganini**, *Paganinus de Paganinis de Brixia*) used as the basis of this work belongs to the library of the **k. k. Österreichisches Museum für Kunst und Industrie** in Vienna, kindly placed at the editor's disposal by the late Director Hofrat **Rudolf von Eitelberger**; in doubtful passages, the illuminated manuscript in the **Vatican Library** (*Cod. Vat. Lat. 3129*) was also consulted.

.. rubric:: Winterberg's Footnotes to the Introduction (*Einleitung*, pp. 1–15)

1. **Footnote 1 (p. 2)**: **Guillaume Libri**, *Histoire des sciences mathématiques en Italie*, Vol. III.
2. **Footnote 2 (p. 2)**: **Jean-Étienne Montucla**, *Histoire des mathématiques*.
3. **Footnote 3 (p. 2)**: **Giorgio Vasari**, *Vite de' più eccellenti pittori, scultori, e architettori*.
4. **Footnote 4 (p. 4)**: **Adolf Zeising**, *Neue Lehre von den Proportionen des menschlichen Körpers* (Leipzig, 1854).
5. **Footnote 5 (p. 5)**: Unless a misprint in the 1509 Venice edition (`"in ogibilibus"`) is to be assumed and read as `"in agibilibus"` (compare Compendio Chapter LIV and Architectura Chapter XIX).
6. **Footnote 6 (p. 9)**: **Constantin Winterberg**, *"Das Malerbuch Lionardo da Vinci's"*, in *Jahrbücher der königlich preussischen Kunstsammlungen* (1887).
7. **Footnote 7 (p. 9)**: If by $a, b$ and $a', b'$ we understand not numerical magnitudes, but pairs of linear forces meeting at an angle, and by $c, c'$ their resultants in magnitude and direction, then the composition of the latter two yields a new resultant force $c + c'$, and so forth.
8. **Footnote 8 (p. 11)**: **Niccolò Tartaglia**, *General Trattato di Numeri et Misure* (*General-Trattato di Matematiche*, Venice, 1556–1560).
"""


WINTERBERG_INTRO_DE = """.. rubric:: Reihentitelblatt (*Quellenschriften für Kunstgeschichte*, Wien, 1889)

*Quellenschriften für Kunstgeschichte und Kunsttechnik des Mittelalters und der Neuzeit*, mit Unterstützung des österreichischen k. k. Ministeriums für Cultus und Unterricht im Vereine mit Fachgenossen begründet von **Rudolf Eitelberger von Edelberg**, fortgesetzt von **Albert Ilg**. Neue Folge, II. Band: **Fra Luca Pacioli**, *Divina Proportione: Die Lehre vom Goldenen Schnitt*, nach der Venezianischen Ausgabe vom Jahre 1509 neu herausgegeben, übersetzt und erläutert von **Constantin Winterberg** (Wien: Verlag von **Carl Graeser**, Hofbuchdruckerei **Carl Fromme**, 1889).

----

.. rubric:: Vorwort (Karlsruhe i. B., März 1889)

Die Bestrebungen der Neuzeit gingen, wie bekannt, schon längst darauf aus, den verloren gegangenen technischen Grundlagen, welche insbesondere bei der malerischen Composition der Meisterwerke aus der Zeit der Renaissance stets wiederkehren, auf den Grund zu kommen, um so wiederum auf die Kunst der Gegenwart anregend zu wirken. Durch sorgfältige Veröffentlichung der schriftlichen Ueberlieferungen hervorragender Meister jener Periode der Lösung dieser Aufgabe näher getreten zu sein, ist das grosse Verdienst der *„Quellenschriften für Kunstgeschichte und Kunsttechnik des Mittelalters und der Neuzeit“*.

In der That sind es gerade die technischen Tractate, welchen das unverdiente Schicksal zu Theil ward, entweder unbenutzt und theilweise verschollen in den Bibliotheken Italiens zu vermodern, oder wenn etwa in früheren Jahrhunderten publicirt, dem heutigen Verständniss so fern zu stehen, dass nur Wenige sich mit ihrem Studium befassen. Das gilt insbesondere von den Pacioli'schen Tractaten der *„Divina Proportione“* und dem *„Libellus de quinque corporibus regularibus“*. Als wissenschaftliche Werke unbedeutend, besteht ihr Hauptwerth vielmehr darin, dass sie, im engsten Zusammenhang mit den Bedürfnissen der künstlerischen Praxis entstanden, ein bedeutendes Licht auf die Art der Anwendung mathematischer Disciplinen in den bildenden Künsten insbesondere zur Zeit des ersten Aufschwunges der Frührenaissance werfen. Die vorerwähnten Uebelstände: die schwerfällige veraltete Ausdrucksweise, dazu die oft kaum zu entziffernden Abkürzungen, welche die noch vorhandene aus dem Anfang des 16. Jahrhunderts datirende Ausgabe dieser beiden Werke kennzeichnet, erklären, warum dieselben unter den ausübenden Künstlern bisher so gut wie verschollen geblieben, abgesehen davon, dass das Studium der nur in wenig Exemplaren auf einzelnen Bibliotheken befindlichen Tractate nur schwer zu ermöglichen war.

Diesen Mangel durch die vorliegende neue Ausgabe zum Theil wenigstens zu beseitigen, durch dieselbe einen neuen Beitrag zum Verständniss des künstlerischen Schaffens einer grossen Zeit zu liefern und den Manen des hochverehrten **Hofrath von Eitelberger**, welcher neben seinem Freunde **Heinrich Ludwig** in Rom die erste Anregung dazu gegeben, den Tribut seiner Dankbarkeit weihen zu dürfen, gereicht dem Herausgeber dieses zu besonderer Genugthuung.

*Karlsruhe i. B., März 1889 — Constantin Winterberg*

----

1. Pacioli, Piero della Francesca und Lionardo da Vinci
-------------------------------------------------------

Unter den wenigen Schriften aus der Frührenaissance, welche von technisch-mathematischen Disciplinen handeln, soweit sie mit der künstlerischen Praxis in Beziehung stehen, dürfte keine das Interesse des Historikers wie des Fachmannes so sehr verdienen, als die ihrer Zeit vielgenannten Tractate Pacioli's. Enthält doch selbst das grösste und bedeutendste Werk aus jener Zeit, **Lionardo da Vinci**'s *Malerbuch*, im Wesentlichen Nichts als kurz aneinandergereihte Notizen ohne innern Zusammenhang, über alle möglichen Hilfswissenschaften der Malerei sich erstreckend, woraus die wissenschaftliche Bedeutung des grossen Meisters in keiner Weise genügend hervorgeht. Etwas anderes ist es mit den Schriften Pacioli's, die im Gegensatz dazu trotz aller sonstigen Mängel doch ein fertig durchgearbeitetes Ganze bilden, von um so grösserem Interesse, als sie, wie bekannt, im ersten Anschluss an die künstlerischen Bedürfnisse jener Zeit entstanden, der eine von den fünf regelmässigen Körpern (*Libellus de quinque corporibus regularibus*) sogar seine Autorschaft nicht von Pacioli, sondern von **Piero della Francesca**, also einem wirklichen Künstler, ableitet. Erst beim Lesen dieser Schriften gewinnt man einen vollen Einblick in die grossen Schwierigkeiten, welche sich damals selbst bei einfacheren Problemen der Geometrie den Künstlern darboten, und man kann nicht genug die Einsicht und Energie bewundern, mit welcher die hervorragendsten unter ihnen sich unablässig bemüht, mit den mangelhaften wissenschaftlichen Mitteln, wie sie vom Alterthum her überkommen, die für ihre Zwecke nothwendigen Fragen zu erledigen.

**Fra Luca Pacioli**, dem Franziskanerorden angehörig, ist nach **Libri** (*Histoire des sciences mathématiques en Italie*, III) zu Borgo San Sepolcro geboren, demselben im Toscanischen Apennin gelegenen Flecken, wo auch der vorerwähnte **Piero della Francesca** das Licht der Welt erblickte. Nach **Montucla** (*Histoire des mathématiques*) habe er auf Befehl seiner Vorgesetzten Reisen in den Orient gemacht, wo er vielleicht mit der arabischen Wissenschaft näher vertraut ward. Die Resultate seiner Studien finden sich in seinem Hauptwerke der *„Summa de arithmetica“* (1494) niedergelegt. Das Werk dürfte deswegen auch von praktischem Interesse sein, als sich darin ausser dem algebraischen ein von Geometrie handelnder Abschnitt findet, wo insbesondere von den Proportionen die Rede ist, unter denen speciell den stetigen die grössere Brauchbarkeit zuerkannt und eine Reihe darauf bezüglicher Sätze abgeleitet wird, die in der That weniger aus theoretischer Speculation als aus praktischem Bedürfnisse hervorgegangen scheinen. Da der goldene Schnitt darin als specieller Fall auftritt, so scheint das auf einen gewissen Zusammenhang mit der *„Divina proportione“* hinzudeuten.

Pacioli stand nämlich, wie berichtet wird (**Vasari**, *Vite*), mit den hervorragendsten Künstlern seiner Zeit in wissenschaftlichem Verkehr. Von **Piero della Francesca**, seinem älteren Landsmanne, heisst es insbesondere, dass dieser ihn in den mathematischen Disciplinen unterrichtet habe, und selbst der gefeierte **Lionardo da Vinci** verschmähte es nicht, zur *Divina proportione* die Figuren zu entwerfen. Es sind dieselben Zeichnungen der fünf regelmässigen und aus diesen durch Abschneiden der Ecken oder pyramidale Erhöhung der Flächen abgeleiteten Körper, die sich bei späteren Autoren von Tractaten über Perspective wiederholen. Vielfach spricht ausserdem Pacioli selbst von seinen freundschaftlichen Beziehungen zu beiden Meistern. Piero insbesondere bezeichnet er in der Einleitung des dem Herzog **Guidobaldo** von Urbino gewidmeten Hauptwerkes als *„il monarca alli tempi nostri della pictura“*, während im Tractate vom goldenen Schnitt die freundschaftlichen Beziehungen zu Lionardo mehrfach betont und dessen *Cenacolo*, wie auch die leider nur im Modell vollendete Reiterstatue des Herzogs **Francesco Sforza** von Mailand unter den Meisterwerken jener Zeit genannt werden. Aus diesem lebendigen Verkehr von Theorie und Praxis, von Wissenschaft und Kunst gingen wesentlich wohl jene beiden Tractate hervor, deren erster, *De divina proportione*, dem Herzog **Ludovico Sforza**, genannt *il Moro*, gewidmet ist.

2. Der Goldene Schnitt, Vitruv's Harmonische Verhältnisse und Aesthetischer Rhythmus
------------------------------------------------------------------------------------

Der kurze Tractat über Architektur (*Tractato de l'Architectura*) steht sachlich ziemlich ausser Zusammenhang mit dem ersten Theil, es sei denn, dass man einen solchen annimmt, wie **Libri** (*Histoire des sciences mathématiques en Italie*, III) darin zu erkennen glaubt. Derselbe sagt nämlich, indem er von der *Divina proportione* spricht, Pacioli habe darin nachweisen wollen, wie jene Proportion, welche man auch als goldenen Schnitt benennt, in den Gliederungen aller wohlgebildeten menschlichen Gestalten ebenso wie in den Gebilden der Kunst, der Architektur insbesondere sich finde, und überall da wiederkehren müsse, wo etwas Schönes entstehen solle, so dass sogar die Buchstaben des Alphabets dieser Regel entsprechend zu construiren seien. Nun ist aber das, was Pacioli in jenem Tractat über Architektur von der menschlichen Gestalt sagt, im Wesentlichsten nichts als eine Wiederholung der Angaben **Vitruv**'s (*De Architectura*), und das Gleiche lässt sich auch hinsichtlich der Säulenordnungen behaupten, umsomehr als der Autor selber keinen Hehl daraus macht. Bei **Vitruv** aber, und ebenso bei allen Architekten der Renaissance, die wie **Alberti** und **Serlio** von ihm geschöpft, spielt nicht der goldene Schnitt, sondern vielmehr das auf Grund der musikalischen Accorde abgeleitete harmonische Zahlenverhältniss die Hauptrolle. Was endlich das Alphabet betrifft, so ist dasselbe nebst den vom Autor gegebenen constructiven Bestimmungen am Ende des Tractates hinzugefügt, wonach sich Jeder selber überzeugen kann, inwieweit nach dieser Seite die Ansicht **Libri**'s motivirt erscheint.

Gleichwohl steht fest und geht aus den im Tractat selber gelegentlich verstreuten Bemerkungen hervor, dass Pacioli, wenn er auch den goldenen Schnitt nicht als Basis eines allgemein giltigen Natur- und Kunstprincipes auffasst, doch dessen Bedeutung beiweitem überschätzt: nach seinen Ergebnissen zeigen sich nicht nur die fünf regulären, sondern überhaupt alle möglichen durch Abschneiden der Ecken und so fort daraus erhaltenen Modificationen dem goldenen Schnitt direct oder indirect bezüglich ihrer Formverhältnisse unterworfen. Ja er denkt sich seine Theorie des Ueberganges von den einfacheren zu den complicirteren, d. h. von einer grösseren und grösseren Flächenzahl umgrenzten Körpern, die sich durch Eckenabschneiden aus jenen ergeben, gleichsam als Ersatzmittel für die Differentialrechnung, um auf diese Art zu allen möglichen krummflächig begrenzten Körpern zu gelangen (*in agibilibus*, im Druck von 1509 *„in ogibilibus“*). Ausserdem versäumt er keine Gelegenheit, Architekten und Bildhauern die praktische Anwendung der regulären Körper zu empfehlen, so dass selbst **Phidias**, der grösste Meister der Antike, dieselben anzuwenden nicht unterlassen habe.

Wie denn **Euklid** im Wesentlichen bereits alles das bekannt war, was Pacioli über die *Divina proportione* beibringt, lassen sich alle darin enthaltenen Sätze als nothwendige Folgerungen aus der Definition selbst ableiten. Erst in der Mitte dieses Jahrhunderts ward durch **Adolf Zeising** (*Neue Lehre von den Proportionen des menschlichen Körpers*, 1854) der Gegenstand von neuem aufgenommen und der goldene Schnitt nicht nur als morphologisches Princip der Naturgebilde, sondern auch als ästhetisches Grundprincip alles Kunstschaffens aufgefasst, um einen sogenannten *Kanon* der menschlichen Gestalt zu construiren. In der That haben die Messungen **Zeising**'s und die darnach vorgenommenen Constructionen normaler menschlicher Figuren (cfr. unter Anderen **Brocheneck**, *Die männliche und weibliche Normalgestalt*) ergeben, dass die Verhältnisse des goldenen Schnittes den wirklichen Naturformen ebensowohl wie den besten Bildungen der antiken Kunst sich mit relativ unbedeutenden Abweichungen anschliessen. Aber mit Recht bemerkt **Emil Harless** (*Lehrbuch der plastischen Anatomie*), dass auch jede beliebige andere stetige Proportion durch fortgesetzte lineare Theilung zu demselben Resultate bezüglich empirischer Mittelwerthe führen müsse, ohne dass der einen vor der anderen darum der Vorzug gebührt, ob wir mit **Carl Gustav Carus** (*Die Proportionslehre der menschlichen Gestalt*) von der Wirbelsäule aus die natürliche Gliederung der Form suchen, oder wie **Carl Schmidt** (*Proportionsschlüssel*) eine an sich ganz willkürliche geometrische Construction zu Grunde legen, oder wie **Adolphe Quetelet** (*Anthropométrie*) und nach ihm **J. J. Trost** (*Die Proportionslehre Dürer's*) nach dem Princip der Wahrscheinlichkeitsrechnung rein empirisch verfahren.

Anders verhält es sich aber mit der **ästhetischen Wirkung**, welche nach diesem Princip gegliederte Formen dem Beschauer erzeugen:

1. Soll das Auge bei der Betrachtung eines Gegenstandes die Empfindung von gesetzmässiger Gliederung seiner Theile empfangen, so ist in erster Linie erforderlich, dass das fragliche Gesetz möglichst einfach sei, um sich auf den ersten Blick als einen bestimmten **Rhythmus** zum Bewusstsein zu bringen.
2. Von Proportionen im allgemeinsten Sinne sind zweierlei: **arithmetische** und **geometrische** zu unterscheiden. Die einfachste Form für Reihen der ersten Art ist die, wo nur zwei Anfangsglieder $a$ und $b$ anzunehmen sind, aus denen die folgenden durch die Relationen $c = a + b$, $d = b + c$, $e = c + d$ u. s. f. abgeleitet werden. Jeder solchen Reihe liegt, wie schon in **Constantin Winterberg**'s Abhandlung *„Das Malerbuch Lionardo da Vinci's“* (*Jahrbücher der königlich preussischen Kunstsammlungen*, 1887) hervorgehoben, ein organisches Princip zu Grunde, welches sagt, dass aus zwei schwächeren ein stärkeres, oder umgekehrt aus diesem zwei schwächere hervorgehen, wie beim Baumwuchs oder bei der Zusammensetzung zweier sich unter einem Winkel begegnenden linearen Kräfte zu einer neuen Mittelkraft.
3. Dagegen würde das Auge die Gleichheit zweier unzusammenhängender geometrischer Verhältnisse $\\frac{a}{b}$ und $\\frac{c}{d}$ zwischen vier auf derselben Linie aneinanderstossenden Stücken $a, b, c, d$ nicht ohne weiteres übersehen. Erst wenn diese Lücke durch die Bestimmung ausgefüllt wird, dass das Verhältniss von $\\frac{b}{a}$ gleich dem Nachbarverhältniss $\\frac{c}{b}$ sein soll, wie bei **stetigen Proportionen**, ist ein fortlaufender Vergleich und somit eine Erkenntniss des Rhythmus möglich.
4. Tritt ferner zu dieser einfachsten dem Auge stets kenntlichen geometrischen Proportion $\\frac{b}{a} = \\frac{c}{b}$ die Bedingung, dass zwischen den drei Grössen $a, b, c$ auch das arithmetische Verhältniss $a + b = c$ stattfinden soll, so ergibt sich dadurch das, was als **goldener Schnitt** bezeichnet wird, während zugleich die doppelte Beziehung, welche unter je dreien seiner Glieder stattfindet, dem Auge unmittelbar und ohne weitere Hilfsmittel klar wird.

3. Mathematische Gliederung des Tractats und Kritik der Gegenseitigen Einbeschreibungen
---------------------------------------------------------------------------------------

Dem Inhalte nach zerfällt der Tractat in vier Gruppen:

1. **Elementare Sätze über den goldenen Schnitt (Cap. I–XXIII)**: Eine Reihe elementarer Sätze über den goldenen Schnitt, wobei hinsichtlich der Beweise auf die betreffenden Stellen **Euklid**'s verwiesen wird; die meisten dieser Sätze sind im Anhang (**Anmerkungen 1–9**) kurz mathematisch erläutert.
2. **Geometrische Construction der fünf regulären Körper (Cap. XXIV–XXXIV)**: Beschäftigt sich neben dem Lehrsatze des **Pythagoras** und den Sehnen- und Tangentensätzen des Kreises bei **Euklid** mit der geometrischen Construction der fünf regulären Körper in der Kugel und dem Nachweis, dass im Gegensatze zur unendlichen Zahl regulärer Polygone nur fünf entsprechende Körperformen existiren (**Anmerkungen 10–14**).
3. **Gegenseitige Einbeschreibungen und abhängige Körper (Cap. XXXV–LV)**: Es werden die zwölf Probleme gegenseitiger Ein- oder Umschreibungen besagter Körper aus dem fünfzehnten Buche **Euklid**'s und seines Vorgängers **Campanus** discutirt, wobei Pacioli den schon von **Niccolò Tartaglia** (*General-Trattato di Matematiche*) gerügten Fehler begeht, eine Anzahl von Fällen mit Stillschweigen zu übergehen, ja in einem Falle—der Einschreibung des Oktaeders ins Ikosaeder (Cap. XLVI)—unter Beibringung mysteriöser Gründe der Lehre **Platon**'s von den vier Elementen und der fünften Himmelskraft den Nachweis versucht, dass dieser Fall unmöglich sei (**Anmerkung 15**). Doch schon **Tartaglia** bewies die Haltlosigkeit dieser Ansicht mit weit klareren und kürzeren Beweismethoden und fügte zwei neue Fälle—die Einschreibung des Ikosaeders in den Kubus (die auch im *Libellus* des **Piero della Francesca** vorkommt) und den von Pacioli geleugneten Fall—hinzu. Es schien darum im Interesse der Sache nothwendig, die Gesammtheit aller **21 möglichen Fälle** gegenseitiger Einbeschreibungen auf Grund der Theorie von **Pol und Polare** im Anhang (**Anmerkung 17**) kurz zu erledigen. Als Schluss dieses Theiles behandelt der Inhalt die „abhängigen“ abgeschnittenen und erhöhten Körper (**Anmerkung 16**).
4. **Kugel, Prismen, Pyramiden und Inhaltsbestimmungen (Cap. LVI–LXXI)**: Die letzte Gruppe gibt die Deduction der Inhaltsbestimmungen von Prismen, Cylindern, ganzen und abgestumpften Pyramiden und Kegeln sowie den Nachweis, warum die Pyramide genau den dritten Theil des Volumens vom Prisma gleicher Grundfläche und Höhe ergeben müsse, als Vorbereitung für die im folgenden Tractat, dem *Libellus*, enthaltenen Probleme.

Schon die Zeitgenossen—insbesondere **Annibale Caro** (*Apologia*)—bezeichneten Pacioli's weitschweifige, halb latinisirte Schreibweise in wenig schmeichelhafter Art als *„Ceneraccio“* (Aschenlauge, Schmutzbrühe); doch erklärt sich die Einschaltung unterhaltender Episoden daraus, dass sich der dem Herzog **Ludovico Sforza** von Mailand gewidmete Tractat formell als ein vor Fürsten, hohen Herren, Künstlern und Technikern gehaltener mündlicher Vortrag darstellt.

4. Textgrundlage (Venezianische Ausgabe 1509 & Vatikanisches Manuscript)
------------------------------------------------------------------------

Die Neuausgabe der *Divina proportione* stellte sich zunächst den Zweck, den alterthümlichen, durch Abkürzungen aller Art fast ungeniessbar gewordenen Text der früheren Ausgabe (**Paganino de' Paganini**, Venedig 1509) wieder lesbar zu machen, zugleich die sachlichen Mängel und Ungenauigkeiten zu berichtigen, und durch die Zeichnungen **Lionardo da Vinci**'s sowie die Hilfsmittel der neueren Geometrie anregend auf den heutigen Künstler, Techniker, Ingenieur und Architekten zu wirken. Das der Bearbeitung zu Grunde gelegte Exemplar der Ausgabe von 1509 gehört der Bibliothek des **k. k. Oesterreichischen Museums für Kunst und Industrie** in Wien an, von welcher es vom verstorbenen Director **Hofrath v. Eitelberger** gütigst zur Verfügung gestellt worden. Daneben wurde gelegentlich bei zweifelhaften Stellen das Manuscript der **Vaticana** (*Cod. Vat. Lat. 3129*) zu Rathe gezogen.

.. rubric:: Fussnoten zur Einleitung (Winterberg 1889, S. 1–15)

1. **Fussnote 1 (S. 2)**: **Guillaume Libri**, *Histoire des sciences mathématiques en Italie*, III.
2. **Fussnote 2 (S. 2)**: **Jean-Étienne Montucla**, *Histoire des mathématiques*.
3. **Fussnote 3 (S. 2)**: **Giorgio Vasari**, *Vite*.
4. **Fussnote 4 (S. 4)**: **Adolf Zeising**, *Neue Lehre von den Proportionen des menschlichen Körpers* etc. (Leipzig, 1854).
5. **Fussnote 5 (S. 5)**: Wenn nicht etwa ein Druckfehler (*„in ogibilibus“*) anzunehmen und zu lesen *„in agibilibus“* (vgl. die betreffende Stelle des Textes, Cap. LIV und Arch. Cap. XIX).
6. **Fussnote 6 (S. 9)**: **Constantin Winterberg**, *„Das Malerbuch Lionardo da Vinci's“* in *Jahrbücher der königlich preussischen Kunstsammlungen*, 1887.
7. **Fussnote 7 (S. 9)**: Versteht man unter $a, b$, $a', b'$ nicht Zahlengrössen, sondern je zwei sich unter einem Winkel begegnende lineare Kräfte, unter $c, c'$ deren Resultanten nach Grösse und Richtung, so ergibt die Zusammensetzung der zwei letzteren eine neue Mittelkraft, u. s. f.
8. **Fussnote 8 (S. 11)**: **Niccolò Tartaglia**, *General-Trattato di Matematiche* (*General Trattato di Numeri et Misure*).
"""


WINTERBERG_ANMERKUNGEN: List[Dict[str, Any]] = [
    {
        "num": 1,
        "chapters": [("compendio", 7)],
        "locus": "Cap. VII, p. 198, l. 4 from bottom",
        "title_en": "Note 1 (Cap. VII): Equivalence of Pacioli's Initial Characterization with Euclid's Definition of Extreme and Mean Ratio",
        "title_de": "Anmerkung 1 (Cap. VII, S. 198): Identität der zu Anfang gegebenen Definition der stetigen Theilung mit der Euklidischen Definition",
        "text_en": """Since the definition of continuous division (extreme and mean ratio) according to Euclid (:just:`VI.def.3`, :just:`II.11`) is stated at the close of Chapter VII—namely, when a given line $ac$ is divided at $b$ into two segments such that the square on the greater segment $ab^2$ equals the rectangle $ac \\cdot bc$ contained by the whole line and the lesser segment—we demonstrate its identity with the numerical property stated at the beginning of Chapter VII (:just:`XIII.1`):

- **Hypothesis**: Let the line $ac$ be divided in extreme and mean ratio at $b$, so that $ab^2 = ac \\cdot bc$.
- **Claim**: $\\left(ac + \\frac{bc}{2}\\right)^2 = 5\\left(\\frac{bc}{2}\\right)^2$, or equivalently $\\left(ab + \\frac{ac}{2}\\right)^2 = 5\\left(\\frac{ac}{2}\\right)^2$.
- **Proof**: By hypothesis, $ab^2 = ac(ac - ab)$, whence

  .. math::

     ac^2 = ab^2 + ab \\cdot ac \\quad \\text{and} \\quad ab^2 + ab \\cdot ac = ac^2.

  Adding $\\left(\\frac{ac}{2}\\right)^2$ to both sides yields

  .. math::

     \\left(ab + \\frac{ac}{2}\\right)^2 = ab^2 + ab \\cdot ac + \\left(\\frac{ac}{2}\\right)^2 = ac^2 + \\frac{ac^2}{4} = 5\\left(\\frac{ac}{2}\\right)^2. \\quad \\text{Q.E.D.}""",
        "text_de": """Da die Definition der stetigen Theilung nach Euklid gewöhnlich so angegeben wird, wie am Schluss des Capitels gesagt, d. h. wenn die gegebene Linie $ac$ im Punkte $b$ in zwei Abschnitte zerfällt, wovon das Quadrat des grössern $ab^2$ gleich dem Product $ac \\cdot bc$ aus der ganzen Länge mal dem kleinern Abschnitte ist, so sei zum Nachweise der Identität der letztern mit der zu Anfang dieses Capitels gegebenen Eigenschaft Folgendes bemerkt:

- **Voraussetzung**: Es sei nach der bekannten Euklidischen Definition die Linie $ac$ im Punkte $b$ stetig getheilt, so dass $ab^2 = ac \\cdot bc$.
- **Behauptung**: $\\left(ab + \\frac{ac}{2}\\right)^2 = 5\\left(\\frac{ac}{2}\\right)^2$.
- **Beweis**: Nach Voraussetzung ist $ab^2 = ac(ac - ab)$ oder $ac^2 = ab^2 + ab \\cdot ac$. Fügt man rechts und links $\\left(\\frac{ac}{2}\\right)^2$ hinzu, so folgt unmittelbar:

  .. math::

     \\left(ab + \\frac{ac}{2}\\right)^2 = 5\\left(\\frac{ac}{2}\\right)^2. \\quad \\text{w. z. b. w.}""",
    },
    {
        "num": 2,
        "chapters": [("compendio", 7)],
        "locus": "Cap. VII, p. 198, l. 14 from bottom",
        "title_en": "Note 2 (Cap. VII): Bisection of the Whole Line and Continuous Division of the Half",
        "title_de": "Anmerkung 2 (Cap. VII, S. 198): Halbirung der Linie und stetige Theilung der Hälfte",
        "text_en": """This corollary (:just:`XIII.1` / :just:`XIII.2`) follows immediately if we bisect the line $ab$ at $c$ ($ac = bc = \\frac{1}{2}ab$) and divide $bc$ in extreme and mean ratio at $d$; considering the three parts of the line $ab$, the greater segment of the half-line together with the other half satisfies the fivefold square relation $ad^2 = 5\\,ac^2$.""",
        "text_de": """Diese Folgerung ergibt sich, indem man sich die Linie $ab$ in $c$ halbirt, und sodann $bc$ im Punkte $d$ auf die gewöhnliche Art stetig getheilt denkt. Betrachtet man dann die drei Theile, aus denen die Linie $ab$ besteht, so ist der zusammengesetzte Abschnitt $ad = ac + cd$.""",
    },
    {
        "num": 3,
        "chapters": [("compendio", 12)],
        "locus": "Cap. XII, p. 203, l. 3 from top",
        "title_en": "Note 3 (Cap. XII): Algebraic Proof of the Third Effect (Euclid XIII.3)",
        "title_de": "Anmerkung 3 (Cap. XII, S. 203): Mathematischer Nachweis des dritten Effects (Euklid XIII.3)",
        "text_en": """Expressed algebraically for the line $ac$ divided in extreme and mean ratio at $b$ ($ab > bc$):

- **Hypothesis**: $ab^2 = ac \\cdot bc = (ab + bc)\\,bc$.
- **Claim**: $\\left(bc + \\frac{ab}{2}\\right)^2 = 5\\left(\\frac{ab}{2}\\right)^2$.
- **Proof**: Since $ab^2 = bc^2 + ab \\cdot bc$ by hypothesis, adding $\\left(\\frac{ab}{2}\\right)^2$ to both sides yields

  .. math::

     \\left(bc + \\frac{ab}{2}\\right)^2 = bc^2 + ab \\cdot bc + \\left(\\frac{ab}{2}\\right)^2 = ab^2 + \\frac{ab^2}{4} = 5\\left(\\frac{ab}{2}\\right)^2.

  Substituting the numerical values of Chapter XII ($ac = 10$, $ab = \\sqrt{125} - 5$, $bc = 15 - \\sqrt{125}$) confirms the identity of both sides immediately.""",
        "text_de": """Mathematisch ausgedrückt heisst dies mit Bezug auf die in $b$ stetig getheilte Linie $ac$:

- **Voraussetzung**: $ab^2 = ac \\cdot bc$.
- **Behauptung**: $\\left(bc + \\frac{ab}{2}\\right)^2 = 5\\left(\\frac{ab}{2}\\right)^2$.
- **Beweis**: $ab^2 = bc^2 + ab \\cdot bc$ (nach Voraussetzung), daher analog wie in Anmerkung 1 durch Hinzufügung von $\\left(\\frac{ab}{2}\\right)^2$ rechts und links:

  .. math::

     \\left(bc + \\frac{ab}{2}\\right)^2 = 5\\left(\\frac{ab}{2}\\right)^2.

  Setzt man die Werthe des in Cap. XII behandelten Beispiels ein ($ab = \\sqrt{125} - 5$, $bc = 15 - \\sqrt{125}$), so ergibt sich die Richtigkeit durch Uebereinstimmung der beiden Seiten der Gleichung ohne weiteres.""",
    },
    {
        "num": 4,
        "chapters": [("compendio", 13)],
        "locus": "Cap. XIII, p. 203, l. 7 from bottom",
        "title_en": "Note 4 (Cap. XIII): Algebraic Proof of the Fourth Effect (Euclid XIII.5)",
        "title_de": "Anmerkung 4 (Cap. XIII, S. 203): Mathematischer Nachweis des vierten Effects (Euklid XIII.5)",
        "text_en": """In algebraic form, let the segment $bc$ be divided in extreme and mean ratio at $d$ ($cd > bd$), and let $ac = cd$ be adjoined to form the whole line $ad = ac + bc$:

- **Hypothesis**: $cd^2 = bc \\cdot bd$ and $ac = cd$.
- **Claim**: $bc^2 = ad \\cdot cd = ad \\cdot ac$.
- **Proof**: By hypothesis, $cd^2 = bc(bc - cd) = bc^2 - bc \\cdot cd$, whence

  .. math::

     bc^2 = cd^2 + bc \\cdot cd = cd(cd + bc) = cd(ac + bc) = ad \\cdot cd. \\quad \\text{Q.E.D.}""",
        "text_de": """In mathematischer Form (wenn $bc$ in $d$ stetig getheilt und $ac = cd$ angesetzt wird):

- **Voraussetzung**: $cd^2 = bc \\cdot bd$ und $ac = cd$.
- **Behauptung**: $bc^2 = ad \\cdot cd$.
- **Beweis**: Nach Voraussetzung ist $cd^2 = bc(bc - cd)$, folglich:

  .. math::

     ad \\cdot cd = (ac + bc)\\,cd = cd^2 + bc \\cdot cd = bc^2. \\quad \\text{w. z. b. w.}""",
    },
    {
        "num": 5,
        "chapters": [("compendio", 14)],
        "locus": "Cap. XIV, p. 204, l. 14 from top",
        "title_en": "Note 5 (Cap. XIV): Algebraic Proof of the Fifth Effect (Euclid XIII.4)",
        "title_de": "Anmerkung 5 (Cap. XIV, S. 204): Mathematischer Nachweis des fünften Effects (Euklid XIII.4)",
        "text_en": """In general algebraic form, for the line $bc$ divided in extreme and mean ratio at $d$ ($cd > bd$):

- **Hypothesis**: $cd^2 = bc \\cdot bd$.
- **Claim**: $bd^2 + bc^2 = 3\\,cd^2$.
- **Proof**:
  a) From Note 4, $bc^2 = bc \\cdot cd + cd^2$.
  b) Expanding $bd^2 = (bc - cd)^2 = bc^2 - 2\\,bc \\cdot cd + cd^2$.
  Adding (a) and (b) together and substituting $bc^2 - bc \\cdot cd = bc(bc - cd) = bc \\cdot bd = cd^2$ gives:

  .. math::

     bd^2 + bc^2 = 2\\,cd^2 + bc(bc - cd) = 2\\,cd^2 + bc \\cdot bd = 3\\,cd^2. \\quad \\text{Q.E.D.}""",
        "text_de": """In allgemeiner Form unter der früheren Voraussetzung ($cd^2 = bc \\cdot bd$):

- **Behauptung**: $bd^2 + bc^2 = 3\\,cd^2$.
- **Beweis**:
  a) $bc^2 = bc \\cdot cd + cd^2$ (nach Anm. 4).
  b) $bd^2 = (bc - cd)^2 = bc^2 - 2\\,bc \\cdot cd + cd^2$.
  Durch Addition von a) und b) erhält man:

  .. math::

     bd^2 + bc^2 = 2\\,cd^2 + bc(bc - cd) = 2\\,cd^2 + bc \\cdot bd = 3\\,cd^2. \\quad \\text{w. z. b. w.}""",
    },
    {
        "num": 6,
        "chapters": [("compendio", 16)],
        "locus": "Cap. XVI, p. 205, l. 11 from bottom",
        "title_en": "Note 6 (Cap. XVI): Seventh Effect — Hexagon Side (Radius) and Decagon Side (Euclid XIII.9)",
        "title_de": "Anmerkung 6 (Cap. XVI, S. 205): Siebenter Effect — Sechsecksseite und Zehnecksseite (Euklid XIII.9)",
        "text_en": """This follows immediately from Note 4 (:just:`XIII.5`), once one observes that the side of the regular decagon inscribed in a circle is the greater segment of the radius (the hexagon side) divided in extreme and mean ratio.""",
        "text_de": """Dies folgt unmittelbar aus Anmerkung 4, wenn man berücksichtigt, dass die Zehnecksseite der grössere Abschnitt des stetig getheilten Radius (der Sechsecksseite) ist.""",
    },
    {
        "num": 7,
        "chapters": [("compendio", 18)],
        "locus": "Cap. XVIII, p. 206, l. 11 from bottom",
        "title_en": "Note 7 (Cap. XVIII): Ninth Effect — Diagonals of the Regular Pentagon (Euclid XIII.8)",
        "title_de": "Anmerkung 7 (Cap. XVIII, S. 206): Neunter Effect — Diagonalen des regulären Fünfecks (Euklid XIII.8)",
        "text_en": """The proof follows immediately from the similarity of the isosceles triangles $\\triangle bca \\sim \\triangle baf$ formed by the two intersecting chords $ac$ and $be$ (meeting at $f$) of the regular pentagon:

.. math::

   \\frac{ca}{ba} = \\frac{ba}{af} \\implies ba^2 = ca \\cdot af,

and since $ba = bc = cf$, we have $cf^2 = ca \\cdot af$, so the chord $ca$ is cut in extreme and mean ratio at $f$.""",
        "text_de": """Der Beweis folgt aus der Aehnlichkeit der gleichschenkligen Dreiecke $\\triangle bca$ und $\\triangle baf$, wonach sich unmittelbar ergibt:

.. math::

   \\frac{ca}{ba} = \\frac{ba}{af}, \\quad \\text{d. h.} \\quad ba^2 = ca \\cdot af,

oder, da $ba = bc = cf$ ist: $cf^2 = ca \\cdot af$.""",
    },
    {
        "num": 8,
        "chapters": [("compendio", 21)],
        "locus": "Cap. XXI, p. 209, l. 13 from bottom",
        "title_en": "Note 8 (Cap. XXI): Twelfth Effect — Ratio of the Cube Edge to the Icosahedron Edge in the Same Sphere",
        "title_de": "Anmerkung 8 (Cap. XXI, S. 209): Zwölfter Effect — Verhältniss der Seite des Kubus zur Seite des Ikosaeders",
        "text_en": """Denoting by $s$ and $s'$ the edges of the cube and regular icosahedron inscribed in the same sphere, and letting the segment $ab$ be divided in extreme and mean ratio at $c$ ($ac > bc$), Pacioli's claim (following Campanus XIV.9) is:

.. math::

   \\sqrt{\\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \\frac{s'}{s} \\quad \\left(\\text{or reciprocally } \\sqrt{\\frac{ab^2 + bc^2}{ab^2 + ac^2}} = \\frac{s}{s'}\\right).

**Proof**: Using the extreme and mean ratio relations (a) $ac^2 = ab \\cdot bc$ and (b) $bc^2 = (ab - ac)^2 = ab^2 - 2\\,ab \\cdot ac + ac^2$, we have $ab^2 + bc^2 = 3\\,ac^2 = 3\\,ab \\cdot bc$ (by Note 5) and $ab^2 + ac^2 = ab^2 + ab \\cdot bc = ab(ab + bc)$. Hence the quotient under the radical simplifies to:

.. math::

   \\frac{ab^2 + ac^2}{ab^2 + bc^2} = \\frac{ab(ab + bc)}{3\\,ab \\cdot bc} = \\frac{ab + bc}{3\\,bc}.

Solving $ac^2 = ab \\cdot bc = ab(ab - ac)$ gives $bc = \\frac{3 - \\sqrt{5}}{2}\\,ab$, and substituting this into the quotient yields:

.. math::

   \\sqrt{\\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \\sqrt{\\frac{ab + bc}{3\\,bc}} = \\sqrt{\\frac{5 + \\sqrt{5}}{6}} \\quad \\left(\\text{and its reciprocal } \\sqrt{\\frac{3\\,bc}{ab + bc}} = \\sqrt{\\frac{5 - \\sqrt{5}}{6}}\\right).

The exact same value is obtained when we express $s$ and $s'$ in terms of the circumradius $r$ of the common sphere (:just:`XIII.15`, :just:`XIII.16`, :just:`XIII.18`):

.. math::

   s = \\frac{2r}{\\sqrt{3}}, \\qquad s' = \\frac{4r}{\\sqrt{10 + 2\\sqrt{5}}} = r\\sqrt{\\frac{10 - 2\\sqrt{5}}{5}}, \\qquad \\frac{s}{s'} = \\sqrt{\\frac{5 + \\sqrt{5}}{6}}. \\quad \\text{Q.E.D.}""",
        "text_de": """Bezeichnet man mit $s, s'$ resp. die Seiten des Kubus und des regulären Ikosaeders, so wird, wenn die Linie $ab$ in $c$ stetig getheilt ist ($ac > bc$), behauptet:

.. math::

   \\sqrt{\\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \\frac{s}{s'}.

**Beweis**: Der Ausdruck unter dem Wurzelzeichen links lässt sich vereinfachen, indem zufolge Voraussetzung:
a) $ac^2 = ab \\cdot bc$,
b) $bc^2 = (ab - ac)^2$.
Durch Einsetzen dieser Ausdrücke und Ausführung der Quadratur des letzteren erhält man:

.. math::

   \\frac{ab^2 + ac^2}{ab^2 + bc^2} = \\frac{ab(ab + bc)}{3\\,ab \\cdot bc} = \\frac{ab + bc}{3\\,bc}.

Aus der Gleichung a), nachdem darin $ac = ab - bc$ gesetzt, erhält man $bc^2 - 3\\,ab \\cdot bc + ab^2 = 0$, und durch Einsetzen in den vorstehenden Quotienten:

.. math::

   \\sqrt{\\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \\sqrt{\\frac{ab + bc}{3\\,bc}} = \\sqrt{\\frac{5 + \\sqrt{5}}{6}}.

Derselbe Werth ergibt sich aber auch, wenn man das Verhältniss $\\frac{s}{s'}$ durch den Radius $r$ der umschriebenen Kugel ausgedrückt berechnet, indem bekanntlich ist:

.. math::

   s = \\frac{2r}{\\sqrt{3}}, \\qquad s' = \\frac{4r}{\\sqrt{10 + 2\\sqrt{5}}}, \\qquad \\text{somit} \\quad \\frac{s}{s'} = \\sqrt{\\frac{5 + \\sqrt{5}}{6}}.""",
    },
    {
        "num": 9,
        "chapters": [("compendio", 22)],
        "locus": "Cap. XXII, p. 211, l. 7 from top",
        "title_en": "Note 9 (Cap. XXII): Cross-Reference to the *Libellus de Quinque Corporibus Regularibus*",
        "title_de": "Anmerkung 9 (Cap. XXII, S. 211): Verweis auf den Tractat über die fünf regelmässigen Körper",
        "text_en": """Compare on this pentagon construction the *Tractatus de Quinque Corporibus Regularibus* (*Libellus*, Tractate II, Case 20 ff.).""",
        "text_de": """Vgl. hierüber den Tractat über die fünf regelmässigen Körper (*Libellus*, Tract. II, Cas. 20 u. s. w.).""",
    },
    {
        "num": 10,
        "chapters": [("compendio", 26)],
        "locus": "Cap. XXVI, p. 216, l. 12 from top",
        "title_en": "Note 10 (Cap. XXVI): Division of the Sphere Diameter by the Base of the Inscribed Tetrahedron (Euclid XIII.13)",
        "title_de": "Anmerkung 10 (Cap. XXVI, S. 216): Theilung des Kugeldurchmessers beim regulären Tetraeder (Euklid XIII.13)",
        "text_en": """In every regular tetrahedron, the four altitudes intersect at the center of the circumscribed sphere (of radius $r$) in the ratio $1 : 3$. Denoting the smaller segment (from the sphere center to the base plane) by $x = \\frac{r}{3}$, and extending the altitude $ac = r + x$ beyond the base plane to meet the sphere at $b$ (so that $ab = 2r$ is the sphere diameter and $bc = r - x$), the ratio of the extension $bc$ to the tetrahedron altitude $ac$ is:

.. math::

   \\frac{bc}{ac} = \\frac{r - x}{r + x} = \\frac{r - \\frac{r}{3}}{r + \\frac{r}{3}} = \\frac{\\frac{2}{3}r}{\\frac{4}{3}r} = \\frac{1}{2}, \\qquad \\text{whence } ab : ac = 3 : 2 \\text{ and } ac : bc = 2 : 1.""",
        "text_de": """Bekanntlich verhalten sich in jedem regulären Tetraeder die Abschnitte der Höhen, welche sich im Centrum der umschriebenen Kugel vom Radius $r$ schneiden, zu einander wie $1 : 3$. Bezeichnet man nun den kleinern Abschnitt mit $x$ und denkt sich ferner eine der Höhen über die Grundfläche hinaus bis zum Durchschnitt mit der Kugel verlängert, so ergibt sich das Verhältniss dieser Verlängerung $bc$ zu der Höhe $ac$ des Tetraeders:

.. math::

   \\frac{bc}{ac} = \\frac{r - x}{r + x}, \\qquad \\text{folglich, da } x = \\frac{r}{3} \\text{ ist:} \\quad \\frac{bc}{ac} = \\frac{1}{2}.

Alles Uebrige ergibt sodann der Text von selber.""",
    },
    {
        "num": 11,
        "chapters": [("compendio", 27)],
        "locus": "Cap. XXVII, p. 217, l. 17 from top",
        "title_en": "Note 11 (Cap. XXVII): Division of the Sphere Diameter by the Inscribed Cube (Euclid XIII.15)",
        "title_de": "Anmerkung 11 (Cap. XXVII, S. 217): Theilung des Kugeldurchmessers beim Kubus (Euklid XIII.15)",
        "text_en": """The square of the diagonal of a square is double the square of its side ($ad^2 = 2\\,bd^2$). Passing a plane through one of the three main space diagonals $ab$ of the cube and an edge $bd$, this plane intersects the circumscribed sphere in a great circle whose diameter is $ab$, while the two chords drawn from its endpoints to $d$ are the cube edge $bd$ and the face diagonal $ad$. By the right-triangle projection theorem (:just:`VI.8`):

.. math::

   bd^2 = bc \\cdot ab \\quad \\text{and} \\quad ad^2 = ac \\cdot ab.

Since $ad^2 = 2\\,bd^2$, dividing the two equations gives:

.. math::

   \\frac{bc}{ac} = \\frac{bd^2}{ad^2} = \\frac{1}{2}, \\qquad \\text{and } ab^2 = 3\\,bd^2. \\quad \\text{Q.E.D.}""",
        "text_de": """Bekanntlich ist das Quadrat der Diagonale eines Quadrats doppelt so gross als das Quadrat der Seite. Denkt man sich nun durch eine der drei Hauptaxen $ab$ des Kubus und eine Kante $bd$ eine Ebene gelegt, so schneidet sie die umschriebene Kugel in einem Kreise, dessen Durchmesser jene Axe $ab$ ist, während die zwei von ihren Endpunkten ausgehenden Sehnen die Seite $bd$ und Flächendiagonale $ad$ des Quadrats sind. Daher hat man nach bekannten Sätzen:

.. math::

   bd^2 = bc \\cdot ab \\quad \\text{und} \\quad ad^2 = ac \\cdot ab.

Somit, da $ad^2 = 2\\,bd^2$ ist, erhält man durch Division vorstehender Gleichungen:

.. math::

   \\frac{bc}{ac} = \\frac{1}{2}. \\quad \\text{w. z. b. w.}""",
    },
    {
        "num": 12,
        "chapters": [("compendio", 29)],
        "locus": "Cap. XXIX, p. 220, l. 15 from top",
        "title_en": "Note 12 (Cap. XXIX): Construction of the Regular Icosahedron in the Sphere (Euclid XIII.16)",
        "title_de": "Anmerkung 12 (Cap. XXIX, S. 220): Construction des regulären Ikosaeders in der Kugel (Euklid XIII.16)",
        "text_en": """The edge $a$ of the regular icosahedron in terms of the circumradius $r$ of the sphere is:

.. math::

   a = \\frac{4r}{\\sqrt{10 + 2\\sqrt{5}}}.

Passing a plane through the sphere diameter $ab = 2r$ and a polar cap edge $ad = a$ (which cuts the sphere in a semicircle $adb$), the projection $ac$ of $ad$ on the diameter $ab$ satisfies:

.. math::

   ac = \\frac{ad^2}{ab} = \\frac{a^2}{2r} = r\\left(1 - \\frac{1}{\\sqrt{5}}\\right), \\qquad \\text{whence } cm = r - ac = \\frac{r}{\\sqrt{5}},

and therefore the middle axial segment between the two parallel pentagon planes is $cc' = 2\\,cm = \\frac{2r}{\\sqrt{5}} = \\frac{d}{\\sqrt{5}}$, where $d = 2r$ is the sphere diameter.

Now in the auxiliary semicircle of Chapter XXIX with $ac_{\\text{aux}} = 2\\,bc_{\\text{aux}}$, we have $bd = \\frac{d}{\\sqrt{5}} = cc'$—that is, $bd$ equals the height of the ten-triangle antiprism belt (the segments called *catheti* in the text) erected perpendicular to the two pentagon planes at $c$ and $c'$. Moreover, the circumradius $r'$ of these two parallel pentagons (and of the inscribed decagon) with pentagon side $a$ is:

.. math::

   r' = a\\sqrt{\\frac{5 + \\sqrt{5}}{10}} = \\frac{d}{\\sqrt{5}} = bd,

so the circumradius $r'$ of the pentagon circle equals both the line $bd$ of the text and the axial height $cc'$ of the perpendicular *catheti*, exactly as constructed in Euclid :just:`XIII.16`!""",
        "text_de": """Bekanntlich ist die Seite $a$ des regulären Ikosaeders, durch den Halbmesser $r$ der umschriebenen Kugel ausgedrückt:

.. math::

   a = \\frac{4r}{\\sqrt{10 + 2\\sqrt{5}}}.

Denkt man sich nun durch die Axe $ab = 2r$ und eine Kante $ad$ des Ikosaeders eine Ebene gelegt, welche zugleich die Kugel im Halbkreise $adb$ schneidet, so ist nach bekannten Sätzen:

.. math::

   ac = \\frac{ad^2}{ab} = \\frac{a^2}{2r} = r\\left(1 - \\frac{1}{\\sqrt{5}}\\right),

woraus hervorgeht, dass $cm = r - ac = \\frac{r}{\\sqrt{5}}$, somit das Doppelte $cc' = \\frac{2r}{\\sqrt{5}} = \\frac{d}{\\sqrt{5}}$, wenn der Kugeldurchmesser mit $d = 2r$ bezeichnet wird. Nun ist dem Text zufolge $\\frac{bd}{d} = \\frac{1}{\\sqrt{5}}$, sonach $bd = cc'$, d. h. gleich der Länge der im Text als Katheten bezeichneten Höhen, welche man in den Ecken der Fünfecke zu errichten hat. Der Radius $r'$ des diesen Fünfecken umschriebenen Kreises ist aber, wenn $a$ zugleich Fünfecksseite sein soll:

.. math::

   r' = a\\sqrt{\\frac{5 + \\sqrt{5}}{10}} = \\frac{d}{\\sqrt{5}} = bd,

d. h. es muss $r'$ genau gleich der Linie $bd$ des Textes und zugleich gleich den als Katheten bezeichneten Höhen sein, wie solches der dort angegebenen Construction zufolge auch wirklich der Fall ist.""",
    },
    {
        "num": 13,
        "chapters": [("compendio", 30)],
        "locus": "Cap. XXX, p. 224, l. 4 from bottom",
        "title_en": "Note 13 (Cap. XXX): Verification of the Pentagon Diagonal in the Dodecahedron Construction (Euclid XIII.17)",
        "title_de": "Anmerkung 13 (Cap. XXX, S. 224): Nachweis der Diagonalengleichung beim Dodekaeder (Euklid XIII.17)",
        "text_en": """Retaining the lettering of the figure in Chapter XXX (where $ke$ is half the cube edge, divided in extreme and mean ratio at $l$ with $kl > le$, and $an = hn = 2\\,kl$ is the cube edge): by the three-dimensional Pythagorean projection,

.. math::

   ln^2 = an^2 - ke^2 - le^2 = 4\\,kl^2 - ke^2 - le^2.

Since $kl^2 = ke \\cdot le$, we can rewrite this as:

.. math::

   ln^2 = 2\\,kl^2 + 2\\,ke \\cdot le - ke^2 - le^2 = 2\\,kl^2 - (ke - le)^2 = 2\\,kl^2 - kl^2 = kl^2,

whence $ln = kl$, proving that the five vertices lie at equal radii and form an equilateral and equiangular pentagon (:just:`XIII.17`).""",
        "text_de": """Dies ergibt sich unter Beibehaltung der Figur des Textes folgendermassen: Es ist der Construction zufolge (da $an = 2\\,kl$ als Kante des Würfels gleich $hn$ u. s. w. ist):

.. math::

   ln^2 = an^2 - ke^2 - le^2 = 4\\,kl^2 - ke^2 - le^2.

Da $kl^2 = ke \\cdot le$ ist, kann man diese Gleichung auch schreiben:

.. math::

   ln^2 = 2\\,kl^2 - (ke^2 - 2\\,ke \\cdot le + le^2) = 2\\,kl^2 - (ke - le)^2 = kl^2. \\quad \\text{w. z. b. w.}""",
    },
    {
        "num": 14,
        "chapters": [("compendio", 30)],
        "locus": "Cap. XXX, p. 225, l. 5 from top",
        "title_en": "Note 14 (Cap. XXX): Semicircle Proof of the Fifth Effect Used in the Dodecahedron Sphere Inscription",
        "title_de": "Anmerkung 14 (Cap. XXX, S. 225): Geometrischer Beweis der Relation $el^2 + ke^2 = 3\\,kl^2$",
        "text_en": """This relation ($el^2 + ke^2 = 3\\,kl^2$, already proved algebraically in Note 5) is seen most simply geometrically if we describe a semicircle on $ek$ as diameter, erect at $l$ a perpendicular meeting the semicircle at $m$, and draw the chords $em$ and $km$:

- By hypothesis, $kl^2 = ke \\cdot el$, and by the right triangle $emk$ in the semicircle, $em^2 = ke \\cdot el$, so $em = kl$.
- Moreover, $el^2 = em^2 - ml^2$ and $ke^2 = em^2 + mk^2$. Adding both gives:

  .. math::

     el^2 + ke^2 = 2\\,em^2 + (mk^2 - ml^2) = 2\\,em^2 + kl^2 = 3\\,em^2 = 3\\,kl^2. \\quad \\text{Q.E.D.}""",
        "text_de": """Dies ergibt sich am einfachsten, wenn man sich über $ek$ als Durchmesser einen Halbkreis denkt und im Punkte $l$ eine Senkrechte bis zum Durchschnitt $m$ mit ihm, sowie die Sehnen $em, km$ zieht. Dann ist nach Voraussetzung $kl^2 = ke \\cdot el$, und ferner nach bekannten Sätzen:

.. math::

   el^2 = em^2 - ml^2, \\qquad ke^2 = em^2 + mk^2,

also addirt:

.. math::

   el^2 + ke^2 = 2\\,em^2 + mk^2 - ml^2 = 2\\,em^2 + lk^2.

Da ferner $em^2 = el \\cdot ek = lk^2$, so folgt: $el^2 + ke^2 = 3\\,em^2 = 3\\,kl^2$. w. z. b. w.""",
    },
    {
        "num": 15,
        "chapters": [("compendio", 46)],
        "locus": "Cap. XLVI, p. 235",
        "title_en": "Note 15 (Cap. XLVI): Refutation of Pacioli's Claim That the Octahedron Cannot Be Inscribed in the Icosahedron (Tartaglia & Isoperimetric Approximation to the Sphere)",
        "title_de": "Anmerkung 15 (Cap. XLVI, S. 235): Widerlegung der Behauptung Pacioli's über die Einbeschreibung des Oktaeders ins Ikosaeder",
        "text_en": """The assertion stated here by Pacioli (following Campanus XV.13) is **manifestly false**: in a completely analogous manner to how the octahedron is inscribed in the dodecahedron (:ref:`Chapter XLIII <compendio-cap_43-en>`, :just:`XV.9`), **the regular octahedron can also be inscribed in the regular icosahedron**!

- **Construction of the Octahedron in the Icosahedron**: One need only connect the midpoints of each pair of opposite parallel edges of the icosahedron. Among the 15 such segments (since the 30 edges of the icosahedron fall into 15 opposite parallel pairs), there are 5 sets of **three mutually perpendicular axes** meeting at the center of the icosahedron; the six endpoints of any such orthogonal triad of edge-midpoints form the 6 vertices of a **regular octahedron inscribed in the icosahedron**! (As **Niccolò Tartaglia** already demonstrated in his *General Trattato di Numeri et Misure*, refuting Campanus and Pacioli.)
- **Cosmological Bias vs. Isoperimetric Truth**: The reason why Pacioli denies this elementary geometric fact stems from his desire to vindicate the Platonic cosmological hierarchy by assigning to the **dodecahedron** (as the symbol of the Quintessence / Heaven) the unique privilege of containing all four other regular solids, while restricting the **icosahedron** (Water) to only three.
  Pacioli's preference for the dodecahedron over the icosahedron would have been mathematically well-founded had he chosen as his criterion not how many other solids can be inscribed in it, but rather **which regular solid inscribed in the same sphere approaches most closely to the sphere itself—that is, which solid encompasses the greatest surface area and the greatest volume**! By this isoperimetric criterion (already proved by Hypsicles in Book XIV, Proposition 2, and by Pappus), the decision falls decisively in favor of the **dodecahedron** over the icosahedron.""",
        "text_de": """Die hier ausgesprochene Behauptung ist **offenbar falsch**, denn auf ganz analoge Art wie das Oktaeder dem Dodekaeder sich einbeschreiben lässt, kann es auch dem Ikosaeder eingeschrieben werden. Man braucht sich zu diesem Zweck nur die Mitten je zweier sich parallel gegenüberliegenden Kanten verbunden zu denken. Unter ihnen wird man drei solche als Axenkreuz wählen, welche senkrecht aufeinander stehen, was auf vielfache (fünffache) Art möglich ist. Damit ist zugleich die Lage des Oktaeders bestimmt. (Uebrigens hat schon **Tartaglia** im *General-Trattato* diese Ansicht widerlegt.)

Der Grund, warum Pacioli das Vorhandensein dieser einfachen Thatsache leugnet, scheint aus dem einseitigen Bestreben hervorgegangen zu sein, im Sinne der platonischen Lehre einem unter den fünf Körpern, dem Dodekaeder, vor allen andern den Vorzug grösster Vollkommenheit zuzuerkennen—eine Anschauung, die sich nach dem Vorherigen als durchaus unhaltbar beweist. Mit mehr Recht würde des Verfassers Annahme als zulässig erscheinen, hätte er als Massstab seines Urtheils nicht die Frage entscheiden lassen, welchem Körper die meisten andern sich einbeschreiben lassen, sondern **welcher Körper sich der Kugel als dem vollkommensten Körper am meisten nähere, wenn sie sämmtlich derselben Kugel einbeschrieben gedacht werden, d. h. welcher die grösste Oberfläche und das grösste Volumen umfasse**? Hierbei stellt sich nämlich, wie leicht nachweisbar, die Entscheidung entschieden zu Gunsten des Dodekaeders.""",
    },
    {
        "num": 16,
        "chapters": [
            ("compendio", 47),
            ("compendio", 48),
            ("compendio", 49),
            ("compendio", 50),
            ("compendio", 51),
            ("compendio", 52),
        ],
        "locus": "Cap. XLVII–LII, pp. 236–242",
        "title_en": "Note 16 (Cap. XLVII–LII): Reciprocal (Dual) Polyhedra Generated by Pyramidal Elevation of Faces and Planar Truncation of Vertices",
        "title_de": "Anmerkung 16 (Cap. XLVII–LII): Reciproke (duale) reguläre Körper durch pyramidale Erhöhung und Eckenabschneiden",
        "text_en": """Regarding the generation of the regular bodies and their dependent derivatives, Pacioli distinguishes two primary classes: **plane (convex)** and **truncated (*abscisi*)** bodies, each rendered both **solid (*solidum*)** and **hollow/skeletal (*vacuum*)**, and then modifies them further by **elevating equilateral pyramids (*elevati*)** outward upon their faces. (The inverse operation—excavating pyramids inward upon the same faces—is not mentioned.)

The star-like elevated polyhedra can likewise be inscribed in a sphere passing through all the pyramid apices. If we regard those **pyramid apices as the vertices of a new convex polyhedron**, we immediately obtain the **reciprocal (dual) regular solid**:

- The **elevated tetrahedron** leads again to a **regular tetrahedron** (4 apices);
- The **elevated cube** leads to the **regular octahedron** (6 apices);
- The **elevated octahedron** (*Stella Octangula*) leads to the **regular cube** (8 apices);
- The **elevated icosahedron** leads to the **regular dodecahedron** (20 apices);
- The **elevated dodecahedron** leads to the **regular icosahedron** (12 apices).

More generally, the five regular solids correspond two by two as **reciprocal (dual) pairs** with respect to the numbers of their vertices ($V$), edges ($E$), and faces ($F$):

- **Tetrahedron $\\leftrightarrow$ Tetrahedron (Self-Reciprocal)**: $E = 6$, $V = 4$, $F = 4$.
- **Cube $\\leftrightarrow$ Octahedron**: $E = 12$, with $V = 8, F = 6$ for the Cube and $V = 6, F = 8$ for the Octahedron.
- **Icosahedron $\\leftrightarrow$ Dodecahedron**: $E = 30$, with $V = 12, F = 20$ for the Icosahedron and $V = 20, F = 12$ for the Dodecahedron.

From any regular body, its **reciprocal (dual) body** arises in two dual ways:

1. **By transforming faces into vertices (Elevation)**: Erecting pyramids upon the faces and taking their apices as the vertices of the new body (when the pyramid height is chosen so that the apices of the pyramids sharing a common vertex of the original solid become coplanar with that vertex, the new reciprocal solid circumscribes the sphere that circumscribed the original solid).
2. **By transforming vertices into planes (Truncation)**: Slicing off the corners by planes until the cuts around each face meet at the **centroid of that face**, so that the original faces shrink to points (vertices) and the new body is circumscribed about the sphere that was inscribed in the original body.""",
        "text_de": """Hinsichtlich der Art des Zustandekommens der regulären Körper und der von ihnen abhängigen unterscheidet der Verfasser zwei Classen, nämlich ebene (einfache) und abgeschnittene regelmässige Körper, die er in volle und hohle eintheilt. Diese einfachen und abgeschnittenen werden dann ferner noch dadurch modificirt, dass man sich auf ihren Seitenflächen gleichseitige Pyramiden errichtet denkt.

Die auf diese Art erhaltenen sternförmigen Körper sind ebenfalls in eine Kugel construirbar, welche alle Pyramidenspitzen umfasst, und betrachtet man die Pyramidenspitzen als Ecken eines neuen Körpers, so erkennt man unmittelbar, dass sich dafür wieder einfache reguläre Körper ergeben: das erhöhte Tetraeder führt zum einfachen Tetraeder, der erhöhte Kubus zum einfachen Oktaeder, das erhöhte Oktaeder zum einfachen Kubus u. s. f.

Die fünf einfachen regulären Körper verhalten sich hinsichtlich der Anzahl ihrer Ecken, Kanten und Seitenflächen zwei und zwei **reciprok** zu einander:

- Das **Tetraeder** entspricht nur sich selbst ($6$ Kanten, $4$ Ecken, $4$ Seitenflächen).
- Der **Kubus** ($12$ Kanten, $8$ Ecken, $6$ Flächen) entspricht dem **Oktaeder** ($12$ Kanten, $6$ Ecken, $8$ Flächen) und umgekehrt.
- Dem **Ikosaeder** ($30$ Kanten, $12$ Ecken, $20$ Seitenflächen) entspricht das **Dodekaeder** ($30$ Kanten, $20$ Ecken, $12$ Flächen) und umgekehrt.

Aus einem derselben ergibt sich der reciproke Körper auf zweierlei Art:

1. **Durch Verwandlung der Seitenflächen in Eckpunkte** (Aufsetzen oder Aushöhlen von Pyramiden, indem man deren Spitzen als die Ecken des neuen Körpers betrachtet; wird die Höhe der Pyramiden genau so bemessen, dass die Spitzen sämmtlicher Pyramiden um eine Ecke mit dieser Ecke genau in einer Ebene liegen, so umhüllt der neue Körper diejenige Kugel, welche dem ursprünglichen umschrieben ist).
2. **Durch Verwandlung der Ecken in Ebenen**, d. h. durch Abschneiden der Ecken bis sich sämmtliche um die Ecken einer Seitenfläche geführten Schnitte im **Schwerpunkt dieser Figur** schneiden, so dass die Seitenflächen in Punkte übergehen (wobei der erhaltene Körper von derjenigen Kugel umhüllt wird, welche dem ursprünglichen Körper einbeschrieben ist).""",
    },
    {
        "num": 17,
        "chapters": [("compendio", 35), ("compendio", 46)],
        "locus": "Cap. XXXV–XLVI, pp. 227–235 (Anmerkungen pp. 345–352)",
        "title_en": "Note 17 (Cap. XXXV–XLVI): Complete Projective Theory of the 21 Mutual Inscriptions of the Five Regular Solids via Polar Reciprocity in the Sphere",
        "title_de": "Anmerkung 17 (Cap. XXXV–XLVI, S. 345–352): Vollständige Theorie aller 21 gegenseitigen Einbeschreibungen der fünf regulären Körper mittelst Polarität an der Kugel",
        "text_en": """To understand the mutual relationships of the five regular solids systematically and resolve **all possible questions of mutual inscription** at a single stroke, we employ the projective theory of **poles and polar planes with respect to a concentric sphere**.

1. Direct vs. Reciprocal Correspondence and Polarity in the Sphere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Between the elements (vertices and bounding faces) of two polyhedra, we distinguish two kinds of correspondence:

- **Direct Correspondence**: Each vertex of the inner solid corresponds to a vertex of the outer solid, or each face corresponds to a face.
- **Reciprocal Correspondence**: Each vertex of the first solid corresponds to a bounding face of the second, or conversely each face of the first corresponds to a vertex of the second.

The simplest universal mechanism for establishing a mutual reciprocal correspondence is **polar reciprocation with respect to a concentric sphere**:

- The **pole** of a plane cutting a sphere is the apex of the tangent cone touching the sphere along the circle of intersection; conversely, that plane is the **polar plane** of the point.
- Taking a sphere concentric with any regular solid, the polar planes of all its vertices (or equivalently, the poles of all its faces) form its **polar reciprocal regular solid**:
  - **Tetrahedron $\\leftrightarrow$ Tetrahedron**
  - **Cube $\\leftrightarrow$ Octahedron**
  - **Icosahedron $\\leftrightarrow$ Dodecahedron**
- As the radius $R$ of the reciprocating sphere expands continuously from $0$ to $\\infty$:
  1. **First Limit ($R = \\rho$, the inradius of the original solid)**: The sphere touches the faces of the original solid from within; the poles of the faces are the **centroids of the faces**, so the reciprocal solid is **inscribed** in the original solid with its vertices at the face-centers.
  2. **Symmetric Dual Intersection ($R = \\sqrt{r\\rho}$, the geometric mean of the circumradius $r$ and inradius $\\rho$)**: Both reciprocal solids are **inscribed in the same outer sphere of radius $r$ and circumscribed about the same inner sphere of radius $\\rho$**!
  3. **Second Limit ($R = r$, the circumradius of the original solid)**: The sphere passes through the vertices of the original solid; the polar planes are the tangent planes at those vertices, so the original solid is now **inscribed** in its reciprocal solid!

2. Complete Classification of All 21 Possible Mutual Inscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By means of polar reciprocation, all **20 mutual inscriptions between distinct regular solids** (plus **1 self-inscription of the tetrahedron in the tetrahedron**, making **21 cases in all**) fall into **three direct groups (a)** and **three polar-reciprocal groups (b)**, where an asterisk (``*``) marks the 12 cases treated by Euclid Book XV / Campanus / Pacioli in Chapters XXXV–XLVI:

.. list-table:: Complete System of Mutual Inscriptions of the Five Regular Solids (Winterberg 1889, p. 348)
   :header-rows: 1
   :widths: 50 50

   * - **(a) Direct Inscriptions (Vertices of Inner Solid)**
     - **(b) Polar-Reciprocal Inscriptions (Faces of Outer Solid)**
   * - **Group I(a): Vertex on Vertex** (*Ecke auf Ecke*)
     - **Group I(b): Face on Face** (*Fläche auf Fläche*)
   * - **1.** Tetrahedron in Cube ``*`` (:ref:`Cap. XXXV <compendio-cap_35-en>`, :just:`XV.1`)
     - **2.** Octahedron in Tetrahedron ``*`` (:ref:`Cap. XXXVI <compendio-cap_36-en>`, :just:`XV.2`)
   * - **3.** Tetrahedron in Dodecahedron ``*`` (:ref:`Cap. XLI <compendio-cap_41-en>`, :just:`XV.7`)
     - **4.** Icosahedron in Tetrahedron (*omitted by Pacioli*)
   * - **5.** Cube in Dodecahedron ``*`` (:ref:`Cap. XLII <compendio-cap_42-en>`, :just:`XV.8`)
     - **6.** Icosahedron in Octahedron (*omitted by Pacioli*)
   * - **Group II(a): Vertex on Face** (*Ecke auf Fläche*)
     - **Group II(b): Face on Vertex** (*Fläche auf Ecke*)
   * - **7.** Octahedron in Cube ``*`` (:ref:`Cap. XXXVII <compendio-cap_37-en>`, :just:`XV.3`)
     - **8.** Cube in Octahedron ``*`` (:ref:`Cap. XXXVIII <compendio-cap_38-en>`, :just:`XV.4`)
   * - **9.** Icosahedron in Dodecahedron ``*`` (:ref:`Cap. XLIV <compendio-cap_44-en>`, :just:`XV.10`)
     - **10.** Dodecahedron in Icosahedron ``*`` (:ref:`Cap. XLV <compendio-cap_45-en>`, :just:`XV.11`)
   * - **11.** Tetrahedron in Icosahedron ``*`` (:ref:`Cap. XL <compendio-cap_40-en>`, :just:`XV.6`)
     - **12.** Dodecahedron in Tetrahedron (*omitted by Pacioli*)
   * - **13.** Cube in Icosahedron ``*`` (:ref:`Cap. XLVI <compendio-cap_46-en>`, :just:`XV.12`)
     - **14.** Dodecahedron in Octahedron (*omitted by Pacioli*)
   * - **Group III(a): Vertex on Edge** (*Ecke auf Kante*)
     - **Group III(b): Edge on Face** (*Kante in Fläche*)
   * - **15.** Octahedron in Dodecahedron ``*`` (:ref:`Cap. XLIII <compendio-cap_43-en>`, :just:`XV.9`)
     - **16.** Icosahedron in Cube (*treated in Piero/Pacioli's Libellus!*)
   * - **17.** Octahedron in Icosahedron (*denied by Pacioli in Cap. XLVI; proved by Tartaglia & Note 15*)
     - **18.** Dodecahedron in Cube (*omitted by Pacioli*)
   * - **19.** Tetrahedron in Octahedron ``*`` (:ref:`Cap. XXXIX <compendio-cap_39-en>`, :just:`XV.5`)
     - **20.** Cube in Tetrahedron (*omitted by Pacioli*)
   * - **21.** Tetrahedron in Tetrahedron (*vertices at face-centroids; omitted in Cap. XXXV–XLVI*)
     - *(Self-reciprocal)*

3. Geometric Derivation of the Reciprocal Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Group I (1 $\\leftrightarrow$ 2, 3 $\\leftrightarrow$ 4, 5 $\\leftrightarrow$ 6)**: Taking the polar reciprocals of two solids sharing common vertices on a circumscribed sphere converts the inner solid into the outer reciprocal solid and the outer solid into the inner reciprocal solid, with **coincident faces** replacing coincident vertices:
  - From **1 (Tetrahedron in Cube)** arises **2 (Octahedron in Tetrahedron)**, where 4 of the 8 faces of the octahedron lie in the 4 faces of the tetrahedron and the 6 vertices of the octahedron lie at the 6 edge-midpoints of the tetrahedron.
  - From **3 (Tetrahedron in Dodecahedron)** arises **4 (Icosahedron in Tetrahedron)**, where 4 faces of the icosahedron lie in the 4 faces of the circumscribing tetrahedron (obtained by extending the 4 icosahedron faces whose centroids form the inscribed tetrahedron of Case 11 until they meet!).
  - From **5 (Cube in Dodecahedron)** arises **6 (Icosahedron in Octahedron)**, where 8 faces of the icosahedron lie in the 8 faces of the octahedron and all 12 vertices of the icosahedron lie on the 12 edges of the octahedron (dividing them in the golden ratio!).
- **Group II (7 $\\leftrightarrow$ 8, 9 $\\leftrightarrow$ 10, 11 $\\leftrightarrow$ 12, 13 $\\leftrightarrow$ 14)**:
  - **7 $\\leftrightarrow$ 8 (Octahedron $\\leftrightarrow$ Cube)** and **9 $\\leftrightarrow$ 10 (Icosahedron $\\leftrightarrow$ Dodecahedron)** are dual pairs directly.
  - From **11 (Tetrahedron in Icosahedron)**, reciprocating with respect to the sphere touching the icosahedron and circumscribing the dodecahedron yields **12 (Dodecahedron in Tetrahedron)**: passing tangent planes through the 4 common vertices of the dodecahedron and its inscribed tetrahedron (Case 3) forms the circumscribing tetrahedron touching 4 vertices of the dodecahedron.
  - From **13 (Cube in Icosahedron)** arises **14 (Dodecahedron in Octahedron)**, where the centers of the 8 octahedron faces contain the 8 vertices of the dodecahedron that form an inscribed cube.
- **Group III (15 $\\leftrightarrow$ 16, 17 $\\leftrightarrow$ 18, 19 $\\leftrightarrow$ 20)**: Because the two solids do not share a common circumsphere when vertices fall on edges, we reciprocate with respect to any concentric sphere (e.g., the sphere circumscribing the outer solid), transforming **vertices on edges** into **faces containing edges**:
  - From **15 (Octahedron in Dodecahedron)** arises **16 (Icosahedron in Cube)**, where **6 opposite parallel edges of the icosahedron lie in the 6 square faces of the cube** along their midlines in three mutually perpendicular directions, so that all 12 vertices of the icosahedron rest in pairs on the 6 faces of the cube! Remarkably, although omitted here in the *Compendio*, this exact inscription is explicitly treated in Piero della Francesca / Pacioli's companion *Libellus de Quinque Corporibus Regularibus*!
  - From **17 (Octahedron in Icosahedron)** arises **18 (Dodecahedron in Cube)**, where 6 opposite parallel edges of the dodecahedron lie along the midlines of the 6 faces of the cube (while the 8 remaining vertices of the dodecahedron, corresponding to an inscribed cube, lie free inside).
  - From **19 (Tetrahedron in Octahedron)** arises **20 (Cube in Tetrahedron)**, where the 4 faces of the tetrahedron contain 4 edges of the cube (two opposite top edges of the cube and the two perpendicular bottom edges).""",
        "text_de": """Wenn auch Pacioli die Bedeutung der fünf regelmässigen Körper in theoretischer wie in praktischer Hinsicht weit überschätzt, so scheint es gleichwohl von Interesse, auf die Theorie dieses Gegenstandes etwas näher einzugehen, um die Eigenschaften jener Körper in ihrem gegenseitigen Zusammenhange leichter zu verstehen. Es werden hierdurch leicht alle auf die gegenseitige Einbeschreibung bezüglichen Fragen erledigt.

1. Directe und reciproke Beziehung mittelst Polarität an der Kugel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Von irgend einem Körper kann man stets die Ecken und Grenzflächen auf zweierlei Art aufeinander bezogen denken:

- **Directe Beziehung**: Jedem Eckpunkt des einen Körpers wird ein Eckpunkt des andern, oder jeder Ebene des einen eine Ebene des andern zugeordnet.
- **Reciproke Beziehung**: Zu jeder Ecke des ersten wird eine Grenzfläche des zweiten oder umgekehrt zu jeder Grenzfläche des ersten eine Ecke des zweiten zugeordnet.

Die einfachste Art, eine wechselseitige reciproke Beziehung herzustellen, ist die **polare Beziehung mittelst einer concentrischen Kugel**. Unter dem **Pol** einer Ebene bezüglich einer Kugel versteht man die Spitze des Tangentenkegels, dessen Basis der von jener Ebene aus der Kugel ausgeschnittene Kreis ist, wie umgekehrt diese Ebene die **Polarebene** jenes Punktes genannt wird. Bestimmt man auf diese Weise von irgend einem der regelmässigen Körper seinen polaren Körper mittelst einer concentrischen Kugel, so ergibt sich für jeden Körper der reciproke als polare Figur.

Denkt man sich die Kugel vom Radius $R$ allmählich wachsend:

1. **Erster Grenzfall ($R = \\rho$)**: Berührt die Kugel den ursprünglich gegebenen Körper von innen, so fallen die Pole seiner Tangentialebenen in die Berührungspunkte (Flächenmitten), deren Verbindung den polaren Körper liefert, der somit dem ursprünglichen genau **einbeschrieben** ist.
2. **Gegenseitige Durchdringung bei gemeinsamer Um- und Inkugel ($R = \\sqrt{r\\rho}$)**: Beide Körper werden von derselben Kugel vom Radius $r$ umschlossen und umhüllen dieselbe Kugel vom Radius $\\rho$.
3. **Zweiter Grenzfall ($R = r$)**: Umhüllt die Kugel den ursprünglichen Körper genau, so vertauschen beide Körper ihre Stellen, und der ursprüngliche ist dem polaren genau **einbeschrieben**.

2. Schema aller 21 möglichen Fälle gegenseitiger Einbeschreibung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die sämmtlichen überhaupt möglichen **20 oder genauer 21 Fälle** dieser Art ergeben sich, indem man zunächst nach drei Gruppen ordnet, je nachdem bei der Einschreibung **Ecke auf Ecke**, **Ecke auf Seitenfläche** oder **Ecke auf Kante** fällt. Durch reciproke Uebertragung leitet man sodann aus den zehn hierauf bezüglichen Fällen ebensoviel neue ab, je nachdem **Fläche auf Fläche**, **Fläche auf Ecke** und **Kante in Fläche** fällt (die mit ``*`` bezeichneten sind die im Text Pacioli's bereits erwähnten 12 Fälle):

.. list-table:: Vollständiges System der gegenseitigen Einbeschreibungen (Winterberg 1889, S. 348)
   :header-rows: 1
   :widths: 50 50

   * - **a) Direct**
     - **b) Durch reciproke Uebertragung**
   * - **I. Ecke auf Ecke**
     - **I'. Fläche auf Fläche**
   * - **1.** Tetraeder im Kubus ``*`` (Cap. XXXV)
     - **2.** Oktaeder im Tetraeder ``*`` (Cap. XXXVI)
   * - **3.** Tetraeder im Dodekaeder ``*`` (Cap. XLI)
     - **4.** Ikosaeder im Tetraeder
   * - **5.** Kubus im Dodekaeder ``*`` (Cap. XLII)
     - **6.** Ikosaeder im Oktaeder
   * - **II. Ecke auf Fläche**
     - **II'. Fläche auf Ecke**
   * - **7.** Oktaeder im Kubus ``*`` (Cap. XXXVII)
     - **8.** Kubus im Oktaeder ``*`` (Cap. XXXVIII)
   * - **9.** Ikosaeder im Dodekaeder ``*`` (Cap. XLIV)
     - **10.** Dodekaeder im Ikosaeder ``*`` (Cap. XLV)
   * - **11.** Tetraeder im Ikosaeder ``*`` (Cap. XL)
     - **12.** Dodekaeder im Tetraeder
   * - **13.** Kubus im Ikosaeder ``*`` (Cap. XLVI)
     - **14.** Dodekaeder im Oktaeder
   * - **III. Ecke auf Kante**
     - **III'. Kante in Fläche**
   * - **15.** Oktaeder im Dodekaeder ``*`` (Cap. XLIII)
     - **16.** Ikosaeder im Kubus (*im Libellus behandelt*)
   * - **17.** Oktaeder im Ikosaeder (*von Pacioli geleugnet*)
     - **18.** Dodekaeder im Kubus
   * - **19.** Tetraeder im Oktaeder ``*`` (Cap. XXXIX)
     - **20.** Kubus im Tetraeder
   * - **21.** Tetraeder ins Tetraeder (*im Text übersehen*)
     - *(Selbstreciprok)*

3. Ableitung der einzelnen Gruppen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Erste Gruppe (1–6)**: Mittelst der Kugel, welche je zweien der Körper aus der linken Gruppe umschrieben ist, werden die Polarebenen der gemeinsamen Ecken zu gemeinsamen Tangentialebenen:
  - In **2 (Oktaeder im Tetraeder)** fallen vier Ebenen des Oktaeders in die vier Tetraederflächen, während die sechs Ecken des Oktaeders in die Mitten der sechs Kanten des Tetraeders fallen.
  - Aus **3** entsteht **4 (Ikosaeder im Tetraeder)**, wobei vier Ebenen des Ikosaeders mit den vier Tetraederebenen zusammenfallen (indem man die vier Flächen des Ikosaeders, deren Mitten die Ecken des eingeschriebenen Tetraeders bilden, bis zu ihrem gegenseitigen Durchschnitt verlängert).
  - Aus **5** wird **6 (Ikosaeder im Oktaeder)** abgeleitet, wobei acht Ikosaederflächen mit den acht Flächen des Oktaeders zusammenfallen und zugleich die zwölf Ecken des Ikosaeders in die zwölf Kanten des Oktaeders fallen.
- **Zweite Gruppe (7–14)**:
  - **7 $\\leftrightarrow$ 8** und **9 $\\leftrightarrow$ 10** ergeben sich unmittelbar.
  - Um aus **11** den Fall **12 (Dodekaeder im Tetraeder)** abzuleiten, vergegenwärtigt man sich den Fall **3** des dem Dodekaeder eingeschriebenen Tetraeders und legt durch die gemeinsamen vier Eckpunkte beider Körper Tangentialebenen, deren Gesammtheit das dem Dodekaeder umschriebene Tetraeder bildet.
  - Analog ergibt sich **14 (Dodekaeder im Oktaeder)** aus **13**, wobei die Mitten der acht Oktaederflächen diejenigen acht Ecken des Dodekaeders enthalten, welche verbunden den eingeschriebenen Kubus bilden würden.
- **Dritte Gruppe (15–20)**: Fallen bei den Körpern links Ecken auf Kanten, so fallen bei den reciproken Körpern rechts **Ebenen auf Kanten** (d. h. Kanten in die Seitenflächen):
  - Aus **15** ergibt sich **16 (Ikosaeder im Kubus)**, wobei sechs Ikosaederkanten in die sechs Kubusflächen, und zwar in deren Mittellinien je zwei und zwei parallel fallen, so dass sämmtliche 12 Ecken des Ikosaeders als Endpunkte der Kanten zu je zwei auf den Kubusflächen liegen. Dieser im Text der *Divina proportione* nicht aufgezählte Fall wird eigenthümlicherweise im *Tractat über die fünf regelmässigen Körper* (*Libellus*) ausdrücklich erwähnt und behandelt!
  - Aus **17** entsteht **18 (Dodekaeder im Kubus)**, wobei die Kantenlage dieselbe ist wie bei 16, ausserdem aber noch acht Ecken frei liegen, welche den Ecken des dem Dodekaeder eingeschriebenen Kubus entsprechen.
  - Aus **19** endlich findet sich **20 (Kubus im Tetraeder)**, wobei die vier Flächen des Tetraeders vier Kanten des Kubus enthalten (zwei sich gegenüberliegende Seiten des obern und die sie kreuzenden des untern Quadrats).""",
    },
]


# Additional brief textual footnotes by Winterberg on individual chapters
WINTERBERG_CHAPTER_FOOTNOTES: Dict[Tuple[str, int], List[Tuple[str, str]]] = {
    ("compendio", 1): [
        (
            "Winterberg Footnote 1 (Cap. I, p. 171): In the 1509 Italian text, read *quanto* instead of *quarto*.",
            "Winterberg Fussnote 1 (Cap. I, S. 171): *Text l. quanto statt quarto.*",
        )
    ],
    ("compendio", 2): [
        (
            "Winterberg Footnote 1 (Cap. II, TOC p. 166 & p. 176): *La Teberina* (*Tyberiadis*)—a treatise by Bartolus of Sassoferrato on the alluvial deposits caused by the flooding of the Tiber.",
            "Winterberg Fussnote 1 (Cap. II, Inh. S. 166): *Ein Werk über die Tiberüberschwemmung.*",
        ),
        (
            "Winterberg Footnote 2 (Cap. II, p. 176): Pacioli calls Euclid 'the Megarian philosopher' (*Euclide Megarense*)—throughout erroneously confusing the Socratic philosopher Euclid of Megara with the mathematician Euclid of Alexandria who lived in Egypt.",
            "Winterberg Fussnote 2 (Cap. II, S. 176): *Durchgehends fälschlich anstatt des in Aegypten lebenden Mathematikers gleichen Namens angegeben.*",
        ),
    ],
    ("compendio", 3): [
        (
            "Winterberg Footnote 1 (Cap. III, p. 179): Supply the verb *exclude* (*scil. ausschliessen*) regarding those who admit only athreefold division of the mathematical sciences.",
            "Winterberg Fussnote 1 (Cap. III, S. 179): *scil. ausschliessen.*",
        )
    ],
    ("compendio", 4): [
        (
            "Winterberg Footnote 1 (Cap. IV, p. 180): By the *power* (*potentia*) of a line, Pacioli means its *square* (*Quadrat*).",
            "Winterberg Fussnote 1 (Cap. IV, S. 180): *Quadrat.*",
        )
    ],
    ("compendio", 5): [
        (
            "Winterberg Footnote 1 (Cap. V, p. 181): By the product $ab \\cdot bc$ ('contained under the whole and lesser part'), Euclid and Pacioli mean the *rectangle* (*Rechteck*), in contrast to the product multiplied by the cosine of the angle of inclination, which corresponds to the area of an oblique parallelogram.",
            "Winterberg Fussnote 1 (Cap. V, S. 181): *D. i. Rechteck im Gegensatze zu dem mit dem cos. des Neigungswinkels zu multiplicirenden Producte, welches dem Inhalt eines schiefwinkeligen Parallelogramms entspricht.*",
        )
    ],
    ("compendio", 25): [
        (
            "Winterberg Footnote 1 (Cap. XXV, p. 214): Namely, each regular solid can be accurately inscribed in the others (*scil. der eine lässt sich genau in den andern einbeschreiben*).",
            "Winterberg Fussnote 1 (Cap. XXV, S. 214): *scil. der eine lässt sich genau in den andern einbeschreiben.*",
        )
    ],
    ("compendio", 26): [
        (
            "Winterberg Footnotes 1–3 (Cap. XXVI, pp. 215–216): (1) Instead of the term 'edge' (*Kante*), Pacioli frequently uses the synonymous designation 'side' (*lato / Seite*). (2) Namely, the diameter of the circumscribed sphere (*scil. der umbeschriebenen*). (3) Compare Chapter LXXI on the technical term *corausto* (the slant edge of the pyramid).",
            "Winterberg Fussnoten 1–3 (Cap. XXVI, S. 215–216): *1) Statt des Ausdrucks „Kante“ kehrt häufig die dasselbe besagende Bezeichnung „Seite“ wieder. 2) scil. der umbeschriebenen. 3) cfr. Cap. LXXI.*",
        )
    ],
    ("compendio", 28): [
        (
            "Winterberg Footnote 1 (Cap. XXVIII, p. 218): Compare Chapter LXXI on the technical term *cono* (the apex of the pyramid).",
            "Winterberg Fussnote 1 (Cap. XXVIII, S. 218): *cfr. Cap. LXXI.*",
        )
    ],
    ("compendio", 29): [
        (
            "Winterberg Footnotes 1–5 (Cap. XXIX, pp. 219–221): (1) When the total length of a line divided in extreme and mean ratio is rational, its segments are always irrational (apotomes), which gave rise to Euclid's classification of the *minor* irrational line (:just:`X.76`, :just:`XIII.16`). (2) A rational diameter—one whose length itself or whose square is rational. (3) *Catheti*, i.e., perpendiculars; compare Chapter LXXI on the technical terms occurring here. (4) Namely, equal to the radius $bd$ of the circle. (5) *In potentia*, i.e., in their second power (square).",
            "Winterberg Fussnoten 1–5 (Cap. XXIX, S. 219–221): *1) Wenn die ganze Länge der stetig zu theilenden Linie rational ist, so werden die Abschnitte stets irrational sein, was zu obiger heute nicht mehr gebräuchlicher Benennung Veranlassung gegeben. 2) scil. dessen Länge selbst oder deren Quadrat rational sei. 3) scil. Senkrechten; über die hier und im Folgenden vorkommenden Benennungen cfr. Cap. LXXI. 4) scil. dem Radius bd des Kreises gleich. 5) d. h. ihrer zweiten Potenz.*",
        )
    ],
    ("compendio", 30): [
        (
            "Winterberg Footnotes 1–4 (Cap. XXX, pp. 222–224): (1) Mathematical abbreviations are introduced occasionally here and in the following chapters for clearer overview. (2) Namely, because of the similarity of the two triangles $ksh$ and $qrh$ following from the proportion, since the sum of the two adjacent angles plus the dihedral angle enclosed by the two cube faces equals $180^\\circ$. (3) For brevity, the expression 'continuous division' (*stetige Theilung*) is used for Pacioli's 'proportion having a mean and two extremes'. (4) Compare Chapter LXXI.",
            "Winterberg Fussnoten 1–4 (Cap. XXX, S. 222–224): *1) Es sei erlaubt, hier und im Folgenden einige mathematische Abkürzungen der bessern Uebersicht wegen gelegentlich anzubringen. 2) scil. wegen der aus obiger Proportion folgenden Aehnlichkeit der beiden Dreiecke ksh und qrh, da die Summe der beiden anstossenden Winkel plus dem durch die beiden Kubusflächen eingeschlossenen zusammen gleich 180° sind. 3) Der Kürze wegen ist hier und im Folgenden dieser Ausdruck für den gleichbedeutenden: „nach der Proportion, die einen mittlern und zwei äussere Abschnitte hat“ gesetzt worden. 4) cfr. Cap. LXXI.*",
        )
    ],
    ("compendio", 31): [
        (
            "Winterberg Footnotes 1–5 (Cap. XXXI, pp. 225–226): (1) Namely, $bd^2$. (2) That is, its square equals five times the square of the radius of the circle in which the pentagons of the icosahedron were described (compare Chapter XXIX, :just:`XIII.16`). (3) Namely, the icosahedron. (4) Namely, of the sphere diameter (:just:`VI.8` Corollary, :just:`XIII.18`). (5) Namely, the regular tetrahedron.",
            "Winterberg Fussnoten 1–5 (Cap. XXXI, S. 225–226): *1) scil. bd². 2) D. h. sein Quadrat ist gleich dem fünffachen Quadrat des Radius desjenigen Kreises, in welchem die Pentagone beschrieben wurden (cfr. Cap. XXIX). 3) scil. Ikosaeder. 4) scil. vom Kugeldurchmesser. 5) scil. reguläre Tetraeder.*",
        )
    ],
    ("compendio", 33): [
        (
            "Winterberg Footnote 1 (Cap. XXXIII, p. 226): Pacioli's traditional Boethian proportion names (*sesquitertia* = $4:3$, etc.) are retained here for brevity.",
            "Winterberg Fussnote 1 (Cap. XXXIII, S. 226): *Der Ausdruck ist hier der Kürze wegen beibehalten = 4:3.*",
        )
    ],
    ("compendio", 39): [
        (
            "Winterberg Footnote 1 (Cap. XXXIX, p. 230): Namely, the midpoints (*scil. Mittelpunkte*) of the edges of the octahedron.",
            "Winterberg Fussnote 1 (Cap. XXXIX, S. 230): *scil. Mittelpunkte.*",
        )
    ],
    ("compendio", 41): [
        (
            "Winterberg Footnote 1 (Cap. XLI, p. 231): Under the designation *pyramide* in Chapters XLI–XLVI, Pacioli always understands the regular triangular pyramid (the regular tetrahedron).",
            "Winterberg Fussnote 1 (Cap. XLI, S. 231): *Unter dieser Bezeichnung ist im Folgenden stets das dreiseitige reguläre Tetraeder verstanden.*",
        )
    ],
    ("compendio", 46): [
        (
            "Winterberg Footnote 1 (Cap. XLVI, p. 234): For the cube inscribed in the icosahedron, the 8 vertices of the cube must fall at the centroids of 8 of the 20 triangular faces of the icosahedron (via the inscribed dodecahedron of Chapter XLIV).",
            "Winterberg Fussnote 1 (Cap. XLVI, S. 234): *Die Ecken des Würfels müssen in die Mitte der Dreiecksfläche des Ikosaeders fallen (zuf. Cap. XLIV).*",
        )
    ],
    ("compendio", 48): [
        (
            "Winterberg Footnotes 1–3 (Cap. XLVIII, p. 238): (1) The clause 'equiangular' refers to the regular hexagons produced by trisecting the edges. (2) Compare Chapter LXXI on *corausto*. (3) Here and in the following chapters on elevated bodies, Pacioli always assumes pyramids bounded by equilateral triangles of the same edge length.",
            "Winterberg Fussnoten 1–3 (Cap. XLVIII, S. 238): *1) Dieser Zusatz ist natürlich auf die Hexagone zu beziehen. 2) cfr. Cap. LXXI. 3) Es werden hier wie im Folgenden stets Körper von gleicher Kantenlänge vorausgesetzt.*",
        )
    ],
    ("compendio", 50): [
        (
            "Winterberg Footnote 1 (Cap. L, p. 239): Instead of 'solid angle' (*angulo solido* / *körperlicher Winkel*), the synonymous shorter term 'vertex' (*Ecke*) is preferred.",
            "Winterberg Fussnote 1 (Cap. L, S. 239): *Statt „körperlicher Winkel“ ist der gleichbedeutende „Ecke“ als der kürzere meist vorgezogen.*",
        )
    ],
    ("compendio", 53): [
        (
            "Winterberg Footnotes 1–2 (Cap. LIII, p. 243): (1) Compare Chapter LXXI. (2) Namely, the 8 edges of the regular octagon lying in the same plane—a construction that can also be found by purely elementary geometry without the 'profound science' presupposed by the author.",
            "Winterberg Fussnoten 1–2 (Cap. LIII, S. 243): *1) cfr. Cap. LXXI. 2) scil. welche in derselben Ebene liegen, was übrigens auch ohne die vom Autor vorausgesetzten „tiefen Kenntnisse“ auf rein elementarem Wege zu finden ist.*",
        )
    ],
    ("compendio", 54): [
        (
            "Winterberg Footnotes 1–3 (Cap. LIV, pp. 244–245): (1) Namely, generated from the truncated hexahedron (cuboctahedron), so that the truncation operation is repeated twice on the ordinary cube. (2) Pacioli's remark on elevating the 72-base body requires modification, since the faces of the 72-base body are no longer equilateral polygons and therefore cannot support equilateral triangular pyramids of equal edge length. (3) Namely, the 72-faced body (*72-Flächner*).",
            "Winterberg Fussnoten 1–3 (Cap. LIV, S. 244–245): *1) scil. aus dem abgeschnittenen Hexaeder; die Operation des Abschneidens wiederholt sich also zweimal beim gewöhnlichen Kubus. 2) Dies scheint insofern wenigstens nicht zutreffend und einer Modification zu bedürfen, als die Längen der Seitenkanten ihrer Pyramiden nicht mehr den bisherigen Anforderungen entsprechen können, indem ihre Grundflächen selbst keine gleichseitigen Figuren sind. 3) scil. 72-Flächner.*",
        )
    ],
    ("compendio", 57): [
        (
            "Winterberg Footnote 1 (Cap. LVII, p. 249): Point $d$, which is missing in the 1509 woodcut diagram (Folio 0050, ``0050.g1.png``), must be conceived in the initial plane from which the rotation of the semicircle begins.",
            "Winterberg Fussnote 1 (Cap. LVII, S. 249): *Punkt d, welcher in der Zeichnung fehlt, muss in der Ebene gedacht werden, von wo die Drehung beginnt.*",
        )
    ],
    ("compendio", 59): [
        (
            "Winterberg Footnote 1 (Cap. LIX, p. 251): Compare the second marginal diagram on p. 106 (Paganini Folio 0051, ``0051.g2.png``).",
            "Winterberg Fussnote 1 (Cap. LIX, S. 251): *cfr. 2. Fig. pag. 106.*",
        )
    ],
    ("compendio", 60): [
        (
            "Winterberg Footnotes 1–2 (Cap. LX, p. 253): (1) Compare the marginal prism diagrams on p. 107 (Paganini Folio 0052, ``0052.g1.png``–``0052.g3.png``). (2) In the 1509 TOC (p. 168), *elmuhaym* and *elmuariffe* denote the rhombus and rhomboid/trapezium.",
            "Winterberg Fussnoten 1–2 (Cap. LX, S. 253, Inh. S. 168): *1) vgl. Fig. pag. 107. *) Rhombus und Rhomboide.*",
        )
    ],
    ("compendio", 61): [
        (
            "Winterberg Footnote 1 (Cap. LXI, p. 255): Rendering *simili* literally as 'similar' here would give a false sense; Pacioli means 'uniform / homogeneous' (*gleichartig*).",
            "Winterberg Fussnote 1 (Cap. LXI, S. 255): *simili = ähnlich, würde einen falschen Sinn geben.*",
        )
    ],
    ("compendio", 62): [
        (
            "Winterberg Footnotes 1–4 (Cap. LXII, pp. 256–257): (1) Namely, solid bodies (*scil. Körper*). (2) Compare the marginal figures on pp. 104 and 108 (Paganini Folios 0051–0053). (3) Compare the first figure on p. 110 (Paganini Folio 0053, ``0053.g2.png``). (4) Supply the missing verb 'proved' (*bewiesen*) in Pacioli's sentence on Archimedes's quadrature of the circle.",
            "Winterberg Fussnoten 1–4 (Cap. LXII, S. 256–257): *1) scil. Körper. 2) vgl. die Figuren pag. 104 und 108. 3) vgl. 1. Fig. pag. 110. 4) Das im Text fehlende Verbum „bewiesen“ zu ergänzen.*",
        )
    ],
    ("compendio", 63): [
        (
            "Winterberg Footnote 1 (Cap. LXIII, p. 258): Compare the second figure on p. 110 (Paganini Folio 0053, ``0053.g3.png``).",
            "Winterberg Fussnote 1 (Cap. LXIII, S. 258): *vgl. 2. Fig. pag. 110.*",
        )
    ],
    ("compendio", 64): [
        (
            "Winterberg Footnotes 1–2 (Cap. LXIV, p. 260): (1) The marginal cone diagram (Paganini Folio 0054, ``0054.g1.png``) is placed alongside for clarity. (2) Namely, directed (*gerichtet sein*) from the apex to the center of the circular base.",
            "Winterberg Fussnoten 1–2 (Cap. LXIV, S. 260): *1) Des Verständnisses wegen ist die nebenstehende Figur hinzugefügt. 2) D. h. gerichtet sein.*",
        )
    ],
    ("compendio", 65): [
        (
            "Winterberg Footnote 1 (Cap. LXV, p. 262): By *pyramide corta non equale*, Pacioli means a right frustum of a pyramid (*gerade abgestumpfte Pyramide*) whose top and bottom bases are unequal parallel similar polygons.",
            "Winterberg Fussnote 1 (Cap. LXV, S. 262): *Gerade Pyramide.*",
        )
    ],
    ("compendio", 66): [
        (
            "Winterberg Footnotes 1–2 (Cap. LXVI, p. 263): (1) That is, according to the numerical value of its volume (*dem Zahlenwerthe ihres Inhalts nach*), since $\\pi$ is irrational, even though geometrically the cone is exactly $\\frac{1}{3}$ of the cylinder (:just:`XII.10`). (2) Namely, given numerical data (*scil. Daten*).",
            "Winterberg Fussnoten 1–2 (Cap. LXVI, S. 263): *1) d. i. dem Zahlenwerthe ihres Inhalts nach. 2) scil. Daten.*",
        )
    ],
    ("compendio", 69): [
        (
            "Winterberg Footnote 1 (Cap. LXIX, p. 268): Namely, Your Ducal Highness (*scil. Hoheit*, Ludovico Maria Sforza).",
            "Winterberg Fussnote 1 (Cap. LXIX, S. 268): *scil. Hoheit.*",
        )
    ],
    ("compendio", 71): [
        (
            "Winterberg Footnote 1 (Cap. LXXI, p. 274): Namely, regular polyhedra (*scil. reguläre*).",
            "Winterberg Fussnote 1 (Cap. LXXI, S. 274): *scil. reguläre.*",
        )
    ],
    ("architectura", 0): [
        (
            "Winterberg Footnotes 1–2 (Arch. Prohemio, pp. 287, 289): (1) *San Rocco* (Saint Roch)—referring to the architectural works in Venice (Church / Scuola Grande di San Rocco) where Giovan Marco Canozi da Lendinara was active. (2) *By the King* (*dal Re*)—namely, King Ferrante I (Ferdinand I) of Naples, as is clear from the preceding sentence on the wars between the houses of Anjou and Aragon.",
            "Winterberg Fussnoten 1–2 (Arch. Widmung, S. 287, 289): *1) San Rocco. 2) Von Neapel, wie aus dem Vorigen hervorgeht.*",
        )
    ],
    ("architectura", 2): [
        (
            "Winterberg Footnote 1 (Arch. Cap. II, p. 299): By *quadro* here Pacioli means a right-angled *rectangle* (*Rechteck*), partitioned by parallel lines.",
            "Winterberg Fussnote 1 (Arch. Cap. II, S. 299): *Rechteck.*",
        )
    ],
    ("architectura", 3): [
        (
            "Winterberg Footnotes 1–5 (Arch. Cap. III, pp. 301–303): (1) Namely, equal to the distance from the chin to the base of the nostrils (*vom Kinn bis zum Nasenstachel*). (2) Namely, in breadth (*scil. Breite*). (3) The cubit (*cubito*)—from the elbow joint to the tip of the middle finger. (4) Square (*Quadrat*, $4^2 = 16$). (5) Biquadrate / fourth power (*Biquadrat*, $16^2 = 256$).",
            "Winterberg Fussnoten 1–5 (Arch. Cap. III, S. 301–303): *1) D. h. wie der Abstand vom Kinn bis zum Nasenstachel. 2) scil. Breite. 3) d. h. vom Ellbogengelenk bis zur Mittelfingerspitze. 4) Quadrat. 5) Biquadrat.*",
        )
    ],
    ("architectura", 5): [
        (
            "Winterberg Footnotes 1–3 (Arch. Cap. V, pp. 305–306): (1) Compare the column plate at the end of the treatise (Paganini Folio 0213, ``0213.g1.png``). (2) Instead of the nonsensical reading *'immedietate'* in the 1509 print, read *'immediate'* ('immediately'). (3) Compare Chapter LIX of the preceding treatise (*Compendio*) on the circular base and shaft.",
            "Winterberg Fussnoten 1–3 (Arch. Cap. V, S. 305–306): *1) Vgl. die betreffende Figur am Ende des Tractats. 2) Statt des keinen Sinn gebenden Ausdrucks „immedietate“ wohl „immediate“ zu lesen. 3) cfr. Cap. LIX des vorigen Tractats.*",
        )
    ],
    ("architectura", 6): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. VI, pp. 307–308): (1) Compare the *Porta Speciosa* and Column plates at the end of the treatise (Paganini Folios 0185 and 0213). (2) Namely, the geometric letters of the Roman Alphabet (*scil. die Buchstaben*) in Appendix I.",
            "Winterberg Fussnoten 1–2 (Arch. Cap. VI, S. 307–308): *1) Vgl. die betreffende Figur am Ende des Tractats. 2) scil. die Buchstaben.*",
        )
    ],
    ("architectura", 7): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. VII, pp. 309–310): (1) *Baladere* (*ballatoio*)—literally, the uppermost gallery or deck. (2) In the 1509 Italian text, read *poco* ('little') instead of *però*.",
            "Winterberg Fussnoten 1–2 (Arch. Cap. VII, S. 309–310): *1) Baladere eigentlich: oberstes Verdeck. 2) Text soll poco statt però heissen.*",
        )
    ],
    ("architectura", 8): [
        (
            "Winterberg Footnote 1 (Arch. Cap. VIII, p. 313): Namely, the monolithic twisted columns (*scil. Säulen*) in St. Peter's in Rome, said to have been brought from Solomon's Temple in Jerusalem.",
            "Winterberg Fussnote 1 (Arch. Cap. VIII, S. 313): *scil. Säulen.*",
        )
    ],
    ("architectura", 11): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. XI, p. 316): (1) Namely, the geometric figures in Euclid (*scil. die geometrischen Formen im Euklid*). (2) Read *rimasi* for the dialectal form *romase*.",
            "Winterberg Fussnoten 1–2 (Arch. Cap. XI, S. 316): *1) scil. die geometr. Formen im Euklid. 2) romase wohl rimasi.*",
        )
    ],
    ("architectura", 12): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. XII, p. 318): (1) Pacioli writes *tygraphi* for Vitruvius's *triglyphi* (triglyphs). (2) In the 1509 print, read *tecto* ('roof') instead of *lecto* ('bed').",
            "Winterberg Fussnoten 1–2 (Arch. Cap. XII, S. 318): *1) Tygraphen = Triglyphen. 2) Text l. tecto st. lecto.*",
        )
    ],
    ("architectura", 14): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. XIV, p. 324): (1) Compare the Entablature plate at the end of the treatise (Paganini Folio 0215, ``0215.g1.png``). (2) Where the 1509 print reads $\\frac{1}{3}$ for the bead-moulding $b$, Vitruvius III.5.10 gives $\\frac{1}{7}$ of the fascia (or $\\frac{1}{4}$ in Fra Giocondo's edition).",
            "Winterberg Fussnoten 1–2 (Arch. Cap. XIV, S. 324): *1) Vgl. die betr. Figur a. Ende des Tractats. 2) wohl 1/4.*",
        )
    ],
    ("architectura", 16): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. XVI, p. 328): (1) The repeated words *'e dali antichi'* in the 1509 print are a dittography to be deleted for sense. (2) Bead-and-reel (*Paternostri*) or olive-leaf moulding.",
            "Winterberg Fussnoten 1–2 (Arch. Cap. XVI, S. 328): *1) Die Worte des Textes: „e dali antichi“ des Sinnes wegen zu streichen. 2) Paternostri oder Olivenschmuck.*",
        )
    ],
    ("architectura", 17): [
        (
            "Winterberg Footnotes 1–2 (Arch. Cap. XVII, p. 330): (1) Compare the *Porta Speciosa* plate at the end of the treatise (Paganini Folio 0185, ``0185.g1.png``). (2) Compare Chapters XIV and XV on the epistyle and frieze.",
            "Winterberg Fussnoten 1–2 (Arch. Cap. XVII, S. 330): *1) Vgl. betr. Fig. a. Ende des Tractats. 2) cfr. Cap. XIV, XV.*",
        )
    ],
}


# Winterberg's critical footnotes on the Alphabet Plates (06_plates.txt)
WINTERBERG_ALPHABET_FOOTNOTES: Dict[str, Tuple[str, str]] = {
    "H": (
        "**Winterberg Note (1889, p. 358)**: In the 1509 Italian text (*'doue se intersecano li diametri del tondo suo quadro'*), read more precisely: *where the circumference (periphery) of the circle and the diagonals of its square intersect*.",
        "**Winterberg Anmerkung (1889, S. 358)**: *\\*) Soll heissen: wo Peripherie des Kreises und Diagonalen des Quadrats sich schneiden.*",
    ),
    "N": (
        "**Winterberg Note (1889, p. 359)**: By *'la mita de la gamba grossa cioè duna testa'* ('half the thick leg, namely one head'), Pacioli means $\\frac{1}{2} \\times \\frac{1}{9} = \\frac{1}{18}$ of the side of the square.",
        "**Winterberg Anmerkung (1889, S. 359)**: *\\*) D. h. 1/18 der Quadratseite.*",
    ),
    "S": (
        "**Winterberg Note (1889, p. 360)**: Although the text states that the letter **S** is drawn from *eight* circles (*'se caua de octo tondi'*), in the 1509 woodcut figure (Folio 0175, ``0175.g1.png``) only *six* construction circles are actually drawn.",
        "**Winterberg Anmerkung (1889, S. 360)**: *\\*) In der Figur sind deren nur sechs angegeben.*",
    ),
}


def get_winterberg_notes_for_chapter(part: str, cnum: int) -> str:
    """Return formatted RST block of Constantin Winterberg's 1889 mathematical commentary
    (*Sachliche Anmerkungen*) and textual footnotes for `(part, cnum)`, or empty string if none.
    """
    matched_anm = [
        a for a in WINTERBERG_ANMERKUNGEN if (part, cnum) in a["chapters"]
    ]
    matched_fn = WINTERBERG_CHAPTER_FOOTNOTES.get((part, cnum), [])

    if not matched_anm and not matched_fn:
        return ""

    lines: List[str] = [
        "",
        "Constantin Winterberg's Commentary (1889 Edition)",
        "-------------------------------------------------",
        "",
    ]

    for a in matched_anm:
        lines.append(
            f".. rubric:: {a['title_en']} (:ref:`Sachliche Anmerkungen #{a['num']} <plates-anmerkungen-en>`, {a['locus']})"
        )
        lines.append("")
        lines.append(a["text_en"])
        lines.append("")
        lines.append(f".. rubric:: {a['title_de']}")
        lines.append("")
        lines.append(a["text_de"])
        lines.append("")

    for fn_en, fn_de in matched_fn:
        lines.append(f"- {fn_en}")
        lines.append(f"  ({fn_de})")
        lines.append("")

    return "\n".join(lines)
