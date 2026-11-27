:type: notes
:tracks: English: index | Italian: it | German: de | Notes: notes
:layout: book
:canonical_id: Cap. XXI
:folio: 0029–0030 (f. 7r–f. 7v)

.. _compendio-cap_21-notes:

CHAPTER XXI — Critical Commentary & Notes
=========================================

.. rubric:: On Its Twelfth Almost Incomprehensible Effect

Historical and Philological Commentary
--------------------------------------

1. **Mathematical Verification of the Twelfth Effect (Campanus XIV.9)**:

   - Let a sphere have diameter :math:`D`. By :cite:`Euclid XIII.15 <euclid:elements:XIII.15>`, the edge of the inscribed cube satisfies :math:`s_{\text{cube}}^2 = \frac{1}{3}D^2`.
   - By :cite:`Euclid XIII.16 <euclid:elements:XIII.16>`.p and :cite:`Euclid XIII.18 <euclid:elements:XIII.18>`, the edge of the inscribed :term:`icosahedron <icosahedron>` satisfies :math:`s_{\text{icosa}}^2 = \frac{5 - \sqrt{5}}{10}D^2`.
   - Meanwhile, in :person:`Pacioli's <pacioli>` formula with :math:`a+b = 10`, :math:`a = \sqrt{125}-5`, and :math:`b = 15-\sqrt{125}`:

     - :math:`(a+b)^2 + a^2 = 250 - \sqrt{12500} = 250 - 50\sqrt{5} = 50(5 - \sqrt{5})`.
     - By the Fifth Effect (Chapter XIV, :cite:`Euclid XIII.4 <euclid:elements:XIII.4>`), :math:`(a+b)^2 + b^2 = 3a^2 = 450 - \sqrt{112500} = 3 \times 50(3 - \sqrt{5})`!
     - Wait: notice that :math:`\frac{\sqrt{(a+b)^2 + b^2}}{\sqrt{(a+b)^2 + a^2}} = \frac{\sqrt{3a^2}}{\sqrt{(a+b)^2 + a^2}} = \frac{\sqrt{3} \cdot a}{\sqrt{(a+b)^2 + a^2}}`. Since :math:`(a+b)^2 + a^2` is the square of the hypotenuse of a right triangle with legs :math:`a+b` (radius of the pentagon's/:term:`icosahedron <icosahedron>`'s defining circle) and :math:`a` (the decagon side), by :cite:`Euclid XIII.10 <euclid:elements:XIII.10>` (:math:`s_5^2 = s_6^2 + s_{10}^2`), :math:`\sqrt{(a+b)^2 + a^2}` is the **side of the pentagon** (:math:`s_{\text{icosa}}`) inscribed in the circle of radius :math:`a+b`, while :math:`a` is the decagon side!

   - In :person:`Campanus <campanus>`'s Latin text of Book XIV, Proposition 9 proves this exact relation between the cube edge and :term:`icosahedron <icosahedron>` edge via the segments of a line cut in :term:`extreme and mean ratio <extrema-et-media-ratio>`.

2. **Universal / Bound Roots (*Radici Universali / Radici Legate*)**: Pacioli introduces the Renaissance algebraic term *:term:`radice universale <radice-universale>`* or *:term:`radice legata <radice-universale>`* (written *R.V.* in the *Summa*, Distinctio VIII, Tractatus 3, f. 120r), where the radical sign governs an entire binomial or :term:`apotome <residuo>` (:math:`\sqrt{250 - \sqrt{12500}}`).

Constantin Winterberg's Commentary (1889 Edition)
-------------------------------------------------

.. rubric:: Note 8 (Cap. XXI): Twelfth Effect — Ratio of the Cube Edge to the Icosahedron Edge in the Same Sphere (:ref:`Sachliche Anmerkungen #8 <plates-anmerkungen-en>`, Cap. XXI, p. 209, l. 13 from bottom)

Denoting by :math:`s` and :math:`s'` the edges of the cube and regular :term:`icosahedron <icosahedron>` inscribed in the same sphere, and letting the segment :math:`ab` be divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at :math:`c` (:math:`ac > bc`), :person:`Pacioli's <pacioli>` claim (following :cite:`Campanus XIV.9 <campanus:euclid:XIV.9>`) is:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \frac{s'}{s} \quad \left(\text{or reciprocally } \sqrt{\frac{ab^2 + bc^2}{ab^2 + ac^2}} = \frac{s}{s'}\right).

**Proof**: Using the :term:`extreme and mean ratio <extrema-et-media-ratio>` relations (a) :math:`ac^2 = ab \cdot bc` and (b) :math:`bc^2 = (ab - ac)^2 = ab^2 - 2\,ab \cdot ac + ac^2`, we have :math:`ab^2 + bc^2 = 3\,ac^2 = 3\,ab \cdot bc` (by Note 5) and :math:`ab^2 + ac^2 = ab^2 + ab \cdot bc = ab(ab + bc)`. Hence the quotient under the radical simplifies to:

.. math::

   \frac{ab^2 + ac^2}{ab^2 + bc^2} = \frac{ab(ab + bc)}{3\,ab \cdot bc} = \frac{ab + bc}{3\,bc}.

Solving :math:`ac^2 = ab \cdot bc = ab(ab - ac)` gives :math:`bc = \frac{3 - \sqrt{5}}{2}\,ab`, and substituting this into the quotient yields:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \sqrt{\frac{ab + bc}{3\,bc}} = \sqrt{\frac{5 + \sqrt{5}}{6}} \quad \left(\text{and its reciprocal } \sqrt{\frac{3\,bc}{ab + bc}} = \sqrt{\frac{5 - \sqrt{5}}{6}}\right).

The exact same value is obtained when we express :math:`s` and :math:`s'` in terms of the circumradius :math:`r` of the common sphere (:cite:`Euclid XIII.15 <euclid:elements:XIII.15>`, :cite:`Euclid XIII.16 <euclid:elements:XIII.16>`, :cite:`Euclid XIII.18 <euclid:elements:XIII.18>`):

.. math::

   s = \frac{2r}{\sqrt{3}}, \qquad s' = \frac{4r}{\sqrt{10 + 2\sqrt{5}}} = r\sqrt{\frac{10 - 2\sqrt{5}}{5}}, \qquad \frac{s}{s'} = \sqrt{\frac{5 + \sqrt{5}}{6}}. \quad \text{Q.E.D.}

.. rubric:: Anmerkung 8 (Cap. XXI, S. 209): Zwölfter Effect — Verhältniss der Seite des Kubus zur Seite des Ikosaeders

Bezeichnet man mit :math:`s, s'` resp. die Seiten des Kubus und des regulären :term:`Ikosaeders <icosahedron>`, so wird, wenn die Linie :math:`ab` in :math:`c` stetig getheilt ist (:math:`ac > bc`), behauptet:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \frac{s}{s'}.

**Beweis**: Der Ausdruck unter dem Wurzelzeichen links lässt sich vereinfachen, indem zufolge Voraussetzung:
a) :math:`ac^2 = ab \cdot bc`,
b) :math:`bc^2 = (ab - ac)^2`.
Durch Einsetzen dieser Ausdrücke und Ausführung der Quadratur des letzteren erhält man:

.. math::

   \frac{ab^2 + ac^2}{ab^2 + bc^2} = \frac{ab(ab + bc)}{3\,ab \cdot bc} = \frac{ab + bc}{3\,bc}.

Aus der Gleichung a), nachdem darin :math:`ac = ab - bc` gesetzt, erhält man :math:`bc^2 - 3\,ab \cdot bc + ab^2 = 0`, und durch Einsetzen in den vorstehenden Quotienten:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \sqrt{\frac{ab + bc}{3\,bc}} = \sqrt{\frac{5 + \sqrt{5}}{6}}.

Derselbe Werth ergibt sich aber auch, wenn man das Verhältniss :math:`\frac{s}{s'}` durch den Radius :math:`r` der umschriebenen Kugel ausgedrückt berechnet, indem bekanntlich ist:

.. math::

   s = \frac{2r}{\sqrt{3}}, \qquad s' = \frac{4r}{\sqrt{10 + 2\sqrt{5}}}, \qquad \text{somit} \quad \frac{s}{s'} = \sqrt{\frac{5 + \sqrt{5}}{6}}.


Philological and Folio Apparatus
--------------------------------

- **1509 Paganini Witness Folios**: 0029, 0030 (f. 7r–f. 7v)
- **Winterberg 1889 Italian Source**: ``winterberg/01_divina_proportione_italian/021_cap_XXI.txt``
- **Winterberg 1889 German Source**: ``winterberg/03_divina_proportione_german/021_cap_XXI.txt``
- **Marginal Woodcut Diagrams**: 1 figure(s) extracted from the 1509 Venice witness.
