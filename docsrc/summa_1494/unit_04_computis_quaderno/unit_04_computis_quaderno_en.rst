:layout: book
:canonical_id: Summa I, Dist. IX, Tract. X–XI
:folio: Part I, fols. 197r–210v

.. _summa-unit-04:
.. _summa-unit-04-en:

UNIT IV — PARTICULARIS DE COMPUTIS ET SCRIPTURIS & THE PROBLEM OF POINTS
========================================================================

.. rubric:: Part I, Distinctio IX, Tractatus X–XI: Interrupted Games of Chance (`fol. 197r–197v`) & Venetian Double-Entry Bookkeeping (`fols. 198v–210v`)

.. folio:: Part I, fols. 197r–197v

.. rubric:: The Problem of Points (*Giuoco della Balla* & *Balestrare*)

Immediately preceding his bookkeeping treatise, at the close of *Tractatus X* (`fols. 197r–197v`), :person:`Fra Luca Pacioli <pacioli>` poses in print for the first time the celebrated **Problem of Points** (:term:`giuoco della balla <balla>`), destined to launch mathematical probability in the July–October 1654 correspondence between :person:`Blaise Pascal <pascal>` and :person:`Pierre de Fermat <fermat>` (:cite:`*La règle des partis* <pascal-fermat:correspondence-1654>`):

- **Two-Player Ball Game (`fol. 197r`)**: A company plays *a balla* to $60$ points (at $10$ points per winning *caccia*—i.e., first to **$6$ rounds**) for a stake of **$10$ ducats**; forced by an accident to break off when one side has $50$ ($5$ rounds) and the other $30$ ($3$ rounds, or $20$), how should the $10$ ducats be divided?
- **Problem 51 — Three Crossbowmen (`fol. 197v`)**: Three companions compete *a balestrare* ("whoever first achieves **$6$ best shots** wins **$10$ ducats**"); interrupted when the first has **$4$** shots, the second **$3$**, and the third **$2$**, how much belongs to each?

Treating the contest like a commercial partnership (*compagnia*), Pacioli divides the stake proportionally to **rounds already achieved**: $\left(\frac{5}{8}, \frac{3}{8}\right) \times 10 = \left(6\frac{1}{4}, 3\frac{3}{4}\right)$ ducats for $(5, 3)$, and $\left(\frac{4}{9}, \frac{3}{9}, \frac{2}{9}\right) \times 10 = \left(4\frac{4}{9}, 3\frac{1}{3}, 2\frac{2}{9}\right)$ ducats for $(4, 3, 2)$—whereas :person:`Pascal <pascal>` and :person:`Fermat <fermat>` look forward to the **remaining rounds needed** ($1$ vs. $3$ in the two-player game), yielding exact fair probabilities $\left(\frac{7}{8}, \frac{1}{8}\right) \implies \left(8\frac{3}{4}, 1\frac{1}{4}\right)$ ducats, and $\left(\frac{451}{729}, \frac{195}{729}, \frac{83}{729}\right) \times 10$ ducats in the three-player crossbow match.

.. folio:: Part I, fols. 198v–210v

.. rubric:: *Particularis de Computis et Scripturis* — Double-Entry Bookkeeping *al Modo de Vinegia*

On `fol. 198v`, Pacioli opens the world's first printed treatise on **double-entry bookkeeping** (*Tractatus XI*, 36 chapters), declaring that three things above all are required by anyone who wishes to trade with due diligence: (1) ready cash (*la pecunia numerata*) or solid credit, (2) mastery as a good reckoner (*buon ragionieri*), and (3) **systematic ordering of every affair in Dare and Avere** so that he may know at a glance both his debt and his credit.

1. **The Opening Inventory (`Cap. 2–3, fols. 198v–199r`)**: Drawn up on a single day (exemplified on **November 8, 1493**), recording all cash, jewels, ginger, real estate, debtors, and creditors.
2. **The Three Principal Books (`Cap. 5–14, fols. 199v–202r`)**, authenticated and stamped at the Venetian *Consoli de' Mercanti* (`Cap. 7`):
   - :term:`**Memoriale** <memoriale>` (*Squarzo* / *Vacchetta*): Day-book recording raw transactions hour-by-hour in whatever foreign or local coin occurred.
   - :term:`**Giornale** <giornale>`: Private chronological journal converting every item into uniform Venetian money of account via the formula :term:`**Per <Debitore> // A <Creditore>** <per-a>` (`Cap. 11, fol. 201r`), cross-referenced by a fraction $\frac{\text{Carta Dare}}{\text{Carta Avere}}$.
   - :term:`**Quaderno Grande** <quaderno>`: General ledger with alphabetical *Repertorio*, placing **Dare** (debits) on the left *man sinistra* and **Avere** (credits) on the facing right *man dextra* across four columns of :term:`Venetian money of account <ducato-di-conto>` (`fol. 201v`): **lire**, **soldi**, **grossi**, and **piccoli** ($1\text{ lira} = 10\text{ ducati} = 20\text{ soldi}$; $1\text{ ducato} = 24\text{ grossi}$; $1\text{ grosso} = 32\text{ piccoli}$).

.. picture:: fig_06_quaderno_conservation.svg
   :alt: Skew-symmetric directed conservation network of Pacioli's Venetian Quaderno

.. enunciation::

   **Fundamental Conservation Law of the Quaderno (`Cap. 14, fol. 202r`):**
   *"Never must anything be placed in **Dare** that is not also placed in the same amount in **Avere**, and conversely never must anything be placed in **Avere** that is not placed in the same amount in **Dare**; whence at the closing balance of the book, **the grand total of Dare must equal the grand total of Avere**."*

.. assertion:: [Euclid I.cn.2 & Skew-Symmetric Conservation] <I.cn.2>

   In the directed ledger network inscribed on circle :g:`(OK) <summa.I.9.quaderno:( O K )>`, each *Giornale* entry ``Per u // A v`` of weight $w_e > 0$ forms an oriented chord between accounts :g:`K (Cavedal) <summa.I.9.quaderno:K>`, :g:`S (Cassa) <summa.I.9.quaderno:S>`, :g:`M (Zenzer) <summa.I.9.quaderno:M>`, :g:`D (Martino) <summa.I.9.quaderno:D>`, :g:`P (Pro e Danno) <summa.I.9.quaderno:P>`, and :g:`B (Bilancio) <summa.I.9.quaderno:B>`. Opening cash :g:`KS <summa.I.9.quaderno:/ K S />` (`Per Cassa // A Cavedal`), ginger purchase :g:`SM <summa.I.9.quaderno:/ S M />`, credit sale :g:`MD <summa.I.9.quaderno:/ M D />` and gain :g:`DP <summa.I.9.quaderno:/ D P />`, collection :g:`DS <summa.I.9.quaderno:/ D S />`, and profit transfer :g:`PK <summa.I.9.quaderno:/ P K />` trace the closed trading cycle :g:`KSMDP <summa.I.9.quaderno:< K S M D P >>`. Because every column of the oriented vertex–edge incidence matrix $B \in \{-1, 0, +1\}^{|V| \times |E|}$ contains exactly one $+1$ (*Dare*) and one $-1$ (*Avere*), the pairwise flow matrix $F_{ij}$ is **skew-symmetric** ($F^T = -F$), and:

   $$\mathbf{1}^T B = \mathbf{0}^T \implies \sum_{u \in V} (\text{Dare}_u - \text{Avere}_u) = \mathbf{1}^T (B w) = 0 \iff \text{Summa}(\text{Dare}) = \text{Summa}(\text{Avere})$$

.. qed::

   Together with the domain invariant of `Cap. 12` (`fol. 201r`) that :term:`Cassa <cassa>` can **never have a net credit balance** ($\text{Dare}_{\text{Cassa}} - \text{Avere}_{\text{Cassa}} \ge 0$, since no merchant can pay out more physical coin than has entered the chest), sweeping nominal accounts through :term:`Pro e Danno <pro-e-danno>` into :term:`Cavedal <cavedal>` (`Cap. 27`) and closing open accounts via :g:`SB <summa.I.9.quaderno:/ S B />` and :g:`KB <summa.I.9.quaderno:/ K B />` into :term:`Bilancio del libro <bilancio-del-libro>` (`Cap. 34`) establishes the exact :term:`Summa summarum <summa-summarum>` equilibrium of modern accounting.
