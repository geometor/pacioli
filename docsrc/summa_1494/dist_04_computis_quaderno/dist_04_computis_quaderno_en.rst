:layout: book
:canonical_id: Summa I, Dist. IX, Tract. X–XI
:folio: Part I, fols. 197r–210v

.. _summa-unit-04:
.. _summa-unit-04-en:

PARTICULARIS DE COMPUTIS ET SCRIPTURIS & THE PROBLEM OF POINTS
==============================================================

.. rubric:: Part I, Distinctio IX, Tractatus X–XI: Interrupted Games of Chance (`fol. 197r–197v`) & Venetian Double-Entry Bookkeeping (`fols. 198v–210v`)

.. folio:: Part I, fols. 197r–197v

.. rubric:: The Game of Ball (*Giuoco della Balla*) & Problem 51 (*A Balestrare*)

- **Game of Ball (`fol. 197r`)**: A company plays :term:`at ball (*a balla*) <balla>` to **$60$**, and each winning chase (*caccia*) is worth **$10$**; they lay down a stake of **$10$ ducats**. By certain accidents they cannot finish: one side finds itself with **$50$** and the other with **$20$** (or **$30$**). It is asked what share belongs to each side out of the said $10$ ducats.
- **Problem 51 — Three Crossbowmen (`fol. 197v`)**: Three companions set themselves to shoot **with the crossbow** (*a balestrare*) upon this agreement: that whoever first makes **$6$ best shots** shall win **$10$ ducats**. It happens that when the first has made **$4$** best shots, the second **$3$**, and the third **$2$**, they wish to shoot no more and by mutual consent wish to divide the stake: I ask what each ought to have.

Dividing the stake in the manner of a commercial partnership (*compagnia*) proportionally to the rounds won yields $\left(\frac{5}{8}, \frac{3}{8}\right) \times 10 = \left(6\frac{1}{4}, 3\frac{3}{4}\right)$ ducats for $(5, 3)$, and $\left(\frac{4}{9}, \frac{3}{9}, \frac{2}{9}\right) \times 10 = \left(4\frac{4}{9}, 3\frac{1}{3}, 2\frac{2}{9}\right)$ ducats for $(4, 3, 2)$.

.. folio:: Part I, fols. 198v–210v

.. rubric:: *Distinctio Nona — Tractatus XI: Particularis de Computis et Scripturis* (Cap. 1–14)

Since, as has been said, three things above all are needful to everyone who intends to attend to trade with due order (`Cap. 1, fol. 198v`):

1. The first and most principal is **ready counted cash** (*la pecunia numerata*) and every other substantial faculty.
2. The second thing required for due commerce is that one **be a good reckoner and prompt accountant** (*buon ragionieri e pronto computista*).
3. The third and final needful thing is **that one arrange all one's affairs in fair and due order**, so that with brevity one may have knowledge of each item as to both its **debit** (*debito*) and its **credit** (*credito*). And herein we shall observe **the manner of Venice** (*el modo de Vinegia*), which certainly above all others is greatly to be commended.

Before trading, draw up the **Opening Inventory** on a single day (`Cap. 2–3, fols. 198v–199r`, exemplified on November 8, 1493), and maintain the **Three Principal Books** (`Cap. 5–14, fols. 199v–202r`), presented first to the Venetian *Consoli de' Mercanti* (`Cap. 7`):

- :term:`**Memoriale** <memoriale>` (*Squarzo* / *Vacchetta*): Day-book recording all transactions hour-by-hour in whatever coin they occur.
- :term:`**Giornale** <giornale>`: Private chronological journal wherein two terms are used (`Cap. 11–12, fol. 201r`): :term:`**Per** <per-a>` always denotes the **debtor**, and **A** denotes the **creditor**. And note that :term:`**Cassa** <cassa>` **is always debtor or even, and can never be creditor**—for if in the balance Cash should remain creditor, it would denote error in the book, since no one can spend what he did not have in the chest. By :term:`**Cavedal** <cavedal>` is understood your entire present capital stock. Thus runs the first entry of the Journal (`fol. 201v`): *M.cccc.xciii, on the 8th day of November in Venice. Per Cash in coin // A Capital of myself, etc.*
- :term:`**Quaderno Grande** <quaderno>`: General ledger with alphabetical *Repertorio*, setting **Dare** on the left hand and **Avere** on the right hand across four columns of :term:`Venetian money of account <ducato-di-conto>`: know that in Venice **$24$ grossi make $1$ ducat**, **$32$ piccoli make $1$ grosso**, **$12$ grossi make $1$ soldo di grossi**, and **$20$ soldi make $1$ lira di grossi** (worth **$10$ gold ducats**), so the four columns signify **lire, soldi, grossi, piccoli**.

.. picture:: fig_06_quaderno_conservation.svg
   :alt: Skew-symmetric directed conservation network of Pacioli's Venetian Quaderno

.. enunciation::

   **Fundamental Law of Double-Entry (`Cap. 14, fol. 202r`):**
   Know that of every single entry you have placed in the Journal you must make **two** in the :term:`Quaderno <quaderno>`: namely one in **Dare** and the other in **Avere**. For **never must anything be placed in Dare that is not likewise placed with the same quantity in Avere; and thus never must anything be placed in Avere that is not likewise placed with its amount in Dare.** Hence arises at the :term:`closing balance <bilancio-del-libro>` of the book that **the one sum must equal the other**, namely the :term:`summa summarum <summa-summarum>` of Dare and of Avere.

.. assertion:: [Euclid I.cn.2 & Ledger Equilibrium] <I.cn.2>

   In the directed ledger circuit on circle :g:`(OK) <summa.I.9.quaderno:( O K )>`, each *Giornale* posting ``Per u // A v`` connects accounts :g:`K (Cavedal) <summa.I.9.quaderno:K>`, :g:`S (Cassa) <summa.I.9.quaderno:S>`, :g:`M (Zenzer) <summa.I.9.quaderno:M>`, :g:`D (Martino) <summa.I.9.quaderno:D>`, :g:`P (Pro e Danno) <summa.I.9.quaderno:P>`, and :g:`B (Bilancio) <summa.I.9.quaderno:B>`—opening cash :g:`KS <summa.I.9.quaderno:/ K S />`, ginger purchase :g:`SM <summa.I.9.quaderno:/ S M />`, credit sale :g:`MD <summa.I.9.quaderno:/ M D />` and gain :g:`DP <summa.I.9.quaderno:/ D P />`, collection :g:`DS <summa.I.9.quaderno:/ D S />`, and profit transfer :g:`PK <summa.I.9.quaderno:/ P K />` closing the cycle :g:`KSMDP <summa.I.9.quaderno:< K S M D P >>`. Because every posting enters equal weight in Dare and in Avere, the grand equilibrium holds unconditionally:

   $$\sum_{u} (\text{Dare}_u - \text{Avere}_u) = 0 \iff \text{Summa}(\text{Dare}) = \text{Summa}(\text{Avere})$$

.. qed::

   Observing that :term:`Cassa <cassa>` can never show a net credit balance ($\text{Dare}_{\text{Cassa}} - \text{Avere}_{\text{Cassa}} \ge 0$, `Cap. 12`), sweeping all gain and loss through :term:`Pro e Danno <pro-e-danno>` into :term:`Cavedal <cavedal>` (`Cap. 27`), and closing open accounts via :g:`SB <summa.I.9.quaderno:/ S B />` and :g:`KB <summa.I.9.quaderno:/ K B />` into :term:`Bilancio del libro <bilancio-del-libro>` (`Cap. 34`) yields the exact :term:`Summa summarum <summa-summarum>` of the entire ledger.
