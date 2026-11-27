:type: notes
:tracks: English: index | Italian: it | German: de | Notes: notes
:layout: book
:canonical_id: Cap. XII
:folio: 0027 (f. 6r)

.. _compendio-cap_12-notes:

CHAPTER XII — Critical Commentary & Notes
=========================================

.. rubric:: On Its Third Singular Effect

Historical and Philological Commentary
--------------------------------------

1. **Radical Arithmetic in Chapter XII (Euclid XIII.3)**: :person:`Pacioli's <pacioli>` step-by-step calculation with apotomes is a tour de force of Renaissance abacus algebra:

   - Halving :math:`\sqrt{125}` requires dividing the radicand by :math:`2^2 = 4`: :math:`\frac{1}{2}\sqrt{125} = \sqrt{\frac{125}{4}} = \sqrt{31\frac{1}{4}}`.
   - Subtracting :math:`\sqrt{125} - \sqrt{31\frac{1}{4}} = 2\sqrt{31\frac{1}{4}} - \sqrt{31\frac{1}{4}} = \sqrt{31\frac{1}{4}}` gives :math:`b + \frac{a}{2} = (15 - 2\frac{1}{2}) - \sqrt{31\frac{1}{4}} = 12\frac{1}{2} - \sqrt{31\frac{1}{4}}`.
   - Squaring :math:`12\frac{1}{2} - \sqrt{31\frac{1}{4}}` gives :math:`(12\frac{1}{2})^2 + 31\frac{1}{4} - 2(12\frac{1}{2})\sqrt{31\frac{1}{4}} = 156\frac{1}{4} + 31\frac{1}{4} - \sqrt{625 \times 31\frac{1}{4}} = 187\frac{1}{2} - \sqrt{19531\frac{1}{4}}`.
   - Squaring :math:`\frac{a}{2} = \sqrt{31\frac{1}{4}} - 2\frac{1}{2}` gives :math:`31\frac{1}{4} + 6\frac{1}{4} - \sqrt{25 \times 31\frac{1}{4}} = 37\frac{1}{2} - \sqrt{781\frac{1}{4}}`.
   - Multiplying by :math:`5` scales the rational part by :math:`5` (:math:`5 \times 37\frac{1}{2} = 187\frac{1}{2}`) and the radicand by :math:`5^2 = 25` (:math:`25 \times 781\frac{1}{4} = 19531\frac{1}{4}`).

Constantin Winterberg's Commentary (1889 Edition)
-------------------------------------------------

.. rubric:: Note 3 (Cap. XII): Algebraic Proof of the Third Effect (Euclid XIII.3) (:ref:`Sachliche Anmerkungen #3 <plates-anmerkungen-en>`, Cap. XII, p. 203, l. 3 from top)

Expressed algebraically for the line :math:`ac` divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at :math:`b` (:math:`ab > bc`):

- **Hypothesis**: :math:`ab^2 = ac \cdot bc = (ab + bc)\,bc`.
- **Claim**: :math:`\left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2`.
- **Proof**: Since :math:`ab^2 = bc^2 + ab \cdot bc` by hypothesis, adding :math:`\left(\frac{ab}{2}\right)^2` to both sides yields

  .. math::

     \left(bc + \frac{ab}{2}\right)^2 = bc^2 + ab \cdot bc + \left(\frac{ab}{2}\right)^2 = ab^2 + \frac{ab^2}{4} = 5\left(\frac{ab}{2}\right)^2.

  Substituting the numerical values of Chapter XII (:math:`ac = 10`, :math:`ab = \sqrt{125} - 5`, :math:`bc = 15 - \sqrt{125}`) confirms the identity of both sides immediately.

.. rubric:: Anmerkung 3 (Cap. XII, S. 203): Mathematischer Nachweis des dritten Effects (Euklid XIII.3)

Mathematisch ausgedrückt heisst dies mit Bezug auf die in :math:`b` stetig getheilte Linie :math:`ac`:

- **Voraussetzung**: :math:`ab^2 = ac \cdot bc`.
- **Behauptung**: :math:`\left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2`.
- **Beweis**: :math:`ab^2 = bc^2 + ab \cdot bc` (nach Voraussetzung), daher analog wie in Anmerkung 1 durch Hinzufügung von :math:`\left(\frac{ab}{2}\right)^2` rechts und links:

  .. math::

     \left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2.

  Setzt man die Werthe des in Cap. XII behandelten Beispiels ein (:math:`ab = \sqrt{125} - 5`, :math:`bc = 15 - \sqrt{125}`), so ergibt sich die Richtigkeit durch Uebereinstimmung der beiden Seiten der Gleichung ohne weiteres.


Philological and Folio Apparatus
--------------------------------

- **1509 Paganini Witness Folios**: 0027 (f. 6r–f. 6r)
- **Winterberg 1889 Italian Source**: ``winterberg/01_divina_proportione_italian/012_cap_XII.txt``
- **Winterberg 1889 German Source**: ``winterberg/03_divina_proportione_german/012_cap_XII.txt``
- **Marginal Woodcut Diagrams**: 0 figure(s) extracted from the 1509 Venice witness.
