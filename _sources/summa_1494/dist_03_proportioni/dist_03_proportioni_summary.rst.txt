:layout: book
:canonical_id: Summa I, Dist. VI
:folio: Part I, fols. 68r–98r

.. _summa-unit-03-summary:

MATHEMATICAL & PROPORTIONAL SUMMARY
===================================

.. rubric:: Exact Symbolic Classification, Means & Golden Section Identities

1. Boethian Fivefold Classification (`classify_boethian_ratio`)
---------------------------------------------------------------

Given reduced coprime positive integers :math:`p \neq q`, let :math:`M = \max(p, q)`, :math:`m = \min(p, q)`, and write :math:`M = q_{\text{div}} m + r` with :math:`0 \le r < m`:

.. list-table:: Complete Partition of Positive Rational Ratios
   :header-rows: 1
   :widths: 24 24 26 26

   * - Quotient / Remainder
     - Greater Genus (:math:`p > q`)
     - Lesser Genus (:math:`p < q`)
     - Canonical Example
   * - :math:`r = 0, \; q_{\text{div}} \ge 2`
     - :term:`multiplex <multiplex>`
     - *submultiplex*
     - :math:`12:4 = 3:1` (*tripla*)
   * - :math:`q_{\text{div}} = 1, \; r = 1`
     - :term:`superparticularis <superparticularis>`
     - *subsuperparticularis*
     - :math:`9:6 = 3:2` (*sesquialtera*)
   * - :math:`q_{\text{div}} = 1, \; r > 1`
     - :term:`superpartiens <superpartiens>`
     - *subsuperpartiens*
     - :math:`5:3` (*superbipartiens tertias*)
   * - :math:`q_{\text{div}} \ge 2, \; r = 1`
     - *multiplex superparticularis*
     - *submultiplex superparticularis*
     - :math:`5:2` (*dupla sesquialtera*)
   * - :math:`q_{\text{div}} \ge 2, \; r > 1`
     - *multiplex superpartiens*
     - *submultiplex superpartiens*
     - :math:`11:4` (*dupla supertripartiens quartas*)

2. Semicircle Three Means & Cross-Ratio (`construct_three_means`)
-----------------------------------------------------------------

For distinct positive lengths :math:`a, b > 0`:

.. math::

   A = \frac{a + b}{2}, \qquad G = \sqrt{ab}, \qquad H = \frac{2ab}{a + b}, \qquad G^2 = A \cdot H, \qquad A - G = \frac{(\sqrt{a} - \sqrt{b})^2}{2} > 0

Collinear points :math:`O=(0,0)`, :math:`P_b=(b,0)`, :math:`P_H=(H,0)`, :math:`P_a=(a,0)` form an exact **harmonic range** with projective cross-ratio :math:`(P_b, P_a; P_H, O) = -1`.

3. Extreme and Mean Ratio of :math:`10` (`construct_extreme_and_mean_ratio`)
----------------------------------------------------------------------------

- **Continuous Proportion**: :math:`10 : (\sqrt{125} - 5) = (\sqrt{125} - 5) : (15 - \sqrt{125}) = \phi = \frac{1 + \sqrt{5}}{2}`.
- **Euclidean Rectangle Identity (:just:`II.11`)**: :math:`10 \cdot (15 - \sqrt{125}) = (\sqrt{125} - 5)^2 = 150 - 50\sqrt{5}`.
- **First Marvelous Effect (:just:`XIII.1`)**: :math:`(\text{Major} + 5)^2 = 125 = 5 \cdot 5^2`.
