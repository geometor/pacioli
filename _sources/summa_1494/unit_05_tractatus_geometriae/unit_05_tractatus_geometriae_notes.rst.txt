:layout: book
:canonical_id: Summa II, Dist. I–VIII
:folio: Part II, fols. 1r–76r (Colophon Nov. 10, 1494)

.. _summa-unit-05-notes:

UNIT V — HISTORICAL, PHILOLOGICAL & DEDUCTIVE NOTES
===================================================

.. rubric:: Commentary on `(13, 14, 15)`, Pre-Malfatti Circle Packing, Truncated Polyhedra & the Two Colophons

1. Why Every Renaissance Surveyor Learned `(13, 14, 15)`
--------------------------------------------------------

From :person:`Heron's <heron>` *Metrica* (I.8) through Al-Khwārizmī, :person:`Leonardo Pisano's <leonardo-pisano>` *Practica Geometriae* (1220), and `Part II, fol. 9v` of Pacioli's *Summa*, the scalene triangle $(13, 14, 15)$ served for fifteen centuries as the canonical benchmark of Heron's formula because it is the **smallest non-right Heronian triangle formed by gluing two primitive/scaled Pythagorean triangles**—$(5, 12, 13)$ and $(9, 12, 15)$—along their shared :term:`cathetus <catetto>` $AD = 12$. Every single intermediate quantity in Pacioli's computation ($s = 21$, excesses $6, 7, 8$, area $84$, altitude $12$, segments $5$ and $9$, inradius $r = 4$, and circumradius $R = 65/8$) is rational, allowing the surveyor to verify Heron's fourth-degree radical $\sqrt{s(s-a)(s-b)(s-c)}$ directly against Euclid :just:`II.13`!

2. Pacioli's 1494 Three-Circle Problem (`fol. 57r`) vs. Malfatti (1803)
-----------------------------------------------------------------------

On `Part II, fol. 57r` (scan `n0580`), Pacioli asks for the **three largest equal mutually tangent circles** inside the isosceles $(10, 10, 12)$ triangle (altitude $8$, area $48$, inradius $3$). Setting the unknown radius (or scaled segment) as `1.co.` and applying the Pythagorean theorem to the triangle of circle centers reduces the configuration to the Canon 4 quadratic $5\frac{3}{4}\text{.ce.} + 16\text{.co.} = 48$ ($23r^2 + 64r = 192 \implies r = \frac{8\sqrt{85} - 32}{23} \approx 1.8155$). Historically, this problem in Piero della Francesca's and Pacioli's *abbaco* corpus is the direct Renaissance ancestor of Jakob Bernoulli's (1744) and Gian Francesco Malfatti's (1803) famous three-circle marble-cutting problem.

3. Derivation of $\sqrt{6\frac{6}{11}}$ on `fol. 69v` & the Two November 1494 Dates
-----------------------------------------------------------------------------------

Why does the truncated tetrahedron inscribed in a sphere of diameter $D = 6$ ($R = 3$) have exact edge $\sqrt{6\frac{6}{11}}$ on `fol. 69v`? Trisecting each edge of a regular tetrahedron of side $3e$ removes four corner tetrahedra of side $e$, leaving 4 equilateral triangles and 4 regular hexagons of common edge $e$. In Cartesian coordinates where the parent tetrahedron has vertices $(\pm \frac{3\sqrt{2}}{4}e, \pm \frac{3\sqrt{2}}{4}e, \dots)$, the 12 vertices of the truncated tetrahedron are all permutations with even sign changes of $\left(\frac{3\sqrt{2}}{4}e, \frac{\sqrt{2}}{4}e, \frac{\sqrt{2}}{4}e\right)$, whose squared circumradius from the origin is:

$$R^2 = \left(\frac{9}{8} + \frac{1}{8} + \frac{1}{8}\right) e^2 = \frac{11}{8} e^2 \implies e^2 = \frac{8}{11} R^2 = \frac{2}{11} D^2$$

Setting $D = 6$ gives $e^2 = \frac{72}{11} = 6\frac{6}{11}$, matching Pacioli's printed value to the letter!

Finally, note the fascinating bibliographical chronology preserved across our inspected scans: the Venetian colophon at the end of *Part II* (`fol. 76r`, scan `n0618`) is dated **November 10, 1494**, whereas the typographical register on the preliminary verso (`[prelim. fol. 1v]`, scan `n0005`) is dated **November 20, 1494**—showing that :person:`Paganino de' Paganini <paganino-de-paganini>` completed printing the geometric body of the book on November 10 and struck the preliminary dedication, epigrams, and quire register ten days later on November 20, 1494!
