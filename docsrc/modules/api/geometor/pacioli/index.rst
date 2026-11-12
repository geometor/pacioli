geometor.pacioli
================

.. py:module:: geometor.pacioli

.. autoapi-nested-parse::

   Symbolic modeling, digital codex tools, and conservation algebra for Fra Luca Pacioli.

   Provides tools and exact ``SymPy`` / ``geometor.model`` modules spanning both of
   Fra Luca Pacioli's Venetian folio masterpieces printed by Paganino de' Paganini:

   - **Summa de arithmetica, geometria, proportioni et proportionalita (Venice, 1494)**:

     - :mod:`geometor.pacioli.proportions`: Boethian ratio taxonomy, Euclidean *modi arguendi*,
       semicircle construction of the three classical means, golden section of ``10``, and
       Pacioli's six canonical Cossic quadratic equations.
     - :mod:`geometor.pacioli.tractatus_geometriae`: Heron's ``(13, 14, 15)`` triangle
       construction, *De divisione superficierum* proportional cuts, and inscribed Platonic
       and Archimedean solids in the sphere of diameter ``6``.
     - :mod:`geometor.pacioli.ledger_conservation`: Venetian ``l. s. g. p.`` money of account,
       skew-symmetric conservation algebra of the *Quaderno*, and the *Problem of Points*.
     - :mod:`geometor.pacioli.svg_woodcut`: Deterministic ``.euclid-graphic`` SVG generator.

   - **De Divina Proportione (Venice, 1509 / Vienna, 1889)**:

     - :class:`PacioliParser`, folio extraction, and woodcut graphic calibration utilities.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/pacioli/__main__/index
   /modules/api/geometor/pacioli/app/index
   /modules/api/geometor/pacioli/extraction/index
   /modules/api/geometor/pacioli/graphics/index
   /modules/api/geometor/pacioli/ledger_conservation/index
   /modules/api/geometor/pacioli/pacioli/index
   /modules/api/geometor/pacioli/parse_winterberg/index
   /modules/api/geometor/pacioli/parser/index
   /modules/api/geometor/pacioli/proportions/index
   /modules/api/geometor/pacioli/run_parse/index
   /modules/api/geometor/pacioli/run_winterberg_parse/index
   /modules/api/geometor/pacioli/svg_woodcut/index
   /modules/api/geometor/pacioli/tractatus_geometriae/index


Classes
-------

.. autoapisummary::

   geometor.pacioli.AccountSummary
   geometor.pacioli.JournalEntry
   geometor.pacioli.ProblemOfPointsResult
   geometor.pacioli.QuadernoLedger
   geometor.pacioli.TrialBalanceReport
   geometor.pacioli.VenetianAmount
   geometor.pacioli.PacioliParser
   geometor.pacioli.BoethianClassification
   geometor.pacioli.CossicQuadraticResult
   geometor.pacioli.ExtremeMeanResult
   geometor.pacioli.SixModesResult
   geometor.pacioli.ThreeMeansResult
   geometor.pacioli.EuclidGraphicCanvas
   geometor.pacioli.SVGSpec
   geometor.pacioli.DodecahedronAxis48Result
   geometor.pacioli.HeronTriangleResult
   geometor.pacioli.InscribedPolyhedronSpec
   geometor.pacioli.TriangleDivisionResult


Functions
---------

.. autoapisummary::

   geometor.pacioli.extract_all
   geometor.pacioli.build_graphics_index
   geometor.pacioli.clean_image
   geometor.pacioli.detect_graphics_cv
   geometor.pacioli.detect_initials
   geometor.pacioli.detect_margin_figures
   geometor.pacioli.extract_from_json
   geometor.pacioli.build_venetian_merchant_quaderno_1493
   geometor.pacioli.compare_problem_of_points
   geometor.pacioli.apply_six_euclidean_modes
   geometor.pacioli.classify_boethian_ratio
   geometor.pacioli.compound_ratios
   geometor.pacioli.construct_extreme_and_mean_ratio
   geometor.pacioli.construct_three_means
   geometor.pacioli.solve_cossic_quadratic
   geometor.pacioli.generate_all_summa_svgs
   geometor.pacioli.construct_heron_13_14_15
   geometor.pacioli.construct_triangle_division_cevian
   geometor.pacioli.construct_triangle_division_parallel
   geometor.pacioli.dodecahedron_in_sphere_sqrt48
   geometor.pacioli.inscribed_polyhedra_sphere_table


Package Contents
----------------

.. py:function:: extract_all(pdf_path: pathlib.Path, output_dir: pathlib.Path, start_page: int = 1, end_page: int = 318, dpi: int = 150, max_workers: int = 6, force: bool = False) -> None

   Extract page images and text for the entire volume in parallel.


.. py:function:: build_graphics_index(directory: pathlib.Path) -> pathlib.Path

   Compile all per-folio <folio>.json files into graphics_index.json.


.. py:function:: clean_image(pil_image: PIL.Image.Image, white_point: int = 226, preserve_color: bool = False) -> PIL.Image.Image

   Normalize aged parchment background and binding shadows to pure white (255).

   Uses morphological closing + Gaussian blur to estimate local paper illumination per channel,
   eliminating yellowed paper cast, bleed-through, and gutter shadows while preserving crisp ink.
   When ``preserve_color=True`` (e.g., red rubrication on folios 0005 and 0311), chromatic ink is kept.


.. py:function:: detect_graphics_cv(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect full-page plate graphics using OpenCV if available, falling back to SciPy.


.. py:function:: detect_initials(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect woodcut illuminated initial caps by finding 2D ink-density centers along the text column edge.

   Woodcut initials in the 1509 Paganini edition have consistent square dimensions:
   - Standard chapter initials: 120x132 px (padded around the ~112x118 woodcut frame)
   - Large treatise-opening initials (folios 0017 and 0085): 260x304 px
   - Title-page red initial D (folio 0005): 184x188 px


.. py:function:: detect_margin_figures(image_path: pathlib.Path, is_recto: bool) -> List[Dict[str, Any]]

   Detect geometric diagrams and marginalia strictly in the outer margin of a text folio.

   - Odd (recto) folios: right outer margin (to the right of the main text column).
   - Even (verso) folios: left outer margin (to the left of the main text column).
   Never falls back to full-page text blocks.


.. py:function:: extract_from_json(json_path: pathlib.Path, no_clean: bool = False) -> None

   Extract all margin graphics and illuminated initial caps defined in <folio>.json.


.. py:class:: AccountSummary

   T-account summary in the *Quaderno grande* (Dare on left, Avere on right).


   .. py:attribute:: folio
      :type:  int


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: kind
      :type:  str


   .. py:attribute:: dare_ducati
      :type:  sympy.Rational


   .. py:attribute:: avere_ducati
      :type:  sympy.Rational


   .. py:attribute:: net_dare_ducati
      :type:  sympy.Rational


.. py:class:: JournalEntry

   Single Venetian *Giornale* entry ``Per <debit_account> // A <credit_account>``.


   .. py:attribute:: entry_no
      :type:  int


   .. py:attribute:: date
      :type:  str


   .. py:attribute:: debit_account
      :type:  str


   .. py:attribute:: credit_account
      :type:  str


   .. py:attribute:: amount
      :type:  VenetianAmount


   .. py:attribute:: narrative
      :type:  str


   .. py:method:: format_giornale() -> str

      Render the entry in Pacioli's Venetian *Giornale* syntax (fol. 201r–201v).



.. py:class:: ProblemOfPointsResult

   Comparison of Pacioli's 1494 rule vs. Pascal–Fermat 1654 expectation.


   .. py:attribute:: target_rounds
      :type:  int


   .. py:attribute:: current_scores
      :type:  tuple[int, ...]


   .. py:attribute:: total_stake_ducati
      :type:  sympy.Rational


   .. py:attribute:: pacioli_shares
      :type:  tuple[sympy.Rational, ...]


   .. py:attribute:: pascal_fermat_probabilities
      :type:  tuple[sympy.Rational, ...]


   .. py:attribute:: pascal_fermat_shares
      :type:  tuple[sympy.Rational, ...]


   .. py:attribute:: discrepancies
      :type:  tuple[sympy.Rational, ...]


.. py:class:: QuadernoLedger

   Directed-graph conservation model of Pacioli's *Quaderno grande* (Venice, 1494).


   .. py:property:: accounts
      :type: list[str]


      Ordered list of registered ledger accounts.


   .. py:property:: entries
      :type: list[JournalEntry]


      Chronological list of posted *Giornale* entries.


   .. py:method:: register_account(name: str, kind: str = 'real') -> int

      Register an account in the *Alfabeto / Repertorio* and return its *Quaderno* folio.

      :param name: Account title (e.g., ``"Cassa de contanti"``, ``"Cavedal"``).
      :param kind: Account category (``"cassa"``, ``"capitale"``, ``"mercanzia"``,
                   ``"personal"``, ``"nominal"``, ``"pro_e_danno"``, ``"bilancio"``).

      :returns: 1-indexed *Quaderno* folio (*carta*) number.



   .. py:method:: post(date: str, debit_account: str, credit_account: str, amount: VenetianAmount, narrative: str, *, debit_kind: str = 'real', credit_kind: str = 'real') -> JournalEntry

      Post a *Giornale* item ``Per <debit> // A <credit>`` to both *Quaderno* folios.

      Enforces Pacioli's Cap. 14 rule (fol. 202r): *mai si deue mettere cosa in dare
      che quella ancora non si ponga in hauere*.

      :param date: Venetian entry date string.
      :param debit_account: Debtor account prefixed by ``Per``.
      :param credit_account: Creditor account prefixed by ``A``.
      :param amount: Strictly positive :class:`VenetianAmount`.
      :param narrative: Brief *Giornale* description distilled from the *Memoriale*.
      :param debit_kind: Category if ``debit_account`` is not yet registered.
      :param credit_kind: Category if ``credit_account`` is not yet registered.

      :returns: The recorded :class:`JournalEntry`.



   .. py:method:: incidence_matrix() -> sympy.Matrix

      Return oriented vertex-edge incidence matrix :math:`B \in \{-1, 0, +1\}^{|V| \times |E|}`.

      For entry :math:`e` (``Per u // A v``), :math:`B_{u, e} = +1` (Dare) and
      :math:`B_{v, e} = -1` (Avere), so :math:`\mathbf{1}^T B = \mathbf{0}^T`.



   .. py:method:: weight_vector_ducati() -> sympy.Matrix

      Return column vector :math:`w \in \mathbb{Q}^{|E|}` of transaction weights in ducats.



   .. py:method:: skew_symmetric_flow_matrix() -> sympy.Matrix

      Return skew-symmetric pairwise flow matrix :math:`F \in \mathbb{Q}^{|V| \times |V|}`.

      Entry :math:`F_{i,j}` equals net ducats debited to account :math:`i` against credit
      to account :math:`j`, satisfying :math:`F^T = -F` identically.



   .. py:method:: trial_balance() -> TrialBalanceReport

      Compute Pacioli's *Summa summarum* and verify all conservation invariants.



   .. py:method:: close_to_bilancio(date: str = '1493-12-31', pro_e_danno_account: str = 'Pro e Danno', capitale_account: str = 'Cavedal', bilancio_account: str = 'Bilancio del libro') -> sympy.Rational

      Execute Pacioli's Cap. 27 & Cap. 34 closing cycle (*Pro e Danno* -> *Cavedal* -> *Bilancio*).

      First sweeps all ``"mercanzia"`` (closed venture) and ``"nominal"`` accounts into
      *Pro e Danno*, transfers net profit/loss from *Pro e Danno* to *Cavedal* (Cap. 27),
      and finally closes all remaining open asset/liability/capital accounts into
      *Bilancio del libro* (Cap. 34), bringing every account's net balance to ``0``.

      :param date: Closing date string.
      :param pro_e_danno_account: Profit-and-loss summary account name.
      :param capitale_account: Merchant's capital account name.
      :param bilancio_account: Final closing balance account name.

      :returns: Exact net profit (positive) or loss (negative) in ducats transferred to *Cavedal*.



.. py:class:: TrialBalanceReport

   Exact *Summa summarum* and conservation verification of the *Quaderno*.


   .. py:attribute:: accounts
      :type:  tuple[AccountSummary, ...]


   .. py:attribute:: summa_dare_ducati
      :type:  sympy.Rational


   .. py:attribute:: summa_avere_ducati
      :type:  sympy.Rational


   .. py:attribute:: net_conservation_sum
      :type:  sympy.Rational


   .. py:attribute:: is_balanced
      :type:  bool


   .. py:attribute:: cassa_non_negative
      :type:  bool


.. py:class:: VenetianAmount

   Exact Venetian money of account (``lire, soldi, grossi, piccoli`` *a oro*, fol. 201v).


   .. py:attribute:: piccoli_total
      :type:  sympy.Integer


   .. py:method:: from_lsgp(lire: int = 0, soldi: int = 0, grossi: int = 0, piccoli: int = 0) -> VenetianAmount
      :classmethod:


      Construct an exact amount from ``(lire, soldi, grossi, piccoli)`` columns.



   .. py:method:: from_ducati(ducati: int = 0, grossi: int = 0, piccoli: int = 0) -> VenetianAmount
      :classmethod:


      Construct an exact amount from Venetian gold ducats (``24 grossi = 1 ducato``).



   .. py:method:: to_lsgp() -> tuple[int, int, int, int]

      Decompose into canonical ``(lire, soldi, grossi, piccoli)`` columns.



   .. py:method:: to_ducati_rational() -> sympy.Rational

      Express the exact value in Venetian gold ducats as a ``sympy.Rational``.



   .. py:method:: to_lire_rational() -> sympy.Rational

      Express the exact value in Venetian *lire di grossi* as a ``sympy.Rational``.



   .. py:method:: format_venetian() -> str

      Format in Pacioli's four-column Venetian ledger notation (``l. s. g. p.``).



   .. py:method:: __add__(other: VenetianAmount) -> VenetianAmount

      Add two exact Venetian amounts.



   .. py:method:: __sub__(other: VenetianAmount) -> VenetianAmount

      Subtract two exact Venetian amounts.



.. py:function:: build_venetian_merchant_quaderno_1493() -> QuadernoLedger

   Construct a canonical Venetian *Quaderno* modeled on *Summa* fols. 201v–210r (Nov. 1493).

   Includes opening inventory of cash and gems against *Cavedal*, purchase of sugar
   and Ginger (*zenzer mechini*, fol. 201v item 7), credit sale to Martino da Foro,
   brokerage expense (*Spese de mercanzia*), partial cash settlement, and profit transfer.

   :returns: Populated :class:`QuadernoLedger` prior to final closing.


.. py:function:: compare_problem_of_points(target_rounds: int = 6, current_scores: tuple[int, ...] = (5, 3), total_stake_ducati: int | sympy.Expr = 10) -> ProblemOfPointsResult

   Compare Pacioli's 1494 *balla* / *balestrare* division against Pascal–Fermat (1654).

   Covers both the classic two-player *giuoco della balla* on fol. 197r (e.g., ``(5, 3)``
   or ``(5, 2)`` playing to ``6`` for ``10`` ducats) and Problem 51 on fol. 197v
   (three crossbowmen *a balestrare* playing to ``6`` best shots for ``10`` ducats,
   interrupted at ``(4, 3, 2)``).

   :param target_rounds: Winning score threshold (e.g., ``6``).
   :param current_scores: Tuple of positive/non-negative scores below ``target_rounds``.
   :param total_stake_ducati: Total pot in ducats (default ``10``).

   :returns: Exact :class:`ProblemOfPointsResult` with `sp.Rational` shares and discrepancies.


.. py:class:: PacioliParser(resources_dir: pathlib.Path, output_dir: pathlib.Path)

   .. py:attribute:: resources_dir


   .. py:attribute:: output_dir


   .. py:attribute:: transcribed_file


   .. py:method:: parse()

      Execute the parsing process.

      This method orchestrates the extraction of TOC and text chapters,
      merges them, and generates the RST output structure.



   .. py:method:: create_root_index(book_names: List[str])


   .. py:method:: process_book(lines: List[str], book_config: Dict)


   .. py:method:: extract_chapters(lines: List[str], start_marker: str, end_marker: str, prefix: str) -> Dict[str, Dict]

      Extract chapters from a section of lines.

      :param lines: The list of lines to process.
      :param start_marker: The string marking the start of the section.
      :param end_marker: The string marking the end of the section.
      :param prefix: The prefix for chapter headers (e.g., "Cap", "Gap").

      :returns: A dictionary of chapters keyed by Roman Numeral ID.
      :rtype: dict



   .. py:method:: merge_chapters(toc_chapters: Dict, text_chapters: Dict) -> List[Dict]

      Merge TOC and Text chapters into a single list.

      :param toc_chapters: Dictionary of chapters extracted from the TOC.
      :param text_chapters: Dictionary of chapters extracted from the text.

      :returns: A list of merged chapter dictionaries, sorted by Roman Numeral ID.
      :rtype: list



   .. py:method:: generate_rst_structure(chapters: List[Dict], output_dir: pathlib.Path)

      Generate the RST folder structure and files for the chapters.

      :param chapters: List of chapter dictionaries.
      :param output_dir: The directory where RST files will be generated.



   .. py:method:: create_main_index(chapters: List[Dict], output_dir: pathlib.Path)


   .. py:method:: create_chapter_files(chapter_dir: pathlib.Path, chapter: Dict)


   .. py:method:: indent_text(text: str, indent: str = '   ') -> str


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


.. py:class:: EuclidGraphicCanvas(*, width: int, height: int, graphic_id: str, folio: str, proposition: str, scale: float = 1.0, origin_x: float = 0.0, origin_y: float = 0.0)

   Builder for standard 5-layer ``.euclid-graphic`` interactive SVGs.


   .. py:attribute:: width


   .. py:attribute:: height


   .. py:attribute:: graphic_id


   .. py:attribute:: folio


   .. py:attribute:: proposition


   .. py:attribute:: scale
      :value: 1.0



   .. py:attribute:: origin_x
      :value: 0.0



   .. py:attribute:: origin_y
      :value: 0.0



   .. py:method:: to_px(x: float | int | sympy.Expr, y: float | int | sympy.Expr) -> tuple[float, float]

      Map exact mathematical ``(x, y)`` (y-up) to SVG screen coordinates (y-down).



   .. py:method:: add_circle(el_id: str, cx: float | int | sympy.Expr, cy: float | int | sympy.Expr, r: float | int | sympy.Expr, *, data_ref: str = '', css_class: str = 'geom-circle') -> None

      Add a circle to ``#elements`` and ``#highlights``.



   .. py:method:: add_arc(el_id: str, cx: float | int | sympy.Expr, cy: float | int | sympy.Expr, r: float | int | sympy.Expr, deg_start: float, deg_end: float, *, data_ref: str = '', css_class: str = 'geom-arc') -> None

      Add a circular arc (math degrees counter-clockwise from +x) to ``#elements``.



   .. py:method:: add_polygon(el_id: str, vertices: list[tuple[float | int | sympy.Expr, float | int | sympy.Expr]], *, data_ref: str = '', css_class: str = 'geom-polygon') -> None

      Add a filled polygon to ``#graphics`` and ``#highlights``.



   .. py:method:: add_segment(el_id: str, p1: tuple[float | int | sympy.Expr, float | int | sympy.Expr], p2: tuple[float | int | sympy.Expr, float | int | sympy.Expr], *, data_ref: str = '', css_class: str = 'geom-line') -> None

      Add a 3-vertex midpoint segment path ``M x1 y1 L xm ym L x2 y2`` to ``#graphics``.



   .. py:method:: add_point(pt_id: str, x: float | int | sympy.Expr, y: float | int | sympy.Expr, *, label: str | None = None, dx: float = 0.0, dy: float = -10.0, anchor: str = 'middle', radius: float = 3.4) -> None

      Add a point circle in ``#points`` and optional label in ``#labels``.



   .. py:method:: add_annotation(ann_id: str, x: float | int | sympy.Expr, y: float | int | sympy.Expr, text: str, *, anchor: str = 'middle', data_ref: str = '') -> None

      Add a compact mathematical or woodcut caption inside ``#labels``.



   .. py:method:: render() -> str

      Serialize the complete 5-layer ``.euclid-graphic`` SVG XML string.



.. py:class:: SVGSpec

   Metadata describing a generated *Summa* ``.euclid-graphic`` SVG plate.


   .. py:attribute:: graphic_id
      :type:  str


   .. py:attribute:: unit_dir
      :type:  str


   .. py:attribute:: filename
      :type:  str


   .. py:attribute:: folio
      :type:  str


   .. py:attribute:: proposition
      :type:  str


   .. py:attribute:: path
      :type:  pathlib.Path


.. py:function:: generate_all_summa_svgs(summa_docsrc_dir: pathlib.Path | str) -> list[SVGSpec]

   Generate and write all nine ``.euclid-graphic`` SVGs into ``docsrc/summa_1494/``.

   :param summa_docsrc_dir: Target root directory (typically ``<repo>/docsrc/summa_1494``).

   :returns: Ordered list of :class:`SVGSpec` records written to disk.


.. py:class:: DodecahedronAxis48Result

   Exact symbolic metrics for Problem 21 on Part II, fol. 70r (sphere axis ``sqrt(48)``).


   .. py:attribute:: sphere_axis_squared
      :type:  sympy.Integer


   .. py:attribute:: sphere_axis
      :type:  sympy.Expr


   .. py:attribute:: inscribed_cube_edge_squared
      :type:  sympy.Integer


   .. py:attribute:: inscribed_cube_edge
      :type:  sympy.Integer


   .. py:attribute:: dodecahedron_edge
      :type:  sympy.Expr


   .. py:attribute:: extreme_mean_minor_part
      :type:  sympy.Expr


.. py:class:: HeronTriangleResult

   Exact symbolic invariants of Pacioli's ``(13, 14, 15)`` triangle (Part II, fol. 9v).


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: pt_g
      :type:  sympy.geometry.Point


   .. py:attribute:: pt_b
      :type:  sympy.geometry.Point


   .. py:attribute:: pt_a
      :type:  sympy.geometry.Point


   .. py:attribute:: pt_d
      :type:  sympy.geometry.Point


   .. py:attribute:: incenter
      :type:  sympy.geometry.Point


   .. py:attribute:: circumcenter
      :type:  sympy.geometry.Point


   .. py:attribute:: sides
      :type:  tuple[sympy.Integer, sympy.Integer, sympy.Integer]


   .. py:attribute:: perimeter
      :type:  sympy.Integer


   .. py:attribute:: semiperimeter
      :type:  sympy.Integer


   .. py:attribute:: excesses
      :type:  tuple[sympy.Integer, sympy.Integer, sympy.Integer]


   .. py:attribute:: heron_radicand
      :type:  sympy.Integer


   .. py:attribute:: area
      :type:  sympy.Integer


   .. py:attribute:: altitude
      :type:  sympy.Integer


   .. py:attribute:: base_segments
      :type:  tuple[sympy.Integer, sympy.Integer]


   .. py:attribute:: inradius
      :type:  sympy.Integer


   .. py:attribute:: circumradius
      :type:  sympy.Rational


.. py:class:: InscribedPolyhedronSpec

   Exact symbolic metrics of a regular or Archimedean solid in a sphere of diameter ``D``.


   .. py:attribute:: key
      :type:  str


   .. py:attribute:: italian_name
      :type:  str


   .. py:attribute:: faces_description
      :type:  str


   .. py:attribute:: sphere_diameter
      :type:  sympy.Expr


   .. py:attribute:: edge_squared
      :type:  sympy.Expr


   .. py:attribute:: edge
      :type:  sympy.Expr


   .. py:attribute:: surface_area
      :type:  sympy.Expr


   .. py:attribute:: volume
      :type:  sympy.Expr


   .. py:attribute:: folio_citation
      :type:  str


.. py:class:: TriangleDivisionResult

   Exact symbolic outputs for dividing a triangle's area in ratio ``p : q``.


   .. py:attribute:: model
      :type:  geometor.model.Model


   .. py:attribute:: method
      :type:  str


   .. py:attribute:: ratio_p
      :type:  sympy.Integer


   .. py:attribute:: ratio_q
      :type:  sympy.Integer


   .. py:attribute:: total_area
      :type:  sympy.Expr


   .. py:attribute:: part_1_area
      :type:  sympy.Expr


   .. py:attribute:: part_2_area
      :type:  sympy.Expr


   .. py:attribute:: cut_points
      :type:  tuple[sympy.geometry.Point, ...]


.. py:function:: construct_heron_13_14_15() -> HeronTriangleResult

   Construct and verify Pacioli's ``(13, 14, 15)`` Heron triangle (Part II, fol. 9v).

   On Part II, fol. 9v (*Distinctio prima, Capitulum octavum*), Pacioli computes for
   :math:`\triangle ABG` with :math:`AG=13`, :math:`BG=14`, :math:`AB=15`:

   - Perimeter :math:`13 + 14 + 15 = 42`, semiperimeter :math:`s = 21`,
   - Excesses :math:`(s - 15, s - 14, s - 13) = (6, 7, 8)`,
   - Product :math:`6 \cdot 7 \cdot 8 = 336`, and :math:`336 \cdot 21 = 7056`,
   - Area :math:`\sqrt{7056} = 84` *braccia quadre*, cathetus :math:`AD = 12`, segments :math:`5, 9`.

   :returns: Exact :class:`HeronTriangleResult` containing the proven ``Model`` and invariants.


.. py:function:: construct_triangle_division_cevian(ratio_p: int = 1, ratio_q: int = 2) -> TriangleDivisionResult

   Divide :math:`\triangle GBA` (``13, 14, 15``) in ratio ``p : q`` by a vertex cevian.

   Implements the first problem of *Part II, Distinctio IV: De divisione superficierum*
   (following Euclid ``VI.1`` and Leonardo Pisano's *Practica Geometriae*): dividing base
   :math:`GB` at :math:`K` in ratio :math:`p : q` via Thales's intercept construction (``VI.10``)
   so :math:`\text{Area}(\triangle GAK) : \text{Area}(\triangle KAB) = p : q`.

   :param ratio_p: Positive integer share adjacent to ``G`` (default ``1``).
   :param ratio_q: Positive integer share adjacent to ``B`` (default ``2``).

   :returns: Exact :class:`TriangleDivisionResult` with verified polygonal areas.


.. py:function:: construct_triangle_division_parallel(ratio_p: int = 1, ratio_q: int = 1) -> TriangleDivisionResult

   Divide :math:`\triangle GBA` in ratio ``p : q`` by a cut parallel to side ``BA``.

   Implements Pacioli's *De divisione superficierum* (*Part II, Distinctio IV*, Euclid
   ``VI.13`` + ``VI.19``): to cut off :math:`\triangle GUV \sim \triangle GBA` with
   :math:`\text{Area}(\triangle GUV) / \text{Area}(\triangle GBA) = p / (p + q)`, first divide
   :math:`GB` at :math:`K` with :math:`GK / GB = p / (p+q)`, then construct the geometric mean
   :math:`GU = \sqrt{GB \cdot GK}` via a semicircle on :math:`GB` and draw :math:`UV \parallel BA`.

   :param ratio_p: Positive integer share for sub-triangle ``GUV`` (default ``1``, bisecting area).
   :param ratio_q: Positive integer share for trapezoid ``UBAV`` (default ``1``).

   :returns: Exact :class:`TriangleDivisionResult` with verified radical cut coordinates and rational areas.


.. py:function:: dodecahedron_in_sphere_sqrt48() -> DodecahedronAxis48Result

   Reproduce Problem 21 on Part II, fol. 70r (dodecahedron in sphere of axis ``sqrt(48)``).

   On fol. 70r, Pacioli takes a sphere whose axis has squared length (*possanza*) ``48``:
   by Euclid ``XIII.15``, the inscribed cube has squared edge ``48 / 3 = 16``, so edge ``4``;
   dividing ``4`` in extreme and mean ratio (Campanus ``XIV.18`` / Euclid ``XIII.17`` corollary)
   yields major part ``sqrt(20) - 2`` (the dodecahedron edge) and minor part ``6 - sqrt(20)``.

   :returns: Exact :class:`DodecahedronAxis48Result` verified against :func:`inscribed_polyhedra_sphere_table`.


.. py:function:: inscribed_polyhedra_sphere_table(diameter: int | sympy.Expr = 6) -> dict[str, InscribedPolyhedronSpec]

   Compute exact symbolic metrics for regular & Archimedean solids in a sphere of diameter ``D``.

   Defaults to ``diameter = 6`` (*Summa* Part II, *Distinctio VIII: De corporibus regularibus*,
   fol. 69v–70r), reproducing both Euclid Book XIII's five regular solids and Pacioli's
   dependent Archimedean solids inherited from Piero della Francesca:

   - ``truncated_tetrahedron`` (fol. 69v, prob. 15–16): :math:`e^2 = \frac{2}{11} D^2`
     (:math:`= \frac{72}{11} = 6\frac{6}{11}` for :math:`D=6`, matching Pacioli's ``℞.6 6/11``!).
   - ``cuboctahedron`` (fol. 69v–70r, prob. 17–19): :math:`e = \frac{1}{2} D`
     (:math:`= 3` *braccia* for :math:`D=6`).

   :param diameter: Exact positive sphere diameter ``D`` (default ``6``).

   :returns: Dictionary mapping solid keys to :class:`InscribedPolyhedronSpec`.


