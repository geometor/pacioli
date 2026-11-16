:layout: book
:canonical_id: Summa II, Dist. I–VIII
:folio: Part II, fols. 1r–76r (Colophon Nov. 10, 1494)

.. _summa-unit-05-summary:

GEOMETRIC & STEREOMETRIC SUMMARY
================================

.. rubric:: Exact Symbolic Invariants of *Tractatus Geometriae* (:mod:`geometor.pacioli.tractatus_geometriae`)

1. Heron's `(13, 14, 15)` Archetype (`Part II, fol. 9v`)
--------------------------------------------------------

- **Coordinates**: $G = (0, 0)$, $B = (14, 0)$, $A = (5, 12)$, Foot $D = (5, 0)$, Incenter $I = (6, 4)$, Circumcenter $O = \left(7, \frac{33}{8}\right)$.
- **Heron Product**: $s = 21$, $(s - c, s - b, s - a) = (6, 7, 8)$, $\Delta = \sqrt{21 \cdot 6 \cdot 7 \cdot 8} = \sqrt{7056} = 84$.
- **Radii & Altitude**: :term:`Cathetus <catetto>` $AD = 12$, Inradius $r = \Delta / s = 4$, Circumradius $R = \frac{abc}{4\Delta} = \frac{65}{8}$.

2. Proportional Division of Triangles (`Part II, Dist. IV`)
-----------------------------------------------------------

- **Vertex Cevian (`VI.1`)**: Dividing $GB$ at $K = \left(\frac{14p}{p+q}, 0\right)$ splits area $84$ into $\frac{84p}{p+q}$ and $\frac{84q}{p+q}$ (for $1:2$, $K = \left(\frac{14}{3}, 0\right)$, areas $28$ and $56$).
- **Parallel Cut (`VI.13` + `VI.19`)**: Constructing geometric mean $GU = \sqrt{14 \cdot \frac{14p}{p+q}}$ on the semicircle over $GB$ cuts off $\triangle GUV \sim \triangle GBA$ of exact rational area $\frac{84p}{p+q}$ despite radical vertex coordinates $U = (7\sqrt{2}, 0)$, $V = \left(\frac{5\sqrt{2}}{2}, 6\sqrt{2}\right)$ for $p:q = 1:1$.

3. Regular & Archimedean Solids in Sphere of Diameter $D = 6$ (`fols. 68v–70r`)
-------------------------------------------------------------------------------

.. list-table:: Exact Stereometric Table for Sphere Diameter $D = 6$ ($R = 3$)
   :header-rows: 1
   :widths: 26 16 20 18 20

   * - Inscribed Solid
     - :term:`Possanza <possanza>` ($e^2$)
     - Exact Edge ($e$)
     - Surface Area
     - Exact Volume
   * - **Tetrahedron** (`XIII.13`)
     - $24$
     - $2\sqrt{6}$
     - $24\sqrt{3}$
     - $8\sqrt{3}$
   * - **Cube** (`XIII.15`)
     - $12$
     - $2\sqrt{3}$
     - $72$
     - $24\sqrt{3}$
   * - **Octahedron** (`XIII.14`)
     - $18$
     - $3\sqrt{2}$
     - $36\sqrt{3}$
     - $36$
   * - **Icosahedron** (`XIII.16`)
     - $\frac{18(5 - \sqrt{5})}{5}$
     - $3\sqrt{\frac{10 - 2\sqrt{5}}{5}}$
     - $18\sqrt{3}(5 - \sqrt{5})$
     - $9\sqrt{10 + 2\sqrt{5}}$
   * - **Dodecahedron** (`XIII.17`)
     - $18 - 6\sqrt{5}$
     - $\sqrt{15} - \sqrt{3}$
     - $18\sqrt{10(5 - \sqrt{5})}$
     - $30\sqrt{3} + 6\sqrt{15}$
   * - **Truncated Tetrahedron** (`fol. 69v`)
     - $\frac{72}{11} = 6\frac{6}{11}$
     - $\frac{6\sqrt{22}}{11}$
     - $\frac{504\sqrt{3}}{11}$
     - $\frac{1656\sqrt{11}}{121}$
   * - **Cuboctahedron** (`fol. 69v`)
     - $9$
     - $3$
     - $54 + 18\sqrt{3}$
     - $45\sqrt{2}$
