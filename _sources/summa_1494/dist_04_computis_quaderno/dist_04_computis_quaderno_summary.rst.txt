:layout: book
:canonical_id: Summa I, Dist. IX, Tract. X–XI
:folio: Part I, fols. 197r–210v

.. _summa-unit-04-summary:

CONSERVATION ALGEBRA & PROBABILITY SUMMARY
==========================================

.. rubric:: Symbolic Matrix Formulation of the *Quaderno* & Exact *Problem of Points* Shares

1. Venetian Four-Column Currency Radix (`fol. 201v`)
----------------------------------------------------

.. math::

   \begin{aligned}
   1 \text{ grosso} &= 32 \text{ piccoli}, &
   1 \text{ soldo} &= 12 \text{ grossi} = 384 \text{ piccoli}, \\
   1 \text{ ducato} &= 24 \text{ grossi} = 2 \text{ soldi} = 768 \text{ piccoli}, &
   1 \text{ lira a oro} &= 20 \text{ soldi} = 10 \text{ ducati} = 7{,}680 \text{ piccoli}.
   \end{aligned}

2. Graph-Theoretic Conservation Laws (:mod:`geometor.pacioli.ledger_conservation`)
----------------------------------------------------------------------------------

Let :math:`V = \{1, \dots, n\}` be the registered *Quaderno* accounts and :math:`E = \{1, \dots, m\}` the chronological *Giornale* postings :math:`e_k = (u_k, v_k, w_k)` (`Per u_k // A v_k` of positive weight :math:`w_k \in \mathbb{Q}_{>0}`):

- **Oriented Incidence Matrix** :math:`B \in \{-1, 0, +1\}^{n \times m}`: :math:`B_{u_k, k} = +1`, :math:`B_{v_k, k} = -1`, so :math:`\mathbf{1}^T B = \mathbf{0}^T`.
- **Skew-Symmetric Pairwise Flow Matrix** :math:`F \in \mathbb{Q}^{n \times n}`: :math:`F_{ij} = \sum_{e: (i,j)} w_e - \sum_{e: (j,i)} w_e = -F_{ji}` (:math:`F^T = -F`).
- **Summa Summarum Identity**: :math:`\sum_{i=1}^n \text{Dare}_i = \sum_{k=1}^m w_k = \sum_{i=1}^n \text{Avere}_i`, and :math:`\mathbf{1}^T (B w) = 0`.
- **Cap. 12 Cash Non-Negativity**: :math:`(B w)_{\text{Cassa}} \ge 0` after every prefix of postings.
- **Cap. 27 & Cap. 34 Closing Cycle**: Sweeping nominal accounts into *Pro e Danno*, transferring net profit to *Cavedal*, and sweeping open balances into *Bilancio del libro* drives :math:`B_{\text{closed}} w_{\text{closed}} = \mathbf{0}`.

3. Pacioli (1494) vs. Pascal–Fermat (1654) on `fol. 197r–197v`
--------------------------------------------------------------

.. list-table:: Exact Stake Divisions for Pot = :math:`10` Ducats, Target = :math:`6` Rounds
   :header-rows: 1
   :widths: 28 24 28 20

   * - Interrupted Contest
     - Pacioli 1494 (Past Scores)
     - Pascal–Fermat 1654 (Future Paths)
     - Difference (:math:`\text{PF} - \text{Pac}`)
   * - **2-Player Balla** :math:`(5, 3)`
     - :math:`\frac{25}{4}, \; \frac{15}{4}` (:math:`6.25, \; 3.75`)
     - :math:`\frac{35}{4}, \; \frac{5}{4}` (:math:`8.75, \; 1.25`)
     - :math:`+\frac{5}{2}, \; -\frac{5}{2}`
   * - **2-Player Balla** :math:`(5, 2)`
     - :math:`\frac{50}{7}, \; \frac{20}{7}`
     - :math:`\frac{150}{16} = \frac{75}{8}, \; \frac{5}{8}`
     - :math:`+\frac{125}{56}, \; -\frac{125}{56}`
   * - **3-Player Balestrare** :math:`(4, 3, 2)`
     - :math:`\frac{40}{9}, \; \frac{30}{9}, \; \frac{20}{9}`
     - :math:`\frac{4510}{729}, \; \frac{1950}{729}, \; \frac{830}{729}`
     - :math:`+\frac{1270}{729}, \; -\frac{480}{729}, \; -\frac{790}{729}`
