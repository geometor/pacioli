:type: summary
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
     - :math:`x^0 = 1`
     - Known area / constant magnitude
   * - ``.co.``
     - :term:`Cosa <cosa>` (*res*, *radix*)
     - :math:`x^1`
     - Side of the unknown square
   * - ``.ce.``
     - :term:`Censo <censo>` (*census*)
     - :math:`x^2`
     - Unknown square area
   * - ``.cu.``
     - :term:`Cubo <cubo>` (*cubus*)
     - :math:`x^3`
     - Solid cube on the *cosa*
   * - ``.ce.ce.``
     - :term:`Censo de censo <censo-de-censo>`
     - :math:`x^4`
     - Biquadratic power :math:`(x^2)^2`

2. Pacioli's Six Canonical Equations (`fols. 145r–146r`)
--------------------------------------------------------

Implemented symbolically in :func:`geometor.pacioli.proportions.solve_cossic_quadratic` for positive coefficients :math:`a, b, c > 0` (normalized with :math:`p = b/a`, :math:`q = c/a`):

.. list-table:: Six Positive-Coefficient Cossic Canons
   :header-rows: 1
   :widths: 10 30 35 25

   * - Canon
     - 1494 Cossic Form
     - Positive Root Formula
     - Euclidean Basis
   * - **1**
     - :math:`a.\text{ce.} = b.\text{co.}`
     - :math:`x = b / a`
     - :just:`I.cn.3`
   * - **2**
     - :math:`a.\text{ce.} = c`
     - :math:`x = \sqrt{c / a}`
     - :just:`II.14`
   * - **3**
     - :math:`b.\text{co.} = c`
     - :math:`x = c / b`
     - :just:`VII.19`
   * - **4**
     - :math:`a.\text{ce.} \; \bar{p} \; b.\text{co.} = c`
     - :math:`x = \sqrt{(p/2)^2 + q} - p/2`
     - :just:`II.4` (Gnomon)
   * - **5**
     - :math:`a.\text{ce.} \; \bar{p} \; c = b.\text{co.}`
     - :math:`x = p/2 \mp \sqrt{(p/2)^2 - q}` (if :math:`(p/2)^2 \ge q`)
     - :just:`II.5`
   * - **6**
     - :math:`b.\text{co.} \; \bar{p} \; c = a.\text{ce.}`
     - :math:`x = \sqrt{(p/2)^2 + q} + p/2`
     - :just:`II.6`

3. Equidistant Gradation Criterion (`fols. 149v–150r`)
------------------------------------------------------

- **Reducible Higher Trinomials**: Any equation :math:`a x^{2m} + b x^m = c` (e.g., :math:`m=2`, *censo de censo e censo equale a numero*) reduces via :math:`y = x^m` to Canon 4, 5, or 6, yielding :math:`x = \sqrt[m]{y}`.
- **Irreducible Cubics (`fol. 150r`)**: Non-equidistant forms :math:`x^3 + px = q`, :math:`x^3 = px + q`, and :math:`x^3 + q = px^2` lack quadratic reduction; Pacioli marks them unsolved in general as of November 1494.
