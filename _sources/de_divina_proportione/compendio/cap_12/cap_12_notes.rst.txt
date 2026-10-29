:layout: book
:canonical_id: Cap. XII
:folio: 0027 (f. 6r)

.. _compendio-cap_12-notes:

CHAPTER XII — Critical Commentary & Notes
=========================================

.. rubric:: On Its Third Singular Effect

Historical and Philological Commentary
--------------------------------------

1. **Radical Arithmetic in Chapter XII (:cite:`Euclid XIII.3 <euclid:elements:XIII.3>`)**: Pacioli's step-by-step calculation with apotomes is a tour de force of Renaissance abacus algebra:

   - Halving $\sqrt{125}$ requires dividing the radicand by $2^2 = 4$: $\frac{1}{2}\sqrt{125} = \sqrt{\frac{125}{4}} = \sqrt{31\frac{1}{4}}$.
   - Subtracting $\sqrt{125} - \sqrt{31\frac{1}{4}} = 2\sqrt{31\frac{1}{4}} - \sqrt{31\frac{1}{4}} = \sqrt{31\frac{1}{4}}$ gives $b + \frac{a}{2} = (15 - 2\frac{1}{2}) - \sqrt{31\frac{1}{4}} = 12\frac{1}{2} - \sqrt{31\frac{1}{4}}$.
   - Squaring $12\frac{1}{2} - \sqrt{31\frac{1}{4}}$ gives $(12\frac{1}{2})^2 + 31\frac{1}{4} - 2(12\frac{1}{2})\sqrt{31\frac{1}{4}} = 156\frac{1}{4} + 31\frac{1}{4} - \sqrt{625 \times 31\frac{1}{4}} = 187\frac{1}{2} - \sqrt{19531\frac{1}{4}}$.
   - Squaring $\frac{a}{2} = \sqrt{31\frac{1}{4}} - 2\frac{1}{2}$ gives $31\frac{1}{4} + 6\frac{1}{4} - \sqrt{25 \times 31\frac{1}{4}} = 37\frac{1}{2} - \sqrt{781\frac{1}{4}}$.
   - Multiplying by $5$ scales the rational part by $5$ ($5 \times 37\frac{1}{2} = 187\frac{1}{2}$) and the radicand by $5^2 = 25$ ($25 \times 781\frac{1}{4} = 19531\frac{1}{4}$).

Constantin Winterberg's Commentary (1889 Edition)
-------------------------------------------------

.. rubric:: Note 3 (Cap. XII): Algebraic Proof of the Third Effect (Euclid XIII.3) (:ref:`Sachliche Anmerkungen #3 <plates-anmerkungen-en>`, Cap. XII, p. 203, l. 3 from top)

Expressed algebraically for the line $ac$ divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $b$ ($ab > bc$):

- **Hypothesis**: $ab^2 = ac \cdot bc = (ab + bc)\,bc$.
- **Claim**: $\left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2$.
- **Proof**: Since $ab^2 = bc^2 + ab \cdot bc$ by hypothesis, adding $\left(\frac{ab}{2}\right)^2$ to both sides yields

  .. math::

     \left(bc + \frac{ab}{2}\right)^2 = bc^2 + ab \cdot bc + \left(\frac{ab}{2}\right)^2 = ab^2 + \frac{ab^2}{4} = 5\left(\frac{ab}{2}\right)^2.

  Substituting the numerical values of Chapter XII ($ac = 10$, $ab = \sqrt{125} - 5$, $bc = 15 - \sqrt{125}$) confirms the identity of both sides immediately.

.. rubric:: Anmerkung 3 (Cap. XII, S. 203): Mathematischer Nachweis des dritten Effects (Euklid XIII.3)

Mathematisch ausgedrückt heisst dies mit Bezug auf die in $b$ stetig getheilte Linie $ac$:

- **Voraussetzung**: $ab^2 = ac \cdot bc$.
- **Behauptung**: $\left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2$.
- **Beweis**: $ab^2 = bc^2 + ab \cdot bc$ (nach Voraussetzung), daher analog wie in Anmerkung 1 durch Hinzufügung von $\left(\frac{ab}{2}\right)^2$ rechts und links:

  .. math::

     \left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2.

  Setzt man die Werthe des in Cap. XII behandelten Beispiels ein ($ab = \sqrt{125} - 5$, $bc = 15 - \sqrt{125}$), so ergibt sich die Richtigkeit durch Uebereinstimmung der beiden Seiten der Gleichung ohne weiteres.


Philological and Folio Apparatus
--------------------------------

- **1509 Paganini Witness Folios**: 0027 (f. 6r–f. 6r)
- **Winterberg 1889 Italian Source**: ``winterberg/01_divina_proportione_italian/012_cap_XII.txt``
- **Winterberg 1889 German Source**: ``winterberg/03_divina_proportione_german/012_cap_XII.txt``
- **Marginal Woodcut Diagrams**: 0 figure(s) extracted from the 1509 Venice witness.
