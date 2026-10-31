:layout: book
:canonical_id: Appendix IV
:folio: Winterberg pp. 338–352

.. _plates-anmerkungen-en:
.. _plates-anmerkungen:

Appendix IV: Winterberg's Mathematical Commentary (1889)
========================================================

.. rubric:: Substantive Mathematical Notes (Sachliche Anmerkungen 1–17) by Constantin Winterberg (Vienna, 1889, pp. 338–352)

:person:`Constantin Winterberg <winterberg>` appended seventeen substantive mathematical notes (*Sachliche Anmerkungen*, pp. 338–352) to his 1889 Vienna edition, reformulating :person:`Pacioli's <pacioli>` numerical examples in modern algebraic notation, correcting :person:`Pacioli's <pacioli>` claim in :ref:`Cap. XLVI <compendio-cap_46-en>` regarding the inscription of the :term:`octahedron <octahedron>` in the :term:`icosahedron <icosahedron>`, and establishing a complete projective and polar-reciprocity theory of the twenty-one mutual inscriptions among the five Platonic solids.

.. _winterberg-note-1-en:

Note 1 (Cap. VII): Equivalence of Pacioli's Initial Characterization with Euclid's Definition of Extreme and Mean Ratio
-----------------------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 7 <compendio-cap_07-en>`

Since the definition of continuous division (:term:`extreme and mean ratio <extrema-et-media-ratio>`) according to :person:`Euclid <euclid>` (:cite:`Euclid VI.def.3 <euclid:elements:VI.def.3>`, :cite:`Euclid II.11 <euclid:elements:II.11>`) is stated at the close of Chapter VII—namely, when a given line $ac$ is divided at $b$ into two segments such that the square on the greater segment $ab^2$ equals the rectangle $ac \cdot bc$ contained by the whole line and the lesser segment—we demonstrate its identity with the numerical property stated at the beginning of Chapter VII (:cite:`Euclid XIII.1 <euclid:elements:XIII.1>`):

- **Hypothesis**: Let the line $ac$ be divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $b$, so that $ab^2 = ac \cdot bc$.
- **Claim**: $\left(ac + \frac{bc}{2}\right)^2 = 5\left(\frac{bc}{2}\right)^2$, or equivalently $\left(ab + \frac{ac}{2}\right)^2 = 5\left(\frac{ac}{2}\right)^2$.
- **Proof**: By hypothesis, $ab^2 = ac(ac - ab)$, whence

  .. math::

     ac^2 = ab^2 + ab \cdot ac \quad \text{and} \quad ab^2 + ab \cdot ac = ac^2.

  Adding $\left(\frac{ac}{2}\right)^2$ to both sides yields

  .. math::

     \left(ab + \frac{ac}{2}\right)^2 = ab^2 + ab \cdot ac + \left(\frac{ac}{2}\right)^2 = ac^2 + \frac{ac^2}{4} = 5\left(\frac{ac}{2}\right)^2. \quad \text{Q.E.D.}

.. _winterberg-note-2-en:

Note 2 (Cap. VII): Bisection of the Whole Line and Continuous Division of the Half
----------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 7 <compendio-cap_07-en>`

This corollary (:cite:`Euclid XIII.1 <euclid:elements:XIII.1>` / :cite:`Euclid XIII.2 <euclid:elements:XIII.2>`) follows immediately if we bisect the line $ab$ at $c$ ($ac = bc = \frac{1}{2}ab$) and divide $bc$ in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $d$; considering the three parts of the line $ab$, the greater segment of the half-line together with the other half satisfies the fivefold square relation $ad^2 = 5\,ac^2$.

.. _winterberg-note-3-en:

Note 3 (Cap. XII): Algebraic Proof of the Third Effect (Euclid XIII.3)
----------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 12 <compendio-cap_12-en>`

Expressed algebraically for the line $ac$ divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $b$ ($ab > bc$):

- **Hypothesis**: $ab^2 = ac \cdot bc = (ab + bc)\,bc$.
- **Claim**: $\left(bc + \frac{ab}{2}\right)^2 = 5\left(\frac{ab}{2}\right)^2$.
- **Proof**: Since $ab^2 = bc^2 + ab \cdot bc$ by hypothesis, adding $\left(\frac{ab}{2}\right)^2$ to both sides yields

  .. math::

     \left(bc + \frac{ab}{2}\right)^2 = bc^2 + ab \cdot bc + \left(\frac{ab}{2}\right)^2 = ab^2 + \frac{ab^2}{4} = 5\left(\frac{ab}{2}\right)^2.

  Substituting the numerical values of Chapter XII ($ac = 10$, $ab = \sqrt{125} - 5$, $bc = 15 - \sqrt{125}$) confirms the identity of both sides immediately.

.. _winterberg-note-4-en:

Note 4 (Cap. XIII): Algebraic Proof of the Fourth Effect (Euclid XIII.5)
------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 13 <compendio-cap_13-en>`

In algebraic form, let the segment $bc$ be divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $d$ ($cd > bd$), and let $ac = cd$ be adjoined to form the whole line $ad = ac + bc$:

- **Hypothesis**: $cd^2 = bc \cdot bd$ and $ac = cd$.
- **Claim**: $bc^2 = ad \cdot cd = ad \cdot ac$.
- **Proof**: By hypothesis, $cd^2 = bc(bc - cd) = bc^2 - bc \cdot cd$, whence

  .. math::

     bc^2 = cd^2 + bc \cdot cd = cd(cd + bc) = cd(ac + bc) = ad \cdot cd. \quad \text{Q.E.D.}

.. _winterberg-note-5-en:

Note 5 (Cap. XIV): Algebraic Proof of the Fifth Effect (Euclid XIII.4)
----------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 14 <compendio-cap_14-en>`

In general algebraic form, for the line $bc$ divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $d$ ($cd > bd$):

- **Hypothesis**: $cd^2 = bc \cdot bd$.
- **Claim**: $bd^2 + bc^2 = 3\,cd^2$.
- **Proof**:
  a) From Note 4, $bc^2 = bc \cdot cd + cd^2$.
  b) Expanding $bd^2 = (bc - cd)^2 = bc^2 - 2\,bc \cdot cd + cd^2$.
  Adding (a) and (b) together and substituting $bc^2 - bc \cdot cd = bc(bc - cd) = bc \cdot bd = cd^2$ gives:

  .. math::

     bd^2 + bc^2 = 2\,cd^2 + bc(bc - cd) = 2\,cd^2 + bc \cdot bd = 3\,cd^2. \quad \text{Q.E.D.}

.. _winterberg-note-6-en:

Note 6 (Cap. XVI): Seventh Effect — Hexagon Side (Radius) and Decagon Side (Euclid XIII.9)
------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 16 <compendio-cap_16-en>`

This follows immediately from Note 4 (:cite:`Euclid XIII.5 <euclid:elements:XIII.5>`), once one observes that the side of the regular decagon inscribed in a circle is the greater segment of the radius (the hexagon side) divided in :term:`extreme and mean ratio <extrema-et-media-ratio>`.

.. _winterberg-note-7-en:

Note 7 (Cap. XVIII): Ninth Effect — Diagonals of the Regular Pentagon (Euclid XIII.8)
-------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 18 <compendio-cap_18-en>`

The proof follows immediately from the similarity of the isosceles triangles $\triangle bca \sim \triangle baf$ formed by the two intersecting chords $ac$ and $be$ (meeting at $f$) of the regular pentagon:

.. math::

   \frac{ca}{ba} = \frac{ba}{af} \implies ba^2 = ca \cdot af,

and since $ba = bc = cf$, we have $cf^2 = ca \cdot af$, so the chord $ca$ is cut in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $f$.

.. _winterberg-note-8-en:

Note 8 (Cap. XXI): Twelfth Effect — Ratio of the Cube Edge to the Icosahedron Edge in the Same Sphere
-----------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 21 <compendio-cap_21-en>`

Denoting by $s$ and $s'$ the edges of the cube and regular :term:`icosahedron <icosahedron>` inscribed in the same sphere, and letting the segment $ab$ be divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $c$ ($ac > bc$), :person:`Pacioli's <pacioli>` claim (following :cite:`Campanus XIV.9 <campanus:euclid:XIV.9>`) is:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \frac{s'}{s} \quad \left(\text{or reciprocally } \sqrt{\frac{ab^2 + bc^2}{ab^2 + ac^2}} = \frac{s}{s'}\right).

**Proof**: Using the :term:`extreme and mean ratio <extrema-et-media-ratio>` relations (a) $ac^2 = ab \cdot bc$ and (b) $bc^2 = (ab - ac)^2 = ab^2 - 2\,ab \cdot ac + ac^2$, we have $ab^2 + bc^2 = 3\,ac^2 = 3\,ab \cdot bc$ (by Note 5) and $ab^2 + ac^2 = ab^2 + ab \cdot bc = ab(ab + bc)$. Hence the quotient under the radical simplifies to:

.. math::

   \frac{ab^2 + ac^2}{ab^2 + bc^2} = \frac{ab(ab + bc)}{3\,ab \cdot bc} = \frac{ab + bc}{3\,bc}.

Solving $ac^2 = ab \cdot bc = ab(ab - ac)$ gives $bc = \frac{3 - \sqrt{5}}{2}\,ab$, and substituting this into the quotient yields:

.. math::

   \sqrt{\frac{ab^2 + ac^2}{ab^2 + bc^2}} = \sqrt{\frac{ab + bc}{3\,bc}} = \sqrt{\frac{5 + \sqrt{5}}{6}} \quad \left(\text{and its reciprocal } \sqrt{\frac{3\,bc}{ab + bc}} = \sqrt{\frac{5 - \sqrt{5}}{6}}\right).

The exact same value is obtained when we express $s$ and $s'$ in terms of the circumradius $r$ of the common sphere (:cite:`Euclid XIII.15 <euclid:elements:XIII.15>`, :cite:`Euclid XIII.16 <euclid:elements:XIII.16>`, :cite:`Euclid XIII.18 <euclid:elements:XIII.18>`):

.. math::

   s = \frac{2r}{\sqrt{3}}, \qquad s' = \frac{4r}{\sqrt{10 + 2\sqrt{5}}} = r\sqrt{\frac{10 - 2\sqrt{5}}{5}}, \qquad \frac{s}{s'} = \sqrt{\frac{5 + \sqrt{5}}{6}}. \quad \text{Q.E.D.}

.. _winterberg-note-9-en:

Note 9 (Cap. XXII): Cross-Reference to the *Libellus de Quinque Corporibus Regularibus*
---------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 22 <compendio-cap_22-en>`

Compare on this pentagon construction the :cite:`*Tractatus de Quinque Corporibus Regularibus* <piero:libellus>` (*Libellus*, Tractate II, Case 20 ff.).

.. _winterberg-note-10-en:

Note 10 (Cap. XXVI): Division of the Sphere Diameter by the Base of the Inscribed Tetrahedron (Euclid XIII.13)
--------------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 26 <compendio-cap_26-en>`

In every regular :term:`tetrahedron <tetrahedron>`, the four altitudes intersect at the center of the circumscribed sphere (of radius $r$) in the ratio $1 : 3$. Denoting the smaller segment (from the sphere center to the base plane) by $x = \frac{r}{3}$, and extending the altitude $ac = r + x$ beyond the base plane to meet the sphere at $b$ (so that $ab = 2r$ is the sphere diameter and $bc = r - x$), the ratio of the extension $bc$ to the :term:`tetrahedron <tetrahedron>` altitude $ac$ is:

.. math::

   \frac{bc}{ac} = \frac{r - x}{r + x} = \frac{r - \frac{r}{3}}{r + \frac{r}{3}} = \frac{\frac{2}{3}r}{\frac{4}{3}r} = \frac{1}{2}, \qquad \text{whence } ab : ac = 3 : 2 \text{ and } ac : bc = 2 : 1.

.. _winterberg-note-11-en:

Note 11 (Cap. XXVII): Division of the Sphere Diameter by the Inscribed Cube (Euclid XIII.15)
--------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 27 <compendio-cap_27-en>`

The square of the diagonal of a square is double the square of its side ($ad^2 = 2\,bd^2$). Passing a plane through one of the three main space diagonals $ab$ of the cube and an edge $bd$, this plane intersects the circumscribed sphere in a great circle whose diameter is $ab$, while the two chords drawn from its endpoints to $d$ are the cube edge $bd$ and the face diagonal $ad$. By the right-triangle projection theorem (:cite:`Euclid VI.8 <euclid:elements:VI.8>`):

.. math::

   bd^2 = bc \cdot ab \quad \text{and} \quad ad^2 = ac \cdot ab.

Since $ad^2 = 2\,bd^2$, dividing the two equations gives:

.. math::

   \frac{bc}{ac} = \frac{bd^2}{ad^2} = \frac{1}{2}, \qquad \text{and } ab^2 = 3\,bd^2. \quad \text{Q.E.D.}

.. _winterberg-note-12-en:

Note 12 (Cap. XXIX): Construction of the Regular Icosahedron in the Sphere (Euclid XIII.16)
-------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 29 <compendio-cap_29-en>`

The edge $a$ of the regular :term:`icosahedron <icosahedron>` in terms of the circumradius $r$ of the sphere is:

.. math::

   a = \frac{4r}{\sqrt{10 + 2\sqrt{5}}}.

Passing a plane through the sphere diameter $ab = 2r$ and a polar cap edge $ad = a$ (which cuts the sphere in a semicircle $adb$), the projection $ac$ of $ad$ on the diameter $ab$ satisfies:

.. math::

   ac = \frac{ad^2}{ab} = \frac{a^2}{2r} = r\left(1 - \frac{1}{\sqrt{5}}\right), \qquad \text{whence } cm = r - ac = \frac{r}{\sqrt{5}},

and therefore the middle axial segment between the two parallel pentagon planes is $cc' = 2\,cm = \frac{2r}{\sqrt{5}} = \frac{d}{\sqrt{5}}$, where $d = 2r$ is the sphere diameter.

Now in the auxiliary semicircle of Chapter XXIX with $ac_{\text{aux}} = 2\,bc_{\text{aux}}$, we have $bd = \frac{d}{\sqrt{5}} = cc'$—that is, $bd$ equals the height of the ten-triangle antiprism belt (the segments called :term:`*catheti* <catheto>` in the text) erected perpendicular to the two pentagon planes at $c$ and $c'$. Moreover, the circumradius $r'$ of these two parallel pentagons (and of the inscribed decagon) with pentagon side $a$ is:

.. math::

   r' = a\sqrt{\frac{5 + \sqrt{5}}{10}} = \frac{d}{\sqrt{5}} = bd,

so the circumradius $r'$ of the pentagon circle equals both the line $bd$ of the text and the axial height $cc'$ of the perpendicular :term:`*catheti* <catheto>`, exactly as constructed in :person:`Euclid <euclid>` :cite:`Euclid XIII.16 <euclid:elements:XIII.16>`!

.. _winterberg-note-13-en:

Note 13 (Cap. XXX): Verification of the Pentagon Diagonal in the Dodecahedron Construction (Euclid XIII.17)
-----------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 30 <compendio-cap_30-en>`

Retaining the lettering of the figure in Chapter XXX (where $ke$ is half the cube edge, divided in :term:`extreme and mean ratio <extrema-et-media-ratio>` at $l$ with $kl > le$, and $an = hn = 2\,kl$ is the cube edge): by the three-dimensional Pythagorean projection,

.. math::

   ln^2 = an^2 - ke^2 - le^2 = 4\,kl^2 - ke^2 - le^2.

Since $kl^2 = ke \cdot le$, we can rewrite this as:

.. math::

   ln^2 = 2\,kl^2 + 2\,ke \cdot le - ke^2 - le^2 = 2\,kl^2 - (ke - le)^2 = 2\,kl^2 - kl^2 = kl^2,

whence $ln = kl$, proving that the five vertices lie at equal radii and form an equilateral and equiangular pentagon (:cite:`Euclid XIII.17 <euclid:elements:XIII.17>`).

.. _winterberg-note-14-en:

Note 14 (Cap. XXX): Semicircle Proof of the Fifth Effect Used in the Dodecahedron Sphere Inscription
----------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 30 <compendio-cap_30-en>`

This relation ($el^2 + ke^2 = 3\,kl^2$, already proved algebraically in Note 5) is seen most simply geometrically if we describe a semicircle on $ek$ as diameter, erect at $l$ a perpendicular meeting the semicircle at $m$, and draw the chords $em$ and $km$:

- By hypothesis, $kl^2 = ke \cdot el$, and by the right triangle $emk$ in the semicircle, $em^2 = ke \cdot el$, so $em = kl$.
- Moreover, $el^2 = em^2 - ml^2$ and $ke^2 = em^2 + mk^2$. Adding both gives:

  .. math::

     el^2 + ke^2 = 2\,em^2 + (mk^2 - ml^2) = 2\,em^2 + kl^2 = 3\,em^2 = 3\,kl^2. \quad \text{Q.E.D.}

.. _winterberg-note-15-en:

Note 15 (Cap. XLVI): Refutation of Pacioli's Claim That the Octahedron Cannot Be Inscribed in the Icosahedron (Tartaglia & Isoperimetric Approximation to the Sphere)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 46 <compendio-cap_46-en>`

The assertion stated here by :person:`Pacioli <pacioli>` (following :cite:`Campanus XV.13 <campanus:euclid:XV.13>`) is **manifestly false**: in a completely analogous manner to how the :term:`octahedron <octahedron>` is inscribed in the :term:`dodecahedron <dodecahedron>` (:ref:`Chapter XLIII <compendio-cap_43-en>`, :cite:`Euclid XV.9 <euclid:elements:XV.9>`), **the regular octahedron can also be inscribed in the regular icosahedron**!

- **Construction of the Octahedron in the Icosahedron**: One need only connect the midpoints of each pair of opposite parallel edges of the :term:`icosahedron <icosahedron>`. Among the 15 such segments (since the 30 edges of the :term:`icosahedron <icosahedron>` fall into 15 opposite parallel pairs), there are 5 sets of **three mutually perpendicular axes** meeting at the center of the :term:`icosahedron <icosahedron>`; the six endpoints of any such orthogonal triad of edge-midpoints form the 6 vertices of a **regular octahedron inscribed in the icosahedron**! (As :person:`**Niccolò Tartaglia** <niccolo-tartaglia>` already demonstrated in his :cite:`*General Trattato di Numeri et Misure* <tartaglia:general-trattato>`, refuting :person:`Campanus <campanus>` and :person:`Pacioli <pacioli>`.)
- **Cosmological Bias vs. Isoperimetric Truth**: The reason why :person:`Pacioli <pacioli>` denies this elementary geometric fact stems from his desire to vindicate the Platonic cosmological hierarchy by assigning to the :term:`**dodecahedron** <dodecahedron>` (as the symbol of the :term:`Quintessence <quinta-essentia>` / Heaven) the unique privilege of containing all four other regular solids, while restricting the :term:`**icosahedron** <icosahedron>` (Water) to only three.
  :person:`Pacioli's <pacioli>` preference for the :term:`dodecahedron <dodecahedron>` over the :term:`icosahedron <icosahedron>` would have been mathematically well-founded had he chosen as his criterion not how many other solids can be inscribed in it, but rather **which regular solid inscribed in the same sphere approaches most closely to the sphere itself—that is, which solid encompasses the greatest surface area and the greatest volume**! By this isoperimetric criterion (already proved by :person:`Hypsicles <hypsicles>` in :cite:`Book XIV, Proposition 2 <hypsicles:liber-xiv:2>`, and by :person:`Pappus <pappus>`), the decision falls decisively in favor of the :term:`**dodecahedron** <dodecahedron>` over the :term:`icosahedron <icosahedron>`.

.. _winterberg-note-16-en:

Note 16 (Cap. XLVII–LII): Reciprocal (Dual) Polyhedra Generated by Pyramidal Elevation of Faces and Planar Truncation of Vertices
---------------------------------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 47 <compendio-cap_47-en>`, :ref:`Cap. 48 <compendio-cap_48-en>`, :ref:`Cap. 49 <compendio-cap_49-en>`, :ref:`Cap. 50 <compendio-cap_50-en>`, :ref:`Cap. 51 <compendio-cap_51-en>`, :ref:`Cap. 52 <compendio-cap_52-en>`

Regarding the generation of the regular bodies and their dependent derivatives, :person:`Pacioli <pacioli>` distinguishes two primary classes: **plane (convex)** and **truncated (*:term:`abscisi <abscisum>`*)** bodies, each rendered both **solid (*:term:`solidum <solidum>`*)** and **hollow/skeletal (*:term:`vacuum <vacuum>`*)**, and then modifies them further by **elevating equilateral pyramids (*elevati*)** outward upon their faces. (The inverse operation—excavating pyramids inward upon the same faces—is not mentioned.)

The star-like elevated polyhedra can likewise be inscribed in a sphere passing through all the pyramid apices. If we regard those **pyramid apices as the vertices of a new convex polyhedron**, we immediately obtain the **reciprocal (dual) regular solid**:

- The **elevated tetrahedron** leads again to a **regular tetrahedron** (4 apices);
- The **elevated cube** leads to the **regular octahedron** (6 apices);
- The **elevated octahedron** (:term:`*Stella Octangula* <octahedron-elevatum>`) leads to the **regular cube** (8 apices);
- The **elevated icosahedron** leads to the **regular dodecahedron** (20 apices);
- The **elevated dodecahedron** leads to the **regular icosahedron** (12 apices).

More generally, the five regular solids correspond two by two as **reciprocal (dual) pairs** with respect to the numbers of their vertices ($V$), edges ($E$), and faces ($F$):

- **Tetrahedron $\leftrightarrow$ Tetrahedron (Self-Reciprocal)**: $E = 6$, $V = 4$, $F = 4$.
- **Cube $\leftrightarrow$ Octahedron**: $E = 12$, with $V = 8, F = 6$ for the Cube and $V = 6, F = 8$ for the :term:`Octahedron <octahedron>`.
- **Icosahedron $\leftrightarrow$ Dodecahedron**: $E = 30$, with $V = 12, F = 20$ for the :term:`Icosahedron <icosahedron>` and $V = 20, F = 12$ for the :term:`Dodecahedron <dodecahedron>`.

From any regular body, its **reciprocal (dual) body** arises in two dual ways:

1. **By transforming faces into vertices (Elevation)**: Erecting pyramids upon the faces and taking their apices as the vertices of the new body (when the pyramid height is chosen so that the apices of the pyramids sharing a common vertex of the original solid become coplanar with that vertex, the new reciprocal solid circumscribes the sphere that circumscribed the original solid).
2. **By transforming vertices into planes (Truncation)**: Slicing off the corners by planes until the cuts around each face meet at the **centroid of that face**, so that the original faces shrink to points (vertices) and the new body is circumscribed about the sphere that was inscribed in the original body.

.. _winterberg-note-17-en:

Note 17 (Cap. XXXV–XLVI): Complete Projective Theory of the 21 Mutual Inscriptions of the Five Regular Solids via Polar Reciprocity in the Sphere
-------------------------------------------------------------------------------------------------------------------------------------------------

**Corresponding Chapters**: :ref:`Cap. 35 <compendio-cap_35-en>`, :ref:`Cap. 46 <compendio-cap_46-en>`

To understand the mutual relationships of the five regular solids systematically and resolve **all possible questions of mutual inscription** at a single stroke, we employ the projective theory of **poles and polar planes with respect to a concentric sphere**.

1. Direct vs. Reciprocal Correspondence and Polarity in the Sphere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Between the elements (vertices and bounding faces) of two polyhedra, we distinguish two kinds of correspondence:

- **Direct Correspondence**: Each vertex of the inner solid corresponds to a vertex of the outer solid, or each face corresponds to a face.
- **Reciprocal Correspondence**: Each vertex of the first solid corresponds to a bounding face of the second, or conversely each face of the first corresponds to a vertex of the second.

The simplest universal mechanism for establishing a mutual reciprocal correspondence is **polar reciprocation with respect to a concentric sphere**:

- The **pole** of a plane cutting a sphere is the apex of the tangent cone touching the sphere along the circle of intersection; conversely, that plane is the **polar plane** of the point.
- Taking a sphere concentric with any regular solid, the polar planes of all its vertices (or equivalently, the poles of all its faces) form its **polar reciprocal regular solid**:

  - **Tetrahedron $\leftrightarrow$ Tetrahedron**
  - **Cube $\leftrightarrow$ Octahedron**
  - **Icosahedron $\leftrightarrow$ Dodecahedron**

- As the radius $R$ of the reciprocating sphere expands continuously from $0$ to $\infty$:

  1. **First Limit ($R = \rho$, the inradius of the original solid)**: The sphere touches the faces of the original solid from within; the poles of the faces are the **centroids of the faces**, so the reciprocal solid is **inscribed** in the original solid with its vertices at the face-centers.
  2. **Symmetric Dual Intersection ($R = \sqrt{r\rho}$, the geometric mean of the circumradius $r$ and inradius $\rho$)**: Both reciprocal solids are **inscribed in the same outer sphere of radius $r$ and circumscribed about the same inner sphere of radius $\rho$**!
  3. **Second Limit ($R = r$, the circumradius of the original solid)**: The sphere passes through the vertices of the original solid; the polar planes are the tangent planes at those vertices, so the original solid is now **inscribed** in its reciprocal solid!

2. Complete Classification of All 21 Possible Mutual Inscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By means of polar reciprocation, all **20 mutual inscriptions between distinct regular solids** (plus **1 self-inscription of the tetrahedron in the tetrahedron**, making **21 cases in all**) fall into **three direct groups (a)** and **three polar-reciprocal groups (b)**, where an asterisk (``*``) marks the 12 cases treated by :cite:`Euclid Book XV <euclid:elements:XV>` / :person:`Campanus <campanus>` / :person:`Pacioli <pacioli>` in Chapters XXXV–XLVI:

.. list-table:: Complete System of Mutual Inscriptions of the Five Regular Solids (Winterberg 1889, p. 348)
   :header-rows: 1
   :widths: 50 50

   * - **(a) Direct Inscriptions (Vertices of Inner Solid)**

     - **(b) Polar-Reciprocal Inscriptions (Faces of Outer Solid)**

   * - **Group I(a): Vertex on Vertex** (*Ecke auf Ecke*)

     - **Group I(b): Face on Face** (*Fläche auf Fläche*)

   * - **1.** Tetrahedron in Cube ``*`` (:ref:`Cap. XXXV <compendio-cap_35-en>`, :cite:`Euclid XV.1 <euclid:elements:XV.1>`)

     - **2.** :term:`Octahedron <octahedron>` in :term:`Tetrahedron <tetrahedron>` ``*`` (:ref:`Cap. XXXVI <compendio-cap_36-en>`, :cite:`Euclid XV.2 <euclid:elements:XV.2>`)

   * - **3.** Tetrahedron in Dodecahedron ``*`` (:ref:`Cap. XLI <compendio-cap_41-en>`, :cite:`Euclid XV.7 <euclid:elements:XV.7>`)

     - **4.** :term:`Icosahedron <icosahedron>` in :term:`Tetrahedron <tetrahedron>` (*omitted by Pacioli*)

   * - **5.** Cube in Dodecahedron ``*`` (:ref:`Cap. XLII <compendio-cap_42-en>`, :cite:`Euclid XV.8 <euclid:elements:XV.8>`)

     - **6.** :term:`Icosahedron <icosahedron>` in :term:`Octahedron <octahedron>` (*omitted by Pacioli*)

   * - **Group II(a): Vertex on Face** (*Ecke auf Fläche*)

     - **Group II(b): Face on Vertex** (*Fläche auf Ecke*)

   * - **7.** Octahedron in Cube ``*`` (:ref:`Cap. XXXVII <compendio-cap_37-en>`, :cite:`Euclid XV.3 <euclid:elements:XV.3>`)

     - **8.** Cube in :term:`Octahedron <octahedron>` ``*`` (:ref:`Cap. XXXVIII <compendio-cap_38-en>`, :cite:`Euclid XV.4 <euclid:elements:XV.4>`)

   * - **9.** Icosahedron in Dodecahedron ``*`` (:ref:`Cap. XLIV <compendio-cap_44-en>`, :cite:`Euclid XV.10 <euclid:elements:XV.10>`)

     - **10.** :term:`Dodecahedron <dodecahedron>` in :term:`Icosahedron <icosahedron>` ``*`` (:ref:`Cap. XLV <compendio-cap_45-en>`, :cite:`Euclid XV.11 <euclid:elements:XV.11>`)

   * - **11.** Tetrahedron in Icosahedron ``*`` (:ref:`Cap. XL <compendio-cap_40-en>`, :cite:`Euclid XV.6 <euclid:elements:XV.6>`)

     - **12.** :term:`Dodecahedron <dodecahedron>` in :term:`Tetrahedron <tetrahedron>` (*omitted by Pacioli*)

   * - **13.** Cube in Icosahedron ``*`` (:ref:`Cap. XLVI <compendio-cap_46-en>`, :cite:`Euclid XV.12 <euclid:elements:XV.12>`)

     - **14.** :term:`Dodecahedron <dodecahedron>` in :term:`Octahedron <octahedron>` (*omitted by Pacioli*)

   * - **Group III(a): Vertex on Edge** (*Ecke auf Kante*)

     - **Group III(b): Edge on Face** (*Kante in Fläche*)

   * - **15.** Octahedron in Dodecahedron ``*`` (:ref:`Cap. XLIII <compendio-cap_43-en>`, :cite:`Euclid XV.9 <euclid:elements:XV.9>`)

     - **16.** :term:`Icosahedron <icosahedron>` in Cube (*treated in Piero/Pacioli's Libellus!*)

   * - **17.** Octahedron in Icosahedron (*denied by :person:`Pacioli <pacioli>` in Cap. XLVI; proved by :person:`Tartaglia <niccolo-tartaglia>` & Note 15*)

     - **18.** :term:`Dodecahedron <dodecahedron>` in Cube (*omitted by Pacioli*)

   * - **19.** Tetrahedron in Octahedron ``*`` (:ref:`Cap. XXXIX <compendio-cap_39-en>`, :cite:`Euclid XV.5 <euclid:elements:XV.5>`)

     - **20.** Cube in :term:`Tetrahedron <tetrahedron>` (*omitted by Pacioli*)

   * - **21.** Tetrahedron in Tetrahedron (*vertices at face-centroids; omitted in Cap. XXXV–XLVI*)

     - *(Self-reciprocal)*

3. Geometric Derivation of the Reciprocal Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Group I (1 $\leftrightarrow$ 2, 3 $\leftrightarrow$ 4, 5 $\leftrightarrow$ 6)**: Taking the polar reciprocals of two solids sharing common vertices on a circumscribed sphere converts the inner solid into the outer reciprocal solid and the outer solid into the inner reciprocal solid, with **coincident faces** replacing coincident vertices:

  - From **1 (Tetrahedron in Cube)** arises **2 (Octahedron in Tetrahedron)**, where 4 of the 8 faces of the :term:`octahedron <octahedron>` lie in the 4 faces of the :term:`tetrahedron <tetrahedron>` and the 6 vertices of the :term:`octahedron <octahedron>` lie at the 6 edge-midpoints of the :term:`tetrahedron <tetrahedron>`.
  - From **3 (Tetrahedron in Dodecahedron)** arises **4 (Icosahedron in Tetrahedron)**, where 4 faces of the :term:`icosahedron <icosahedron>` lie in the 4 faces of the circumscribing :term:`tetrahedron <tetrahedron>` (obtained by extending the 4 :term:`icosahedron <icosahedron>` faces whose centroids form the inscribed :term:`tetrahedron <tetrahedron>` of Case 11 until they meet!).
  - From **5 (Cube in Dodecahedron)** arises **6 (Icosahedron in Octahedron)**, where 8 faces of the :term:`icosahedron <icosahedron>` lie in the 8 faces of the :term:`octahedron <octahedron>` and all 12 vertices of the :term:`icosahedron <icosahedron>` lie on the 12 edges of the :term:`octahedron <octahedron>` (dividing them in the golden ratio!).

- **Group II (7 $\leftrightarrow$ 8, 9 $\leftrightarrow$ 10, 11 $\leftrightarrow$ 12, 13 $\leftrightarrow$ 14)**:

  - **7 $\leftrightarrow$ 8 (Octahedron $\leftrightarrow$ Cube)** and **9 $\leftrightarrow$ 10 (Icosahedron $\leftrightarrow$ Dodecahedron)** are dual pairs directly.
  - From **11 (Tetrahedron in Icosahedron)**, reciprocating with respect to the sphere touching the :term:`icosahedron <icosahedron>` and circumscribing the :term:`dodecahedron <dodecahedron>` yields **12 (Dodecahedron in Tetrahedron)**: passing tangent planes through the 4 common vertices of the :term:`dodecahedron <dodecahedron>` and its inscribed :term:`tetrahedron <tetrahedron>` (Case 3) forms the circumscribing :term:`tetrahedron <tetrahedron>` touching 4 vertices of the :term:`dodecahedron <dodecahedron>`.
  - From **13 (Cube in Icosahedron)** arises **14 (Dodecahedron in Octahedron)**, where the centers of the 8 :term:`octahedron <octahedron>` faces contain the 8 vertices of the :term:`dodecahedron <dodecahedron>` that form an inscribed cube.

- **Group III (15 $\leftrightarrow$ 16, 17 $\leftrightarrow$ 18, 19 $\leftrightarrow$ 20)**: Because the two solids do not share a common circumsphere when vertices fall on edges, we reciprocate with respect to any concentric sphere (e.g., the sphere circumscribing the outer solid), transforming **vertices on edges** into **faces containing edges**:

  - From **15 (Octahedron in Dodecahedron)** arises **16 (Icosahedron in Cube)**, where **6 opposite parallel edges of the icosahedron lie in the 6 square faces of the cube** along their midlines in three mutually perpendicular directions, so that all 12 vertices of the :term:`icosahedron <icosahedron>` rest in pairs on the 6 faces of the cube! Remarkably, although omitted here in the *Compendio*, this exact inscription is explicitly treated in :person:`Piero della Francesca <piero-della-francesca>` / :person:`Pacioli's <pacioli>` companion :cite:`*Libellus de Quinque Corporibus Regularibus* <piero:libellus>`!
  - From **17 (Octahedron in Icosahedron)** arises **18 (Dodecahedron in Cube)**, where 6 opposite parallel edges of the :term:`dodecahedron <dodecahedron>` lie along the midlines of the 6 faces of the cube (while the 8 remaining vertices of the :term:`dodecahedron <dodecahedron>`, corresponding to an inscribed cube, lie free inside).
  - From **19 (Tetrahedron in Octahedron)** arises **20 (Cube in Tetrahedron)**, where the 4 faces of the :term:`tetrahedron <tetrahedron>` contain 4 edges of the cube (two opposite top edges of the cube and the two perpendicular bottom edges).
