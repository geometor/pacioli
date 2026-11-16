:layout: book
:canonical_id: Summa I, Dist. VI
:folio: Part I, fols. 68r–98r

.. _summa-unit-03-summary:

MATHEMATICAL & PROPORTIONAL SUMMARY
===================================

.. rubric:: Exact Symbolic Classification, Means & Golden Section Identities

1. Boethian Fivefold Classification (`classify_boethian_ratio`)
---------------------------------------------------------------

Given reduced coprime positive integers $p \neq q$, let $M = \max(p, q)$, $m = \min(p, q)$, and write $M = q_{\text{div}} m + r$ with $0 \le r < m$:

.. list-table:: Complete Partition of Positive Rational Ratios
   :header-rows: 1
   :widths: 24 24 26 26

   * - Quotient / Remainder
     - Greater Genus ($p > q$)
     - Lesser Genus ($p < q$)
     - Canonical Example
   * - $r = 0, \; q_{\text{div}} \ge 2$
     - :term:`multiplex <multiplex>`
     - *submultiplex*
     - $12:4 = 3:1$ (*tripla*)
   * - $q_{\text{div}} = 1, \; r = 1$
     - :term:`superparticularis <superparticularis>`
     - *subsuperparticularis*
     - $9:6 = 3:2$ (*sesquialtera*)
   * - $q_{\text{div}} = 1, \; r > 1$
     - :term:`superpartiens <superpartiens>`
     - *subsuperpartiens*
     - $5:3$ (*superbipartiens tertias*)
   * - $q_{\text{div}} \ge 2, \; r = 1$
     - *multiplex superparticularis*
     - *submultiplex superparticularis*
     - $5:2$ (*dupla sesquialtera*)
   * - $q_{\text{div}} \ge 2, \; r > 1$
     - *multiplex superpartiens*
     - *submultiplex superpartiens*
     - $11:4$ (*dupla supertripartiens quartas*)

2. Semicircle Three Means & Cross-Ratio (`construct_three_means`)
-----------------------------------------------------------------

For distinct positive lengths $a, b > 0$:

$$A = \frac{a + b}{2}, \qquad G = \sqrt{ab}, \qquad H = \frac{2ab}{a + b}, \qquad G^2 = A \cdot H, \qquad A - G = \frac{(\sqrt{a} - \sqrt{b})^2}{2} > 0$$

Collinear points $O=(0,0)$, $P_b=(b,0)$, $P_H=(H,0)$, $P_a=(a,0)$ form an exact **harmonic range** with projective cross-ratio $(P_b, P_a; P_H, O) = -1$.

3. Extreme and Mean Ratio of $10$ (`construct_extreme_and_mean_ratio`)
----------------------------------------------------------------------

- **Continuous Proportion**: $10 : (\sqrt{125} - 5) = (\sqrt{125} - 5) : (15 - \sqrt{125}) = \phi = \frac{1 + \sqrt{5}}{2}$.
- **Euclidean Rectangle Identity (:just:`II.11`)**: $10 \cdot (15 - \sqrt{125}) = (\sqrt{125} - 5)^2 = 150 - 50\sqrt{5}$.
- **First Marvelous Effect (:just:`XIII.1`)**: $(\text{Major} + 5)^2 = 125 = 5 \cdot 5^2$.
