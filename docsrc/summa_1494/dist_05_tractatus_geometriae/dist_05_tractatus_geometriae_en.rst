:layout: book
:canonical_id: Summa II, Dist. I–VIII
:folio: Part II, fols. 1r–76r (Colophon Nov. 10, 1494)

.. _summa-unit-05:
.. _summa-unit-05-en:

TRACTATUS GEOMETRIAE: HERON, SURFACE DIVISION & REGULAR SOLIDS
==============================================================

.. rubric:: Part II, Distinctiones I–VIII: Plane Mensuration, Archimedes's Circle, *De Divisione Superficierum*, Inscribed Polyhedra & the 1494 Colophon (fols. 1r–76r)

.. folio:: Part II, fols. 1r–9v

.. rubric:: Euclid Digest & Heron's `(13, 14, 15)` Triangle Mensuration (`Part II, fol. 9v`)

Opening the separately foliated second tome (*Tractatus Geometriae*, `fols. 1r–2r`), :person:`Fra Luca Pacioli <pacioli>` condenses the foundational definitions and constructions of :person:`Euclid <euclid>` Books I, II, and VI before turning in *Distinctio I, Cap. 8* (`fol. 9v`) to the crown jewel of practical surveyor's mensuration inherited from :person:`Heron of Alexandria <heron>` and :person:`Leonardo Pisano's <leonardo-pisano>` :cite:`*Practica Geometriae* <leonardo-pisano:practica-geometriae>`: determining the exact area, perpendicular :term:`cathetus (*catetto*) <catetto>`, and incircle of a scalene triangle from its three sides alone.

.. picture:: fig_07_heron_13_14_15.svg
   :alt: Heron's (13, 14, 15) triangle ABG on Part II fol. 9v with cathetus AD = 12 and incircle r = 4

.. assertion:: [Heron's Formula & Euclid II.13 / IV.4] <II.13>

   Let scalene triangle :g:`GBA <summa.II.1.heron:< G B A >>` have sides :g:`GA <summa.II.1.heron:/ G A />` $= 13$, base :g:`GB <summa.II.1.heron:/ G B />` $= 14$, and :g:`BA <summa.II.1.heron:/ B A />` $= 15$ *braccia* (:just:`I.22`). Sum the three sides ($13 + 14 + 15 = 42$) and take the **semiperimeter** (*mità dela summa*) $s = 21$. Subtract each side in turn to obtain the three **excesses** (*differentie*):

   $$21 - 15 = 6, \qquad 21 - 14 = 7, \qquad 21 - 13 = 8$$

   Multiply $6 \times 7 \times 8 = 336$, and multiply $336$ by the semiperimeter $21$ to obtain $7056$, whose exact square root gives the area:

   $$\text{Area}(\triangle GBA) = \sqrt{7056} = 84 \text{ square braccia}$$

   Dividing $2 \times 84 = 168$ by base :g:`GB <summa.II.1.heron:/ G B />` ($14$) yields the perpendicular :term:`cathetus <catetto>` :g:`AD <summa.II.1.heron:/ A D />` $= 12$, splitting $GB$ at :g:`D <summa.II.1.heron:D>` into right-triangle base segments :g:`GD <summa.II.1.heron:/ G D />` $= 5$ (inside $(5, 12, 13)$ right triangle :g:`GDA <summa.II.1.heron:< G D A >>`) and :g:`DB <summa.II.1.heron:/ D B />` $= 9$ (inside $(9, 12, 15)$). Dividing area $84$ by semiperimeter $21$ locates the incircle :g:`(IT) <summa.II.1.heron:( I T )>` centered at :g:`I <summa.II.1.heron:I>` $= (6, 4)$ of exact integer inradius :g:`IT <summa.II.1.heron:/ I T />` $= 4$ (:just:`IV.4`).

.. folio:: Part II, fol. 31r & fols. 34r–43v

.. rubric:: Archimedes's Circle (`fol. 31r`) & *De Divisione Superficierum* (`Dist. IV`)

In *Distinctio III, Cap. 6* (`fol. 31r`), Pacioli expounds :person:`Archimedes's <archimedes>` :cite:`*Dimensio Circuli* <archimedes:dimensio-circuli>`, bounding the circumference-to-diameter ratio by inscribed and circumscribed $96$-gons between $3\frac{10}{71}$ and $3\frac{1}{7}$ ($22 : 7$). In *Distinctio IV* (*De divisione superficierum*), he solves estate-partition problems dividing triangles, quadrilaterals, and circles in prescribed ratios $p : q$ both through vertices (:just:`VI.1`) and parallel to a side (:just:`VI.13`, :just:`VI.19`).

.. picture:: fig_08_divisione_superficierum.svg
   :alt: Euclidean VI.13 and VI.19 parallel area bisection of triangle GBA via chord GS = sqrt(98)

.. assertion:: [Euclid VI.13 & VI.19] <VI.19>

   To bisect the area ($84$) of :g:`GBA <summa.II.4.divisione:< G B A >>` by a cut :g:`UV <summa.II.4.divisione:/ U V />` parallel to :g:`BA <summa.II.4.divisione:/ B A />`: erect perpendicular :g:`MS <summa.II.4.divisione:/ M S />` at midpoint :g:`M <summa.II.4.divisione:M>` $(7, 0)$ of semicircle :g:`(MB) <summa.II.4.divisione:( M B )>` to meet the arc at :g:`S <summa.II.4.divisione:S>`, and swing arc :g:`(GS) <summa.II.4.divisione:( G S )>` onto :g:`GB <summa.II.4.divisione:/ G B />` at :g:`U <summa.II.4.divisione:U>`, so :g:`GU <summa.II.4.divisione:U>` is :eq:`equal <summa.II.4.divisione:/ G S / = summa.II.4.divisione:/ G B />` in chord length to :g:`GS <summa.II.4.divisione:/ G S />` $= \sqrt{14 \cdot 7} = \sqrt{98} = 7\sqrt{2}$. Drawing :g:`UV <summa.II.4.divisione:/ U V />` $\parallel$ :g:`BA <summa.II.4.divisione:/ B A />` cuts off similar sub-triangle :g:`GUV <summa.II.4.divisione:< G U V >>` of exact area $\frac{GU^2}{GB^2} \cdot 84 = \frac{98}{196} \cdot 84 = 42$.

In *Distinctio V–VI*, Pacioli gauges wine casks (:term:`botte <botte>`) and solves algebraic-geometric circle packings via *Regola dela Cosa*—culminating on `fol. 57r` in inscribing three mutually tangent equal circles inside the $(10, 10, 12)$ triangle via the Cossic quadratic $5\frac{3}{4}.\text{ce.} \; \bar{p} \; 16.\text{co.} = 48$ ($r = \frac{8\sqrt{85} - 32}{23}$), three centuries before Malfatti (1803).

.. folio:: Part II, fols. 68v–70r & 76r

.. rubric:: *De Corporibus Regularibus* (`Dist. VIII`) & the November 10, 1494 Venetian Colophon

.. picture:: fig_09_inscribed_polyhedra.svg
   :alt: Sphere of diameter D = 6 (R = 3) inscribing cuboctahedron hexagon PQRSTU of edge 3 and golden icosahedral rectangle WXYZ

Closing the entire work in *Distinctio VIII* (`fols. 68v–70v`), Pacioli inscribes the five regular Platonic solids (:just:`XIII.13`–:just:`XIII.17`) and dependent Archimedean truncations (following :person:`Piero della Francesca's <piero-della-francesca>` :cite:`*Libellus de quinque corporibus regularibus* <piero-della-francesca:de-quinque-corporibus>`) inside a sphere :g:`(OP) <summa.II.8.corporibus:( O P )>` of diameter $D = 6$ (radius $R = 3$):

- **Tetrahedron (`fol. 69r`)**: :term:`Possanza <possanza>` $e^2 = \frac{2}{3} D^2 = 24$ ($e = \sqrt{24}$); **Cube**: $e^2 = \frac{1}{3} D^2 = 12$ ($e = \sqrt{12}$); **Octahedron (`fol. 68v`)**: $e^2 = \frac{1}{2} D^2 = 18$ ($e = \sqrt{18}$).
- **Truncated Tetrahedron (`fol. 69v, prob. 15–16`, 4 triangles + 4 hexagons)**: Exact squared edge $e^2 = \frac{2}{11} D^2 = \frac{72}{11} = 6\frac{6}{11}$, matching Pacioli's printed radical $\mathcal{R}.6\frac{6}{11}$!
- **Cuboctahedron (`fol. 69v–70r, prob. 17–19`, 6 squares + 8 triangles)**: Its equatorial great-circle section :g:`PQRSTU <summa.II.8.corporibus:< P Q R S T U >>` across diameters :g:`PS <summa.II.8.corporibus:/ P S />`, :g:`QT <summa.II.8.corporibus:/ Q T />`, and :g:`RU <summa.II.8.corporibus:/ R U />` is a regular hexagon whose side :g:`PQ <summa.II.8.corporibus:/ P Q />` is :eq:`equal <summa.II.8.corporibus:/ P Q / = summa.II.8.corporibus:/ Q R / = summa.II.8.corporibus:/ R S />` to the sphere radius $R = 3$!
- **Icosahedron & Dodecahedron (`fol. 70r, prob. 21–22`)**: Spanned internally by golden rectangle :g:`WXYZ <summa.II.8.corporibus:< W X Y Z >>` (:g:`WX <summa.II.8.corporibus:/ W X />` : :g:`XY <summa.II.8.corporibus:/ X Y />` $= \phi : 1$). In Problem 21 (`fol. 70r`), for a sphere whose axis has :term:`possanza <possanza>` $48$ ($D = \sqrt{48}$), the inscribed cube has edge $\sqrt{48/3} = 4$, and dividing $4$ in :term:`extreme and mean ratio <media-et-estrema-ragione>` yields the exact dodecahedron edge $\sqrt{20} - 2$ and minor segment $6 - \sqrt{20}$, right beside Problem 20's hydrostatic method of :person:`Archimedes <archimedes>` measuring irregular sculptural bodies by displaced water.

.. qed::

   On `Part II, fol. 76r`, :person:`Paganino de' Paganini <paganino-de-paganini>` sets his colophon in Venice on **November 10, 1494**, under the ten-year privilege of :person:`Doge Agostino Barbarigo <agostino-barbarigo>` (*Con spesa e diligentia: e opifitio del prudente homo Paganino de Paganini da Brescia. Nella excelsa cita de vinegia... Negli anni de nostra Salute M.cccc.lxliiii. adi .10. de nouembre*)—launching the mathematical Renaissance in print.
