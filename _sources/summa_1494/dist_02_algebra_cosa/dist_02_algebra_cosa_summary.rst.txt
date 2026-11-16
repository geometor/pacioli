:layout: book
:canonical_id: Summa I, Dist. II–V & VIII
:folio: Part I, fols. 19r–67v, 112r–150r

.. _summa-unit-02-summary:

MATHEMATICAL & ALGEBRAIC SUMMARY
================================

.. rubric:: Exact Symbolic Digest of Cossic Powers, Surds & the Six Quadratic Canons

1. Cossic Power Hierarchy (`fols. 143r–149v`)
---------------------------------------------

.. list-table:: Syncopated 1494 Cossic Lexicon
   :header-rows: 1
   :widths: 18 28 22 32

   * - 1494 Print
     - Vernacular / Latin Term
     - Algebraic Power
     - Geometric Model
   * - ``.n°.``
     - *Numero* (*dragma*)
     - $x^0 = 1$
     - Known area / constant magnitude
   * - ``.co.``
     - :term:`Cosa <cosa>` (*res*, *radix*)
     - $x^1$
     - Side of the unknown square
   * - ``.ce.``
     - :term:`Censo <censo>` (*census*)
     - $x^2$
     - Unknown square area
   * - ``.cu.``
     - :term:`Cubo <cubo>` (*cubus*)
     - $x^3$
     - Solid cube on the *cosa*
   * - ``.ce.ce.``
     - :term:`Censo de censo <censo-de-censo>`
     - $x^4$
     - Biquadratic power $(x^2)^2$

2. Pacioli's Six Canonical Equations (`fols. 145r–146r`)
--------------------------------------------------------

Implemented symbolically in :func:`geometor.pacioli.proportions.solve_cossic_quadratic` for positive coefficients $a, b, c > 0$ (normalized with $p = b/a$, $q = c/a$):

.. list-table:: Six Positive-Coefficient Cossic Canons
   :header-rows: 1
   :widths: 10 30 35 25

   * - Canon
     - 1494 Cossic Form
     - Positive Root Formula
     - Euclidean Basis
   * - **1**
     - $a.\text{ce.} = b.\text{co.}$
     - $x = b / a$
     - :just:`I.cn.3`
   * - **2**
     - $a.\text{ce.} = c$
     - $x = \sqrt{c / a}$
     - :just:`II.14`
   * - **3**
     - $b.\text{co.} = c$
     - $x = c / b$
     - :just:`VII.19`
   * - **4**
     - $a.\text{ce.} \; \bar{p} \; b.\text{co.} = c$
     - $x = \sqrt{(p/2)^2 + q} - p/2$
     - :just:`II.4` (Gnomon)
   * - **5**
     - $a.\text{ce.} \; \bar{p} \; c = b.\text{co.}$
     - $x = p/2 \mp \sqrt{(p/2)^2 - q}$ (if $(p/2)^2 \ge q$)
     - :just:`II.5`
   * - **6**
     - $b.\text{co.} \; \bar{p} \; c = a.\text{ce.}$
     - $x = \sqrt{(p/2)^2 + q} + p/2$
     - :just:`II.6`

3. Equidistant Gradation Criterion (`fols. 149v–150r`)
------------------------------------------------------

- **Reducible Higher Trinomials**: Any equation $a x^{2m} + b x^m = c$ (e.g., $m=2$, *censo de censo e censo equale a numero*) reduces via $y = x^m$ to Canon 4, 5, or 6, yielding $x = \sqrt[m]{y}$.
- **Irreducible Cubics (`fol. 150r`)**: Non-equidistant forms $x^3 + px = q$, $x^3 = px + q$, and $x^3 + q = px^2$ lack quadratic reduction; Pacioli marks them unsolved in general as of November 1494.
