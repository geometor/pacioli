:type: summary
:layout: book
:canonical_id: Summa II, Dist. I–VIII
:folio: Part II, fols. 1r–76r (Colophon Nov. 10, 1494)

.. _summa-unit-05-summary:

GEOMETRIC & STEREOMETRIC SUMMARY
================================

.. rubric:: Exact Symbolic Invariants of *Tractatus Geometriae* (:mod:`geometor.pacioli.tractatus_geometriae`)

1. Heron's `(13, 14, 15)` Archetype (`Part II, fol. 9v`)
--------------------------------------------------------

- **Coordinates**: :math:`G = (0, 0)`, :math:`B = (14, 0)`, :math:`A = (5, 12)`, Foot :math:`D = (5, 0)`, Incenter :math:`I = (6, 4)`, Circumcenter :math:`O = \left(7, \frac{33}{8}\right)`.
- **Heron Product**: :math:`s = 21`, :math:`(s - c, s - b, s - a) = (6, 7, 8)`, :math:`\Delta = \sqrt{21 \cdot 6 \cdot 7 \cdot 8} = \sqrt{7056} = 84`.
- **Radii & Altitude**: :term:`Cathetus <catetto>` :math:`AD = 12`, Inradius :math:`r = \Delta / s = 4`, Circumradius :math:`R = \frac{abc}{4\Delta} = \frac{65}{8}`.

2. Proportional Division of Triangles (`Part II, Dist. IV`)
-----------------------------------------------------------

- **Vertex Cevian (`VI.1`)**: Dividing :math:`GB` at :math:`K = \left(\frac{14p}{p+q}, 0\right)` splits area :math:`84` into :math:`\frac{84p}{p+q}` and :math:`\frac{84q}{p+q}` (for :math:`1:2`, :math:`K = \left(\frac{14}{3}, 0\right)`, areas :math:`28` and :math:`56`).
- **Parallel Cut (`VI.13` + `VI.19`)**: Constructing geometric mean :math:`GU = \sqrt{14 \cdot \frac{14p}{p+q}}` on the semicircle over :math:`GB` cuts off :math:`\triangle GUV \sim \triangle GBA` of exact rational area :math:`\frac{84p}{p+q}` despite radical vertex coordinates :math:`U = (7\sqrt{2}, 0)`, :math:`V = \left(\frac{5\sqrt{2}}{2}, 6\sqrt{2}\right)` for :math:`p:q = 1:1`.

3. Regular & Archimedean Solids in Sphere of Diameter :math:`D = 6` (`fols. 68v–70r`)
-------------------------------------------------------------------------------------

.. list-table:: Exact Stereometric Table for Sphere Diameter :math:`D = 6` (:math:`R = 3`)
   :header-rows: 1
   :widths: 26 16 20 18 20

   * - Inscribed Solid
     - :term:`Possanza <possanza>` (:math:`e^2`)
     - Exact Edge (:math:`e`)
     - Surface Area
     - Exact Volume
   * - **Tetrahedron** (`XIII.13`)
     - :math:`24`
     - :math:`2\sqrt{6}`
     - :math:`24\sqrt{3}`
     - :math:`8\sqrt{3}`
   * - **Cube** (`XIII.15`)
     - :math:`12`
     - :math:`2\sqrt{3}`
     - :math:`72`
     - :math:`24\sqrt{3}`
   * - **Octahedron** (`XIII.14`)
     - :math:`18`
     - :math:`3\sqrt{2}`
     - :math:`36\sqrt{3}`
     - :math:`36`
   * - **Icosahedron** (`XIII.16`)
     - :math:`\frac{18(5 - \sqrt{5})}{5}`
     - :math:`3\sqrt{\frac{10 - 2\sqrt{5}}{5}}`
     - :math:`18\sqrt{3}(5 - \sqrt{5})`
     - :math:`9\sqrt{10 + 2\sqrt{5}}`
   * - **Dodecahedron** (`XIII.17`)
     - :math:`18 - 6\sqrt{5}`
     - :math:`\sqrt{15} - \sqrt{3}`
     - :math:`18\sqrt{10(5 - \sqrt{5})}`
     - :math:`30\sqrt{3} + 6\sqrt{15}`
   * - **Truncated Tetrahedron** (`fol. 69v`)
     - :math:`\frac{72}{11} = 6\frac{6}{11}`
     - :math:`\frac{6\sqrt{22}}{11}`
     - :math:`\frac{504\sqrt{3}}{11}`
     - :math:`\frac{1656\sqrt{11}}{121}`
   * - **Cuboctahedron** (`fol. 69v`)
     - :math:`9`
     - :math:`3`
     - :math:`54 + 18\sqrt{3}`
     - :math:`45\sqrt{2}`
