:layout: book
:canonical_id: Summa I, Dist. I
:folio: Prelim. fols. 1r–3r; Part I, fols. 1r–18v

.. _summa-unit-01:
.. _summa-unit-01-en:

DEDICATIONS, CONTINENTIA & SPECULATIVE ARITHMETIC
=================================================

.. rubric:: Preliminaries (fols. 1r–8v) & Part I, Distinctio I: Continuous and Discrete Quantity, Figurate & Perfect Numbers (fols. 1r–18v)

.. folio:: [prelim. fol. 1r–1v]

.. rubric:: General Contents (*Continentia de tutta lopera*) & Venetian Preliminaries

In the opening pages printed by :person:`Paganino de' Paganini <paganino-de-paganini>` in Venice (November 10–20, 1494), :person:`Fra Luca Pacioli <pacioli>` maps out the five universal divisions of the :cite:`*Summa de arithmetica, geometria, proportioni et proportionalita* <pacioli:summa>`:

1. **Theoretical & Practical Numbers** (*De numeri e misure*): Speculative properties of integers, Hindu–Arabic algorism, fractions, and :term:`proportions <proportione>` (*Distinctiones I–VI*).
2. **The Great Art of Algebra** (*Arte Maggiore, ditta dal vulgo la Regola dela Cosa*): Operations on :term:`radicals <radice-universale>`, :term:`binomials <binomio>`, :term:`apotomes <residuo>`, and the :term:`six canonical equations <capitoli-composti>` (*Distinctio VIII*).
3. **Mercantile Arithmetic** (*Compagnie, baratti, cambi, leghe*): Partnerships, bills of exchange, alloyage, and interrupted games of chance (*Distinctio IX, Tractatus I–X*).
4. **Venetian Double-Entry Bookkeeping** (*De computis et scripturis*): Ordering every merchant's :term:`Inventario <inventario>`, :term:`Memoriale <memoriale>`, :term:`Giornale <giornale>`, and :term:`Quaderno Grande <quaderno>` after the custom of Venice (*Distinctio IX, Tractatus XI*).
5. **Practical & Regular Geometry** (*Tractatus Geometriae*): Plane and solid mensuration, surface division, and the regular and dependent bodies inscribed in the sphere (*Part II, Distinctiones I–VIII*).

On the verso (`[prelim. fol. 1v]`), Pacioli salutes the Venetian patrician and mathematician :person:`Marco Sanudo <marco-sanudo>` (*astrologiae, geometriae, arithmeticaeque cultor exquisitissimus*), thanking him for financing the typographical enterprise so that secrets hitherto locked in Latin manuscripts might nourish Italian scholars, architects, and merchants alike, followed by a Latin elegiac epigram of :person:`Paolo Pompilio <pompilio>` and an Italian sonnet by :person:`Giorgio Sommaripa <giorgio-sommaripa>`.

.. folio:: [prelim. fols. 2r–3r]

.. rubric:: Dedicatory Epistles to Guidobaldo da Montefeltro, Duke of Urbino

Addressing :person:`Guidobaldo da Montefeltro <guidobaldo-da-montefeltro>` in both vernacular Italian and humanist Latin, Pacioli recalls the mathematical splendor of the Ducal Palace of Urbino erected by Guidobaldo's father :person:`Federico da Montefeltro <federico-da-montefeltro>`, argues that military art, perspective, music, cosmography, and architecture all stand or fall with exact measurement, and deliberately defends writing in the Italian mother tongue so that practical artisans and *abbacisti* share one unified science with university philosophers.

.. folio:: Part I, fols. 1r–1v

.. rubric:: Division of Quantity & Explicit Acknowledgment of Authorities

.. enunciation::

   Quantity (*quantità*), Magnanimous Duke, is immediately twofold—namely **continuous** (*continua*, divisible without end: line, surface, body, place, time) and **discrete** (*discreta*, proceeding from the indivisible unit: number and speech)—establishing the fourfold mathematical *Quadrivium* of Arithmetic, Music, Geometry, and Astronomy (:cite:`Boethius, *De Institutione Arithmetica* I.1 <boethius:de-institutione-arithmetica>`).

On `fol. 1v`, Pacioli states his famous scholarly rule of attribution: he draws his demonstrations chiefly from :person:`Euclid <euclid>`, :person:`Severinus Boethius <boethius>`, :person:`Leonardo Pisano <leonardo-pisano>`, :person:`Jordanus Nemorarius <jordanus-nemorarius>`, :person:`Biagio Pelacani of Parma <biagio-pelacani>`, :person:`Johannes de Sacrobosco <sacrobosco>`, and :person:`Prosdocimo de' Beldomandi <prosdocimo-de-beldomandi>`—adding explicitly that **wherever a passage bears no marginal author's name, it is to be understood as drawn from Leonardo Pisano**.

.. folio:: Part I, fol. 8r

.. rubric:: Figurate Polygonal Numbers & Euclid's Theorem on Perfect Numbers (:just:`IX.36`)

.. picture:: fig_01_figurate_perfect.svg
   :alt: Triangular tetractys T4 = 10 and Euclid IX.36 dyadic perfect-number rectangle 4 x 7 = 28

Following :person:`Boethius <boethius>` and :person:`Euclid <euclid>` (:just:`VII.def.22`, :just:`IX.36`), Pacioli classifies integers both geometrically as **figurate polygonal numbers**—such as the fourth triangular number (*tetractys*) $T_4 = 1 + 2 + 3 + 4 = 10$ bounded by the equilateral array :g:`ABC <summa.I.1.figurate:< A B C >>` where :g:`AB <summa.I.1.figurate:/ A B />` is :eq:`equal <summa.I.1.figurate:/ A B / = summa.I.1.figurate:/ B C / = summa.I.1.figurate:/ C A />` to :g:`BC <summa.I.1.figurate:/ B C />` and :g:`CA <summa.I.1.figurate:/ C A />`—and multiplicatively into **abundant** (*superflui*), **deficient** (*diminuti*), and **perfect** (:term:`numeri perfetti <numero-perfetto>`).

.. assertion:: [Euclid IX.36] <IX.36>

   Let successive powers of two be set out from the unit in continuous *dupla* progression:

   $$1, \; 2, \; 4, \; 8, \; 16, \; \dots, \; 2^{n-1}$$

   Whenever their cumulative sum $S_n = 1 + 2 + 4 + \dots + 2^{n-1} = 2^n - 1$ is a **prime incomposite number** (*numero primo incomposto*), the product of that prime sum $S_n$ and the last summed power $2^{n-1}$ forms an exact :term:`perfect number <numero-perfetto>`:

   $$P_n = 2^{n-1}(2^n - 1)$$

   In the dyadic rectangle :g:`DEFG <summa.I.1.figurate:< D E F G >>` for $n = 3$, the base :g:`DE <summa.I.1.figurate:/ D E />` has length $1 + 2 + 4 = 7$ (prime) and the altitude :g:`GD <summa.I.1.figurate:/ G D />` has length $2^2 = 4$ (:eq:`equal <summa.I.1.figurate:/ G D / = summa.I.1.figurate:/ E F />` to :g:`EF <summa.I.1.figurate:/ E F />`), beginning from the unit strip :g:`DHKG <summa.I.1.figurate:< D H K G >>` of area $1 \cdot 4 = 4$. Their product $7 \times 4 = 28$ equals the exact sum of its proper aliquot divisors:

   $$1 + 2 + 4 + 7 + 14 = 28$$

On `fol. 8r`, Pacioli warns the reader against the widespread medieval error of assuming that $2^n - 1$ is prime for *every* odd exponent $n$ (pointing out that $1 + 2 + \dots + 256 = 511 = 7 \times 73$ and $2047 = 23 \times 89$ are composite and therefore must be skipped!), notes that every even perfect number terminates alternately in the digits **$6$** or **$8$**, and prints an explicit numerical register extending all the way to a proposed *Quartus decimus numerus perfectus*.

.. qed::

   Just as the universe is adorned with very few things of supreme perfection (*rarissime sonno le cose perfette*), so among the infinite multitude of integers the :term:`perfect numbers <numero-perfetto>` generated by :just:`IX.36` stand sparse andincorruptible, anchoring both speculative arithmetic and architectural canon (*cf.* :ref:`*De Divina Proportione*, Architectura Cap. III <de-divina-proportione-index>`).
