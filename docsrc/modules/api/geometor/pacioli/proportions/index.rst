geometor.pacioli.proportions
============================

.. py:module:: geometor.pacioli.proportions

.. autoapi-nested-parse::

   Exact symbolic proportion theory and Cossic algebra from Pacioli's *Summa* (1494).

   Formalizes three pillars of Part I of Fra Luca Pacioli's *Summa de arithmetica,
   geometria, proportioni et proportionalita* (Venice, 1494):

   1. **Boethian Ratio Taxonomy & Six Euclidean Modes** (*Part I, Distinctio VI*,
      fols. 68v–98r): Exact classification of rational ratios into the five Boethian
      genera of greater and lesser inequality (*multiplex*, *superparticularis*,
      *superpartiens*, *multiplex superparticularis*, *multiplex superpartiens*),
      compound ratios (*proportioni composte*), and the six Euclidean *modi arguendi*
      on fol. 74r (*conversa*, *permutata*, *congionta*, *disgiunta*, *eversa*, *equa*).
   2. **Semicircle Construction of the Three Classical Means & Golden Section**:
      Targeted ``geometor.model`` straightedge-and-compass constructions proving
      :math:`A \ge G \ge H` and :math:`G^2 = A \cdot H`, harmonic cross-ratio :math:`-1`,
      and Euclidean division of :math:`10` in extreme and mean ratio into
      :math:`\sqrt{125} - 5` and :math:`15 - \sqrt{125}` (*Summa* Dist. VI & *Compendio* Cap. VII–X).
   3. **Six Canonical Cossic Quadratics** (*Part I, Distinctio VIII*, fols. 145r–150r):
      Symbolic solver and gnomon completion-of-the-square parameters matching Pacioli's
      *Primi/Secundi/Tertii canonis versus* and marginal woodcuts on fol. 146r.



Classes
-------

.. autoapisummary::

   geometor.pacioli.proportions.BoethianClassification
   geometor.pacioli.proportions.SixModesResult
   geometor.pacioli.proportions.ThreeMeansResult
   geometor.pacioli.proportions.ExtremeMeanResult
   geometor.pacioli.proportions.CossicQuadraticResult


Functions
---------

.. autoapisummary::

   geometor.pacioli.proportions.classify_boethian_ratio
   geometor.pacioli.proportions.compound_ratios
   geometor.pacioli.proportions.apply_six_euclidean_modes
   geometor.pacioli.proportions.construct_three_means
   geometor.pacioli.proportions.construct_extreme_and_mean_ratio
   geometor.pacioli.proportions.solve_cossic_quadratic


Module Contents
---------------

.. py:class:: BoethianClassification

   Exact Boethian classification of a positive rational ratio :math:`p : q`.


   .. py:attribute:: antecedent
      :type:  sympy.Integer


   .. py:attribute:: consequent
      :type:  sympy.Integer


   .. py:attribute:: reduced_ratio
      :type:  sympy.Rational


   .. py:attribute:: inequality
      :type:  str


   .. py:attribute:: genus
      :type:  str


   .. py:attribute:: latin_species
      :type:  str


   .. py:attribute:: quotient
      :type:  sympy.Integer


   .. py:attribute:: remainder
      :type:  sympy.Integer


   .. py:attribute:: denominator
      :type:  sympy.Integer


.. py:class:: SixModesResult

   The six Euclidean *modi arguendi* (Book V / *Summa* fol. 74r) on :math:`a : b = c : d`.


   .. py:attribute:: original
      :type:  tuple[sympy.Rational, sympy.Rational]


   .. py:attribute:: conversa
      :type:  tuple[sympy.Rational, sympy.Rational]


   .. py:attribute:: permutata
      :type:  tuple[sympy.Rational, sympy.Rational]


   .. py:attribute:: congionta
      :type:  tuple[sympy.Rational, sympy.Rational]


   .. py:attribute:: disgiunta
      :type:  tuple[sympy.Rational, sympy.Rational] | None


   .. py:attribute:: eversa
      :type:  tuple[sympy.Rational, sympy.Rational] | None


   .. py:attribute:: equa
      :type:  tuple[sympy.Rational, sympy.Rational] | None


.. py:class:: ThreeMeansResult

   Exact symbolic outputs of the semicircle construction of the three classical means.


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: a
      :type:  sympy.Expr


   .. py:attribute:: b
      :type:  sympy.Expr


   .. py:attribute:: arithmetic_mean
      :type:  sympy.Expr


   .. py:attribute:: geometric_mean
      :type:  sympy.Expr


   .. py:attribute:: harmonic_mean
      :type:  sympy.Expr


   .. py:attribute:: harmonic_conjugate_point
      :type:  sympy.geometry.Point


.. py:class:: ExtremeMeanResult

   Exact symbolic outputs of dividing a segment in extreme and mean ratio.


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: whole
      :type:  sympy.Expr


   .. py:attribute:: major_part
      :type:  sympy.Expr


   .. py:attribute:: minor_part
      :type:  sympy.Expr


   .. py:attribute:: cut_point
      :type:  sympy.geometry.Point


   .. py:attribute:: phi_ratio
      :type:  sympy.Expr


.. py:class:: CossicQuadraticResult

   Symbolic solution and geometric gnomon invariants for Pacioli's 6 canonical equations.


   .. py:attribute:: canon_number
      :type:  int


   .. py:attribute:: canon_kind
      :type:  str


   .. py:attribute:: cossic_statement
      :type:  str


   .. py:attribute:: positive_roots
      :type:  tuple[sympy.Expr, ...]


   .. py:attribute:: half_cose
      :type:  sympy.Expr


   .. py:attribute:: half_cose_squared
      :type:  sympy.Expr


   .. py:attribute:: completed_square_area
      :type:  sympy.Expr


.. py:function:: classify_boethian_ratio(p: int | sympy.Expr, q: int | sympy.Expr) -> BoethianClassification

   Classify a positive rational ratio :math:`p : q` according to *Summa* Dist. VI.

   Implements Severinus Boethius's and Pacioli's fivefold taxonomy of greater
   (*maior inaequalitas*) and lesser (*minor inaequalitas*, prefixed ``sub-``)
   inequality on fols. 70r–83r.

   :param p: Positive rational or integer antecedent.
   :param q: Positive rational or integer consequent.

   :returns: Exact :class:`BoethianClassification` record with reduced integers and species name.

   :raises ValueError: If ``p`` or ``q`` is non-positive or non-rational.


.. py:function:: compound_ratios(ratios: list[tuple[int | sympy.Expr, int | sympy.Expr]]) -> BoethianClassification

   Compound a sequence of rational ratios (*proportioni composte*, *Summa* fol. 83r).

   For example, compounding musical *sesquialtera* (:math:`3:2`) and *sesquitertia*
   (:math:`4:3`) yields the octave *dupla* (:math:`2:1`).

   :param ratios: Non-empty list of ``(antecedent, consequent)`` pairs.

   :returns: The :class:`BoethianClassification` of the compounded product ratio.


.. py:function:: apply_six_euclidean_modes(a: int | sympy.Expr, b: int | sympy.Expr, c: int | sympy.Expr, d: int | sympy.Expr, e: int | sympy.Expr | None = None, f: int | sympy.Expr | None = None) -> SixModesResult

   Verify and transform :math:`a:b = c:d` under Pacioli's six modes (*Summa* fol. 74r).

   On fol. 74r (*De sex speciebus sive modis arguendi proportionalitatum*), Pacioli
   enumerates: *conversa* (:math:`b:a = d:c`), *permutata* (:math:`a:c = b:d`),
   *congionta* (:math:`(a+b):b = (c+d):d`), *disgiunta* (:math:`(a-b):b = (c-d):d`),
   *eversa* (:math:`a:(a-b) = c:(c-d)`), and *equa* (:math:`a:e = c:f` when :math:`b:e = d:f`).

   :param a: First antecedent.
   :param b: First consequent.
   :param c: Second antecedent.
   :param d: Second consequent.
   :param e: Optional third term for *proportione equa* (Euclid V.22).
   :param f: Optional sixth term for *proportione equa* (Euclid V.22).

   :returns: Exact :class:`SixModesResult` verifying equality of both sides in every valid mode.


.. py:function:: construct_three_means(a: int | sympy.Expr = 9, b: int | sympy.Expr = 4) -> ThreeMeansResult

   Construct Arithmetic, Geometric, and Harmonic means of :math:`a` and :math:`b` in ``Model``.

   Places collinear points :math:`A=(0,0)`, :math:`P=(a,0)`, :math:`B=(a+b,0)`. In the
   semicircle on diameter :math:`AB` with center :math:`M`:

   - Radius :math:`MQ = (a+b)/2 = A` (Arithmetic mean),
   - Altitude :math:`PQ = \sqrt{ab} = G` (Geometric mean, Euclid ``VI.13``),
   - Leg :math:`QN = 2ab/(a+b) = H` on radius :math:`MQ` where :math:`PN \perp MQ` (Harmonic mean),
     satisfying :math:`PQ^2 = MQ \cdot QN \iff G^2 = A \cdot H`.

   Also constructs the collinear harmonic range :math:`(A, C_H; P, D_H)` with cross-ratio :math:`-1`.

   :param a: First positive exact length (default ``9``, matching *Summa* / *Compendio* ratios).
   :param b: Second positive exact length (default ``4``).

   :returns: Exact :class:`ThreeMeansResult` with proven ``Model`` and exact symbolic means.


.. py:function:: construct_extreme_and_mean_ratio(length: int | sympy.Expr = 10) -> ExtremeMeanResult

   Divide a line of given ``length`` (default ``10``) in extreme and mean ratio.

   Reproduces Pacioli's canonical numerical archetype (*Summa* Dist. VI & Part II Dist. VIII;
   *De Divina Proportione* Cap. VIII–X): for :math:`AB = 10`, the major segment is
   :math:`AC = \sqrt{125} - 5 = 5(\sqrt{5} - 1)` and the minor segment is
   :math:`CB = 15 - \sqrt{125} = 5(3 - \sqrt{5})`, satisfying
   :math:`AB \cdot CB = AC^2 = 150 - 10\sqrt{125}` and Euclid ``XIII.1``
   :math:`(AC + 5)^2 = 125 = 5 \cdot 5^2`.

   :param length: Positive exact length of segment :math:`AB` (default ``10``).

   :returns: Exact :class:`ExtremeMeanResult` with proven ``Model`` and closed-form algebraic parts.


.. py:function:: solve_cossic_quadratic(canon_number: int, a_censi: int | sympy.Expr, b_cose: int | sympy.Expr, c_numero: int | sympy.Expr) -> CossicQuadraticResult

   Solve one of Pacioli's six canonical Cossic equations (*Summa* fols. 145r–146r).

   On fol. 145r, Pacioli classifies positive-coefficient equations into three simple
   (*capitoli semplici*, 1–3) and three compound (*capitoli composti*, 4–6) canons:

   1. ``a .ce. = b .co.`` (:math:`a x^2 = b x`)
   2. ``a .ce. = c`` (:math:`a x^2 = c`)
   3. ``b .co. = c`` (:math:`b x = c`)
   4. ``a .ce. p̄ b .co. = c`` (:math:`a x^2 + b x = c` — *Primi canonis versus*:
      *Si res et census numero coaequantur...*)
   5. ``a .ce. p̄ c = b .co.`` (:math:`a x^2 + c = b x` — *Secundi canonis versus*:
      two positive roots when :math:`(b/(2a))^2 > c/a`)
   6. ``b .co. p̄ c = a .ce.`` (:math:`b x + c = a x^2` — *Tertii canonis versus*)

   :param canon_number: Integer ``1`` through ``6`` selecting Pacioli's canon.
   :param a_censi: Coefficient of *censo* (:math:`x^2`), positive for canons 1, 2, 4, 5, 6.
   :param b_cose: Coefficient of *cosa* (:math:`x`), positive for canons 1, 3, 4, 5, 6.
   :param c_numero: Constant *numero*, positive for canons 2, 3, 4, 5, 6.

   :returns: Exact :class:`CossicQuadraticResult` with Cossic statement, positive root(s),
             and completion-of-the-square gnomon invariants.


