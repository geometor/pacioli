:layout: book
:canonical_id: Summa I, Dist. II–V & VIII
:folio: Part I, fols. 19r–67v, 112r–150r

.. _summa-unit-02:
.. _summa-unit-02-en:

ALGORISMUS, EUCLIDEAN SURDS & COSSIC ALGEBRA (REGOLA DELA COSA)
===============================================================

.. rubric:: Part I, Distinctiones II–V (Practical Algorism) & Distinctio VIII: *Arte Maggiore / Algebra e Almucabala* (fols. 112r–150r)

.. folio:: Part I, fols. 19r–67v

.. rubric:: Practical Algorism, Lattice Multiplication (*Gelosia*), *Regola del Tre* & *El Cataym*

In *Distinctiones II–V*, following :person:`Leonardo Pisano's <leonardo-pisano>` :cite:`*Liber Abaci* <leonardo-pisano:liber-abaci>` and :person:`Johannes de Sacrobosco's <sacrobosco>` :cite:`*Algorismus* <sacrobosco:algorismus>`, we set forth the complete practice of calculation:

- **Finger Reckoning (*Indigitatione*) & Place-Value Numeration**: Hand positions signifying units through tens of thousands (`fol. 36v`).
- **Eight Modes of Multiplication**: *Scacchieri* (chessboard), *castelluccio*, *colonna*, *crocetta*, *quadrilatero*, *gelosia* (lattice grating), *repiego* (by factors), and *a scapezza* (by parts).
- **Four Modes of Division**: *A regolo*, *per ripiego*, *a danda*, and *a galea* (the galley method).
- **The Rule of Three (*Regola del Tre*) & Double False Position (*El Cataym*)**: Finding unknowns by two trial suppositions $(x_1, e_1)$ and $(x_2, e_2)$ before resorting to the Great Art.

.. folio:: Part I, fols. 112r–125v

.. rubric:: Characters of the Great Art, Sign Laws & Euclid Book X Surds (:just:`X.36`, :just:`X.73`)

.. picture:: fig_03_book_x_binomial_apotome.svg
   :alt: Euclid Book X Binomial 3 + sqrt(5) and Apotome/Residuo 3 - sqrt(5) square dissection

These are the characters with which the entire speculative practice of :term:`Algebra and Almucabala <cosa>` (*Arte Maggiore*, called by the common people the Rule of the Thing) is exercised:

- **Gradation of Powers**: *.n°.* (*Numero*, $1$), :term:`.co. (*cosa*) <cosa>` (first unknown quantity, root or side, $x$), :term:`.ce. (*censo*) <censo>` (square of the *cosa*, $x^2$), :term:`.cu. (*cubo*) <cubo>` ($x^3$), :term:`.ce.ce. (*censo de censo*) <censo-de-censo>` ($x^4$), *primo relato* ($x^5$), and *ce.cu.* ($x^6$).
- **Signs & Universal Root**: :term:`.p̄. (*più*) and .m̄. (*meno*) <piu-e-meno>`, wherein note that *più by più always makes più*, *meno by meno always makes più*, *più by meno always makes meno*, and *meno by più always makes meno*; together with :term:`.℞.u. (*radice universale* or *legata*) <radice-universale>` over :term:`binomials <binomio>` and :term:`apotomes (*residui*) <residuo>`.
- **Six Binomials & Six Apotomes (*Residui*)**: Following :person:`Euclid <euclid>` Book X (:just:`X.36`, :just:`X.73`), in the left figure let the :term:`binomial <binomio>` line :g:`AB <summa.I.8.surds:/ A B />` join rational :g:`AM <summa.I.8.surds:M>` ($3$) and surd $MB = \sqrt{5}$; its square decomposes by :just:`II.4` into :g:`AMPQ <summa.I.8.surds:< A M P Q >>` ($9$), $b = 5$, and two equal complements :g:`MBRP <summa.I.8.surds:< M B R P >>` ($2 \cdot 3\sqrt{5}$), totaling $14 + 6\sqrt{5}$. In the right figure, cutting $NF = \sqrt{5}$ from :g:`EF <summa.I.8.surds:/ E F />` ($3$) leaves at :g:`N <summa.I.8.surds:N>` the :term:`apotome (*residuo*) <residuo>` $EN = 3 - \sqrt{5}$, whose square :g:`ENKL <summa.I.8.surds:< E N K L >>` inside :g:`EFGH <summa.I.8.surds:< E F G H >>` equals $14 - 6\sqrt{5}$ (:just:`II.7`).

.. folio:: Part I, fols. 145r–146r

.. rubric:: Distinctio Octava, Tractatus Quintus — The Six Chapters & Geometric Gnomon Proof (:just:`II.4`–:just:`II.6`)

.. picture:: fig_02_cossic_gnomon.svg
   :alt: Pacioli fol. 146r geometric gnomon completion of the square for 1.ce. + 10.co. = 39

To come to the knowledge of the :term:`compound chapters <capitoli-composti>`, following :person:`Al-Khwārizmī <al-khwarizmi>` (:cite:`*Al-jabr wa'l-muqābala* <al-khwarizmi:algebra>`) and :person:`Leonardo Pisano <leonardo-pisano>`, we first state the **three simple chapters**:

1. **Censo equal to cose** ($a\,x^2 = b\,x$): divide the *cose* by the *censi*.
2. **Censo equal to numero** ($a\,x^2 = c$): divide the *numero* by the *censi*, and the square root of the quotient is the *cosa*.
3. **Cose equal to numero** ($b\,x = c$): divide the *numero* by the *cose*.

There follow the **three compound chapters** with their Latin verses:

.. enunciation::

   1. **First Compound Canon (*Primi canonis versus*, `fol. 145r`)** — *Censo e cose equale a numero* ($x^2 + b x = c$):
      *"Si res & census numero coaequantur, a rebus dimidio sumpto censum producere debes, addere quem numero, radicem tollere toti, dimidiumque rei de radice abjicere."*
      Take half the *cose* ($b/2$), square it ($(b/2)^2$), add this to the *numero* ($c$), take the square root of the whole, and subtract half the *cosa* from the root:

      $$x = \sqrt{\left(\frac{b}{2}\right)^2 + c} - \frac{b}{2}$$

   2. **Second Compound Canon (*Secundi canonis versus*)** — *Censo e numero equale a cose* ($x^2 + c = b x$):
      Multiply half the *cose* by itself, subtract the *numero*, take the root of the remainder, and either add it to or subtract it from half the *cose* (whenever $(b/2)^2 \ge c$, proved via :just:`II.5`):

      $$x = \frac{b}{2} \mp \sqrt{\left(\frac{b}{2}\right)^2 - c}$$

   3. **Third Compound Canon (*Tertii canonis versus*)** — *Cose e numero equale a censo* ($b x + c = x^2$):
      Take half the *cose*, square it, add it to the *numero*, take the root of the whole, and add half the *cosa* (proved via :just:`II.6`):

      $$x = \sqrt{\left(\frac{b}{2}\right)^2 + c} + \frac{b}{2}$$

.. assertion:: [Euclid II.4] <II.4>

   Let there be for demonstration of the First Compound Chapter $1.\text{ce.} \; \bar{p} \; 10.\text{co.} = 39$ ($x^2 + 10x = 39$). Set out the great square $ABCD$ divided as shown in the margin: let the square :g:`AEFG <summa.I.8.gnomon:< A E F G >>` be **$1$ censo** ($x^2$), and let the two complements around it, :g:`EBHF <summa.I.8.gnomon:< E B H F >>` and :g:`GFID <summa.I.8.gnomon:< G F I D >>`, be each **$5$ cose** (half of the $10$ *cose*), which together with the *censo* make **$39$**. Add the small corner square :g:`FHCI <summa.I.8.gnomon:< F H C I >>` of half the *cose* multiplied by itself—that is, $5 \times 5 = 25$—to $39$: this makes **$64$** for the whole great square $ABCD$, whose sides :g:`AB <summa.I.8.gnomon:/ A B />` and :g:`DA <summa.I.8.gnomon:/ D A />` are :eq:`equal <summa.I.8.gnomon:/ A B / = summa.I.8.gnomon:/ B C / = summa.I.8.gnomon:/ C D / = summa.I.8.gnomon:/ D A />` to :g:`BC <summa.I.8.gnomon:/ B C />` and :g:`CD <summa.I.8.gnomon:/ C D />` along diagonal :g:`AC <summa.I.8.gnomon:/ A C />`. Its square root is **$8$** for the entire side $AB$; subtract $EB$, which is **$5$** (half the *cose*), and there remains $AE = 3$ precisely for the value of the :term:`cosa <cosa>`:

   $$\text{Area}(ABCD) = 39 + 25 = 64 \implies AB = \sqrt{64} = 8 \implies x = AE = 8 - 5 = 3$$

.. folio:: Part I, fols. 149v–150r

.. rubric:: Higher Gradations & Verdict on the Chapters of the Cube (`fol. 150r`)

.. qed::

   Any three-term chapter whose powers stand in equidistant proportional gradation—such as *censo de censo* and *censo* equal to *numero* ($a\,x^4 + b\,x^2 = c$) or $a\,x^6 + b\,x^3 = c$—reduces at once to the three compound chapters above. But where **numero, cosa, and cubo** are compounded, or **numero, censo, and cubo**, or **cosa, censo, and cubo equal to numero**, **it has not up to the present hour been possible to form general rules**, on account of the disproportion of the degrees among themselves—**just as no general way has yet been given to square the circle** by either ancient or modern mathematicians, although in particular cases one may sometimes arrive at a solution by trial.
