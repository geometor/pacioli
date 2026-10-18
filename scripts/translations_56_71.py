"""Complete, unabridged scholarly English translations and Critical Commentary
for Part I: Compendio de Divina Proportione, Section 4 (Chapters LVI–LXXI):
The Sphere, Oblong Bodies (Columns and Pyramids), Mensuration, Leonardo's Plates,
Courtly Panegyric, and the Mathematical Glossary (Plates XLI–LIX).
"""

from typing import Dict

CHAPTERS_56_TO_71: Dict[int, Dict[str, str]] = {
    56: {
        "title_en": "On the Spherical Body and How It Is Formed (Plates XLI–XLII).",
        "body_en": """.. enunciation:: Definition and Generation of the Sphere (:just:`XI.Def.14`)

   The sphere is a solid figure described by the revolution of a semicircle when its diameter remains fixed and the semicircle is turned completely around until it returns to the place from which it began to move; and the center of the sphere is the same as the center of the semicircle (:just:`XI.Def.14`).

The sphere has been defined in various ways by many authors—above all by the worthy mathematician **Dionysius** (and Theodosius in his *Sphaerica*, who defines it as a solid body bounded by a single surface, within which there is a point from which all straight lines drawn to the surface are equal). Yet our author **Euclid**, with supreme brevity, describes its genetic formation in the :just:`eleventh book <XI.Def.14>` in a definition adopted by all posterity (and depicted in perspective in :ref:`Plate XLI (Sperico Solido) and Plate XLII (Sperico Vacuo) <plates-polyhedra-en>`):

.. assertion:: Construction of the Sphere by Revolution (:just:`XI.Def.14`)

   1. Let :math:`adb` be a semicircle constructed upon any straight line :math:`ab` as diameter, with center :math:`c` and curved circumference :math:`adb` (see the marginal diagrams ``0049.g1.png`` and ``0049.g2.png`` on Folio 0049).
   2. Hold the diameter :math:`ab` fixed like an immovable axle (*axe*), and revolve the plane semicircle :math:`adb` completely around :math:`ab`—starting from point :math:`d`, descending through the lower half, and rising through the upper half (or conversely) until the arc :math:`adb` returns to the exact place from which it began to move.
   3. The round solid body traced out (*el vestigio*) by the plane semicircle in its complete revolution is called a **spherical body** or **sphere** (*corpo sperico / spera*), and its center is the same point :math:`c` which was the center of the semicircle.
   4. And to grasp this properly in the imagination, conceive of the semicircle as a flat material half-trencher (*vn mezzo taglieri materiale*): for if only the curved line of the arc revolved without the plane surface inside it, it would leave only a hollow shell without solid body, since a line has neither breadth nor depth (:just:`I.Def.2`).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XLI** (``0273.rst``): *Sperico Solido* (Solid Sphere, labeled ``XL`` in the marginal roman numeral on Folio 0049).
  - **Plate XLII** (``0275.rst``): *Sperico Vacuo* (Hollow/Armillary Sphere with meridian and parallel ribs).
- **Euclid's Genetic Definition (:just:`XI.Def.14`) vs. Theodosius's Locus Definition**: Pacioli contrasts the static locus definition of the sphere (attributed in medieval Latin manuals to *Dionysius* or *Theodosius*, *Sphaerica* I.Def.1) with Euclid's kinematic definition (:just:`XI.Def.14`) by the revolution of a semicircle around its fixed diameter—the exact kinematic method Euclid uses throughout Books XI–XIII to circumscribe a sphere around each of the five Platonic solids.""",
    },
    57: {
        "title_en": "How All Five Regular Bodies Are Placed in the Sphere, How Stonemasons May Carve Them from a Spherical Stone, and the Anecdote of Count Girolamo Riario and Melozzo da Forlì in Rome.",
        "body_en": """In this sphere, most lofty Duke, all five regular bodies are imagined and carved in the following manner—an explanation that will also show how a stonemason (*lapicida* or *scarpellino*) can fashion any of the five regular bodies out of a spherical stone cannonball (*vna pietra de bombarda / balotta*):

.. rubric:: 1. Carving the Five Regular Solids from a Spherical Cannonball

1. **The Tetracedron (4 Points, 6 Edges, 4 Triangular Faces)**:
   If upon the spherical surface (*spoglia* or *veste*) of the sphere one marks **4 points** equidistant from one another in every direction and joins them by **6 straight lines** passing inside the sphere, the regular **tetracedron** is formed within it. And if a stonemason takes a spherical stone cannonball (*pietra de bombarda*) marked with those 4 equidistant points and chisels away (*stempiasse ouer sfaciasse*) the four spherical caps with his iron tools along the flat planes passing through those 6 straight lines, leaving the 4 points intact, he will have reduced the spherical stone to a naked **tetracedron**.
2. **The Exacedron or Cube (8 Points, 12 Edges, 6 Square Faces)**:
   Similarly, if **8 equidistant points** are marked upon the spherical surface and joined by **12 straight lines**, there is placed in the sphere the second regular body, called the **exacedron** or **cube**—the figure of that diabolical instrument called the gaming die (*el diabolico instrumento dicto taxillo*)! And a stonemason chiseling flat along those six planes will reduce the round cannonball to cubic form.
3. **The Octocedron (6 Points, 12 Edges, 8 Triangular Faces)**:
   If **6 equidistant points** are marked upon the sphere and joined by **12 straight lines**, the third regular body, the **octocedron** of 8 triangular bases, is formed; and the stonemason chiseling along those planes will make from the cannonball the body of 8 equilateral triangles.
4. **The Ycocedron (12 Points, 30 Edges, 20 Triangular Faces)**:
   If **12 equidistant points** are marked upon the sphere and joined by **30 straight lines**, the fourth regular body, the **ycocedron** of 20 triangular bases, is formed in the sphere and carved from the stone.
5. **The Duodecedron (20 Points, 30 Edges, 12 Pentagonal Faces)**:
   Finally, if **20 equidistant points** are marked upon the sphere and joined by **30 straight lines**, the fifth and noblest regular body, the **duodecedron** of 12 pentagonal bases, is formed in the sphere and carved from the round stone.

And in every one of these five bodies, when it is placed in the sphere, if **one** of its solid angles touches the spherical surface, **all** its solid angles necessarily touch the sphere at the same time; nor is it ever possible for one vertex to touch without all the others touching.

.. rubric:: 2. How to Expose Boastful Artisans, and the Anecdote of Count Girolamo Riario and Melozzo da Forlì in Rome

By means of this infallible science (:ref:`Chapter XXV <compendio-cap_25-en>`), Your Ducal Highness may at times amuse yourself—as we ourselves have often done—by exposing the ignorance of boastful stonemasons (*lapicidi*) and rash braggarts (*temerarii milantatori*) who promise "Rome and Toma, seas and mountains" (*Roma e toma, maria e montes*), neither knowing geometry nor caring to learn it, against the moral precept:

   *Ne pudeat quae nescieris te velle doceri* ("Be not ashamed to wish to be taught what you do not know").

Simply command them to carve from such a stone a capital, base, or frieze block bounded by equal faces, equal sides, and equal solid angles, **but which is none of the five regular forms**—for instance:
- A regular body of **4 equal faces** that are **not** triangles; or
- A regular body of **6 equal faces** that are **not** squares (say triangles or pentagons); or
- A regular body of **8** or **20 equal faces** that are **not** triangles; or
- A regular body of **12 equal faces** that are **not** pentagons!
All of which are **absolutely impossible in nature**, as we proved demonstratively in :ref:`Chapter XXV <compendio-cap_25-en>`.

Such ignorant artisans are like:
- The carpenter (*carpentieri*) who, when asked what he would do if he had no plane (*pialla*), replied that he would plane a block of wood into a plane using another plane!
- Or the other joiner (*marangone*) who declared that his large try-square (*squadra*) was "too large" to test a small square, imagining that right angles vary in size according to the length of their legs (contra :just:`I.Post.4`: *All right angles are equal to one another*)!
- Or the simpleton who, placing two equal little rods in the form of a **Tau** (:math:`\\mathbf{T}`) before his eyes, judged first the vertical stem and then the horizontal crossbar to be the longer!

Just such an incident actually occurred in Rome at the time of the building of the palace of **Count Girolamo Riario** (*Conte Girolamo*, nephew of Pope Sixtus IV, today the Palazzo Altemps) of blessed memory. While we were conversing in the Count's presence and inspecting the building works along with many worthy men of diverse faculties in his retinue—among them the renowned painter **Melozzo da Forlì** (*Melozzo da Furlì*)—in order to give pleasure to speculation, Melozzo and I urged the Count to commission a certain capital in one of those impossible forms, without revealing the geometric impossibility to the Count, saying only that it would be a most worthy piece.

The Count agreed, summoned his chief master stonemason—and at that time the Roman stonemasons were famous—and asked him whether he knew how to carve it. The mason replied that this was a trifling matter (*piccola facenda*) and that he had made such pieces many times before! Whereupon the Count began to doubt whether the form was really as rare and worthy as we had praised it to be. Melozzo and I stood firm, openly declaring that the mason would **never** make it because of the geometric impossibility proved above.

Recalling the stonemason, the Count asked him again if he would truly make it. Laughing scornfully, the mason offered to wager upon it (*al sì e al non sempre fia pronto lo impegnare*). The Count asked: *"If you fail to make it, what are you willing to forfeit?"* The mason cleverly replied: *"My Lord, whatever more Your Most Illustrious Lordship pleases beyond what I stand to earn!"* They agreed on a term of twenty days, though the mason boasted he needed only four.

In the end, after spoiling many fine blocks of marble and cutting one bungled piece after another, he could never make the faces and angles meet! The Count graciously held him liable only for the cost of the ruined marble, and the mason was left thoroughly shamed (*scornato*). Yet he never rested until he learned who had proposed the problem; and discovering that it was the Friar (*el frate*, namely myself!), he bore me no small grudge until he found me and said: *"Messer, Messer, I will never forgive you the injury you did me unless you teach me the reason and the way of these bodies!"* I gladly offered him whatever skill I possessed, and during several days in Rome I was not ungenerous to him, opening to him the secrets of these and other geometric matters pertaining to his art; and that courteous master insisted on having a fine friar's cloak (*vna degna cappa*) made for me in his name!

Thus Your Highness sees how great lords can cure presumptuous artisans of their boasting—just as **King Hiero of Syracuse** did with the poet **Simonides**, as **Cicero** recounts in *De natura deorum* (I.22.60): when Hiero asked Simonides what God was, Simonides rashly asked for a single day to state the exact definition; after one day he asked for two, then four, and after many extensions finally confessed that the more he pondered it, the less he understood, remaining confounded in his initial rashness.""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Count Girolamo Riario, Melozzo da Forlì, and Pacioli in Rome (c. 1477–1480 or 1484–1488)**: This vivid autobiographical narrative is one of the richest historical documents of Renaissance workshop culture:
  - **Count Girolamo Riario** (1443–1488), Lord of Imola and Forlì and Captain General of the Church under his uncle Pope Sixtus IV, began constructing his Roman palace near Sant'Apollinare (incorporated into **Palazzo Altemps**) in the late 1470s / early 1480s.
  - **Melozzo da Forlì** (1438–1494), the celebrated *pictor papalis* and master of *sotto in su* perspective (who also came from Riario's city of Forlì and knew Piero della Francesca), joined Pacioli in setting the geometric trap for Riario's boastful master stonemason.
- **The Tau (:math:`\\mathbf{T}`) Optical Illusion**: Pacioli's remark on the two equal rods placed in the shape of a ``T`` (*doi verghette equali in forma de tau, cioè così T, inanze ali occhi suoi, ora vna ora l'altra più longa giudicaua*, Folio 0050–0051) is the **earliest documented scientific description of the Vertical-Horizontal (T) Optical Illusion** in Western history (nearly four centuries before Fick, 1851, and Oppel, 1855)!
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2/57.txt`` draft cut out the entire second half of this chapter—omitting the three carpenter jokes, the Tau optical illusion, the entire story of Count Girolamo Riario, Melozzo da Forlì, and the Roman stonemason's wager and gift of a cloak, and Cicero's story of Hiero and Simonides! Here the complete text of Folios ``0050.rst``–``0051.rst`` (``f. 17v``–``f. 18r``) is translated in full.""",
    },
    58: {
        "title_en": "On Oblong Bodies, That Is, Bodies Longer or Higher Than They Are Wide: And First on the Round Column (Cylinder, Plates XLIII–XLIV).",
        "body_en": """It now follows in order, most lofty Duke, for the complete understanding of this treatise, to say something concerning **oblong bodies** (*corpi oblonghi*)—that is, bodies that are longer or higher than they are wide, such as **columns** (*colonne*, cylinders and prisms) and their **pyramids** (*pyramidi*, cones and pyramids), of which many species are found. First we shall treat of columns and their origin, and then of their pyramids.

Columns are of **two kinds**: **round** (*rotonde*, cylinders) and **lateral/faceted** (*laterate*, prisms), just as plane figures are divided into **curvilinear** (bounded by curved lines) and **rectilinear** (bounded by straight lines).

.. enunciation:: Definition and Generation of the Round Column (Cylinder, :just:`XI.Def.21`)

   The round column (*colonna rotonda*, cylinder) is a solid body contained between two equal and parallel circular bases, described by the revolution of a right-angled parallelogram when one of its sides containing the right angle remains fixed as the axis and the parallelogram is turned completely around until it returns to the place from which it began to move (:just:`XI.Def.21`). And the round column, the sphere, and the circle that have the same diameter all share one and the same center.

.. assertion:: Proof that the Cylinder, Sphere, and Circle Share the Same Center (:just:`XI.Def.21`, :just:`I.15`, :just:`I.26`, :just:`III.31`)

   1. Let :math:`abcd` be a right-angled parallelogram (rectangle), and hold its vertical side :math:`ab` fixed while revolving the rectangle :math:`abcd` completely around :math:`ab` until it returns to its starting position (see the marginal diagram ``0052.g1.png`` on Folio 0052, and :ref:`Plates XLIII–XLIV <plates-polyhedra-en>`).
   2. The solid figure traced out by the revolution of :math:`abcd` is the **round column** (cylinder). Its fixed side :math:`ab` is the **axis** (*l'axe*) of the column; the horizontal sides :math:`bc` and :math:`ad` sweep out the two parallel **circular bases** with centers :math:`b` and :math:`a`; and the outer side :math:`cd` sweeps out the curved cylindrical surface.
   3. Now consider the rectangle :math:`abcd` at the moment when its revolution brings it to the opposite side :math:`abef` in the same plane, so that the two halves together form a single axial cross-section rectangle :math:`dcef`.
   4. Draw the diagonal :math:`de` across the axial rectangle :math:`dcef`, cutting the axis :math:`ab` at point :math:`g`. We say that :math:`de` is the **diameter of the column**, and that :math:`g` is the **common center** of the column, of the circle described on diameter :math:`de`, and of the sphere circumscribing the column!
   5. **Proof**:
      - In the two triangles :math:`agd` and :math:`bgc` (or :math:`bge`), the vertical angles at :math:`g` are equal by the :just:`fifteenth of the first <I.15>`; the angles at :math:`a` and :math:`b` are right angles by hypothesis; and the opposite radii :math:`ad` and :math:`be` (each equal to :math:`bc`) are equal.
      - Therefore, by the :just:`twenty-sixth of the first <I.26>`, the axis is bisected at :math:`g` (:math:`ag = gb`), and the diameter :math:`de` is also bisected at :math:`g` (:math:`dg = ge`).
      - Moreover, since the corner angles at :math:`c, d, e, f` of the rectangle :math:`dcef` are right angles, by the converse of the :just:`thirty-first of the third <III.31>` (*la trigesima del terzo* in Campanus), a circle described with center :math:`g` and radius :math:`gd = ge` passes through all four corners :math:`d, c, e, f`!
      - And as the rectangle revolves around the axis :math:`ab`, this circle sweeps out the **circumscribing sphere** of diameter :math:`de` centered at :math:`g`.

Therefore, a circle can be circumscribed around every right-angled parallelogram, and a **sphere can be circumscribed around every right round column**, all sharing the same center :math:`g`!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram & Plates**:
  - Folio 0052 (``f. 18v``) displays diagram ``0052.g1.png`` showing the axial rectangle :math:`dcef` of the cylinder with its axis :math:`ab` and diagonal :math:`de` intersecting at the center :math:`g`.
  - **Plate XLIII** (``0277.rst``) and **Plate XLIV** (``0279.rst``): Note that in the 1509 plates, Plates XLIII–XLIV show the round cone (*Cono Solido / Vacuo*) while the marginal text numerals shifted slightly between prisms and cones; ``Cap. LXX`` explains how to match the Roman numerals in the margins.
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2/58.txt`` draft omitted the entire Euclidean proof (:just:`I.15`, :just:`I.26`, :just:`III.31`) that the center :math:`g` bisects both the axis :math:`ab` and the diagonal :math:`de` so that every right cylinder is inscribable in a sphere.""",
    },
    59: {
        "title_en": "On Lateral (Faceted) Columns, and First on the Three-Sided (Triangular) Column, Called the Serratile Body (Plates XLV–XLVI).",
        "body_en": """Another species of columns is called **lateral** or **faceted** (*colonne laterate*, prisms), of which the first is the **three-sided** or **triangular column** (*colonna laterata trilatera*, :ref:`Plates XLV–XLVI <plates-polyhedra-en>`):

.. assertion:: Structure of the Triangular Column (*Corpo Seratile*)

   1. Its two opposite bases—the upper (*suprema*) :math:`abc` and the lower (*inferiore*) :math:`def`—are **two equal and parallel triangles** separated by the height (altitude) of the column (see the marginal diagram ``0053.g1.png`` on Folio 0053).
   2. Our author **Euclid** (in Campanus Book XI/XII) calls this triangular prism the **serratile body** (*corpo seratile*, from *serra*, a saw, because it is formed by sawing a parallelepiped diagonally in half!).
   3. Visually, when laid horizontally, it resembles the pitched ridge of a house roof (*el colmo de vn tecto de vna casa*) that slopes down on two sides with two triangular gables at the ends.
   4. Its two triangular bases may be either **equilateral** or **non-equilateral** (isosceles or scalene), while its **three lateral faces** joining the bases are always **right-angled parallelograms** (rectangles).
   5. Thus every triangular column (*corpo seratile*) is bounded by **5 plane surfaces** in all: **3 quadrangular** (rectangular) lateral faces and **2 triangular** bases, with **6 solid angles** and **9 edges**.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XLV** (``0281.rst``, *Laterato Solido* / Triangular Prism, solid) and **Plate XLVI** (``0283.rst``, *Laterato Vacuo* / Triangular Prism, skeletal).
- **Etymology of *Corpo Seratile***: In the medieval Gerard of Cremona and Campanus translations of Euclid Books XI–XII, a triangular prism (:g:`prisma`) is rendered *corpus serratile* ("sawed body").""",
    },
    60: {
        "title_en": "On Four-Sided (Quadrilateral) Lateral Columns and the Five Species of Quadrilaterals (Plates XLVII–XLVIII).",
        "body_en": """The second species of lateral columns comprises the **four-sided** or **quadrilateral columns** (*colonne laterate quadrilatere*, :ref:`Plates XLVII–XLVIII <plates-polyhedra-en>`), which have two parallel quadrangular bases (upper and lower) surrounded by four rectangular or parallelogrammic lateral faces.

Because these columns vary according to the shape of their quadrangular bases, Your Highness must recall from the beginning of the :just:`first book of Euclid <I.Def.22>` (as preserved in the Arabic-Latin tradition of Campanus) that all rectilinear four-sided plane figures are divided into **four regular/parallelogrammic species** and a **fifth irregular class** (illustrated by the five marginal diagrams ``0053.g2.png`` and ``0054.g1.png``–``0054.g5.png``):

.. assertion:: The Five Species of Rectilinear Quadrilaterals (:just:`I.Def.22`)

   1. **Figure A — Quadrato (Square)**: Has all four sides equal and all four angles right angles (:g:`tetragonon`).
   2. **Figure B — Tetragono Longo (Oblong Rectangle)**: Has all four angles right angles, and opposite sides equal and parallel, but is longer than it is wide (:g:`heteromekes`).
   3. **Figure C — Elmuaym or Rombo (Rhombus)**: Has all four sides equal and opposite sides parallel, but its angles are **not** right angles (:g:`rhombos`).
   4. **Figure D — Simile al Elmuaym or Romboide (Rhomboid / Parallelogram)**: Has only opposite sides equal and parallel, and its angles are **not** right angles (:g:`rhomboeides`).
   5. **Figure E — Elmuariffe (Trapezia / Irregular Quadrilaterals)**: All other four-sided figures beyond the first four species—having neither all sides equal nor opposite sides both equal and parallel—are called *elmuariffe* in the Arabic-Latin geometry (that is, *irregulari* or trapezia, :g:`trapezia`).

According to all these variations of their bases, quadrilateral columns may be equilateral or inequilateral, rectangular or oblique; yet in every case their **altitude** (*altezza*) is understood as the **perpendicular distance** (*equidistantia*) between their upper and lower bases, and every such column is bounded by **6 quadrilateral surfaces** (2 bases and 4 lateral faces), **8 solid angles**, and **12 edges**.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Arabic-Latin Geometric Terminology (*Elmuaym* and *Elmuariffe*)**: In Adelard of Bath's, Gerard of Cremona's, and Campanus's Latin editions of Euclid :just:`I.Def.22`, the Arabic terms *al-mu'ayyan* (rhombus) and *al-munharif* (trapezium / irregular quadrilateral) were transliterated as *helmuaym*, *simile helmuaym* (rhomboid), and *helmuariphe* (*elmuariffe*). Pacioli preserves both the Greek/Italian terms (*rombo*, *romboide*, *irregulari*) and the Campanian Arabic-Latin terms (*elmuaym*, *elmuariffe*), illustrating each with lettered marginal woodcuts ``A, B, C, D, E`` on Folios 0053–0054.
- **Paganini 1509 Plates Referenced**:
  - **Plate XLVII** (``0285.rst``, Quadrilateral Prism, solid) and **Plate XLVIII** (``0287.rst``, Quadrilateral Prism, skeletal).""",
    },
    61: {
        "title_en": "On Five-Sided (Pentagonal) Lateral Columns and How the Species of Lateral Columns Proceed to Infinity (Plates XLIX–L).",
        "body_en": """In the third place among lateral columns stand the **five-sided** or **pentagonal columns** (*colonne laterate pentagone*, :ref:`Plates XLIX–L <plates-polyhedra-en>`, and marginal diagram ``0054.g6.png``):

.. assertion:: Properties of Pentagonal and General Polygonal Prisms (:just:`XIII.7`)

   1. A pentagonal column is bounded laterally by **5 rectangular faces** (*ciascuna tetragona ouer quadrilatera*) and closed at the top and bottom by **2 parallel pentagonal bases** (rectilinear figures of 5 sides and 5 angles—for in every rectilinear plane figure, the number of angles equals the number of sides).
   2. Like quadrilateral columns, pentagonal columns may be either **equilateral and equiangular** or **inequilateral**, depending on their pentagonal bases.
   3. **Geometric Caution on Pentagons (:just:`XIII.7`)**: Note well that a pentagon can have all five sides equal and even **two** angles equal without being equiangular! However, as we proved in :ref:`Chapter XXI <compendio-cap_21-en>` by the :just:`seventh of the thirteenth <XIII.7>`, **every equilateral pentagon that has three angles equal (either consecutive or non-consecutive) is necessarily equiangular**.
   4. **Infinite Progression of Lateral Columns**: Just as plane polygons increase in number of sides to infinity (triangles, quadrangles, pentagons, hexagons, heptagons, octagons, and so forth), so the species of lateral columns increase **to infinity** (*in infinito*).
   5. In every lateral column, the two bases (upper and lower) must be **similar and equal polygons** of the same number of sides (it could not have a triangle for one base and a quadrangle for the other!), while all the lateral faces are **rectangles**; and each column takes its name (*denominatione*) from its bases: *triangula* (3 lateral faces), *quadrangola* (4), *pentagona* (5), *exagona* (6), *et sic de singulis*.

All of these may be seen both in the material models suspended in public and in perspective drawing at their corresponding Roman numerals (:ref:`Plates XLIX–L <plates-polyhedra-en>`).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XLIX** (``0289.rst``, Pentagonal Prism, solid) and **Plate L** (``0291.rst``, Pentagonal Prism, skeletal).
- **Invocation of :just:`XIII.7`**: Pacioli deftly reminds the reader why in :ref:`Chapter XXI <compendio-cap_21-en>` (:just:`XIII.7`) he proved that an equilateral pentagon requires *three* equal angles to force equiangularity (since a non-regular equilateral pentagon—such as a house-shaped pentagon—can have five equal sides and two right angles without being regular).""",
    },
    62: {
        "title_en": "On the Way to Measure All Kinds of Columns, and First the Round Columns (Cylinders).",
        "body_en": """Having described the forms of all columns, it is now fitting to give Your Ducal Highness the general rule for **measuring their solid capacity or volume** (*massa corporea / capacita*)—which, although treated at full length in our great work (*Summa de Arithmetica*), we summarize here briefly, beginning with **round columns** (cylinders).

.. enunciation:: General Rule for the Volume of a Round Column (Cylinder)

   First find the area of one of its circular bases by squaring the diameter of the base and taking **eleven-fourteenths** (:math:`\\frac{11}{14}`) of that square, according to the close approximation discovered by the noble geometer **Archimedes** in his book *De quadratura circuli* (*On the Measurement of the Circle*). Then multiply the area of the circular base by the **altitude** (*altezza*) of the column; the final product is the solid volume (*massa corporea*) of the entire round column:

   .. math::

      \\text{Area}_{\\text{base}} \\approx \\frac{11}{14}\\,d^{2}, \\qquad \\text{Volume}_{\\text{cylinder}} = \\text{Area}_{\\text{base}} \\times h \\approx \\frac{11}{14}\\,d^{2}\\,h

.. assertion:: Worked Numerical Example and Geometric Explanation

   1. Let :math:`abcd` be a round column whose altitude :math:`ac = bd` is :math:`10` (*braccia*, *piedi*, *passi*, or *palmi*), and let the diameter of each circular base :math:`ab = cd` be :math:`7` (see the marginal diagrams ``0054.g7.png`` and ``0054.g8.png`` on Folio 0054).
   2. Multiply the diameter :math:`7` by itself:

      .. math::

         7 \\times 7 = 49

   3. Take **eleven-fourteenths** (:math:`\\frac{11}{14}`) of :math:`49`:

      .. math::

         \\frac{11}{14} \\times 49 = 38\\frac{1}{2}

      which is the plane area of the circular base.
   4. Multiply this base area :math:`38\\frac{1}{2}` by the altitude :math:`10` of the column:

      .. math::

         38\\frac{1}{2} \\times 10 = 385

   5. We say that the solid capacity (*capacita ouer aria corporale*) of the entire round column is **385 cubic units** (*385 quadrettini cubici*)—meaning that if the units are *braccia*, the column contains **385 little cubes** (*commo dadi*), each 1 *braccio* long, 1 *braccio* wide, and 1 *braccio* high (as shown in the marginal cube diagram ``0054.g7.png``).
   6. **Why Eleven-Fourteenths (:math:`\\frac{11}{14}`) Is Taken**: Because Archimedes demonstrated with great approximation (since the exact quadrature of the circle has not yet been found by any sage, though it varies by very little) that the ratio of the circle to the circumscribed square on its diameter (:math:`abcd` circumscribing the circle of diameter :math:`ef` with center :math:`g`, in diagram ``0054.g8.png``) is as **11 to 14** (:math:`\\frac{\\pi}{4} \\approx \\frac{11}{14}` where :math:`\\pi \\approx 3\\frac{1}{7} = \\frac{22}{7}`), while the four corner spandrels (*anguli*) left outside the circle inside the square :math:`abcd` take up the remaining **three-fourteenths** (:math:`\\frac{3}{14}`) of the square!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagrams**: Folio 0054 (``f. 19v``) includes the unit cube diagram ``0054.g7.png`` and the circle inscribed in the square :math:`abcd` with diameter :math:`ef` and center :math:`g` (``0054.g8.png``), visually showing why the circle occupies :math:`\\frac{11}{14}` of the circumscribed square and the four corner spandrels occupy :math:`\\frac{3}{14}`.
- **Archimedes' *Measurement of a Circle***: Proposition 3 of Archimedes' *Dimensio Circuli* proves :math:`3\\frac{10}{71} < \\pi < 3\\frac{1}{7}`, whence Proposition 2 states that the area of a circle to the square on its diameter is very nearly :math:`11 : 14`.""",
    },
    63: {
        "title_en": "On the Way to Know How to Measure All Lateral (Prismatic) Columns.",
        "body_en": """Having shown the rule for measuring round columns, we now give the general—and **exact**—rule for measuring all **lateral columns** (*colonne laterate*, prisms).

.. enunciation:: General Rule for the Volume of Any Lateral Column (Prism)

   In every lateral column, whatever be the number or shape of its lateral faces, first find the exact plane area (*quadratura*) of one of its polygonal bases, and multiply that base area by the perpendicular **altitude** (*altezza ouer lunghezza*) of the column. The final product is infallibly the exact solid volume (*massa corporale ouer capacita*) of the column:

   .. math::

      \\text{Volume}_{\\text{prism}} = \\text{Area}_{\\text{base}} \\times h

.. assertion:: Worked Numerical Example and General Application

   1. Let :math:`ab` be a square-based lateral column (*colonna laterata tetragona*) whose altitude is :math:`10` and whose square bases measure :math:`6` on each side.
   2. First square one of the bases by multiplying a side by itself:

      .. math::

         6 \\times 6 = 36

      which is the exact plane area of the square base.
   3. Multiply this base area :math:`36` by the altitude :math:`10` of the column:

      .. math::

         36 \\times 10 = 360

      Thus the column contains **360 cubic braccia** (or cubic feet).
   4. And if the bases are inequilateral or irregular quadrilaterals (*elmuariffe*), or if the column is **triangular** (3-sided), **pentagonal** (5-sided), **hexagonal** (6-sided), **heptagonal** (7-sided), *et sic de singulis*, first measure the polygonal base by the rules of triangles, pentagons, or hexagons set forth at length in our printed great work (*Summa de Arithmetica*, 1494—to which access is easy for everyone, since it has been printed in copious multitude and spread throughout the world!), and multiply that base area by the altitude of the column.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Reference to the Print Run of the *Summa* (1494)**: Notice Pacioli's proud remark on Folio 0054 (``f. 19v``) that his *Summa de Arithmetica, Geometria, Proportioni e Proportionalita* (printed at Venice by Paganino de' Paganini in November 1494) is easily accessible to all readers *"per la lor copiosa multitudine stampato e per l'universo ormai divulgata"* ("because of the copious multitude printed and now disseminated throughout the world").""",
    },
    64: {
        "title_en": "On Pyramids and All Their Differences, and First on the Round Pyramid (Cone, Plates XLIII–XLIV).",
        "body_en": """It now follows in order, most lofty Duke, to treat of **pyramids** and their varieties—first those called **round pyramids** (*pyramidi rotonde*, cones, :ref:`Plates XLIII–XLIV <plates-polyhedra-en>`), and then all the **lateral pyramids** (*pyramidi laterate*).

.. enunciation:: Definition and Three Species of the Round Pyramid (Cone, :just:`XI.Def.18`)

   With our philosopher in the :just:`eleventh book <XI.Def.18>`, we define the **round pyramid** (cone) as a solid figure traced out by the revolution of a **right-angled triangle** when one of its two sides containing the right angle remains fixed as the axis and the triangle is turned completely around until it returns to the place from which it began to move. Its fixed side is the **axis** (*l'axe*), its base swept out by the other leg is a **circle**, and it is called the **pyramid of the round column** (having the same base and altitude). Moreover, according to the ratio of the fixed leg to the revolving leg, there are **three species** of round pyramids (:just:`XI.Def.18`):

   1. **Right-Angled (*Rectangola*)**: When the fixed leg :math:`ab` is **equal** to the revolving leg :math:`bc` (:math:`ab = bc`).
   2. **Acute-Angled (*Acutiangola*)**: When the fixed leg :math:`ab` is **longer** than the revolving leg :math:`bc` (:math:`ab > bc`).
   3. **Obtuse-Angled (*Obtusiangola*)**: When the fixed leg :math:`ab` is **shorter** than the revolving leg :math:`bc` (:math:`ab < bc`).

.. assertion:: Proof of the Three Species at the Apex Angle (:just:`I.5`, :just:`I.19`, :just:`I.32`)

   Let :math:`abc` be the generating right triangle with right angle at :math:`b` (:math:`\\angle abc = 90^{\\circ}`), fixed vertical axis :math:`ab`, and revolving base leg :math:`bc`. When the revolving triangle reaches the opposite position :math:`abd` in the same plane, the two legs :math:`bc` and :math:`bd` form a single straight line :math:`bcd` (the diameter of the circular base), and the axial cross-section of the cone is the isosceles triangle :math:`acd` with apex angle :math:`\\angle cad = 2\\,\\angle cab`:

   1. **Case 1 (:math:`ab = bc`, Right-Angled Cone)**:
      In the right triangle :math:`abc`, since :math:`ab = bc`, by the :just:`fifth <I.5>` and :just:`thirty-second of the first <I.32>`, the acute angle :math:`\\angle cab` is **half a right angle** (:math:`45^{\\circ}`). Therefore the full apex angle :math:`\\angle cad = 2\\,\\angle cab` is **one right angle** (:math:`90^{\\circ}`), and the cone is called **right-angled** (*pyramide rectangola*).
   2. **Case 2 (:math:`ab > bc`, Acute-Angled Cone)**:
      If the axis :math:`ab` is longer than the radius :math:`bc`, then by the :just:`nineteenth <I.19>` and :just:`thirty-second of the first <I.32>` (since the greater side subtends the greater angle), :math:`\\angle cab < \\angle acb`, so :math:`\\angle cab` is **less than half a right angle** (:math:`< 45^{\\circ}`). Therefore the full apex angle :math:`\\angle cad = 2\\,\\angle cab` is **less than a right angle** (acute), and the cone is called **acute-angled** (*pyramide acutiangola*).
   3. **Case 3 (:math:`ab < bc`, Obtuse-Angled Cone)**:
      If the axis :math:`ab` is shorter than the radius :math:`bc`, then by :just:`I.19` and :just:`I.32`, :math:`\\angle cab > \\angle acb`, so :math:`\\angle cab` is **greater than half a right angle** (:math:`> 45^{\\circ}`). Therefore the full apex angle :math:`\\angle cad = 2\\,\\angle cab` is **greater than a right angle** (obtuse), and the cone is called **obtuse-angled** (*pyramide obtusiangola*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Archimedean & Apollonian Classification of Cones (:just:`XI.Def.18`)**: Before Apollonius of Perga generalized conic sections to slices of any circular cone, Menaechmus, Euclid, and Archimedes generated the three conic sections—the **parabola** (*section of a right-angled cone*), the **ellipse** (*section of an acute-angled cone*), and the **hyperbola** (*section of an obtuse-angled cone*)—by slicing the three species of cones defined in :just:`XI.Def.18` with a plane perpendicular to a generator! Pacioli gives the complete Euclidean proof via :just:`I.5`, :just:`I.19`, and :just:`I.32`.""",
    },
    65: {
        "title_en": "On Lateral (Polygonal) Pyramids and Their Varieties: Right, Oblique, and Truncated (Plates LI–LIX).",
        "body_en": """Just as lateral columns have infinitely many species according to the polygons of their bases, so **lateral pyramids** (*pyramidi laterate*, :ref:`Plates LI–LIX <plates-polyhedra-en>`) have infinitely many species derived from their corresponding lateral columns.

.. enunciation:: Definition and Derivation of Lateral Pyramids (:just:`XI.Def.12`)

   In the :just:`eleventh book <XI.Def.12>`, our philosopher defines the **lateral pyramid** as a solid figure contained by plane surfaces that rise from a single plane base to meet at a single opposite point overhead, called the **cone** or **apex** (*cono dela pyramide*).

.. assertion:: Properties and Classification of Lateral Pyramids

   1. **Triangular Lateral Faces**: In every lateral pyramid, all the lateral surfaces surrounding it (except the base itself) rise to meet at the single apex (*cono*) and are therefore **triangles**, whereas the base may be a triangle (as in Pyramid ``A`` with apex ``B`` in marginal diagram ``0055.g1.png``), a quadrangle (Pyramid ``D`` with apex ``E`` in ``0055.g2.png``), a pentagon (Pyramid ``F`` with apex ``G`` in ``0055.g3.png``), a hexagon, or any polygon whatever (see :ref:`Plates LI–LVI <plates-polyhedra-en>`).
   2. **Derivation from the Corresponding Column**: Every lateral pyramid is generated from its corresponding lateral column by fixing a single point in the upper base of the column and drawing straight lines from that point to all the vertices of the lower base: the resulting pyramid has as many triangular lateral faces as the base has sides, and shares the same name (*trigona/triangulare*, *quadrilatera*, *pentagona*, etc.) as its column.
   3. **Right (*Recta a Livello*) vs. Oblique/Declining (*Declinante ouer China*) Pyramids**:
      - It is not necessary that the apex point fixed in the upper plane lie directly over the exact **center** of the lower base: so long as straight lines are drawn from that apex to the corners of the base, a pyramid is formed.
      - When the apex lies directly over the center of the base (so that the axis falls at right angles to the base), it is called a **right or plumb pyramid** (*pyramide recta a livello*); when the apex leans to one side, it is called a **declining or oblique pyramid** (*declinante ouer china*).
   4. **Short or Truncated Pyramids (*Pyramidi Curte, Troncate, ouer Scapezze*)**:
      - Finally, there are pyramids that do not rise all the way to their apex (*cono*), having their top sliced off parallel to the base; these are called **short, truncated, or lopped pyramids** (*pyramidi curte, troncate, scapezze, ouer tagliate*), whether round (frustum of a cone, Figure ``A`` on Folio 0056) or lateral—such as the truncated triangular pyramid (Figure ``B``) and the truncated quadrangular pyramid (Figure ``C`` and :ref:`Plates LVII–LVIII (Piramide Tronca Solida / Vacua) <plates-polyhedra-en>`).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagrams & Plates**:
  - Folio 0055 (``f. 20r``) and Folio 0056 (``f. 20v``) contain 10 marginal woodcut diagrams (``0055.g1.png``–``0055.g3.png`` and ``0056.g1.png``–``0056.g7.png``) depicting the triangular, quadrangular, and pentagonal pyramids and their truncated frusta (*tronca tonda A*, *corta triangola B*, *tagliata quadrangola C*).
  - **Plates LI–LIX** (``0293.rst``–``0309.rst``) show Leonardo's full-page perspective drawings of the triangular, quadrangular, and pentagonal pyramids and the truncated pyramid.""",
    },
    66: {
        "title_en": "On the Way and Rule to Know How to Measure Every Complete Pyramid, Round or Lateral.",
        "body_en": """The true and exact measure of every complete pyramid (*pyramide integra*), whether **round** (cone) or **lateral** (polygonal pyramid), is obtained from the volume of its corresponding column in the following universal manner (:just:`XII.7` Corollary, :just:`XII.10`):

.. enunciation:: Universal Rule for the Volume of Any Complete Pyramid or Cone (:just:`XII.7`, :just:`XII.10`)

   First find the area of the base of the pyramid by the rules given above for round and lateral columns (:ref:`Chapters LXII–LXIII <compendio-cap_62-en>`), and multiply that base area by the perpendicular **altitude** (*axe / altezza*) of the pyramid; the product is the solid volume of the entire corresponding **column**. Then take **one-third** (:math:`\\frac{1}{3}`) of that column's volume; that third part is **infallibly and exactly** the solid volume (*quantità corporale*) of the pyramid:

   .. math::

      \\text{Volume}_{\\text{pyramid}} = \\frac{1}{3}\\,\\text{Volume}_{\\text{column}} = \\frac{1}{3}\\,\\text{Area}_{\\text{base}} \\times h

.. assertion:: Worked Example and Euclidean Justification (:just:`XII.10` [Campanus XII.9], :just:`XII.7` [Campanus XII.8])

   1. Let :math:`abc` be a round pyramid (cone) whose circular base :math:`bc` has diameter :math:`7` and whose perpendicular altitude (axis) :math:`ad` is :math:`10` (see the marginal diagram ``0057.g1.png``).
   2. As we found in :ref:`Chapter LXII <compendio-cap_62-en>` for the round column of diameter :math:`7` and altitude :math:`10`, the area of the circular base is :math:`\\frac{11}{14} \\times 49 = 38\\frac{1}{2}`, and multiplying by the altitude :math:`10` gives :math:`385` for the volume of the entire round column.
   3. Taking **one-third** (:math:`\\frac{1}{3}`) of :math:`385` gives:

      .. math::

         \\frac{385}{3} = 128\\frac{1}{3}

      which is the solid volume of the round pyramid!
   4. **Distinction Between the Approximation of the Circle and the Exactness of the One-Third Ratio**:
      Note well, most lofty Duke, that although in the round pyramid the numerical area of the circular base uses Archimedes' close ratio of :math:`11` to :math:`14` (because the exact quadrature of the circle is not yet known in numbers), nevertheless **the geometric ratio of the round pyramid to its round column is not an approximation at all, but is with absolute mathematical precision one-third (:math:`\\frac{1}{3}`)**! For in the :just:`tenth of the twelfth <XII.10>` (the ninth of the twelfth in Campanus), our philosopher proves demonstratively that **every round column (cylinder) is triple (:math:`3 : 1`) its round pyramid (cone)** having the same base and equal altitude.
   5. And in all **lateral pyramids**, because their bases are rectilinear polygons whose areas can be expressed without circular quadrature, both the base area and the volume are exact, and by the :just:`seventh of the twelfth <XII.7>` (and the eighth of the twelfth in Campanus), **every lateral column is exactly triple (:math:`3 : 1`) its lateral pyramid**.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Epistemological Clarity on :math:`\\pi \\approx \\frac{22}{7}` vs. :math:`V_{\\text{cone}} = \\frac{1}{3}V_{\\text{cylinder}}`**: Pacioli makes a remarkably sharp mathematical distinction on Folio 0056 (``f. 20v``): while the *numerical* area of the circular base (:math:`\\frac{11}{14}d^{2}`) is an Archimedean approximation (*per la ignorantia dela quadratura del cerchio*), the *proportional* theorem that the cone is **exactly one-third** (:math:`\\frac{1}{3}`) of the cylinder (:just:`XII.10`, proved by Eudoxus's method of exhaustion) is **exact without the slightest error**!""",
    },
    67: {
        "title_en": "How It Is Manifestly Demonstrated That Every Lateral Pyramid Is One-Third (*Subtripla*) of Its Column, and Why Every Polygon of N Sides Resolves into N − 2 Triangles.",
        "body_en": """To make clear to the eye why every lateral pyramid is **one-third** (*subtripla*) of its corresponding lateral column, we set forth the demonstration from the :just:`seventh of the twelfth book <XII.7>` (the sixth and eighth of the twelfth in Campanus) and the :just:`thirty-second of the first book <I.32>`:

.. enunciation:: Resolution of Every Prism into Triangular Prisms (*Corpi Seratili*) and Triangulation of Polygons (:just:`XII.7`, :just:`I.32`)

   1. Every three-sided column (*corpo seratile*) is divisible into **three equal triangular pyramids**, and is therefore **triple** (:math:`3 : 1`) each of them (:just:`XII.7`, Campanus XII.6).
   2. Every :math:`n`-sided polygon is resolvable into :math:`n - 2` triangles by drawing diagonals from one vertex to the non-adjacent vertices (:just:`I.32` Corollary), and therefore every :math:`n`-sided lateral column is resolvable into :math:`n - 2` triangular columns (*corpi seratili*), each of which is triple its pyramid; hence the whole lateral column is **triple** (:math:`3 : 1`) the whole lateral pyramid!

.. assertion:: Proof and General Polygon Triangulation Rule (:just:`XII.7`, :just:`I.32`)

   1. **The Triangular Column (*Corpo Seratile*)**: In the :just:`sixth of the twelfth <XII.7>` (Campanus numbering), our philosopher proves that a triangular prism (*corpo seratile*) is divided by two diagonal plane cuts into **three equal triangular pyramids** having triangular bases, so that the *corpo seratile* is **triple** (:math:`3 : 1`) its pyramid.
   2. **The Quadrilateral Column**: Take any four-sided column. Since its base :math:`abcd` is a quadrilateral (4 angles and 4 sides), drawing a single diagonal :math:`bd` from one corner to the opposite corner (see the marginal diagram ``0057.g1.png`` on Folio 0057) resolves the quadrilateral base :math:`abcd` into **two triangles** :math:`abd` and :math:`bcd`. Passing a vertical plane through the diagonal :math:`bd` resolves the entire quadrilateral column into **two triangular columns (*doi corpi seratili*)**, and resolves its quadrilateral pyramid into **two triangular pyramids**. Since each *corpo seratile* is triple its triangular pyramid, both *corpi seratili* together (the whole quadrilateral column) are **triple** both triangular pyramids together (the whole quadrilateral pyramid)!
   3. **The Pentagonal Column**: Take any five-sided column, whose base is the pentagon :math:`abcde` (see the marginal diagram ``0057.g2.png`` on Folio 0057). From a single vertex :math:`a`, draw the two pentagonal chords (*corde pentagoniche*) :math:`ac` and :math:`ad` to the two opposite vertices :math:`c` and :math:`d`. This resolves the pentagon :math:`abcde` into **three triangles** :math:`abc`, :math:`acd`, and :math:`ade`, and resolves the pentagonal column into **three triangular columns (*tre corpi seratili*)**, each triple its pyramid; hence all three together (the whole pentagonal column) are **triple** all three pyramids together (the whole pentagonal pyramid)!
   4. **Universal Law of Polygon Triangulation (:just:`I.32` Scholium)**:
      In general, as demonstrated upon the :just:`thirty-second of the first <I.32>`, **every polygonal figure of :math:`n` angles (and :math:`n` sides) is minimally resolved into :math:`n - 2` triangles** (*in tanti triangoli quanti sonno li suoi angoli ouer lati men doi*):
      - A **quadrilateral** (4 sides) resolves into :math:`4 - 2 =` **2 triangles**;
      - A **pentagon** (5 sides) resolves into :math:`5 - 2 =` **3 triangles**;
      - A **hexagon** (6 sides) resolves into :math:`6 - 2 =` **4 triangles**;
      *et sic in reliquis*.

.. rubric:: Praise of Euclid of Megara and Book X of the *Elements*

How deeply obligated we are, most lofty Duke, to the Ancients who by their long nightly vigils illuminated our minds—and above all to our **Euclid of Megara** (*al nostro Megarense Euclide*), who in an orderly chain gathered the discoveries of his predecessors and added his own with such diligent demonstrations throughout his sublime volume! Truly his intellect shows itself **not human, but divine** (*non humano ma divino*)—most especially in his **tenth book** (*nel suo decimo*), where he exalted human reason as high as is permitted to mortal man; nor can I comprehend how anyone could have spoken more sublimely of those most abstract **irrational lines** (*linee abstractissime irrationali*), whose science is the deepest above all others in the judgment of those who know best!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagrams**: Folio 0057 (``f. 21r``) displays two woodcut diagrams (``0057.g1.png`` and ``0057.g2.png``) showing the quadrilateral :math:`abcd` divided by diagonal :math:`bd` into 2 triangles (:math:`\\triangle abd, \\triangle bcd`) and the pentagon :math:`abcde` divided from vertex :math:`a` by chords :math:`ac, ad` into 3 triangles (:math:`\\triangle abc, \\triangle acd, \\triangle ade`).
- **Additivity of Ratios (:just:`V.12`)**: Notice how Pacioli uses :just:`V.12` (if :math:`A_1 : B_1 = A_2 : B_2 = A_3 : B_3 = 3 : 1`, then :math:`(A_1+A_2+A_3) : (B_1+B_2+B_3) = 3 : 1`) to extend the :math:`3:1` prism-to-pyramid volume theorem from the triangular prism (*corpo seratile*, :just:`XII.7`) to any :math:`n`-gonal prism decomposed into :math:`n-2` triangular prisms.""",
    },
    68: {
        "title_en": "How Short or Truncated Pyramids (*Pyramidi Corte ouer Scapezze*) Are Measured.",
        "body_en": """For **short, lopped, or truncated pyramids** (*pyramidi corte, scapezze, ouer troncate*, whether round frusta of cones or lateral frusta of pyramids, :ref:`Plates LVII–LVIII <plates-polyhedra-en>`), their solid measure is found by means of their **complete pyramids**, reducing the imperfect to its perfect whole in the following manner:

.. enunciation:: Rule for Measuring Any Truncated Pyramid or Cone (Frustum)

   1. First **complete the truncated pyramid to its full apex (*cono*)** by the proportional rule given in our published great work (*Summa de Arithmetica*: using the ratio of a side or diameter of the lower base :math:`B_1` to the corresponding side or diameter of the parallel upper cut :math:`B_2` and the height :math:`h_{\\text{frustum}}` of the frustum to find the height :math:`h_{\\text{top}} = \\frac{s_2}{s_1 - s_2}\\,h_{\\text{frustum}}` of the missing top pyramid, and hence the total height :math:`h_{\\text{total}} = h_{\\text{frustum}} + h_{\\text{top}}` of the completed pyramid).
   2. Second, **measure the entire completed pyramid** (base :math:`B_1` and total height :math:`h_{\\text{total}}`) by the rule of :ref:`Chapter LXVI <compendio-cap_66-en>` (:math:`V_{\\text{total}} = \\frac{1}{3}B_1\\,h_{\\text{total}}`), and set that total volume aside.
   3. Third, **measure the small upper pyramid (*pyramidella*)** that was added to the top to make it complete (base :math:`B_2` and height :math:`h_{\\text{top}}`, giving :math:`V_{\\text{top}} = \\frac{1}{3}B_2\\,h_{\\text{top}}`).
   4. Finally, **subtract the volume of the small added pyramid (*pyramidella*) from the volume of the entire completed pyramid**:

      .. math::

         \\text{Volume}_{\\text{truncated}} = V_{\\text{total}} - V_{\\text{top}} = \\frac{1}{3}\\,B_{1}\\,h_{\\text{total}} - \\frac{1}{3}\\,B_{2}\\,h_{\\text{top}}

      The remainder is necessarily the exact solid volume of the truncated pyramid! Among all the methods given by geometers, this way is the shortest and most secure, and holds equally for round and lateral truncated pyramids.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Subtraction of the *Pyramidella* vs. Heron's Mean-Base Formula**: In the *Summa de Arithmetica* (Part II, *Tractatus Geometriae*, Dist. VI), Pacioli gives both this geometric completion-and-subtraction method (:math:`V = \\frac{1}{3}B_1 h_{\\text{total}} - \\frac{1}{3}B_2 h_{\\text{top}}`) and the equivalent algebraic formula :math:`V = \\frac{1}{3}h(B_1 + \\sqrt{B_1 B_2} + B_2)`. Notice how the completion-and-subtraction method prepares the exact conceptual model for measuring **truncated (*abscisi*) polyhedra** in the very next chapter (``Cap. LXIX``)!""",
    },
    69: {
        "title_en": "On the Measure of All the Regular and Dependent Bodies, and the Panegyric to Duke Ludovico Maria Sforza and the 1498 Franciscan General Chapter in Milan.",
        "body_en": """It now follows to speak of the mensuration (*dimensione*) of the **five regular bodies** and of **all their dependent bodies** (*abscisi* and *elevati*).

.. rubric:: 1. Measuring the Five Regular Solids and Their Truncated (*Abscisi*) and Elevated (*Elevati*) Dependents

- **The Five Regular Bodies**: Concerning the five regular bodies themselves, I need not expand further here, because I already composed a dedicated treatise on their exact surface and solid measures for Your Ducal Highness's most illustrious kinsman, **Guidobaldo da Montefeltro, Duke of Urbino** (*Guido Ubaldo Duca de Urbino*), included in our printed great work (*Summa de Arithmetica*, 1494) dedicated to His Lordship—of which many copies are found here in your renowned city of Milan. Truly their mensuration is as speculative and sublime as those bodies are more excellent and perfect than all others: a matter for the tragic buskin (*materia certamente da coturno e non da sciocco*), not for a fool!
- **The Truncated Dependent Bodies (*Corpi Abscisi*)**: The method for measuring all the **truncated** dependent bodies is identical to that just given in :ref:`Chapter LXVIII <compendio-cap_68-en>` for truncated pyramids:
  1. First **restore the truncated body to its complete, perfect regular parent body** (*redurli ali suoi totali perfecti*), and measure the volume of that complete regular body by the rules given in our treatise.
  2. Next, **measure the corner pyramids (*pyramidelle*)** that were sliced off from the vertices of the regular parent body to produce the truncated body. Because all the vertices of a regular body are equal and uniform, all these sliced-off *pyramidelle* are equal to one another: thus, as soon as **one** corner *pyramidella* is measured by the rules of pyramids (:ref:`Chapter LXVI <compendio-cap_66-en>`), multiplying it by the number of vertices of the regular parent body (4 in the *tetracedron absciso*, 8 in the *cubo absciso*, 6 in the *octocedron absciso*, 12 in the *ycocedron absciso*, 20 in the *duodecedron absciso*) gives the total volume of all the missing corner pyramids.
  3. **Subtract** the sum of those corner *pyramidelle* from the volume of the complete regular parent body; the remainder is the **exact solid volume of the truncated body** (*absciso*):

     .. math::

        \\text{Volume}_{\\text{absciso}} = \\text{Volume}_{\\text{regular}} - N_{\\text{vertices}} \\times \\text{Volume}_{\\text{corner pyramidella}}

- **The Elevated Dependent Bodies (*Corpi Elevati*)**: Conversely, if the dependent body belongs to the class of the **elevated** (*elevati*) bodies (formed by erecting pyramids upon the faces of a core body):
  1. First measure the **core perfect body** (*el suo perfecto*).
  2. Next measure **one** of the equal **elevated pyramids (*pyramidelle*)** standing upon its bases, and multiply by the number of bases of the core body (4 on the *tetracedron elevato*, 6 on the *cubo elevato*, 8 on the *octocedron elevato*, 20 on the *ycocedron elevato*, 12 on the *duodecedron elevato*, and similarly for the 14, 26, and 32 bases of the *abscisi elevati*).
  3. **Add** the total volume of those outer *pyramidelle* to the volume of the core body:

     .. math::

        \\text{Volume}_{\\text{elevato}} = \\text{Volume}_{\\text{core}} + N_{\\text{faces}} \\times \\text{Volume}_{\\text{face pyramidella}}

Thus, guided always by the light of the perfect regular bodies—subtracting from them for the *abscisi* and adding to them for the *elevati*—one finds the measure of every dependent body; whereas anyone who attempted to measure them without reducing them to their regular parents would wander into an **inextricable chaos** (*in chaos inextricabile*)!

.. rubric:: 2. Encomium of Duke Ludovico Maria Sforza, Santa Maria delle Grazie, and the 1498 Franciscan General Chapter in Milan

In setting forth these rules, I have always presupposed the rare and speculative intellects ready for every discipline—and above all, by antonomasia and preeminence, the supreme intellect of **Your Ducal Highness**, to whom I have never presumed to speak as to one ignorant of these or any other sciences. For Your Highness is adorned with every virtue, so that to recount them all, not merely paper but a whole lifetime would not suffice (*Sed quod patet expresse non est probare necesse*):

- With a single glance Your Highness heals and gladdens every troubled sight, shining like the sun that warms and illumines both poles—the sole peace, refuge, and refreshment not only of Italy, but of all Christendom!
- In Your Highness dwell mercy, piety (*pietade*), and magnificence; before your eloquence Demosthenes, Cicero, and Quintilian yield, as from your mouth flows a wide river of nectar to the good and a stern blade to the wicked.
- In religious devotion Your Highness is not merely the restorer of sacred temples, but their unceasing founder and author, attending the diurnal and nocturnal divine offices with no less reverence than professed prelates—as is made manifest by your devout **Ducal Chapel** (*la dignissima sua devota capella*), adorned with the most worthy singers (*dignissimi cantori*), and by the most sacred temple of **Santa Maria delle Grazie** (*el suo sacratissimo tempio de Gratie*), which Your Highness has constructed in your renowned city of Milan with no less fitness than **Octavian Augustus** built his universal Temple of Peace in Rome, never tiring of adorning it day by day and supplying its every need!

And I beg the reader not to attribute this brief discourse to flattery (*adulatione*), from which both by nature and by my religious profession I am wholly alien (*Sed quod oculis vidimus testamur*—"what we have seen with our own eyes, we bear witness to"!). For all of this was witnessed not by me alone, but by my entire most sacred **Seraphic Order of St. Francis** together with its reverend head and pastor, our Father **Master Francesco Sansone of Brescia** (*M. Francesco Sansone da Brescia*), most worthy **Minister General**, at our **General Chapter held this present year [May–June 1498] here in your renowned city of Milan**!

To that General Chapter gathered a vast multitude of the most famous doctors and bachelors in sacred theology and other sciences from the whole world and from every nation under heaven (*ex omni natione quae sub caelo est*). Every day solemn cathedral and public disputations were held in the constant presence of Your Ducal Highness's immense humanity and devout condescension toward your servants, together with the Most Reverend Lordship of your brother-in-law **Monsignor Ippolito d'Este, Cardinal Deacon of Santa Lucia in Selci** (*Hipolyto tituli Sanctae Luciae in Silice dyacono Cardinale Estense*), and your ornate courtly retinue. I pass over in silence the overflowing abundance of provisions poured forth from Your Ducal Highness's hands to sustain that vast multitude—so abundant that it sufficed not only for the thousands then present, but for our friars for many months afterward! For your salvation and happy state the whole Order of Friars Minor lifts its joined hands in prayer to the Most High, and particularly I, an unworthy and wretched sinner, who continually commend myself to Your Ducal Highness.""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Additivity and Subtractivity of Polyhedral Volumes**: Mathematically, ``Cap. LXIX`` formulates the exact modern decomposition method for computing the volumes of Archimedean truncations (:math:`V_{\\text{trunc}} = V_{\\text{parent}} - \\sum V_{\\text{vertex pyramids}}`) and Catalan/stellated cumulations (:math:`V_{\\text{elev}} = V_{\\text{core}} + \\sum V_{\\text{face pyramids}}`).
- **Historical Witness to the Milanese Court in 1498**:
  - **The Ducal Chapel Choir (*dignissimi cantori*)**: Under Ludovico Sforza, the *Cappella Musicale* of the Castello Sforzesco (directed by Franchino Gaffurio and having included Josquin des Prez and Loyset Compère) was one of the premier musical institutions of Europe.
  - **Santa Maria delle Grazie**: Bramante's monumental tribune (commissioned by Ludovico Sforza as the Sforza dynastic mausoleum) and Leonardo da Vinci's *Last Supper* in its refectory were both being completed in 1497–1498.
  - **The Franciscan General Chapter of Pentecost 1498 in Milan**: Presided over by the famous Conventual Minister General **Francesco Sansone da Brescia** (1414–1499, General 1475–1499, also a patron of learning) and attended by **Cardinal Ippolito I d'Este** (1479–1520, Archbishop of Milan and brother of Duchess Beatrice d'Este). This passage confirms that Pacioli was writing the final chapters of the *Compendio* in Milan between June and December 1498.
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2/69.txt`` draft completely omitted the entire second half of ``Cap. LXIX`` (the panegyric to Ludovico Sforza, the Ducal Chapel choir, Santa Maria delle Grazie compared to Augustus's Temple of Peace, and the eyewitness account of the 1498 Franciscan General Chapter in Milan with Francesco Sansone and Cardinal Ippolito d'Este). Everything is restored in full here.""",
    },
    70: {
        "title_en": "How to Locate in Order All the Bodies Drawn in Perspective in This Book, as Well as Their Physical Models According to Their Public Table.",
        "body_en": """Because where there is no order there is always confusion (*ubi non est ordo, ibi est confusio*), for the full understanding of this *Compendium*—and so that Your Ducal Highness may readily find both the **perspective figures** drawn on the plane pages of this book and the **three-dimensional material models** (*le forme materiali*) according to their public table—you shall observe the following method:

.. assertion:: Concordance of Marginal Roman Numerals, Leonardo's Perspective Plates, and the Suspended Physical Models

   1. **In the Text Chapters**: As you read above in the chapters treating of the creation and formation of these bodies (from :ref:`Chapter XLVIII <compendio-cap_48-en>` onward), look in the margin of the page for the number marked in **ancient Roman numerals** (*per abaco antico*), proceeding in order: ``I``, ``II``, ``III``, ``IV``, ``V``, and so on up to the end (``LIX`` / ``LX``).
   2. **In Leonardo da Vinci's Perspective Plates**: Seek that exact same Roman numeral in the section of full-page plates (:ref:`Appendix II: Plates I–LIX <plates-polyhedra-en>`), where all the said bodies are drawn in order, matching ``I`` to ``I``, ``II`` to ``II``, ``III`` to ``III``, and so forth in all of them. And each plate presents that body drawn upon the plane with **all the perfection of perspective, as only our Leonardo da Vinci knows how to do** (*facto in piano con tutta perfectione de prospectiva commo sa el nostro Lionardo Vinci*)!
   3. **In the Suspended Physical Models (*Forme Materiali*)**: You shall likewise seek those same Roman numerals among the **material models of the said bodies**, suspended by their cords (*pendenti nel suo cordiglio*), each bearing a parchment scroll (*vn breve*) fixed between **two beads of black amber** (*fra doi ambre negre*) inscribed with its number and its **name in Greek and in Latin**, referring each model to the Roman numeral where it is treated in the text.

In this way Your Ducal Highness will have their complete disposition both in perspective drawing and in physical form—models which truly deserved to be wrought not of humble material (*non de vil materia*, as poverty forced me to make them, out of wooden laths and pasteboard), but adorned with **precious metal and fine gems** (*de pretioso metallo e fine gemme*)! Yet Your Ducal Highness will look upon the geometric effect and the devoted heart of your perpetual servant.""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Pacioli's Physical Polyhedra Models (*Forme Materiali*)**: ``Cap. LXX`` gives us a precious physical description of the sets of **60 three-dimensional models** that Pacioli constructed with his own hands (as he also notes in ``Architectura Cap. VI``, Folio 0072: one set of 60 for Duke Ludovico Sforza, one set for Galeazzo Sanseverino, and a third set in Florence for Gonfaloniere Piero Soderini):
  - Each polyhedron was suspended from a cord (*cordiglio*);
  - Attached to the cord between **two black amber (jet) beads** (*fra doi ambre negre*) was a small parchment label (*vn breve*) bearing the Roman numeral (``I``–``LX``) and the body's name in **Greek and Latin** (identical to the cartouches printed on Leonardo's woodcut plates!).""",
    },
    71: {
        "title_en": "What Is Understood by the Mathematical Terms Used in This Compendium—Namely Hypothesis, Hypotenuse, Corausto, Pyramidal Cone, Pentagonal Chord, Perpendicular, Cathetus, Diameter, Parallelogram, Diagonal, Center, and Sagitta—and Conclusion of Part I (December 14, 1498).",
        "body_en": """There are certain technical terms (*vocabuli*), most lofty Duke, introduced by the ancient sages among the mathematical disciplines for the precise understanding of their parts and to avoid all equivocation, which might trouble a reader not deeply versed in geometry, and which we have frequently used in this *Compendium* so as not to deviate from the Ancients. It therefore seems useful to define them briefly here in order:

.. rubric:: Glossary of Twelve Mathematical Terms

1. **Ypothesi (Hypothesis)**:
   By *hypothesis* is understood the premise admitted and granted between the disputants—the author and the adversary—by means of which the demonstration proceeds to its conclusion; if it is denied, the conclusion does not follow, and therefore it is never posited unless it is possible.
2. **Ypothumissa (Hypotenuse)**:
   In general, in any rectilinear figure, *hypotenuse* means the line opposite the greatest angle. Properly, however, in the art of geometry it means **the side opposite the right angle** in right-angled triangles (*triangoli rectangoli ouer ortogonii*), which triangles are always necessarily half of a square or of an oblong rectangle (*tetragono longo*).
3. **Corausto (Slant Edge / Ridge Line)**:
   By *corausto* (from the medieval Latin *coraustus* / Greek *koryphe*) is understood a straight line that joins the extremities of rising lines elevated on high (or the slant edges rising to the ridge or apex of an elevated body); and there may be more or fewer *corausti* according to the number of elevated lines.
4. **Cono della Pyramide (Apex / Vertex of a Pyramid)**:
   *Cone of the pyramid* means the highest point at the summit (*el ponto supremo dela cima*) where all the straight lines rising from the corners of its base meet and concur.
5. **Corda Pentagonica (Pentagonal Chord / Diagonal)**:
   *Pentagonal chord*, or *chord of the pentagonal angle*, means a straight line drawn across a regular pentagon from any one of its five angles to an opposite (non-adjacent) angle, subtending three sides (and one interior angle) of the pentagon, as we have used many times above (:just:`XIII.8`, :just:`XIII.17`).
6. **Perpendiculare (Perpendicular)**:
   *Perpendicular* means a straight line erected or standing upon another straight line (or upon a plane surface) **at a right angle** (*a squadro*), making one or more right angles around itself (:just:`I.Def.10`, :just:`XI.Def.3`). In triangles it is commonly found in order to measure their area (multiplying the perpendicular altitude by half the base).
7. **Catheto (Cathetus / Altitude)**:
   *Cathetus* (from the Greek :g:`kathetos`, "let fall like a plumb-line") means the exact same thing as the *perpendicular*; among vernacular practitioners (*per li vulgari*) in triangles it is coarsely called the *saetta* (arrow) of the triangle.
8. **Dyametro (Diameter)**:
   Properly, in a **circle**, *diameter* means a straight line passing through its center and touching the circumference at both extremities, dividing the circle into two equal parts (:just:`I.Def.17`). By extension it is also used in **squares** for the line joining opposite angles; and to avoid equivocation one says *diameter of the circle* (*dyametro de cerchio*) and *diameter of the square* (*dyametro del quadrato*).
9. **Parallelogrammo (Parallelogram)**:
   *Parallelogram* means a plane surface bounded by parallel opposite sides (*lati equidistanti*). Properly these are the **four quadrilateral species** that we defined above in :ref:`Chapter LX <compendio-cap_60-en>` (Folio 0053, misprinted *capitolo 69* in the 1509 type): the **square** (*quadrato*), the **oblong rectangle** (*tetragono longo*), the **rhombus** (*rombo / elmuaym*), and the **rhomboid** (*romboide / simile al elmuaym*). For although every regular polygon of an even number of sides—such as the hexagon, octagon, decagon, and dodecagon—has parallel opposite sides, nevertheless by *parallelogram* those four quadrilateral species are specifically understood.
10. **Dyagonale (Diagonal)**:
    *Diagonal* means primarily a straight line drawn from one angle to the opposite angle in an oblong rectangle (*tetragono longo*), dividing it into two equal right triangles just like the diameter of a square; and it is likewise used in the rhombus and rhomboid.
11. **Centro (Center)**:
    Properly, in a **circle** (and sphere), *center* means that middle point upon which the fixed foot of the compass (*el pede immobile del sexto*) stands while the other foot revolves to describe the curved line called the *circumference* or *periphery* (:just:`I.Def.15`), so that all straight lines drawn from that point to the circumference are equal. By extension, in equilateral and equiangular rectilinear figures—such as equilateral triangles, squares, pentagons, and hexagons—*center* also means the middle point of their surface from which all straight lines drawn to their vertices are equal.
12. **Saetta (Sagitta / Versine Arrow)**:
    Properly, *saetta* ("arrow", Latin *sagitta* or *sinus versus*, :ref:`Marginal Diagram 0059.g1.png <compendio-cap_71-en>`) means that straight line which starts from the midpoint of the arc of any segment of a circle (*portione del cerchio*) and falls perpendicularly (*a squadro*) upon the midpoint of its chord. It is called *saetta* (arrow) in relation to the curved part of the circumference called the *arco* (bow) and the straight line called the *corda* (bowstring), in exact likeness to a material bow and arrow (*arco materiale*), which uses the very same three names: **corda** (bowstring), **arco** (bow), and **saetta** (arrow)!

.. rubric:: Conclusion of the Compendio de Divina Proportione (Milan, December 14, 1498)

Although countless other mathematical terms are in use—all of which we have treated in full in our great work (*Summa de Arithmetica*)—I have judged it sufficient to set down here only these twelve necessary for understanding the present *Compendium*. Though completed in no vast number of pages, this *Compendium* treats of matters of the highest substance and most lofty speculation: indeed, most lofty Duke, speaking without falsehood, **the speculation of mathematicians cannot ascend virtually any higher**, for with these very bodies our philosopher **Euclid of Megara** concluded and crowned his entire fifteen-book volume of Arithmetic, Geometry, Proportions, and Proportionality!

Therefore this volume will add no small grace and dignity to your renowned Ducal Library, as we said in our opening Epistle (:ref:`Chapter I <compendio-cap_01-en>`), being unique and the first work of this order ever composed, and hitherto known to no one in the universe save Your Ducal Highness—composed here in your glorious and great city of **Milan**, with no small labor and long nightly vigils, under the shelter of Your Ducal Highness and of one who is like a son to you and my own singular patron, **Messer Galeazzo Sanseverino of Aragon** (*San Galeazzo Sforza Severino de Aragonia*), second to none in military prowess and supreme lover of our mathematical disciplines, who daily tastes the subtlest and sweetest fruit from his assiduous reading of them.

And let the conclusion of our treatise be the humble request for pardon and due reverence of Your Ducal Highness's perpetual servant, who commends himself infinitely to you in every way. *Quae iterum atque iterum ad vota felicissime valeat!*

**FINIS — Completed on the 14th day of December in Milan, in our nurturing Franciscan Convent, MCCCCXCVIII [printed MCCCCXCVII], in the seventh year of the pontificate of Supreme Pontiff Alexander VI.**""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0059 (``f. 22r``) contains diagram ``0059.g1.png`` illustrating the circular segment with its **arco** (arc/bow), **corda** (chord/bowstring), and **saetta** (sagitta/arrow).
- **Dating of the Colophon (December 14, 1498)**: The colophon on Folio 0061 (``f. 23r``) reads *"Finis a di 14. decembre in Milano nel nostro almo convento MCCCCXCVII. Sedente summo pontifice Alexandro VI. del suo pontificato anno VII."* Because Pope Alexander VI (Rodrigo Borgia) was elected on August 11, 1492, his **seventh pontifical year** (*anno VII*) ran from August 11, 1498 to August 10, 1499—and ``Cap. LXIX`` explicitly refers to the Franciscan General Chapter held in Milan in May–June **1498** (*de l'anno presente*). Thus ``MCCCCXCVII`` in the 1509 print dropped a final ``I`` for ``MCCCCXCVIII`` (**December 14, 1498**), the exact date recorded in the presentation manuscripts (Geneva MS l.e. 210 and Milan Biblioteca Ambrosiana MS 170 sup.).""",
    },
}
