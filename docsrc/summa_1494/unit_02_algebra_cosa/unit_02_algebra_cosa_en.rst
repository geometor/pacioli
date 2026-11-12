:layout: book
:canonical_id: Summa I, Dist. II–V & VIII
:folio: Part I, fols. 19r–67v, 112r–150r

.. _summa-unit-02:
.. _summa-unit-02-en:

UNIT II — ALGORISMUS, EUCLIDEAN SURDS & COSSIC ALGEBRA (*REGOLA DELA COSA*)
===========================================================================

.. rubric:: Part I, Distinctiones II–V (Practical Algorism) & Distinctio VIII: *Arte Maggiore / Algebra e Almucabala* (fols. 112r–150r)

.. folio:: Part I, fols. 19r–67v

.. rubric:: Practical Algorism, Lattice Multiplication (*Gelosia*), *Regola del Tre* & *El Cataym*

Across *Distinctiones II–V*, :person:`Fra Luca Pacioli <pacioli>` codifies the complete computational repertory of the Italian *scuole d'abbaco* inherited from :person:`Leonardo Pisano's <leonardo-pisano>` :cite:`*Liber Abaci* <leonardo-pisano:liber-abaci>` and :person:`Johannes de Sacrobosco's <sacrobosco>` :cite:`*Algorismus* <sacrobosco:algorismus>`:

- **Finger Reckoning (*Indigitatione*) & Place-Value Numeration**: Woodcut hand positions representing units through tens of thousands (`fol. 36v`).
- **Eight Modes of Multiplication**: *Scacchieri* (chessboard), *castelluccio*, *colonna*, *crocetta*, *quadrilatero*, *gelosia* (Venetian lattice grating), *repiego* (factor decomposition), and *a scapezza* (distributive partitioning).
- **Four Modes of Division**: *A regolo*, *per ripiego*, *a danda* (forerunner of modern long division), and *a galea* (*galley* scratch-method prized by Venetian shipwrights and merchants).
- **Rule of Three (*Regola del Tre*) & Double False Position (*El Cataym*)**: Linear interpolation of unknowns via two trial hypotheses $(x_1, e_1)$ and $(x_2, e_2)$, eliminating affine error prior to invoking full algebraic unknowns.

.. folio:: Part I, fols. 112r–125v

.. rubric:: Syncopated Cossic Notation, Sign Laws & Euclid Book X Surds (:just:`X.36`, :just:`X.73`)

.. picture:: fig_03_book_x_binomial_apotome.svg
   :alt: Euclid Book X Binomial 3 + sqrt(5) and Apotome/Residuo 3 - sqrt(5) square dissection

Entering *Distinctio VIII* (*De l'Arte Maggiore, ditta dal vulgo la Regola dela Cosa*), Pacioli standardizes in print the syncopated Renaissance algebraic lexicon:

- **Gradation of Cossic Powers**: *Numero* ($1$), :term:`.co. (*cosa*) <cosa>` ($x$), :term:`.ce. (*censo*) <censo>` ($x^2$), :term:`.cu. (*cubo*) <cubo>` ($x^3$), :term:`.ce.ce. (*censo de censo*) <censo-de-censo>` ($x^4$), *primo relato* ($x^5$), and *ce.cu.* ($x^6$).
- **Operational & Grouping Symbols**: :term:`.p̄. (*più*) and .m̄. (*meno*) <piu-e-meno>` governed by the four sign rules (*più via più sempre fa più; meno via meno sempre fa più; più via meno sempre fa meno*), together with the compound radical :term:`.℞.u. (*radice universale*) <radice-universale>`.
- **Six Binomials & Six Apotomes (*Residui*)**: Before solving quadratic equations, Pacioli translates :person:`Euclid's <euclid>` geometric theory of compound irrationals (:just:`X.36`, :just:`X.73`) into radical arithmetic. In the left diagram, the :term:`binomial <binomio>` segment :g:`AB <summa.I.8.surds:/ A B />` joins rational :g:`AM <summa.I.8.surds:M>` ($3$) and surd $MB = \sqrt{5}$, so its square decomposes by :just:`II.4` into :g:`AMPQ <summa.I.8.surds:< A M P Q >>` ($9$), $b = 5$, and two symmetric gnomon wings :g:`MBRP <summa.I.8.surds:< M B R P >>` ($2 \cdot 3\sqrt{5}$), totaling $14 + 6\sqrt{5}$. In the right diagram, subtracting $NF = \sqrt{5}$ from :g:`EF <summa.I.8.surds:/ E F />` ($3$) leaves at :g:`N <summa.I.8.surds:N>` the :term:`apotome (*residuo*) <residuo>` $EN = 3 - \sqrt{5}$, whose square :g:`ENKL <summa.I.8.surds:< E N K L >>` inside :g:`EFGH <summa.I.8.surds:< E F G H >>` equals $14 - 6\sqrt{5}$ (:just:`II.7`).

.. folio:: Part I, fols. 145r–146r

.. rubric:: The Six Canonical Cossic Equations & Geometric Gnomon Proofs (:just:`II.4`–:just:`II.6`)

.. picture:: fig_02_cossic_gnomon.svg
   :alt: Pacioli fol. 146r geometric gnomon completion of the square for 1.ce. + 10.co. = 39

Following :person:`Al-Khwārizmī <al-khwarizmi>` (:cite:`*Al-jabr wa'l-muqābala* <al-khwarizmi:algebra>`) and :person:`Leonardo Pisano <leonardo-pisano>`, since all terms on each side of a classic equation must carry positive coefficients, `fol. 145r` arranges all linear and quadratic equations into three **simple** (*semplici*: $a x^2 = b x$, $a x^2 = c$, $b x = c$) and three **compound** (:term:`capitoli composti <capitoli-composti>`), printing Latin hexameter mnemonics for each compound canon:

.. enunciation::

   1. **First Compound Canon (*Primi canonis versus*, `fol. 145r`)** — *Censo e cose equale a numero* ($x^2 + b x = c$):
      *"Si res et census numero coaequantur, a rebus dimidio sumpto censum producere debes, addere quem numero, radicem tollere toti, dimidiumque rei de radice abjicere."*
      Halve the *cose* ($b/2$), square that half ($(b/2)^2$), add it to the *numero* ($c$), extract the square root, and subtract half the *cose*:

      $$x = \sqrt{\left(\frac{b}{2}\right)^2 + c} - \frac{b}{2}$$

   2. **Second Compound Canon (*Secundi canonis versus*)** — *Censo e numero equale a cose* ($x^2 + c = b x$):
      Valid whenever $(b/2)^2 \ge c$, yielding **two positive roots** $x = \frac{b}{2} \mp \sqrt{(b/2)^2 - c}$ (proved via :just:`II.5`).

   3. **Third Compound Canon (*Tertii canonis versus*)** — *Cose e numero equale a censo* ($b x + c = x^2$):
      Yielding $x = \sqrt{(b/2)^2 + c} + \frac{b}{2}$ (proved via :just:`II.6`).

.. assertion:: [Euclid II.4] <II.4>

   On `fol. 146r`, Pacioli proves the First Compound Canon geometrically on the archetype $1.\text{ce.} \; \bar{p} \; 10.\text{co.} = 39$ ($x^2 + 10x = 39$). Let :g:`AEFG <summa.I.8.gnomon:< A E F G >>` represent the unknown *censo* ($x^2$) on side $AE = x$. Halving the $10$ *cose* into two equal rectangles of width $EB = GD = 5$ attaches the gnomon wings :g:`EBHF <summa.I.8.gnomon:< E B H F >>` and :g:`GFID <summa.I.8.gnomon:< G F I D >>`, whose combined area with :g:`AEFG <summa.I.8.gnomon:< A E F G >>` is given as $39$. Filling in the corner square :g:`FHCI <summa.I.8.gnomon:< F H C I >>` of side $5$ and area $5^2 = 25$ completes the great square $ABCD$ whose sides :g:`AB <summa.I.8.gnomon:/ A B />` and :g:`DA <summa.I.8.gnomon:/ D A />` are :eq:`equal <summa.I.8.gnomon:/ A B / = summa.I.8.gnomon:/ B C / = summa.I.8.gnomon:/ C D / = summa.I.8.gnomon:/ D A />` to :g:`BC <summa.I.8.gnomon:/ B C />` and :g:`CD <summa.I.8.gnomon:/ C D />` along diagonal :g:`AC <summa.I.8.gnomon:/ A C />`:

   $$\text{Area}(ABCD) = 39 + 25 = 64 \implies AB = \sqrt{64} = 8 \implies x = AE = 8 - 5 = 3$$

.. folio:: Part I, fols. 149v–150r

.. rubric:: Higher Cossic Gradations & the Historic Verdict on Cubic Equations (`fol. 150r`)

.. qed::

   Closing *Distinctio VIII* on `fols. 149v–150r`, Pacioli shows that any higher three-term equation whose powers stand in **equidistant proportional gradation**—such as $a\,x^4 + b\,x^2 = c$ (*censo de censo e censo equale a numero*) or $a\,x^6 + b\,x^3 = c$—reduces immediately to the three compound quadratic canons. By contrast, for **disproportionate** cubic and quartic equations (*cubo, censo e cosa equale a numero*), Pacioli records his famous 1494 boundary verdict: **up to the present hour, the art has not yet yielded a general rule, just as no general method has yet been given for squaring the circle** (*"si commo ancora non è dato modo al quadrare del cerchio"*)—the exact printed challenge that inspired :person:`Scipione del Ferro <scipione-del-ferro>` at Bologna, :person:`Niccolò Tartaglia <tartaglia>` in Venice, and :person:`Gerolamo Cardano's <cardano>` :cite:`*Ars Magna* (1545) <cardano:ars-magna>`.
