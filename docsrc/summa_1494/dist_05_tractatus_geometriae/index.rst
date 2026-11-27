:layout: book
:canonical_id: Summa II, Dist. I–VIII
:folio: Part II, fols. 1r–76r (Colophon Nov. 10, 1494)

.. _summa-unit-05:
.. _summa-unit-05-en:

TRACTATUS GEOMETRIAE: HERON, SURFACE DIVISION & REGULAR SOLIDS
==============================================================

.. rubric:: Part II, Distinctiones I–VIII: Plane Mensuration, Archimedes's Circle, *De Divisione Superficierum*, Inscribed Polyhedra & the 1494 Colophon (fols. 1r–76r)

.. folio:: Part II, fols. 1r–9v

.. rubric:: Distinctio Prima, Capitulum Octavum — Rule of :person:`Heron <heron>` on the `(13, 14, 15)` Triangle (`Part II, fol. 9v`)

Having first set down the foundational definitions and constructions of :person:`Euclid <euclid>` Books I, II, and VI (`fols. 1r–2r`), we turn to measuring the area, perpendicular :term:`cathetus (*catetto*) <catetto>`, and inscribed circle of a scalene triangle from its three sides alone, following :person:`Heron <heron>` and :person:`Leonardo Pisano's <leonardo-pisano>` :cite:`*Practica Geometriae* <leonardo-pisano:practica-geometriae>`.

.. picture:: fig_07_heron_13_14_15.svg
   :alt: Heron's (13, 14, 15) triangle ABG on Part II fol. 9v with cathetus AD = 12 and incircle r = 4

.. assertion:: [Heron's Formula & Euclid II.13 / IV.4] <II.13>

   Let the triangle :g:`GBA <summa.II.1.heron:< G B A >>` be such that along side :g:`GA <summa.II.1.heron:/ G A />` it is :math:`13`, along side :g:`BA <summa.II.1.heron:/ B A />` it is :math:`15`, and along base :g:`GB <summa.II.1.heron:/ G B />` it is :math:`14` *braccia* (:just:`I.22`). Add all three sides together: they make :math:`42`; take the half thereof, which is :math:`21`. Subtract each side separately: there remain :math:`6`, :math:`7`, and :math:`8`:

   .. math::

      21 - 15 = 6, \qquad 21 - 14 = 7, \qquad 21 - 13 = 8

   Multiply :math:`6` by :math:`7`, which makes :math:`42`, and this by :math:`8`, which makes :math:`336`; and multiply this by the aforesaid half, namely :math:`21`: it will make :math:`7056`, whose square root is precisely :math:`84` **square braccia** for the entire area of the said triangle:

   .. math::

      \text{Area}(\triangle GBA) = \sqrt{7056} = 84 \text{ square braccia}

   And dividing double the area (:math:`168`) by base :g:`GB <summa.II.1.heron:/ G B />` (:math:`14`) yields :math:`12` for the :term:`cathetus <catetto>` :g:`AD <summa.II.1.heron:/ A D />`, falling at :g:`D <summa.II.1.heron:D>` with segments :g:`GD <summa.II.1.heron:/ G D />` :math:`= 5` (in right triangle :g:`GDA <summa.II.1.heron:< G D A >>`) and :g:`DB <summa.II.1.heron:/ D B />` :math:`= 9` (in right triangle :g:`DBA <summa.II.1.heron:< D B A >>`). Dividing area :math:`84` by semiperimeter :math:`21` gives the inscribed circle :g:`(IT) <summa.II.1.heron:( I T )>` centered at :g:`I <summa.II.1.heron:I>` of radius :g:`IT <summa.II.1.heron:/ I T />` :math:`= 4` (:just:`IV.4`).

.. folio:: Part II, fol. 31r & fols. 34r–43v

.. rubric:: Measurement of the Circle (`fol. 31r`), Division of Surfaces (`Dist. IV`) & Three Circles in a Triangle (`fol. 57r`)

By :person:`Archimedes of Syracuse <archimedes>` in :cite:`*Dimensio circuli* <archimedes:dimensio-circuli>` (`fol. 31r`), by means of the :math:`96`-sided polygon within and without the circle, the circumference to the diameter is proved to be less than *tripla sesquisettima* (:math:`3\frac{1}{7}`) and greater than :math:`3\frac{10}{71}`. And in *Distinctio IV* (*De divisione superficierum*), we divide triangles, quadrilaterals, and circles in prescribed ratios :math:`p : q` both through vertices (:just:`VI.1`) and parallel to a side (:just:`VI.13`, :just:`VI.19`).

.. picture:: fig_08_divisione_superficierum.svg
   :alt: Euclidean VI.13 and VI.19 parallel area bisection of triangle GBA via chord GS = sqrt(98)

.. assertion:: [Euclid VI.13 & VI.19] <VI.19>

   To bisect the area (:math:`84`) of :g:`GBA <summa.II.4.divisione:< G B A >>` by a cut :g:`UV <summa.II.4.divisione:/ U V />` parallel to :g:`BA <summa.II.4.divisione:/ B A />`: erect perpendicular :g:`MS <summa.II.4.divisione:/ M S />` at midpoint :g:`M <summa.II.4.divisione:M>` of semicircle :g:`(MB) <summa.II.4.divisione:( M B )>` to meet the arc at :g:`S <summa.II.4.divisione:S>`, and transfer chord :g:`GS <summa.II.4.divisione:/ G S />` :math:`= \sqrt{14 \cdot 7} = \sqrt{98} = 7\sqrt{2}` via arc :g:`(GS) <summa.II.4.divisione:( G S )>` onto :g:`GB <summa.II.4.divisione:/ G B />` at :g:`U <summa.II.4.divisione:U>` (:eq:`equal <summa.II.4.divisione:/ G S / = summa.II.4.divisione:/ G B />`). Drawing :g:`UV <summa.II.4.divisione:/ U V />` parallel to :g:`BA <summa.II.4.divisione:/ B A />` cuts off similar sub-triangle :g:`GUV <summa.II.4.divisione:< G U V >>` of exact area :math:`\frac{98}{196} \cdot 84 = 42`.

In *Distinctio V–VI* we gauge wine casks (:term:`botte <botte>`) and solve circle packings (`fol. 57r`): given a triangle whose two equal sides are each :math:`10` and whose base is :math:`12`, I wish to place inside it :math:`3` **equal circles**, the largest that can fit therein. Operating by the :term:`Rule of the Thing <cosa>`, you will arrive at :math:`5\frac{3}{4}` **censi and** :math:`16` **cose equal to** :math:`48`, whence the radius :math:`r = \frac{8\sqrt{85} - 32}{23}` is made manifest.

.. folio:: Part II, fols. 68v–70r & 76r

.. rubric:: *Distinctio Octava — De Corporibus Regularibus* & Venetian Colophon (November 10, 1494)

.. picture:: fig_09_inscribed_polyhedra.svg
   :alt: Sphere of diameter D = 6 (R = 3) inscribing cuboctahedron hexagon PQRSTU of edge 3 and golden icosahedral rectangle WXYZ

In *Distinctio VIII* (`fols. 68v–70v`), we inscribe the five regular bodies (:just:`XIII.13`–:just:`XIII.17`) and their dependent bodies (following :person:`Piero della Francesca <piero-della-francesca>`, :cite:`*Libellus de quinque corporibus regularibus* <piero-della-francesca:de-quinque-corporibus>`) inside a sphere :g:`(OP) <summa.II.8.corporibus:( O P )>` of diameter :math:`D = 6` (radius :math:`R = 3`):

- **Tetrahedron (`fol. 69r`)**: :term:`Possanza <possanza>` :math:`e^2 = \frac{2}{3} D^2 = 24` (:math:`e = \sqrt{24}`); **Cube**: :math:`e^2 = \frac{1}{3} D^2 = 12` (:math:`e = \sqrt{12}`); **Octahedron (`fol. 68v`)**: :math:`e^2 = \frac{1}{2} D^2 = 18` (:math:`e = \sqrt{18}`).
- **Truncated Tetrahedron (`fol. 69v, prob. 15–16`)**: Let there be a sphere whose diameter is :math:`6`; I wish to place within it the **body of** :math:`4` **triangular and** :math:`4` **hexagonal bases**. You will find its side to be :math:`\mathcal{R}.6\frac{6}{11}` (namely :math:`\sqrt{72/11}`).
- **Cuboctahedron (`fol. 69v–70r, prob. 17–19`)**: Wishing to place in the same sphere of diameter :math:`6` the **body of** :math:`14` **bases, namely** :math:`6` **square and** :math:`8` **triangular**, I say its side is precisely half the diameter of the sphere, namely :math:`3` **braccia**, forming the equatorial regular hexagon :g:`PQRSTU <summa.II.8.corporibus:< P Q R S T U >>` across diameters :g:`PS <summa.II.8.corporibus:/ P S />`, :g:`QT <summa.II.8.corporibus:/ Q T />`, and :g:`RU <summa.II.8.corporibus:/ R U />`, with side :g:`PQ <summa.II.8.corporibus:/ P Q />` :eq:`equal <summa.II.8.corporibus:/ P Q / = summa.II.8.corporibus:/ Q R / = summa.II.8.corporibus:/ R S />` to the sphere radius :math:`R = 3`.
- **Hydrostatic Mensuration & Dodecahedron (`fol. 70r, prob. 20–21`)**: Just as :person:`Archimedes <archimedes>` found the measure of a statue or irregular body by water overflowing from a filled vessel (*Prob. 20*), let there be a sphere whose axis has :term:`possanza <possanza>` :math:`48` (:math:`\text{axis} = \mathcal{R}.48`, *Prob. 21*): I seek the side of the **dodecahedron** inscribed therein (spanned with the icosahedron by golden rectangle :g:`WXYZ <summa.II.8.corporibus:< W X Y Z >>`, :g:`WX <summa.II.8.corporibus:/ W X />` : :g:`XY <summa.II.8.corporibus:/ X Y />` :math:`= \phi : 1`). Take one third of :math:`48`, which is :math:`16`, whose root :math:`4` is the side of the inscribed cube (:just:`XIII.15`); divide :math:`4` according to the :term:`proportion having extreme and mean ratio <media-et-estrema-ragione>`, whose greater part :math:`\mathcal{R}.20 \;\bar{m}\; 2` is the side of the dodecahedron, and the lesser part is :math:`6 \;\bar{m}\; \mathcal{R}.20`.

.. qed::

   *Colophon (`Part II, fol. 76r`):* At the expense, diligence, and workmanship of the prudent man :person:`Paganino de' Paganini of Brescia <paganino-de-paganini>`, in the exalted city of **Venice**, by grace of its exalted Dominion for ten years that no other may reprint it, under the most felicitous government of Our Most Serene Prince :person:`Agostino Barbarigo <agostino-barbarigo>`, **Brother Luca of Borgo Sansepolcro** of the Order of Minorites and humble professor of Sacred Theology has shown forth his small judgment and strength—**in the year of our Salvation M.cccc.lxliiii, on the 10th day of November.**
