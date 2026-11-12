geometor.pacioli.ledger_conservation
====================================

.. py:module:: geometor.pacioli.ledger_conservation

.. autoapi-nested-parse::

   Exact conservation algebra of Pacioli's Venetian *Quaderno* & *Problem of Points* (1494).

   Models *Part I, Distinctio IX, Tractatus X–XI* (fols. 197r–210v) of Fra Luca Pacioli's
   *Summa de arithmetica, geometria, proportioni et proportionalita* (Venice, 1494):

   1. **Venetian Money of Account** (*fol. 201v*): Exact rational arithmetic in the four
      ledger columns ``l[ire] s[oldi] g[rossi] p[icioli]`` (*a oro*, where
      :math:`1\text{ lira} = 10\text{ ducati} = 20\text{ soldi}`,
      :math:`1\text{ soldo} = 12\text{ grossi}`, :math:`1\text{ ducato} = 24\text{ grossi}`,
      :math:`1\text{ grosso} = 32\text{ piccoli}`).
   2. **Skew-Symmetric Conservation Algebra of Double-Entry Bookkeeping**
      (*Particularis de computis et scripturis*, fols. 198v–210v): Models every *Giornale*
      entry ``Per <Debitore> // A <Creditore>`` as a directed edge in a conservation network
      with oriented incidence matrix :math:`B` (:math:`\mathbf{1}^T B = \mathbf{0}^T`) and
      skew-symmetric flow matrix :math:`F = -F^T`, proving the *Summa summarum* identity
      :math:`\sum \text{Dare} = \sum \text{Avere}`, Pacioli's *Cassa* non-negativity rule
      (fol. 201r), and *Bilancio del libro* closure via *Pro e Danno* :math:`\to` *Capitale*.
   3. **The Problem of Points (*Giuoco della Balla & Balestrare*, fol. 197r–197v)**:
      Exact rational comparison between Pacioli's 1494 past-score proportionality rule and
      the 1654 Pascal–Fermat combinatorial expectation for two or more players.



Classes
-------

.. autoapisummary::

   geometor.pacioli.ledger_conservation.VenetianAmount
   geometor.pacioli.ledger_conservation.JournalEntry
   geometor.pacioli.ledger_conservation.AccountSummary
   geometor.pacioli.ledger_conservation.TrialBalanceReport
   geometor.pacioli.ledger_conservation.ProblemOfPointsResult
   geometor.pacioli.ledger_conservation.QuadernoLedger


Functions
---------

.. autoapisummary::

   geometor.pacioli.ledger_conservation.build_venetian_merchant_quaderno_1493
   geometor.pacioli.ledger_conservation.compare_problem_of_points


Module Contents
---------------

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


