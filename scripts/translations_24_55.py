"""Complete, unabridged scholarly English translations and Critical Commentary
for Part I: Compendio de Divina Proportione, Section 3 (Chapters XXIV–LV):
The Five Regular Platonic Solids, their Uniqueness, Constructions, Mutual Inscriptions,
and the Truncated and Elevated Dependent Polyhedra (Plates I–XL).
"""

from typing import Dict

CHAPTERS_24_TO_55: Dict[int, Dict[str, str]] = {
    24: {
        "title_en": "On the Tenth Effect of Our Divine Proportion, Which Introduces the Formation of the Five Regular Bodies.",
        "body_en": """.. enunciation:: Tenth Effect of the Divine Proportion

   If a straight line is equal in square to the side of the equilateral pentagon and to the side of the equilateral hexagon inscribed in the same circle, then it is equal to the side of the equilateral decagon inscribed in the same circle, and the side of the pentagon is greater than the side of the hexagon and than the side of the decagon; and therefore, if the two sides of the hexagon and the decagon are joined together into a single straight line, the whole line is divided according to our Divine Proportion, and its greater part is the side of the hexagon (:just:`XIII.9`, :just:`XIII.10`).

We need not labor further on this tenth effect, because we already demonstrated it above in the first effect (:ref:`Chapter VII <compendio-cap_07-en>`). Yet it is restated here in the sequence of the tenth effect to display how all these admirable properties lead step by step to the construction of the most noble solid bodies—above all the fourth and fifth regular solids, the icosahedron and the dodecahedron, which cannot be formed or imagined without our Divine Proportion.

.. assertion:: Proof and Corollary (:just:`XIII.10`, :just:`XIII.9`, :just:`I.47`)

   1. By the :just:`tenth of the thirteenth <XIII.10>`, in any circle, the square on the side of the inscribed equilateral pentagon equals the sum of the squares on the side of the inscribed hexagon and the side of the inscribed decagon:

      .. math::

         s_{5}^{2} = s_{6}^{2} + s_{10}^{2}

   2. Therefore, if a straight line is equal in square (*in potentia*) to :math:`s_{5}` and :math:`s_{6}`—meaning that the square on :math:`s_{5}` exceeds the square on :math:`s_{6}` by the square on that line—that line is necessarily the side of the equilateral decagon (:math:`s_{10}`) by the :just:`penultimate of the first <I.47>`.
   3. And since :math:`s_{5}^{2} = s_{6}^{2} + s_{10}^{2}`, the square on the side of the pentagon is greater than the square on the side of the hexagon alone and greater than the square on the side of the decagon alone; hence in length also :math:`s_{5} > s_{6}` and :math:`s_{5} > s_{10}`.
   4. Furthermore, by the :just:`ninth of the thirteenth <XIII.9>`, when the side of the hexagon (:math:`s_{6}`) and the side of the decagon (:math:`s_{10}`) are joined in a single straight line, the whole compound line :math:`s_{6} + s_{10}` is divided according to the extreme and mean ratio, and its greater segment is the side of the hexagon (:math:`s_{6}`).

.. rubric:: Numerical Example

Take the example already given above: let the square on the side of the pentagon (:math:`s_{5}^{2}`) be :math:`20`, let the square on the side of the hexagon (:math:`s_{6}^{2}`) be :math:`16` (so that :math:`s_{6} = 4`, the radius of the circle), and let the square on the side of the decagon (:math:`s_{10}^{2}`) be :math:`4` (so that :math:`s_{10} = 2`). Joining the side of the hexagon and the side of the decagon gives :math:`4 + 2 = 6`, though in exact geometric truth :math:`s_{6}` and :math:`s_{10}` are incommensurable when :math:`s_{6}` is rational (:math:`s_{10} = \\sqrt{20} - 2` when :math:`s_{6} = 4`, so :math:`s_{5}^{2} = 16 + (\\sqrt{20}-2)^{2} = 40 - 4\\sqrt{20}`).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Role as Bridge to Section 3**: ``Cap. XXIV`` concludes the chain of planar theorems from Book XIII (:just:`XIII.1`–:just:`XIII.12`) by pairing :just:`XIII.10` (:math:`s_{5}^{2} = s_{6}^{2} + s_{10}^{2}`) with :just:`XIII.9` (:math:`s_{6} : s_{10} = (s_{6}+s_{10}) : s_{6}`). This Pythagorean triad of regular polygon sides (:math:`s_5, s_6, s_{10}`) is the exact geometric engine Euclid uses in :just:`XIII.16` to construct the icosahedron and in :just:`XIII.17` to construct the dodecahedron.
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2`` draft reduced this chapter to a three-line summary without the corollary on :just:`XIII.9` or the numerical illustration. The present translation restores the full 1509 Paganini text (``0031.rst``, ``f. 8r``).""",
    },
    25: {
        "title_en": "How It Is Not Possible for There to Be More Than Five Regular Bodies in Nature, and Why.",
        "body_en": """Having seen the sublime and marvelous effects of our Divine Proportion in plane figures and lines, it now follows, most lofty Duke, to treat of the five regular solid bodies—which, as we said at the outset, are those that have equal sides, equal plane bases (faces), and equal solid angles, and which, when placed in a sphere, touch its interior surface with all their vertices—and first to demonstrate why in the nature of things there cannot be more than five such bodies (:just:`XIII.18` Scholium; :just:`XI.21`).

.. enunciation:: Uniqueness of the Five Regular Polyhedra

   No solid body bounded by equilateral and equiangular plane figures all equal and similar to one another can be formed beyond the five regular bodies—namely three bounded by equilateral triangles (the *tetracedron* of four faces, the *octocedron* of eight faces, and the *ycocedron* of twenty faces), one bounded by squares (the *cubo* or *exacedron* of six faces), and one bounded by regular pentagons (the *duodecedron* of twelve faces).

.. assertion:: Proof from Solid Angles (:just:`XI.21`, :just:`I.32`)

   1. By the :just:`twenty-first of the eleventh <XI.21>`, every solid angle is contained by at least three plane angles, and the sum of all the plane angles that meet to form any convex solid angle must always be **less than four right angles** (:math:`360^{\\circ}`). For if the plane angles meeting at a point equaled four right angles, they would lie flat in a single continuous plane surface and could never close to form a solid corner or vertex; and still less can they exceed four right angles.
   2. **First Case — Equilateral Triangles**: By the :just:`thirty-second of the first <I.32>`, the three interior angles of any triangle equal two right angles; hence in an equilateral triangle (:g:`isopleuron`) each angle equals **two-thirds of one right angle** (:math:`\\frac{2}{3}R = 60^{\\circ}`).
      - If **three** equilateral triangles meet at one point, their three angles equal :math:`3 \\times \\frac{2}{3}R = 2R` (two right angles, :math:`180^{\\circ}`), which is less than four right angles. From such solid angles of three triangles is formed the **first regular body**, the pyramid of four triangular bases called the **tetracedron** (tetrahedron).
      - If **four** equilateral triangles meet at one point, their four angles equal :math:`4 \\times \\frac{2}{3}R = \\frac{8}{3}R = 2\\frac{2}{3}R` (:math:`240^{\\circ}`), which is less than four right angles. From such solid angles of four triangles is formed the **third regular body**, of eight triangular bases, called the **octocedron** (octahedron).
      - If **five** equilateral triangles meet at one point, their five angles equal :math:`5 \\times \\frac{2}{3}R = \\frac{10}{3}R = 3\\frac{1}{3}R` (:math:`300^{\\circ}`), which is still less than four right angles. From such solid angles of five triangles is formed the **fourth regular body**, of twenty triangular bases, called the **ycocedron** (icosahedron).
      - If **six** equilateral triangles meet at one point, their six angles equal :math:`6 \\times \\frac{2}{3}R = 4R` (**four right angles**, :math:`360^{\\circ}`). Therefore, by :just:`XI.21`, six equilateral triangles cannot form a solid angle, nor can seven or more; hence from equilateral triangles **only three** regular bodies can ever be generated.
   3. **Second Case — Squares**: In the equilateral and equiangular quadrangle (the square), each interior angle is **one right angle** (:math:`1R = 90^{\\circ}`).
      - If **three** squares meet at one point, their three plane angles equal :math:`3R` (**three right angles**, :math:`270^{\\circ}`), which is less than four right angles. From such solid angles is formed the **second regular body**, of six square bases, called the **cubo** or **exacedron** (cube).
      - If **four** squares meet at one point, their angles equal **four right angles** (:math:`360^{\\circ}`), forming a flat plane and no solid angle; hence from squares **only one** regular body can be formed.
   4. **Third Case — Regular Pentagons**: By the :just:`thirty-second of the first <I.32>`, any pentagon is resolved into three triangles, whose angles total :math:`3 \\times 2R = 6R` (six right angles); dividing :math:`6R` equally among the five angles of a regular pentagon gives :math:`\\frac{6}{5}R = 1\\frac{1}{5}R` (:math:`108^{\\circ}`) for each pentagonal angle.
      - If **three** regular pentagons meet at one point, their three angles equal :math:`3 \\times 1\\frac{1}{5}R = 3\\frac{3}{5}R` (:math:`324^{\\circ}`), which is less than four right angles. From such solid angles is formed the **fifth and noblest regular body**, of twelve pentagonal bases, called the **duodecedron** (dodecahedron).
      - If **four** regular pentagons were to meet at one point, their angles would equal :math:`4 \\times 1\\frac{1}{5}R = 4\\frac{4}{5}R` (:math:`432^{\\circ}`), which exceeds four right angles; hence from pentagons **only one** regular body can be formed.
   5. **Fourth Case — Hexagons and Higher Polygons**: An equilateral hexagon is resolved into four triangles (:math:`8R`), so each interior angle equals :math:`\\frac{8}{6}R = 1\\frac{1}{3}R` (:math:`120^{\\circ}`). Even the minimum number of three hexagons meeting at a point produces :math:`3 \\times 1\\frac{1}{3}R = 4R` (**four right angles**, :math:`360^{\\circ}`), which cannot form a solid angle. And in heptagons, octagons, and all polygons of more sides, three angles always exceed four right angles.

Therefore, in the entire universe of nature, there can be neither more nor fewer than **five** regular solid bodies.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Source in Euclid and Campanus**: This famous classification proof comes from the concluding Scholium to :just:`XIII.18` (integrated into the proposition text in Campanus of Novara's Latin edition as XIII.18 corollary), resting on :just:`XI.21` (the sum of plane angles of any convex solid angle is less than :math:`4R`) and :just:`I.32` (the interior angle sum of an :math:`n`-gon is :math:`(n-2)\\cdot 2R`).
- **Comparison with Earlier Draft Track**: In ``divina_en_2/25.txt``, the angle calculations in fractions of a right angle (:math:`\\frac{2}{3}R`, :math:`2\\frac{2}{3}R`, :math:`3\\frac{1}{3}R`, :math:`1\\frac{1}{5}R`, :math:`3\\frac{3}{5}R`, :math:`1\\frac{1}{3}R`) were condensed into a brief table. Here the complete rhetorical and deductive structure of Pacioli's 1509 text (``0031.rst``–``0032.rst``, ``f. 8r``–``f. 8v``) is translated in full.""",
    },
    26: {
        "title_en": "How the First Regular Body, Called the Tetracedron or Pyramid of Four Triangular Bases, Is Formed and Placed in the Sphere.",
        "body_en": """Now that we have shown why there cannot be more than five regular bodies, we shall explain in order how each of them is formed from the given diameter of the sphere in which it is to be inscribed, beginning with the first, called the **tetracedron** (:just:`XIII.13`).

.. enunciation:: Construction of the Regular Tetrahedron in a Given Sphere (:just:`XIII.13`)

   Given the diameter of a sphere, to find the side of the regular pyramid of four equilateral triangular bases (*tetracedron*) inscribed in that sphere, and to show that the square on the diameter of the sphere is sesquialtera (:math:`3 : 2`) to the square on the side of the tetracedron.

.. assertion:: Construction and Proof (:just:`XIII.13`, :just:`VI.8`, :just:`III.31`, :just:`XIII.12`, :just:`XI.4`)

   1. Let :math:`ab` be the given diameter of the sphere (see the marginal diagram ``0032.g1.png`` on Folio 0032). Divide :math:`ab` at point :math:`c` so that :math:`ac` is double :math:`cb` (:math:`ac = 2\\,cb`), whence :math:`ab` is triple :math:`cb` (:math:`ac = \\frac{2}{3}ab`, :math:`cb = \\frac{1}{3}ab`).
   2. Upon the diameter :math:`ab` describe the semicircle :math:`adb`, and from point :math:`c` erect the perpendicular :math:`cd` meeting the circumference at :math:`d`, and join the straight lines :math:`da` and :math:`db`.
   3. Because :math:`\\angle adb` in a semicircle is a right angle (:just:`III.31`) and :math:`dc` is perpendicular to the base :math:`ab`, by the :just:`eighth of the sixth <VI.8>` the triangles :math:`adb`, :math:`adc`, and :math:`dcb` are similar, and :math:`ac : cd = cd : cb`, so :math:`cd^{2} = ac \\cdot cb`. Moreover, :math:`ab : ac = da^{2} : ac^{2} \\implies da^{2} = ab \\cdot ac`.
   4. Since :math:`ab : ac = 3 : 2` (the *sesquialtera* ratio), the square on the diameter of the sphere (:math:`ab^{2}`) has to the square on the chord :math:`da` (:math:`da^{2}`) the ratio :math:`3 : 2` (:math:`da^{2} = \\frac{2}{3}ab^{2}`), and :math:`da^{2} : cd^{2} = ac : cb = 2 : 1`.
   5. Now construct in a plane a circle whose radius (semidiameter) equals :math:`cd`, and inscribe in it the equilateral triangle :math:`efg`. By the :just:`twelfth of the thirteenth <XIII.12>`, the square on the side of an equilateral triangle inscribed in a circle is triple the square on the radius of that circle (:math:`ef^{2} = 3\\,cd^{2}`).
   6. Because :math:`ac = 2\\,cb`, we have :math:`da^{2} = ac^{2} + cd^{2} = 4\\,cb^{2} + cd^{2}`; and since :math:`cd^{2} = ac \\cdot cb = 2\\,cb^{2}`, it follows that :math:`da^{2} = 2\\,cd^{2} + cd^{2} = 3\\,cd^{2}`. Therefore :math:`da^{2} = ef^{2}`, so each side :math:`ef, fg, ge` of the equilateral base equals :math:`da`!
   7. Erect from the center :math:`h` of the circle :math:`efg` a perpendicular to the plane of the triangle (:just:`XI.12`) of length :math:`hk = ac`, and join the vertex :math:`k` to :math:`e, f, g`. By the :just:`fourth of the eleventh <XI.4>` and the :just:`penultimate of the first <I.47>`, each slant edge satisfies:

      .. math::

         ke^{2} = kh^{2} + he^{2} = ac^{2} + cd^{2} = da^{2}

      Thus all six edges :math:`ef, fg, ge, ke, kf, kg` are mutually equal to :math:`da`, and as the semicircle :math:`adb` revolves around the fixed axis :math:`ab`, its circumference passes simultaneously through all four vertices :math:`k, e, f, g`.

Therefore the regular tetracedron has been formed and inscribed in the given sphere, and the square on the sphere's diameter :math:`ab` is *sesquialtera* (:math:`3 : 2`, or :math:`1\\frac{1}{2}`) to the square on the edge :math:`da` of the tetracedron. For example, if the diameter of the sphere is :math:`6` (so its square is :math:`36`), the square on the side of the tetracedron is :math:`24`, and the side itself is :math:`\\sqrt{24}` (*radice de 24*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0032 (``f. 8v``) includes diagram ``0032.g1.png``, showing the semicircle :math:`adb` cut at :math:`c` (:math:`ac = 2\\,cb`) alongside the base circle and triangle of the tetrahedron.
- **Mathematical Identity**: For a sphere of diameter :math:`D`, the edge :math:`a_{4}` of the inscribed regular tetrahedron satisfies :math:`D^{2} : a_{4}^{2} = 3 : 2`, or :math:`a_{4} = D\\sqrt{\\frac{2}{3}}`.
- **Comparison with Earlier Draft Track**: The earlier draft omitted Steps 5–7 (how the perpendicular :math:`hk = ac` from the center of the circumscribed circle of radius :math:`cd` proves :math:`ke = da` via :just:`XIII.12` and :just:`XI.4`).""",
    },
    27: {
        "title_en": "How the Second Regular Body, Called the Exacedron or Cube, Is Formed and Placed in the Sphere.",
        "body_en": """Following the order of Campanus in the thirteenth book (where the cube is placed as the fourteenth proposition, :just:`XIII.15` in the Greek text), we now show how to form the second regular body, called the **cubo** or **exacedron**, which has six square faces, eight solid angles, and twelve equal edges (:just:`XIII.15`).

.. enunciation:: Construction of the Cube in a Given Sphere (:just:`XIII.15` [Campanus XIII.14])

   Given the diameter of a sphere, to find the side of the cube inscribed in it, and to show that the square on the diameter of the sphere is triple (:math:`3 : 1`) the square on the side of the cube.

.. assertion:: Construction and Proof (:just:`XIII.15`, :just:`VI.8`, :just:`III.31`, :just:`I.47`, :just:`XI.6`, :just:`XI.33`)

   1. Let :math:`ab` be the diameter of the given sphere (see the marginal diagram ``0033.g1.png`` on Folio 0033), and divide :math:`ab` at point :math:`c` so that :math:`ac` is double :math:`cb` (:math:`ac = 2\\,cb`, hence :math:`ab = 3\\,cb`).
   2. Describe the semicircle :math:`adb` on diameter :math:`ab`, draw :math:`cd` perpendicular to :math:`ab` meeting the arc at :math:`d`, and join :math:`db` and :math:`da`.
   3. By the :just:`thirty-first of the third <III.31>` and the :just:`eighth of the sixth <VI.8>`, in the right triangle :math:`adb`, :math:`ab : cb = db^{2} : cb^{2}` and :math:`ab : db = db : cb`, so :math:`db^{2} = ab \\cdot cb`. Since :math:`ab = 3\\,cb`, the square on :math:`ab` is triple the square on :math:`db`:

      .. math::

         ab^{2} = 3\\,db^{2}

   4. Now construct a cube whose side (edge) equals :math:`db`: form the square base :math:`efgh` with each side equal to :math:`db`, erect four perpendiculars :math:`ek, fl, gm, hn` of length :math:`db` from the four corners of the base (:just:`XI.12`), which are parallel to one another (:just:`XI.6`), and join their upper extremities to complete the six square faces.
   5. Draw the diagonal :math:`eg` of the base square :math:`efgh`, and join the space diagonal :math:`en` from the lower corner :math:`e` to the opposite upper corner :math:`n`.
   6. Because :math:`efgh` is a square of side :math:`db`, by the :just:`penultimate of the first <I.47>` the square on the face diagonal :math:`eg` is double the square on the edge (:math:`eg^{2} = ef^{2} + fg^{2} = 2\\,db^{2}`).
   7. And because the vertical edge :math:`gn` is perpendicular to the base plane, :math:`\\angle egn` is a right angle (:just:`XI.Def.3`); hence in the right triangle :math:`egn`, the square on the space diagonal :math:`en` equals :math:`eg^{2} + gn^{2} = 2\\,db^{2} + db^{2} = 3\\,db^{2}`.
   8. Since we already proved in Step 3 that :math:`ab^{2} = 3\\,db^{2}`, it follows that :math:`en^{2} = ab^{2}`, and therefore the space diagonal :math:`en` of the cube equals the diameter :math:`ab` of the sphere!
   9. If a semicircle is described on the space diagonal :math:`en` as diameter and revolved around :math:`en`, by the :just:`thirty-first of the third <III.31>` the semicircle passes through :math:`g` and through every one of the eight right-angled vertices of the cube.

Thus the cube has been constructed and inscribed in the given sphere, and the square on the sphere's diameter is **triple** (:math:`3 : 1`) the square on the edge of the cube. For example, if the diameter of the sphere is :math:`6` (whose square is :math:`36`), the square on the side of the cube is one-third of :math:`36`, namely :math:`12`, and the side of the cube in length is :math:`\\sqrt{12}` (*radice de 12*), while the face diagonal is :math:`\\sqrt{24}` (equal to the edge of the tetracedron in the same sphere!).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Campanus vs. Heiberg Ordering**: In Campanus's Latin *Elements*, the Cube is Proposition 14 of Book XIII and the Octahedron is Proposition 15 (whereas in Heiberg's Greek text the Octahedron is :just:`XIII.14` and the Cube is :just:`XIII.15`). Pacioli follows Campanus's order here and explicitly explains the reason for this transposition at the end of ``Cap. XXXI``.
- **Relation to the Tetrahedron**: Using the same semicircle :math:`adb` cut at :math:`c` with :math:`ac = 2\\,cb`, the longer chord :math:`da` is the edge of the inscribed **tetrahedron** (:math:`da^{2} = \\frac{2}{3}ab^{2}`), the shorter chord :math:`db` is the edge of the inscribed **cube** (:math:`db^{2} = \\frac{1}{3}ab^{2}`), and therefore the edge of the tetrahedron is the face diagonal of the cube (:math:`da^{2} = 2\\,db^{2}`).""",
    },
    28: {
        "title_en": "How the Third Regular Body, Called the Octocedron of Eight Triangular Bases, Is Formed in the Sphere.",
        "body_en": """Next we show how to form the third regular body, called the **octocedron**, which is bounded by eight equilateral triangles meeting four by four at six solid angles along twelve equal edges (:just:`XIII.14` [Campanus XIII.15]).

.. enunciation:: Construction of the Regular Octahedron in a Given Sphere (:just:`XIII.14`)

   Given the diameter of a sphere, to find the side of the regular body of eight equilateral triangular bases (*octocedron*) inscribed in it, and to show that the square on the diameter of the sphere is double (:math:`2 : 1`) the square on the side of the octocedron.

.. assertion:: Construction and Proof (:just:`XIII.14`, :just:`III.31`, :just:`I.47`, :just:`IV.6`)

   1. Let :math:`ab` be the diameter of the given sphere (see the marginal diagram ``0033.g2.png`` on Folio 0033), and bisect :math:`ab` at its midpoint :math:`c` (:math:`ac = cb = \\frac{1}{2}ab`).
   2. Describe the semicircle :math:`adb` upon diameter :math:`ab`, draw :math:`cd` from the center :math:`c` perpendicular to :math:`ab` meeting the circumference at :math:`d`, and join the chord :math:`db` (and :math:`da`).
   3. Because :math:`ac = cb = cd` (all three being radii of the semicircle :math:`adb`), in the right triangle :math:`dcb` (:just:`I.47`), :math:`db^{2} = dc^{2} + cb^{2} = 2\\,cb^{2}`. Meanwhile :math:`ab = 2\\,cb \\implies ab^{2} = 4\\,cb^{2}`. Therefore the square on the diameter of the sphere (:math:`ab^{2}`) is **double** the square on :math:`db`:

      .. math::

         ab^{2} = 2\\,db^{2}

   4. Now construct in a plane a square :math:`efgh` whose four sides :math:`ef, fg, gh, he` each equal :math:`db` (or equivalently, inscribe the square :math:`efgh` in a circle of diameter :math:`ab` by the :just:`sixth of the fourth <IV.6>`), and draw its two diagonals :math:`eg` and :math:`fh` intersecting at center :math:`k`.
   5. Because :math:`ef = db` and :math:`ab^{2} = 2\\,db^{2}`, each diagonal :math:`eg` and :math:`fh` of the square :math:`efgh` equals :math:`ab`, and each half-diagonal :math:`ke, kf, kg, kh` equals the radius :math:`cb = cd` of the sphere.
   6. Through the center :math:`k` of the square :math:`efgh`, draw a straight line :math:`lm` perpendicular to the plane of the square :math:`efgh` on both sides (:just:`XI.12`), making each half-axis :math:`kl` and :math:`km` equal to :math:`ke = kf = kg = kh = cb` (the radius of the sphere).
   7. Join the upper pole :math:`l` and the lower pole :math:`m` by eight straight lines :math:`le, lf, lg, lh` and :math:`me, mf, mg, mh` to the four corners of the central square :math:`efgh`.
   8. Since :math:`kl` and :math:`km` are perpendicular to the plane :math:`efgh`, all eight triangles :math:`kle, klf, \\dots, kmh` are right-angled at :math:`k` with legs equal to :math:`cb`; hence by :just:`I.47` each of the eight slant edges equals :math:`db`, matching the four edges :math:`ef, fg, gh, he` of the equatorial square.
   9. Thus all twelve edges are equal to :math:`db`, all eight faces are equilateral triangles, and since the six distances :math:`ke, kf, kg, kh, kl, km` from the center :math:`k` are all equal to the radius :math:`cb` of the sphere, the semicircle described on the axis :math:`lm` passes through all six vertices :math:`l, m, e, f, g, h` as it revolves.

Therefore the octocedron is formed and inscribed in the sphere, and the square on the diameter of the sphere is **double** (:math:`2 : 1`) the square on the edge of the octocedron. In numbers, if the diameter of the sphere is :math:`6` (whose square is :math:`36`), the square on the edge of the octocedron is half of :math:`36`, namely :math:`18`, and its edge in length is :math:`\\sqrt{18}` (*radice de 18*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0033 (``f. 9r``) provides diagram ``0033.g2.png`` illustrating the bisected semicircle :math:`adb` and the equatorial square :math:`efgh` with its diagonals and perpendicular axis.
- **Three Perpendicular Axes**: Notice Step 6: the octahedron is spanned by three mutually perpendicular diameters :math:`eg`, :math:`fh`, and :math:`lm` intersecting at the center :math:`k`—a structural property that Pacioli later calls "the glorious sign of the Holy Cross" in ``Cap. XLVI`` when explaining why the octahedron cannot be inscribed in the icosahedron.""",
    },
    29: {
        "title_en": "How the Fourth Regular Body, Called the Ycocedron of Twenty Triangular Bases, Is Formed in the Sphere.",
        "body_en": """Having constructed the first three regular bodies—whose edges are either commensurable in square with the sphere's diameter—we now come to the fourth regular body, called the **ycocedron**, bounded by twenty equilateral triangles meeting five by five at twelve solid angles along thirty equal edges. As promised, its construction requires our **Divine Proportion** (:just:`XIII.16`).

.. enunciation:: Construction of the Regular Icosahedron in a Given Sphere (:just:`XIII.16`)

   Given the diameter of a sphere, to construct the regular body of twenty equilateral triangular bases (*ycocedron*) inscribed in that sphere, and to demonstrate that the side (edge) of the ycocedron is an irrational line of the fourth species of subtraction, called the **Minor** (*linea menore*, :just:`X.76`).

.. assertion:: Construction and Proof (:just:`XIII.16`, :just:`XIII.9`, :just:`XIII.10`, :just:`XIII.3`, :just:`X.16`, :just:`X.76`)

   1. Let :math:`ab` be the diameter of the given sphere (see the marginal diagram ``0034.g1.png`` on Folio 0034), and divide :math:`ab` at point :math:`c` so that :math:`ac` is quadruple :math:`cb` (:math:`ac = 4\\,cb`, so :math:`ab = 5\\,cb`).
   2. Describe the semicircle :math:`adb` upon diameter :math:`ab`, draw the perpendicular :math:`cd` meeting the arc at :math:`d`, and join :math:`db`. By the :just:`eighth of the sixth <VI.8>`, :math:`ab : cb = ab^{2} : db^{2} = 5 : 1` and :math:`ac : cb = cd^{2} : cb^{2} = 4 : 1`, so :math:`ab^{2} = 5\\,db^{2}` and :math:`cd = 2\\,cb`.
   3. Set out in a plane a circle :math:`efghk` whose radius (semidiameter) equals :math:`db`. Thus the square on the diameter :math:`ab` of the sphere is **quintuple** (:math:`5 : 1`) the square on the radius :math:`db` of circle :math:`efghk`.
   4. Inscribe in the circle :math:`efghk` the regular pentagon :math:`efghk` (:just:`IV.11`) and the regular decagon by bisecting the cinco arcs :math:`ef, fg, gh, hk, ke` at their midpoints. Then the side of the hexagon inscribed in circle :math:`efghk` equals the radius :math:`db` (:just:`IV.15` Corollary).
   5. From the five vertices :math:`e, f, g, h, k` of the pentagon, erect five perpendiculars to the plane of the circle (:just:`XI.12`), each of height equal to the radius :math:`db` (the side of the hexagon), and join their upper endpoints to form a second parallel regular pentagon rotated by one decagonal arc (:math:`36^{\\circ}`) relative to the lower pentagon.
   6. Joining the alternating vertices of the upper and lower pentagons gives ten lateral triangles forming a pentagonal antiprism (drum). For each lateral slant edge, its horizontal projection in the circle is the chord of one decagonal arc (:math:`s_{10}`), and its vertical rise is the radius (:math:`s_{6} = db`). By the :just:`penultimate of the first <I.47>` and the :just:`tenth of the thirteenth <XIII.10>` (:ref:`Chapter XXIV <compendio-cap_24-en>`):

      .. math::

         s_{6}^{2} + s_{10}^{2} = s_{5}^{2}

      Therefore all ten lateral slant edges equal the side :math:`s_{5}` of the pentagon :math:`efghk`, so the middle drum consists of **ten equilateral triangles** of side :math:`s_{5}`!
   7. Now erect the central axis through the centers of the two parallel circles, and extend it above the upper circle and below the lower circle by a segment equal to the **side of the decagon** (:math:`s_{10}`) at each pole. Joining the upper pole to the five vertices of the upper pentagon and the lower pole to the five vertices of the lower pentagon adds **five upper** and **five lower** triangles. Because the distance from each pole to the center of its adjacent circle is :math:`s_{10}` and the radius of the circle is :math:`s_{6}`, by :just:`I.47` and :just:`XIII.10` each of the ten polar edges again satisfies :math:`s_{10}^{2} + s_{6}^{2} = s_{5}^{2}`!
   8. Thus all **thirty edges** equal :math:`s_{5}`, and all **twenty faces** are equilateral triangles. Moreover, the total length of the axis from pole to pole is the height of the drum (:math:`s_{6}`) plus the two polar extensions (:math:`2\\,s_{10}`):

      .. math::

         \\text{Axis} = s_{6} + 2\\,s_{10}

      By the :just:`ninth of the thirteenth <XIII.9>`, :math:`s_{6} + s_{10}` is divided in the Divine Proportion with greater segment :math:`s_{6}`; hence by the :just:`third of the thirteenth <XIII.3>` (:ref:`Chapter XI <compendio-cap_11-en>`), the square on :math:`s_{6} + \\frac{1}{2}s_{6}`? Nay, by the :just:`fourth` and :just:`eighth` of Book XIII, :math:`(s_{6} + 2\\,s_{10})^{2} = 5\\,s_{6}^{2} = 5\\,db^{2} = ab^{2}`! Therefore the axis from pole to pole equals the sphere's diameter :math:`ab`, and all twelve vertices lie on the sphere.
   9. **Irrationality of the Edge**: If the diameter :math:`ab` of the sphere is assumed rational, then since :math:`ab^{2} = 5\\,db^{2}`, the radius :math:`db` (:math:`s_{6}`) is rational only in square (:just:`X.Def.3`), and by the :just:`eleventh of the thirteenth <XIII.11>` (:ref:`Chapter XXIII <compendio-cap_23-en>`), the side :math:`s_{5}` of the pentagon—which is the edge of the ycocedron—is an irrational line called the **Minor** (*linea menore*, :just:`X.76`).

.. rubric:: Numerical Example

If the diameter of the sphere is :math:`10` (so its square is :math:`100`), the square on the radius :math:`db` of the pentagon's circle is one-fifth of :math:`100`, namely :math:`20` (:math:`db = \\sqrt{20}`). By :just:`XIII.11`, the edge of the ycocedron is the Minor :math:`\\sqrt{50 - \\sqrt{500}}` (*radice universale de 50 men radice de 500*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0034 (``f. 9v``) includes diagram ``0034.g1.png``, showing the sphere diameter divided in :math:`4:1` ratio (:math:`ac = 4\\,cb`) and the circle containing the pentagon and decagon.
- **Role of the Divine Proportion**: This construction brings together nearly every theorem proved in Section 2: :just:`XIII.9` (sum of hexagon and decagon sides divided in extreme and mean ratio), :just:`XIII.10` (:math:`s_{5}^{2} = s_{6}^{2} + s_{10}^{2}`), and :just:`XIII.11` (the side of the pentagon is a *Minor*, :just:`X.76`).
- **Exact Formula**: For a sphere of diameter :math:`D`, the radius of the circumcircle of the two parallel pentagonal cross-sections is :math:`R = \\frac{D}{\\sqrt{5}}`, and the edge of the icosahedron is :math:`a_{20} = R\\sqrt{\\frac{5 - \\sqrt{5}}{2}} = D\\sqrt{\\frac{5 - \\sqrt{5}}{10}}`. For :math:`D = 10`, :math:`a_{20} = \\sqrt{50 - 10\\sqrt{5}} = \\sqrt{50 - \\sqrt{500}}`.""",
    },
    30: {
        "title_en": "How the Fifth and Most Noble Regular Body, Called the Duodecedron of Twelve Pentagonal Bases, Is Formed in the Sphere.",
        "body_en": """Now we come to the fifth and last regular body, the **duodecedron**, bounded by twelve equilateral and equiangular pentagons meeting three by three at twenty solid angles along thirty equal edges. Just as Plato in the *Timaeus* assigned this body to the fifth essence—the universal heaven (*il cielo*) that encompasses all the elements—so its geometric creation crowns Book XIII (:just:`XIII.17`) and arises directly from the **Cube** by dividing its edges according to our **Divine Proportion**.

.. enunciation:: Construction of the Regular Dodecahedron in a Given Sphere (:just:`XIII.17`)

   Given the diameter of a sphere, to construct the regular body of twelve equilateral and equiangular pentagonal bases (*duodecedron*) inscribed in that sphere, and to demonstrate that the side (edge) of the duodecedron is an irrational line called the **Apotome** or **Residue** (*residuo*, :just:`X.73`), namely the greater segment of the side of the cube inscribed in the same sphere when divided according to our Divine Proportion.

.. assertion:: Construction and Proof (:just:`XIII.17`, :just:`XIII.15`, :just:`II.11`, :just:`XIII.4`, :just:`XIII.5`, :just:`XIII.6`, :just:`XIII.7`, :just:`I.47`)

   1. First inscribe in the given sphere the **cube** (*exacedron*) by the method of :ref:`Chapter XXVII <compendio-cap_27-en>` (:just:`XIII.15`), so that the square on the diameter of the sphere is triple the square on the edge of the cube.
   2. On two adjacent square faces :math:`abcd` and :math:`ebcf` of the cube sharing the common edge :math:`bc` (see the marginal diagram ``0035.g1.png`` on Folio 0035), bisect the sides at their midpoints and join the opposite midpoints by the median lines :math:`gh, kl` on face :math:`abcd` (intersecting at the face center :math:`m`) and :math:`no, pq` on face :math:`ebcf` (intersecting at the face center :math:`r`), so that :math:`gm = mh = np = po = \\frac{1}{2}bc`.
   3. Now divide the half-medians :math:`np, po, mh` according to the **Divine Proportion** (extreme and mean ratio, :just:`II.11`, :just:`VI.30`) at points :math:`s, t, u`, making :math:`ns, pt, mu` their **greater segments** (so :math:`ns = pt = mu`).
   4. From points :math:`s` and :math:`t` on the median :math:`no`, erect perpendiculars :math:`sv` and :math:`tx` to the plane of the face :math:`ebcf` (:just:`XI.12`) outward from the cube, each equal in length to the greater segment :math:`ns = pt = mu`, and join the five straight lines :math:`bv, vx, xc, cu, ub`.
   5. **Equilateral Proof**:
      - By the :just:`fifth of the thirteenth <XIII.5>` (:ref:`Chapter XIII <compendio-cap_13-en>`), because :math:`np` is divided in the Divine Proportion at :math:`s` with greater segment :math:`ns`, if we add :math:`ns = pt` across the center :math:`p`, the segment :math:`st` between the two perpendiculars equals :math:`2\\,sp`; wait—since :math:`np` is half the cube edge :math:`bc` and :math:`ns` is the greater segment of :math:`np`, :math:`st = 2\\,sp`? Nay! The points :math:`s` and :math:`t` are chosen so that :math:`ps` and :math:`pt` are the **lesser** segments, or rather :math:`ps` and :math:`pt` are such that the distance :math:`vx = st` between the two roof vertices equals the greater segment of the full cube edge :math:`bc`! Specifically, since :math:`np = \\frac{1}{2}bc` and :math:`ps` is the lesser segment when :math:`np` is cut in extreme and mean ratio with greater segment :math:`ns`, by :just:`XIII.5` the line :math:`np + ns` is cut in extreme and mean ratio with greater segment :math:`np` and lesser segment :math:`ns`; doubling shows that :math:`st = 2\\,ps`? Rather, in Euclid's exact labeling (:just:`XIII.17`), :math:`ps` and :math:`pt` are the **greater** segments of :math:`np` and :math:`po` (measured outward from the center :math:`p`), while the height of the roof :math:`sv = tx` equals the **lesser** segment :math:`ns`, or conversely the roof ridge :math:`vx = st` has length equal to :math:`2\\,ps`—Wait: if :math:`ns` is the greater segment of :math:`np = \\frac{1}{2}bc`, then :math:`2\\,ns` is the **greater segment of the whole cube edge** :math:`bc`! Setting the ridge :math:`vx` equal to :math:`2\\,ns` (so :math:`s` and :math:`t` are at distance :math:`ns` on either side of the center :math:`p`) and the perpendicular height of :math:`v, x, u` above the cube faces equal to the **lesser segment** of :math:`np`, by the :just:`fourth of the thirteenth <XIII.4>` (:ref:`Chapter XII <compendio-cap_12-en>`) and :just:`I.47`, each of the five sides :math:`bv, vx, xc, cu, ub` of the pentagon :math:`bvxcu` equals :math:`2\\,ns`, the **greater segment of the edge of the cube**!
   6. **Coplanarity and Equiangularity Proof**:
      - By the :just:`sixth of thesixth <VI.6>` and :just:`XI.10`, the five points :math:`b, v, x, c, u` lie in one and the same plane.
      - By the :just:`eighth of the thirteenth <XIII.8>` (:ref:`Chapter XVI <compendio-cap_16-en>`) and :just:`I.47`, each chord :math:`bc, bu, cu` subtending an angle of the pentagon :math:`bvxcu` equals the cube edge :math:`bc`; hence three angles of the equilateral pentagon :math:`bvxcu` are equal, and by the :just:`seventh of the thirteenth <XIII.7>` (:ref:`Chapter XXI <compendio-cap_21-en>`), any equilateral pentagon having three angles equal is **equiangular**!
   7. Constructing such a roof of two pentagonal faces over each of the six square faces of the cube (twelve pentagons in all, sharing the twelve edges of the cube as pentagonal diagonals and having twenty vertices: the eight vertices of the cube plus the twelve roof-ridge vertices) completes the **duodecedron**.
   8. **Inscribability in the Same Sphere**: The distance from the center :math:`z` of the sphere (and cube) to each of the twelve new roof vertices :math:`v, x, u, \\dots` satisfies, by :just:`I.47` and the :just:`fourth of the thirteenth <XIII.4>` (:math:`a^{2} + b^{2} = 3\\,g^{2}`):

      .. math::

         zv^{2} = \\left(\\frac{1}{2}bc + \\text{lesser}\\right)^{2} + (\\text{greater})^{2} = 3\\left(\\frac{1}{2}bc\\right)^{2}

      which is identical to the squared distance from the center :math:`z` to the eight corners of the cube! Hence the same sphere that circumscribes the cube passes through all twenty vertices of the duodecedron.
   9. **Irrationality of the Edge**: Since the square on the sphere's diameter is triple the square on the cube's edge (:math:`D^{2} = 3\\,s_{\\text{cube}}^{2}`), when :math:`D` is rational, the edge of the cube is rational in square only. And by the :just:`sixth of the thirteenth <XIII.6>` (:ref:`Chapter XIV <compendio-cap_14-en>`), when a line rational in square is divided according to our Divine Proportion, each of its segments is an **Apotome** (*residuo*, :just:`X.73`). Therefore the edge of the duodecedron is an irrational line called an **Apotome**.

.. rubric:: Numerical Example

If the diameter of the sphere is :math:`6` (whose square is :math:`36`), the square on the edge of the cube is :math:`12` (:math:`s_{\\text{cube}} = \\sqrt{12}`). Dividing :math:`\\sqrt{12}` according to our Divine Proportion (:ref:`Chapter IX <compendio-cap_09-en>`), its greater segment—which is the edge of the duodecedron—is :math:`\\sqrt{15} - \\sqrt{3}` (*radice de 15 men radice de 3*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0035 (``f. 10r``) displays diagram ``0035.g1.png``, showing the unfolded squares of the cube with their bisected medians and the pentagonal face :math:`bvxcu` pitched like a hipped roof (*coperto / colmo*) over the cube edge :math:`bc`.
- **Why Section 2 Proved :just:`XIII.4`, :just:`XIII.6`, and :just:`XIII.7`**: Every step of Euclid's construction of the dodecahedron in :just:`XIII.17` calls upon a specific proposition from earlier in Book XIII:
  - :just:`XIII.4` (:math:`L^{2} + b^{2} = 3a^{2}`) proves both that the roof edges equal the ridge :math:`2a` and that the twelve roof vertices lie at the same distance :math:`\\sqrt{3}\\cdot(\\frac{1}{2}s_{\\text{cube}})` from the center of the cube as the eight cube corners!
  - :just:`XIII.7` proves that the pentagon :math:`bvxcu` is equiangular because three of its angles are subtended by equal chords (:math:`bc` and the two diagonals meeting at :math:`u`).
  - :just:`XIII.6` proves that the edge :math:`a_{12} = \\frac{\\sqrt{5}-1}{2} s_{\\text{cube}}` is an **Apotome** (:just:`X.73`).
- **Verification of Pacioli's Numerical Example**: For :math:`D = 6`, :math:`s_{\\text{cube}} = \\sqrt{12}`. The greater segment of :math:`\\sqrt{12}` cut in extreme and mean ratio is :math:`\\frac{\\sqrt{5}-1}{2}\\sqrt{12} = \\sqrt{3}(\\sqrt{5}-1) = \\sqrt{15} - \\sqrt{3}`.""",
    },
    31: {
        "title_en": "On the Rule and Way to Find the Sides of All Five Regular Bodies Placed in One and the Same Sphere, and Their Comparison with One Another.",
        "body_en": """Now that we have shown how each of the five regular bodies is individually formed and placed in a sphere, it remains, in accordance with the :just:`eighteenth and last proposition of the thirteenth book <XIII.18>`, to set all five sides together in a single figure upon the diameter of one and the same sphere and compare their magnitudes and proportions with one another.

.. enunciation:: Comparison of the Edges of All Five Regular Solids in the Same Sphere (:just:`XIII.18`)

   To set out in a single plane diagram the sides (edges) of all five regular bodies inscribed in one and the same sphere, and to compare them with one another both in square (*in potentia*) and in length (*in longitudine*).

.. assertion:: Construction on the Semicircle (:just:`XIII.18`)

   1. Let :math:`ab` be the diameter of the sphere, and upon :math:`ab` describe the semicircle :math:`afdb` (see the marginal diagram ``0036.g1.png`` on Folio 0036).
   2. Divide the diameter :math:`ab` at point :math:`c` so that :math:`ac = 2\\,cb` (:math:`cb = \\frac{1}{3}ab`), and at point :math:`e` so that :math:`ae = eb` (:math:`eb = \\frac{1}{2}ab`). Erect the perpendiculars :math:`cd` and :math:`ef` to meet the circumference at :math:`d` and :math:`f`, and join the chords :math:`ad`, :math:`db`, and :math:`fb`.
      - By :ref:`Chapter XXVI <compendio-cap_26-en>` (:just:`XIII.13`), the chord :math:`ad` is the **side of the tetracedron**, and :math:`ab^{2} : ad^{2} = 3 : 2` (:math:`ad^{2} = \\frac{2}{3}ab^{2}`).
      - By :ref:`Chapter XXVII <compendio-cap_27-en>` (:just:`XIII.15`), the chord :math:`db` is the **side of the cube**, and :math:`ab^{2} : db^{2} = 3 : 1` (:math:`db^{2} = \\frac{1}{3}ab^{2}`).
      - By :ref:`Chapter XXVIII <compendio-cap_28-en>` (:just:`XIII.14`), the chord :math:`fb` is the **side of the octocedron**, and :math:`ab^{2} : fb^{2} = 2 : 1` (:math:`fb^{2} = \\frac{1}{2}ab^{2}`).
   3. From point :math:`a`, erect :math:`ag` perpendicular to the diameter :math:`ab` and equal in length to the entire diameter :math:`ab` (:math:`ag = ab`). Join :math:`gb` from the top :math:`g` to the opposite end :math:`b` of the diameter, cutting the circumference of the semicircle at point :math:`h`, and from :math:`h` drop the perpendicular :math:`hk` onto the diameter :math:`ab`.
   4. Because :math:`ag = ab`, in the right triangle :math:`gab` the leg :math:`ab` equals the leg :math:`ag`; by similar triangles (:just:`VI.4`), :math:`hk = ak`, so :math:`ak^{2} = hk^{2}`. And in the semicircle :math:`ahb`, :math:`hk^{2} = ak \\cdot kb`, whence :math:`ak = kb`? Nay: :math:`gb^{2} = ag^{2} + ab^{2} = 2\\,ab^{2}`, and since :math:`\\triangle hkb \\sim \\triangle agb` with :math:`ab = ag`, we have :math:`kb = hk`! Then :math:`hk^{2} = ak \\cdot kb = ak \\cdot hk \\implies ak = hk = kb`? Wait: :math:`ag` is tangent at :math:`a`, and :math:`gb` joins :math:`g` to :math:`b` (or to the center :math:`e`!). Let us follow the exact Euclidean construction (:just:`XIII.18`):
      - If :math:`ag = ab` is drawn perpendicular at :math:`a` and joined not to :math:`b` but to the **center** :math:`e` of the semicircle, cutting the circumference at :math:`h`, then since :math:`ag = 2\\,ae`, by similar right triangles :math:`\\triangle hke \\sim \\triangle age`, the perpendicular :math:`hk` is **double** :math:`ke` (:math:`hk = 2\\,ke`).
      - Since :math:`eh` is the radius (:math:`eh = eb = \\frac{1}{2}ab`), in the right triangle :math:`hke` we have :math:`eh^{2} = hk^{2} + ke^{2} = 4\\,ke^{2} + ke^{2} = 5\\,ke^{2}`, so :math:`ab^{2} = 4\\,eh^{2} = 20\\,ke^{2}` and :math:`hk^{2} = 4\\,ke^{2} = \\frac{1}{5}ab^{2}`!
      - Therefore :math:`hk` equals the radius of the circle in which the pentagon of the **ycocedron** is inscribed (:ref:`Chapter XXIX <compendio-cap_29-en>`), and :math:`ke = \\frac{1}{2}hk`, while :math:`ak = ae - ke` is the side of the decagon! Joining the chord :math:`ah` gives :math:`ah^{2} = ak^{2} + hk^{2} = s_{10}^{2} + s_{6}^{2} = s_{5}^{2}` (:just:`XIII.10`). Thus the chord :math:`ah` is the **side of the ycocedron**!
   5. Finally, divide the chord :math:`db` (which is the **side of the cube**) at point :math:`m` according to our **Divine Proportion**, making :math:`dm` its greater segment. By :ref:`Chapter XXX <compendio-cap_30-en>` (:just:`XIII.17`), :math:`dm` is the **side of the duodecedron**!

.. assertion:: Comparison of the Five Edges (:just:`XIII.18`)

   1. Comparing the first three edges in square (*in potentia*):
      - :math:`s_{\\text{tetra}}^{2} = ad^{2} = \\frac{2}{3}ab^{2}`
      - :math:`s_{\\text{octa}}^{2} = fb^{2} = \\frac{1}{2}ab^{2}`
      - :math:`s_{\\text{cube}}^{2} = db^{2} = \\frac{1}{3}ab^{2}`
      Hence :math:`s_{\\text{tetra}}^{2} = \\frac{4}{3} s_{\\text{octa}}^{2}` (*sesquitertia*, :math:`4 : 3`), :math:`s_{\\text{tetra}}^{2} = 2\\,s_{\\text{cube}}^{2}` (*dupla*, :math:`2 : 1`), and :math:`s_{\\text{octa}}^{2} = \\frac{3}{2} s_{\\text{cube}}^{2}` (*sesquialtera*, :math:`3 : 2`).
   2. Comparing all five edges in length:

      .. math::

         s_{\\text{tetra}} > s_{\\text{octa}} > s_{\\text{cube}} > s_{\\text{icosa}} > s_{\\text{dodeca}}

      For :math:`ad > fb > db` because they subtend successively smaller arcs of the semicircle; and :math:`db > ah` because :math:`db^{2} = \\frac{1}{3}ab^{2}` whereas :math:`ah^{2} = \\frac{5 - \\sqrt{5}}{10}ab^{2} < \\frac{1}{3}ab^{2}`; and :math:`ah > dm` (the side of the ycocedron is greater than the side of the duodecedron, as proved in :just:`XIII.18` and further by Hypsicles in :just:`XIV.2` because the circle circumscribing the triangle of the ycocedron equals the circle circumscribing the pentagon of the duodecedron).

And note that it is **not without mystery** (*non senza misterio*) that in the construction of these bodies Campanus placed the **cube** (the second body, of 6 bases) before the **octocedron** (the third body, of 8 bases), even though the octocedron has a larger edge than the cube: for in the semicircle :math:`adb`, the single perpendicular :math:`cd` drawn at one-third of the diameter simultaneously yields **both** the side :math:`ad` of the tetracedron on one side and the side :math:`db` of the cube on the other!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0036 (``f. 10v``) contains the famous master diagram ``0036.g1.png`` of :just:`XIII.18`, displaying the semicircle with all five edges (:math:`ad` = tetrahedron, :math:`fb` = octahedron, :math:`db` = cube, :math:`ah` = icosahedron, :math:`dm` = dodecahedron).
- **Pacioli's Observation on Campanus's Ordering ("Not Without Mystery")**: Pacioli astutely explains why Campanus of Novara placed the Cube (Campanus XIII.14) immediately after the Tetrahedron (XIII.13) and before the Octahedron (Campanus XIII.15): the single trisection point :math:`c` (:math:`ac = 2\\,cb`) on diameter :math:`ab` gives the tetrahedron edge :math:`ad` as the longer chord and the cube edge :math:`db` as the shorter chord in the very same right triangle :math:`adb`!""",
    },
    32: {
        "title_en": "On the Proportion of the Said Regular Bodies to One Another, Especially that of the Ycocedron to the Duodecedron.",
        "body_en": """Having compared the sides of all five regular bodies inscribed in the same sphere according to the thirteenth book, we now proceed to the **fourteenth book** of our philosopher—composed by **Hypsicles of Alexandria** (*Ypsicle Alexandrino*) following the discoveries of **Aristaeus** (*Aristeo*) and **Apollonius** (*Apollonio*) and commented upon by **Campanus**—which investigates the admirable proportions of the surfaces and solid volumes of these bodies, above all the **ycocedron** and the **duodecedron** inscribed in the same sphere (:just:`XIV.2`, :just:`XIV.6`, :just:`XIV.7`, :just:`XIV.8`).

.. enunciation:: Fundamental Ratios of the Icosahedron and Dodecahedron in the Same Sphere (:just:`XIV.2`, :just:`XIV.6`–:just:`XIV.8`)

   When the regular ycocedron (20 triangular faces) and the regular duodecedron (12 pentagonal faces) are inscribed in one and the same sphere:

   1. **Same Circumcircle of Faces** (:just:`XIV.2` [Campanus XIV.6]): One and the same circle circumscribes both the pentagonal base of the duodecedron and the triangular base of the ycocedron.
   2. **Equal Central Altitude**: Consequently, the perpendiculars drawn from the center of the sphere to the center of a pentagonal face of the duodecedron and to the center of a triangular face of the ycocedron are **equal** to one another; hence a single sphere inscribed within them touches the faces of both bodies equally!
   3. **Ratio of Total Surfaces and Ratio of Solid Volumes** (:just:`XIV.7`, :just:`XIV.8`): The total surface of the twelve pentagons of the duodecedron has to the total surface of the twenty triangles of the ycocedron—and likewise the solid volume (*corporatura*) of the duodecedron has to the solid volume of the ycocedron—the exact same proportion as the **side of the cube** has to the **side of the ycocedron**? Nay, the total surface (and solid volume) of the **ycocedron** has to the total surface (and solid volume) of the **duodecedron** the ratio of the **side of the ycocedron** to the **side of the cube**? Let us state Campanus's exact theorem (:just:`XIV.6`–:just:`XIV.8`):
      - Because the perpendiculars from the center of the sphere to the faces of both solids are equal (:math:`r_{\\text{in}}`), each solid is resolved into pyramids having the sphere's center as common apex and height :math:`r_{\\text{in}}` (12 pentagonal pyramids for the duodecedron, 20 triangular pyramids for the ycocedron). Therefore, **the solid volume of the duodecedron is to the solid volume of the ycocedron exactly as the total surface area of the duodecedron is to the total surface area of the ycocedron**!
      - And by the :just:`seventh and eighth of the fourteenth <XIV.7>`, the surface (and volume) of the duodecedron has to the surface (and volume) of the ycocedron the ratio of the **side of the cube** (:math:`s_{\\text{cube}}`) to the **side of the ycocedron** (:math:`s_{20}`):

      .. math::

         \\frac{\\text{Vol}(\\text{Dodecahedron})}{\\text{Vol}(\\text{Icosahedron})} = \\frac{\\text{Area}(\\text{Dodecahedron})}{\\text{Area}(\\text{Icosahedron})} = \\frac{s_{\\text{cube}}}{s_{\\text{icosa}}} = \\sqrt{\\frac{5 + \\sqrt{5}}{6}}?

      Wait: in a sphere of radius :math:`R`, the circumradius :math:`\\rho` of both the triangle of the icosahedron and the pentagon of the dodecahedron is :math:`\\rho = R\\sqrt{\\frac{3-\\sqrt{5}}{2}}`? No, :math:`r_{\\text{in}}^{2} + \\rho^{2} = R^{2}`: since both faces have the **same circumradius** :math:`\\rho`, the **icosahedron** has a larger edge (:math:`s_{20} = \\rho\\sqrt{3}`) than the dodecahedron (:math:`s_{12} = \\rho\\sqrt{\\frac{5-\\sqrt{5}}{2}}`), and the **icosahedron** has a **larger surface area and larger volume** than the dodecahedron! Specifically:

      .. math::

         \\frac{\\text{Vol}(\\text{Icosahedron})}{\\text{Vol}(\\text{Dodecahedron})} = \\frac{\\text{Area}(\\text{Icosahedron})}{\\text{Area}(\\text{Dodecahedron})} = \\frac{s_{\\text{cube}}}{s_{\\text{icosa}}}

      because :math:`s_{\\text{cube}} > s_{\\text{icosa}}` (as proved in :ref:`Chapter XXXI <compendio-cap_31-en>`), so the ratio :math:`s_{\\text{cube}} : s_{\\text{icosa}}` is a ratio of **greater inequality** (:math:`\\sqrt{\\frac{10}{3(5-\\sqrt{5})}} = \\sqrt{\\frac{5+\\sqrt{5}}{6}} > 1`)!

.. assertion:: Proof Summary (:just:`XIV.2`, :just:`XIV.6`, :just:`XIV.7`, :just:`XIV.8`)

   1. By Aristaeus's theorem proved in :just:`XIV.2`, one and the same circle circumscribes both the pentagon of the duodecedron and the triangle of the ycocedron inscribed in the same sphere.
   2. Since equal circles in a sphere stand at equal perpendicular distances from the center of the sphere (:just:`III.14`), the perpendicular from the sphere's center to a pentagonal base of the duodecedron equals the perpendicular to a triangular base of the ycocedron.
   3. Dividing the duodecedron into 12 pyramids of height :math:`h` and the ycocedron into 20 pyramids of the same height :math:`h`, their solid volumes are in the exact same proportion as their total surface areas (the sum of the 12 pentagons to the sum of the 20 triangles).
   4. And by :just:`XIV.7`–:just:`XIV.8`, the ratio of the 20 triangles of the ycocedron to the 12 pentagons of the duodecedron equals the ratio of the **side of the cube** to the **side of the ycocedron** inscribed in the same sphere; and also equals the ratio of the line whose square is :math:`\\sqrt{\\frac{5+\\sqrt{5}}{6}}`.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Hypsicles' Book XIV**: Book XIV of the *Elements* was written by Hypsicles of Alexandria (2nd century BCE), who cites the lost treatise *On the Comparison of the Five Figures* by Aristaeus the Elder and the treatise on the dodecahedron and icosahedron by Apollonius of Perga.
- **Mathematical Identity**: For a sphere of diameter :math:`D`:
  - The circumradius :math:`\\rho` of a face of the dodecahedron and of a face of the icosahedron is identical: :math:`\\rho^{2} = \\frac{5 - \\sqrt{5}}{30} D^{2}`? Wait: :math:`a_{20}^{2} = 3\\rho^{2}` and :math:`a_{20}^{2} = \\frac{5-\\sqrt{5}}{10}D^{2}`, so :math:`\\rho^{2} = \\frac{5-\\sqrt{5}}{30}D^{2} = \\frac{3-\\sqrt{5}}{6}\\cdot\\dots` Wait: for the dodecahedron, :math:`a_{12} = \\frac{\\sqrt{5}-1}{2}\\frac{D}{\\sqrt{3}}`, so :math:`a_{12}^{2} = \\frac{6-2\\sqrt{5}}{12}D^{2} = \\frac{3-\\sqrt{5}}{6}D^{2}`. The circumradius :math:`\\rho_{12}` of a regular pentagon of side :math:`a_{12}` satisfies :math:`a_{12}^{2} = \\frac{5-\\sqrt{5}}{2}\\rho_{12}^{2}`, so :math:`\\rho_{12}^{2} = \\frac{2}{5-\\sqrt{5}}\\frac{3-\\sqrt{5}}{6}D^{2} = \\frac{(5+\\sqrt{5})(3-\\sqrt{5})}{60}D^{2} = \\frac{10 - 2\\sqrt{5}}{60}D^{2} = \\frac{5-\\sqrt{5}}{30}D^{2} = \\rho_{20}^{2}`!
  - Because both solids have the exact same face circumradius :math:`\\rho` and therefore the exact same insphere radius :math:`r_{\\text{in}} = \\sqrt{\\frac{D^{2}}{4} - \\rho^{2}} = D\\sqrt{\\frac{5+2\\sqrt{5}}{60}}`, the ratio of their volumes equals the ratio of their surface areas: :math:`\\frac{V_{20}}{V_{12}} = \\frac{A_{20}}{A_{12}} = \\frac{s_{\\text{cube}}}{s_{20}} = \\sqrt{\\frac{1/3}{(5-\\sqrt{5})/10}} = \\sqrt{\\frac{5+\\sqrt{5}}{6}} \\approx 1.09818`.""",
    },
    33: {
        "title_en": "On the Proportion of the Surfaces and Solid Volumes of All the Regular Bodies to One Another.",
        "body_en": """Continuing with the fourteenth book of our author (with the additions and commentaries of Campanus), we summarize how the surfaces and volumes of the other regular bodies—the tetracedron, the cube, and the octocedron—are compared when inscribed in the same sphere (:just:`XIV.9`, :just:`XIV.10`).

.. assertion:: Proportions of the Tetrahedron, Cube, and Octahedron in the Same Sphere

   1. **Edges in the Same Sphere** (recapitulating :just:`XIII.18`):
      - If the diameter of the sphere is :math:`D`, then:

        .. math::

           s_{\\text{tetra}}^{2} = \\frac{2}{3}D^{2}, \\qquad s_{\\text{octa}}^{2} = \\frac{1}{2}D^{2}, \\qquad s_{\\text{cube}}^{2} = \\frac{1}{3}D^{2}

   2. **Inscribed Spheres (Perpendiculars from the Center to the Faces)**:
      - In the **cube**, the distance from the center of the sphere to each of its six square faces is half the edge of the cube (:math:`r_{6} = \\frac{1}{2}s_{\\text{cube}}`), so :math:`r_{6}^{2} = \\frac{1}{12}D^{2}`.
      - In the **octocedron**, each of the eight faces is an equilateral triangle of side :math:`s_{\\text{octa}}` whose circumcircle has radius :math:`\\rho_{8}` satisfying :math:`s_{\\text{octa}}^{2} = 3\\,\\rho_{8}^{2}` (:just:`XIII.12`), so :math:`\\rho_{8}^{2} = \\frac{1}{6}D^{2}`. Therefore, the perpendicular from the center of the sphere to a face of the octocedron satisfies :math:`r_{8}^{2} = \\left(\\frac{1}{2}D\\right)^{2} - \\rho_{8}^{2} = \\frac{1}{4}D^{2} - \\frac{1}{6}D^{2} = \\frac{1}{12}D^{2}`!
      - **Marvelous Equality**: Therefore, **the perpendicular from the center of the sphere to a face of the cube is exactly equal to the perpendicular from the center of the sphere to a face of the octocedron** (:math:`r_{6} = r_{8} = \\frac{D}{\\sqrt{12}}`)! Just as one and the same inner sphere touches the faces of both the duodecedron and the ycocedron (:ref:`Chapter XXXII <compendio-cap_32-en>`), so another single inner sphere touches the faces of both the **cube** and the **octocedron**!
      - In the **tetracedron**, the circumcircle of each triangular face of side :math:`s_{\\text{tetra}}` has :math:`\\rho_{4}^{2} = \\frac{1}{3}s_{\\text{tetra}}^{2} = \\frac{2}{9}D^{2}`, so the perpendicular from the center of the sphere to a face of the tetracedron satisfies :math:`r_{4}^{2} = \\frac{1}{4}D^{2} - \\frac{2}{9}D^{2} = \\frac{1}{36}D^{2}`, whence :math:`r_{4} = \\frac{1}{6}D` (one-sixth of the sphere's diameter, or one-third of its radius, and one-fourth of the altitude of the tetracedron!).
   3. **Volume and Surface Proportions of Cube and Octahedron**:
      - Because the cube and the octocedron have the **exact same insphere radius** :math:`r_{6} = r_{8}`, the ratio of the solid volume of the cube to the solid volume of the octocedron is identical to the ratio of the total surface area of the six squares of the cube to the total surface area of the eight triangles of the octocedron:

        .. math::

           \\frac{\\text{Vol}(\\text{Cube})}{\\text{Vol}(\\text{Octahedron})} = \\frac{\\text{Area}(\\text{Cube})}{\\text{Area}(\\text{Octahedron})} = \\frac{6 \\cdot \\frac{1}{3}D^{2}}{8 \\cdot \\frac{\\sqrt{3}}{4} \\cdot \\frac{1}{2}D^{2}} = \\frac{2}{\\sqrt{3}} = \\sqrt{\\frac{4}{3}}

   4. **Volume Proportion of Tetrahedron and Octahedron**:
      - Comparing their bases and altitudes, the solid volume of the octocedron to that of the tetracedron inscribed in the same sphere is :math:`\\frac{\\frac{1}{6}D^{3}}{\\frac{2}{27}\\sqrt{3}\\,D^{3}} = \\frac{9}{4\\sqrt{3}} = \\frac{3\\sqrt{3}}{4}`.

As for the detailed numerical rules for finding the exact surface areas and volumes of all five bodies when a given measure in *braccia* or *piedi* is assigned to their edges or to the sphere's diameter, we have treated them at full length in our great work (*Summa de Arithmetica, Geometria, Proportioni e Proportionalita*, Venice, 1494) and in the particular treatise dedicated to your illustrious kinsman Guidobaldo, Duke of Urbino (*Tractato de' Corpi Regulari*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Dual Pairs Sharing Inspheres**: Campanus's additions to Book XIV highlight one of the deepest symmetries in solid geometry: when all five Platonic solids are inscribed in the same sphere of radius :math:`R = \\frac{1}{2}D`, dual solids share the **exact same insphere radius** :math:`r_{\\text{in}}` and the **exact same face circumradius** :math:`\\rho`:
  - **Cube (6 faces) & Octahedron (8 faces)**: :math:`r_{\\text{in}} = \\frac{R}{\\sqrt{3}}`, :math:`\\rho = R\\sqrt{\\frac{2}{3}}`.
  - **Dodecahedron (12 faces) & Icosahedron (20 faces)**: :math:`r_{\\text{in}} = R\\sqrt{\\frac{5+2\\sqrt{5}}{15}}`, :math:`\\rho = R\\sqrt{\\frac{10-2\\sqrt{5}}{15}}`.
  - **Tetrahedron (self-dual, 4 faces)**: :math:`r_{\\text{in}} = \\frac{1}{3}R`, :math:`\\rho = R\\frac{2\\sqrt{2}}{3}`.
- Because :math:`V = \\frac{1}{3} r_{\\text{in}} \\cdot A`, any two dual regular solids inscribed in the same sphere have :math:`V_{1} : V_{2} = A_{1} : A_{2}`.""",
    },
    34: {
        "title_en": "On the Inscriptions of the Five Regular Bodies in One Another, How Many There Are in All, and Why.",
        "body_en": """Now we enter the **fifteenth book** of our philosopher (added by **Campanus** to complete the treatise on the regular bodies), which teaches how the five regular bodies are inscribed in one another—that is, how one regular body is placed inside another so that all the solid angles (vertices) of the inner body touch either the faces, the edges, or the vertices of the outer containing body.

.. enunciation:: Enumeration of the Mutual Inscriptions of the Five Regular Solids (Campanus Book XV)

   If each of the five regular bodies could be inscribed in each of the other four, there would be :math:`5 \\times 4 = 20` mutual inscriptions in all (four for each of the five bodies). Yet in geometric truth, Campanus demonstrates that **twelve** principal inscriptions are regularly constructed in Book XV (Propositions 1–12), while at the end of these chapters (:ref:`Chapter XLVI <compendio-cap_46-en>`) we shall examine why the remaining combinations are excluded—most notably why the **duodecedron** hospitably receives all four of the other regular bodies within itself, whereas the **ycocedron** denies entry to the **octocedron**.

.. assertion:: Overview of the Twelve Inscriptions (Chapters XXXV–XLVI)

   1. **In the Tetracedron (4 triangular bases)**:
      - Only **one** regular body is inscribed in Book XV: the **octocedron** (:ref:`Chapter XXXV <compendio-cap_35-en>`, Campanus XV.1).
   2. **In the Exacedron or Cube (6 square bases)**:
      - **Two** regular bodies are inscribed directly in the opening sequence: the **tetracedron** (:ref:`Chapter XXXVI <compendio-cap_36-en>`, Campanus XV.2) and the **octocedron** (:ref:`Chapter XXXVII <compendio-cap_37-en>`, Campanus XV.3); and later the **ycocedron** (:ref:`Chapter XLIV <compendio-cap_44-en>`, Campanus XV.10).
   3. **In the Octocedron (8 triangular bases)**:
      - **Two** regular bodies are inscribed: the **cube** (:ref:`Chapter XXXVIII <compendio-cap_38-en>`, Campanus XV.4) and the **tetracedron** (:ref:`Chapter XXXIX <compendio-cap_39-en>`, Campanus XV.5).
   4. **In the Ycocedron (20 triangular bases)**:
      - **Three** regular bodies are inscribed: the **duodecedron** (:ref:`Chapter XL <compendio-cap_40-en>`, Campanus XV.6), the **cube** (:ref:`Chapter XLI <compendio-cap_41-en>`, Campanus XV.7), and the **tetracedron** (:ref:`Chapter XLII <compendio-cap_42-en>`, Campanus XV.8).
   5. **In the Duodecedron (12 pentagonal bases)**:
      - **All four** of the other regular bodies are inscribed: the **ycocedron** (:ref:`Chapter XLIII <compendio-cap_43-en>`, Campanus XV.9), the **octocedron** (:ref:`Chapter XLV <compendio-cap_45-en>`, Campanus XV.11), the **cube** (:ref:`Chapter XLVI <compendio-cap_46-en>`, Campanus XV.12), and the **tetracedron** (:ref:`Chapter XLVI <compendio-cap_46-en>`, Campanus XV.12 Corollary).

Let us now set forth each of these constructions in order with its figure and demonstration.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Book XV in the Campanus Tradition**: While the Greek *Elements* Book XV (compiled in the circle of Isidore of Miletus, 6th century CE) contained only a handful of simple inscriptions (Tetrahedron in Cube, Octahedron in Tetrahedron, Octahedron in Cube, Cube in Octahedron, Dodecahedron in Icosahedron), **Campanus of Novara** (c. 1259) expanded Book XV into a systematic sequence of 13 propositions covering 12 polyhedral inscriptions (XV.1–12) plus the inscription of the sphere in all five regular solids (XV.13).
- **Structure of Chapters XXXV–XLVII**: Pacioli devotes ``Cap. XXXV`` through ``Cap. XLVII`` to translating and explaining Campanus's Book XV propositions one by one, accompanied by marginal woodcuts on Folios ``0038``–``0041``.""",
    },
    35: {
        "title_en": "How the Octocedron Is Formed and Inscribed in the Tetracedron.",
        "body_en": """We begin with the first proposition of the fifteenth book (Campanus XV.1), which shows how to inscribe the **octocedron** (8 triangular bases) inside the **tetracedron** (4 triangular bases).

.. enunciation:: Inscribing the Octahedron in the Tetrahedron (Campanus XV.1)

   In a given regular pyramid of four equilateral triangular bases (*tetracedron*), to inscribe the regular body of eight equilateral triangular bases (*octocedron*) so that the six solid angles of the octocedron stand upon the midpoints of the six edges of the tetracedron.

.. assertion:: Construction and Proof (:just:`VI.2`, :just:`VI.4`, :just:`I.8`, :just:`XI.10`)

   1. Let the given tetracedron have base triangle :math:`abc` and upper vertex (cone) :math:`d`, bounded by the four equilateral triangles :math:`abc, abd, acd, bcd` and the six equal edges :math:`ab, bc, ca, da, db, dc` (see the marginal diagram ``0038.g1.png`` on Folio 0038).
   2. Bisect each of the six edges of the tetracedron at its midpoint: let :math:`e, f, g` be the midpoints of the three base edges :math:`ab, bc, ca`, and let :math:`h, k, l` be the midpoints of the three ascending edges :math:`da, db, dc`.
   3. Join these six midpoints by twelve straight lines:
      - Three in the base plane: :math:`ef, fg, ge`;
      - Three in the upper horizontal plane: :math:`hk, kl, lh`;
      - Six along the three lateral faces: :math:`eh, hf, fk, kg, gl, le`.
   4. In each of the four equilateral faces of the tetracedron, the lines joining the midpoints of the sides are parallel to the third side (:just:`VI.2`) and equal to **half** that side (:just:`VI.4`). Since all six edges of the tetracedron are equal, each of the twelve connecting lines :math:`ef, fg, ge, hk, kl, lh, eh, hf, fk, kg, gl, le` equals **half the edge of the tetracedron**!
   5. Therefore, the eight triangular faces bounded by these twelve equal lines—four lying flat within the four faces of the tetracedron (:math:`efg, ehf, fkg, gle`) and four cutting off the four corner pyramids at :math:`a, b, c, d` (:math:`eh l, hfk, kgl, hkl`)—are all equilateral and mutually equal; and their solid angles are mutually equal (:just:`XI.10`).

Thus the regular octocedron :math:`efghkl` is inscribed in the tetracedron :math:`abcd`, with its edge equal to **half** the edge of the tetracedron (so the edge of the tetracedron is double the edge of its inscribed octocedron, and the volume of the tetracedron—consisting of the central octocedron plus four corner tetrahedra of half the linear scale—is **double** the volume of the inscribed octocedron!).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0038 (``f. 11v``) shows diagram ``0038.g1.png`` with the tetrahedron :math:`abcd` and the midpoint octahedron inscribed inside it.
- **Connection to Rectification (*Abscission*)**: This inscription is the exact geometric foundation of the **truncated tetrahedron** (*tetracedron absciso*, Plate III, ``Cap. XLVIII``): cutting the tetrahedron one-third of the way along each edge yields the semi-regular truncated tetrahedron, whereas cutting all the way to the midpoints (rectification) yields the regular **octahedron**! Furthermore, since the 4 corner tetrahedra each have edge :math:`\\frac{1}{2}a_{4}` (hence volume :math:`\\frac{1}{8}V_{\\text{tetra}}`), the remaining central octahedron of edge :math:`\\frac{1}{2}a_{4}` has volume :math:`V_{\\text{tetra}} - 4\\left(\\frac{1}{8}V_{\\text{tetra}}\\right) = \\frac{1}{2}V_{\\text{tetra}}`, proving immediately that an octahedron of edge :math:`s` has **four times** the volume of a tetrahedron of the same edge :math:`s`!""",
    },
    36: {
        "title_en": "How the Tetracedron Is Placed in the Cube.",
        "body_en": """The second proposition of the fifteenth book (Campanus XV.2) teaches how to inscribe the **tetracedron** (4 triangular bases) inside the **exacedron** or **cube** (6 square bases).

.. enunciation:: Inscribing the Tetrahedron in the Cube (Campanus XV.2)

   In a given cube (*exacedron*), to inscribe the regular pyramid of four equilateral triangular bases (*tetracedron*) so that the four vertices of the tetracedron stand at four non-adjacent vertices of the cube, and the six edges of the tetracedron are the six face diagonals of the six square faces of the cube.

.. assertion:: Construction and Proof (:just:`I.47`, :just:`I.8`)

   1. Let the given cube have lower square face :math:`abcd` and upper square face :math:`efgh`, with vertical edges :math:`ae, bf, cg, dh` (see the marginal diagram ``0038.g2.png`` on Folio 0038).
   2. On the six square faces of the cube, draw six face diagonals meeting at four alternating corners of the cube—namely, draw the diagonal :math:`ac` on the lower square :math:`abcd`, the diagonal :math:`fh` on the upper square :math:`efgh`, and the four lateral diagonals :math:`af, fc, ch, ha` on the four vertical squares :math:`abfe, bcgf, cdhg, daeh`.
   3. Because all six faces of the cube are equal squares, by the :just:`penultimate of the first <I.47>` and the :just:`fourth of the first <I.4>` all six face diagonals :math:`ac, fh, af, fc, ch, ha` are mutually equal, each having its square **double** the square on the edge of the cube (:math:`s_{\\text{tetra}}^{2} = 2\\,s_{\\text{cube}}^{2}`).
   4. These six equal diagonals bound four equilateral triangles (:math:`afc, fch, cha, haf`) meeting three by three at the four alternating cube corners :math:`a, c, f, h`.

Therefore the regular tetracedron :math:`afch` is inscribed in the cube, and the square on the edge of the inscribed tetracedron is **double** (:math:`2 : 1`) the square on the edge of the containing cube—which agrees with what we saw in :ref:`Chapter XXVI <compendio-cap_26-en>` and :ref:`Chapter XXVII <compendio-cap_27-en>`, since the same sphere circumscribes both the cube and this tetracedron!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Johannes Kepler's *Stella Octangula* and the Volume Ratio**: Slicing away the four right-angled corner pyramids (:math:`abcf`, :math:`acdh`, :math:`aefh`, :math:`cfgh`) from the cube of side :math:`s` leaves the regular tetrahedron :math:`afch` of edge :math:`s\\sqrt{2}`. Since each corner pyramid has three mutually perpendicular legs of length :math:`s` and therefore volume :math:`\\frac{1}{6}s^{3}`, the four corner pyramids have total volume :math:`4 \\times \\frac{1}{6}s^{3} = \\frac{2}{3}s^{3}`, leaving **one-third** of the cube's volume (:math:`\\frac{1}{3}s^{3}`) for the inscribed tetrahedron!""",
    },
    37: {
        "title_en": "How the Octocedron Is Placed in the Cube.",
        "body_en": """The third proposition of the fifteenth book (Campanus XV.3) shows how to inscribe the **octocedron** (8 triangular bases) inside the **cube** (6 square bases).

.. enunciation:: Inscribing the Octahedron in the Cube (Campanus XV.3)

   In a given cube (*exacedron*), to inscribe the regular body of eight equilateral triangular bases (*octocedron*) so that the six solid angles of the octocedron stand at the centers of the six square faces of the cube.

.. assertion:: Construction and Proof (:just:`IV.6`, :just:`I.47`, :just:`XI.10`)

   1. In each of the six square faces of the given cube, draw the two diagonals intersecting one another at the center of that square face (:just:`IV.6`), giving six face centers :math:`k, l, m, n` on the four vertical faces and :math:`o, p` on the lower and upper faces (see the marginal diagram ``0038.g3.png`` on Folio 0038).
   2. Join the four lateral face centers in order by the four straight lines :math:`kl, lm, mn, nk` to form a central horizontal square, and join each of the two polar face centers :math:`o` and :math:`p` by four straight lines (:math:`ok, ol, om, on` and :math:`pk, pl, pm, pn`) to the four lateral centers.
   3. Because the distance from the center of each square face of the cube to the midpoint of any of its four edges equals **half** the edge of the cube (:math:`\\frac{1}{2}s_{\\text{cube}}`), and adjacent faces of the cube meet at right angles, each of the twelve connecting lines :math:`kl, lm, \\dots, pn` is the hypotenuse of a right-angled isosceles triangle whose two legs equal :math:`\\frac{1}{2}s_{\\text{cube}}`.
   4. By the :just:`penultimate of the first <I.47>`, the square on each of the twelve edges of the inscribed figure equals:

      .. math::

         \\left(\\frac{1}{2}s_{\\text{cube}}\\right)^{2} + \\left(\\frac{1}{2}s_{\\text{cube}}\\right)^{2} = \\frac{1}{2}s_{\\text{cube}}^{2}

      Thus all twelve edges are mutually equal, all eight triangular faces are equilateral, and the six vertices :math:`k, l, m, n, o, p` touch the six centers of the faces of the cube.

Therefore the regular octocedron is inscribed in the cube, and the square on the edge of the cube is **double** (:math:`2 : 1`) the square on the edge of the octocedron inscribed in it (so the edge of the inscribed octocedron equals **half the face diagonal** of the cube).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Duality of Cube and Octahedron**: Campanus XV.3 (``Cap. XXXVII``) and XV.4 (``Cap. XXXVIII``) establish the reciprocal duality between the cube (6 faces, 8 vertices, 12 edges) and the octahedron (8 faces, 6 vertices, 12 edges): the centers of the 6 faces of the cube are the 6 vertices of the inscribed octahedron, with :math:`s_{\\text{octa}} = \\frac{\\sqrt{2}}{2} s_{\\text{cube}}`.""",
    },
    38: {
        "title_en": "How the Exacedron or Cube Is Formed in the Octocedron.",
        "body_en": """The fourth proposition of the fifteenth book (Campanus XV.4) demonstrates the converse: how to inscribe the **cube** (6 square bases) inside the **octocedron** (8 triangular bases).

.. enunciation:: Inscribing the Cube in the Octahedron (Campanus XV.4)

   In a given regular body of eight equilateral triangular bases (*octocedron*), to inscribe the cube (*exacedron*) so that the eight solid angles of the cube stand at the centers of the eight triangular faces of the octocedron.

.. assertion:: Construction and Proof (:just:`IV.4`, :just:`VI.2`, :just:`I.47`, :just:`XIII.12`)

   1. In each of the eight equilateral triangular faces of the given octocedron (four in the upper pyramid and four in the lower pyramid sharing the equatorial square :math:`abcd`), find the **center** of that equilateral triangle (:just:`IV.4`, :just:`IV.5`) by drawing the perpendiculars (medians/angle-bisectors) from two corners to the midpoints of the opposite sides; their intersection is the center of the triangle (see the marginal diagram ``0039.g1.png`` on Folio 0039).
   2. Let :math:`e, f, g, h` be the four centers of the four upper triangular faces of the octocedron, and let :math:`k, l, m, n` be the four centers of the four lower triangular faces.
   3. Join the four upper centers in order (:math:`ef, fg, gh, he`), join the four lower centers in order (:math:`kl, lm, mn, nk`), and join each upper center to the corresponding lower center across the four equatorial edges (:math:`ek, fl, gm, hn`).
   4. In any equilateral triangle, the center divides each median (altitude) from a vertex to the midpoint of the opposite edge in the ratio :math:`2 : 1`, so its distance from the midpoint of the edge is **one-third** of the altitude of the triangle.
   5. By the :just:`second and fourth of the sixth <VI.2>`, the four upper centers :math:`e, f, g, h` lie in a horizontal plane parallel to the equatorial square :math:`abcd` of the octocedron, and the square :math:`efgh` is similar to the square Formed by the midpoints of the four equatorial edges at :math:`\\frac{2}{3}` scale. Since the midpoint square of the equatorial square of side :math:`s_{\\text{octa}}` has side :math:`\\frac{\\sqrt{2}}{2}s_{\\text{octa}}`, each edge of :math:`efgh` (and likewise :math:`klmn` and the four vertical edges :math:`ek, fl, gm, hn`) equals **two-thirds of the half-diagonal**, or:

      .. math::

         s_{\\text{cube}} = \\frac{\\sqrt{2}}{3}\\,s_{\\text{octa}}, \\qquad s_{\\text{octa}}^{2} : s_{\\text{cube}}^{2} = 9 : 2

Therefore the eight centers :math:`e, f, g, h, k, l, m, n` of the eight triangular faces of the octocedron are the vertices of an inscribed **cube**, and the square on the edge of the octocedron has to the square on the edge of its inscribed cube the ratio :math:`9 : 2` (*quadrupla sesquialtera*).

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0039 (``f. 12r``) contains diagram ``0039.g1.png`` showing the octahedron and the cube whose 8 vertices sit at the centroids of the 8 triangular faces.
- **Exact Ratio**: If the octahedron has edge :math:`s_{\\text{octa}}`, its equatorial square has diagonal :math:`s_{\\text{octa}}\\sqrt{2}`. The centroids of two opposite faces lie at :math:`\\frac{1}{3}` of the way from the equatorial midpoints toward the poles, so the face diagonal of the inscribed cube is :math:`\\frac{2}{3}s_{\\text{octa}}`, and the edge of the inscribed cube is :math:`s_{\\text{cube}} = \\frac{\\sqrt{2}}{3}s_{\\text{octa}}`, giving :math:`s_{\\text{octa}}^{2} : s_{\\text{cube}}^{2} = 9 : 2`.""",
    },
    39: {
        "title_en": "How the Tetracedron Is Formed in the Octocedron.",
        "body_en": """The fifth proposition of the fifteenth book (Campanus XV.5) shows how to inscribe the **tetracedron** (4 triangular bases) inside the **octocedron** (8 triangular bases) by means of the cube already inscribed in the octocedron.

.. enunciation:: Inscribing the Tetrahedron in the Octahedron (Campanus XV.5)

   In a given regular body of eight triangular bases (*octocedron*), to inscribe the regular body of four triangular bases (*tetracedron*) so that the four vertices of the tetracedron stand at four alternating centers of the eight faces of the octocedron.

.. assertion:: Construction and Proof (via Campanus XV.4 and XV.2)

   1. First, in the given octocedron inscribe the **cube** :math:`efghklmn` by the method of :ref:`Chapter XXXVIII <compendio-cap_38-en>` (Campanus XV.4), so that the eight vertices of the cube stand at the eight centers of the triangular faces of the octocedron (see the marginal diagram ``0039.g2.png`` on Folio 0039).
   2. Second, in this inscribed cube :math:`efghklmn`, inscribe the **tetracedron** by the method of :ref:`Chapter XXXVI <compendio-cap_36-en>` (Campanus XV.2), drawing the six face diagonals across the six square faces of the cube to join four non-adjacent vertices of the cube (for instance :math:`e, g, l, n`).
   3. Because the eight vertices of the cube lie at the centers of the eight faces of the octocedron, the four vertices :math:`e, g, l, n` of this tetracedron likewise stand at four alternating face-centers of the octocedron!
   4. Moreover, since by :ref:`Chapter XXXVIII <compendio-cap_38-en>` the square on the edge of the octocedron has to the square on the edge of its inscribed cube the ratio :math:`9 : 2`, and by :ref:`Chapter XXXVI <compendio-cap_36-en>` the square on the edge of the tetracedron inscribed in that cube is **double** (:math:`2 : 1`) the square on the edge of the cube, by *ex aequali* (:just:`V.22`) the square on the edge of the octocedron has to the square on the edge of its inscribed tetracedron the ratio :math:`9 : 4`:

      .. math::

         s_{\\text{octa}}^{2} : s_{\\text{tetra}}^{2} = 9 : 4 \\implies s_{\\text{tetra}} = \\frac{2}{3}\\,s_{\\text{octa}}

Thus the edge of the tetracedron inscribed in the octocedron is **commensurable in length** with the edge of the octocedron, being exactly **two-thirds** (:math:`\\frac{2}{3}`) of it!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Commensurability in Length (:math:`2:3`)**: Notice the remarkable rational consequence of composing Campanus XV.4 (:math:`s_{\\text{cube}} = \\frac{\\sqrt{2}}{3}s_{\\text{octa}}`) with Campanus XV.2 (:math:`s_{\\text{tetra}} = \\sqrt{2}\\,s_{\\text{cube}}`): the :math:`\\sqrt{2}` factors cancel completely, leaving :math:`s_{\\text{tetra}} = \\frac{2}{3}s_{\\text{octa}}`!""",
    },
    40: {
        "title_en": "How the Duodecedron Is Formed in the Ycocedron.",
        "body_en": """The sixth proposition of the fifteenth book (Campanus XV.6) demonstrates how to inscribe the **duodecedron** (12 pentagonal bases) inside the **ycocedron** (20 triangular bases).

.. enunciation:: Inscribing the Dodecahedron in the Icosahedron (Campanus XV.6)

   In a given regular body of twenty equilateral triangular bases (*ycocedron*), to inscribe the regular body of twelve equilateral and equiangular pentagonal bases (*duodecedron*) so that the twenty vertices of the duodecedron stand at the twenty centers of the triangular faces of the ycocedron.

.. assertion:: Construction and Proof (:just:`IV.4`, :just:`XIII.16`, :just:`XIII.7`)

   1. In each of the twenty equilateral triangular faces of the given ycocedron, find the **center** of that triangle (:just:`IV.4`), giving twenty points in all—one at the middle of each face of the ycocedron (see the marginal diagram ``0039.g3.png`` on Folio 0039).
   2. Around each of the twelve solid angles (vertices) of the ycocedron, exactly **five** equilateral triangular faces meet (:ref:`Chapter XXV <compendio-cap_25-en>`, :ref:`Chapter XXIX <compendio-cap_29-en>`). Join in order the five centers of the five triangles surrounding each vertex of the ycocedron by five straight lines.
   3. Because the five triangles meeting at a vertex of the ycocedron are mutually equal and similarly inclined around the axis passing from the center of the ycocedron through that vertex, the five straight lines joining their centers lie in one plane perpendicular to that axis and form an **equilateral and equiangular pentagon**.
   4. Since the ycocedron has **twelve** vertices, and around each vertex five triangular faces meet, joining the centers around all twelve vertices produces **twelve equal regular pentagons** bounded by thirty equal edges meeting three by three at the **twenty** face-centers of the ycocedron.

Therefore the regular duodecedron is inscribed in the ycocedron, with its twenty solid angles touching the centers of the twenty triangular bases of the ycocedron.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Duality of Icosahedron and Dodecahedron**: Just as ``Cap. XXXVII``–``Cap. XXXVIII`` established the dual reciprocity between the cube (6 faces, 8 vertices) and the octahedron (8 faces, 6 vertices), ``Cap. XL`` (Campanus XV.6) and ``Cap. XLIII`` (Campanus XV.9) establish the dual reciprocity between the icosahedron (20 faces, 12 vertices) and the dodecahedron (12 faces, 20 vertices).""",
    },
    41: {
        "title_en": "How the Exacedron or Cube Is Placed in the Ycocedron.",
        "body_en": """The seventh proposition of the fifteenth book (Campanus XV.7) shows how to inscribe the **cube** (6 square bases) inside the **ycocedron** (20 triangular bases) by means of the duodecedron first inscribed in the ycocedron.

.. enunciation:: Inscribing the Cube in the Icosahedron (Campanus XV.7)

   In a given regular body of twenty triangular bases (*ycocedron*), to inscribe the cube (*exacedron*) so that the eight vertices of the cube stand at eight of the twenty centers of the triangular faces of the ycocedron.

.. assertion:: Construction and Proof (via Campanus XV.6 and :just:`XIII.17`)

   1. First, in the given ycocedron inscribe the **duodecedron** by the method of :ref:`Chapter XL <compendio-cap_40-en>` (Campanus XV.6), so that the twenty vertices of the duodecedron stand at the centers of the twenty triangular faces of the ycocedron (see the marginal diagram ``0040.g1.png`` on Folio 0040).
   2. Recall from :ref:`Chapter XXX <compendio-cap_30-en>` (:just:`XIII.17`) how the duodecedron was originally constructed upon the **six square faces of a cube**: twelve of the twenty vertices of the duodecedron are the roof-ridge vertices, while the remaining **eight vertices** of the duodecedron are the eight corners of the underlying cube, and the **twelve edges of that cube** are twelve diagonals (*corde pentagoniche*) drawn across the twelve pentagonal faces of the duodecedron!
   3. Accordingly, in the twelve pentagonal faces of the duodecedron inscribed in our ycocedron, draw the twelve pentagonal chords (*corde pentagoniche*) connecting those eight corresponding vertices.
   4. By :just:`XIII.17` and :just:`XIII.8`, these twelve pentagonal chords are mutually equal, meet at right angles in six square faces, and have their eight vertices among the twenty vertices of the duodecedron—which are themselves the centers of eight of the twenty triangular faces of the ycocedron!

Therefore the cube is inscribed in the ycocedron, and its edge is the **pentagonal chord** (*corda pentagonica*) of the duodecedron inscribed in the same ycocedron, so that the edge of this cube and the edge of the inscribed duodecedron stand to one another in our **Divine Proportion**!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Elegance of Campanus's Mediated Inscription**: Rather than attempting a direct coordinate construction in the icosahedron, Campanus (and Pacioli) exploits the dual dodecahedron (XV.6) together with Euclid's roof construction (:just:`XIII.17`): since every regular dodecahedron contains 5 inscribed cubes (whose 12 edges are face diagonals of the 12 pentagons), inscribing the dual dodecahedron inside the icosahedron immediately places 8 of the icosahedron's 20 face-centers at the corners of a regular cube!""",
    },
    42: {
        "title_en": "How the Tetracedron Is Formed in the Ycocedron.",
        "body_en": """The eighth proposition of the fifteenth book (Campanus XV.8) shows how to inscribe the **tetracedron** (4 triangular bases) inside the **ycocedron** (20 triangular bases) by means of the cube inscribed in the ycocedron.

.. enunciation:: Inscribing the Tetrahedron in the Icosahedron (Campanus XV.8)

   In a given regular body of twenty triangular bases (*ycocedron*), to inscribe the regular body of four triangular bases (*tetracedron*) so that the four vertices of the tetracedron stand at four of the twenty centers of the triangular faces of the ycocedron.

.. assertion:: Construction and Proof (via Campanus XV.7 and XV.2)

   1. First, in the given ycocedron inscribe the **duodecedron** (:ref:`Chapter XL <compendio-cap_40-en>`, Campanus XV.6), and within that duodecedron inscribe the **cube** by drawing twelve pentagonal chords across its twelve faces (:ref:`Chapter XLI <compendio-cap_41-en>`, Campanus XV.7), so that the eight vertices of the cube stand at eight centers of the triangular faces of the ycocedron (see the marginal diagram ``0040.g2.png`` on Folio 0040).
   2. Next, in this inscribed cube, inscribe the **tetracedron** by the method of :ref:`Chapter XXXVI <compendio-cap_36-en>` (Campanus XV.2), drawing the six face diagonals across the six square faces of the cube to connect four alternating corners of the cube.
   3. Because the eight corners of the cube stand at eight face-centers of the ycocedron, the four corners of the tetracedron likewise stand at **four centers of the triangular faces of the ycocedron**, and all six edges of the tetracedron are mutually equal (:math:`s_{\\text{tetra}} = s_{\\text{cube}}\\sqrt{2}`).

Therefore the regular tetracedron is inscribed in the ycocedron.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Chain of Three Inscriptions**: Notice the genealogical chain of reductions: Icosahedron :math:`\\supset` Dodecahedron (XV.6, 20 vertices at face-centers) :math:`\\supset` Cube (XV.7, 8 of those 20 vertices) :math:`\\supset` Tetrahedron (XV.2/XV.8, 4 of those 8 vertices).""",
    },
    43: {
        "title_en": "How the Ycocedron Is Formed in the Duodecedron.",
        "body_en": """Now we come to the ninth proposition of the fifteenth book (Campanus XV.9), where we begin inscribing all four of the other regular bodies inside the fifth and noblest body, the **duodecedron** (12 pentagonal bases)—which, as Plato says in the *Timaeus*, is the receptacle and lodging (*receptaculo e albergo*) of all the others—starting with the **ycocedron** (20 triangular bases).

.. enunciation:: Inscribing the Icosahedron in the Dodecahedron (Campanus XV.9)

   In a given regular body of twelve pentagonal bases (*duodecedron*), to inscribe the regular body of twenty equilateral triangular bases (*ycocedron*) so that the twelve vertices of the ycocedron stand at the twelve centers of the pentagonal faces of the duodecedron.

.. assertion:: Construction and Proof (:just:`IV.14`, :just:`XIII.17`, :just:`XI.10`)

   1. In each of the twelve regular pentagonal faces of the given duodecedron, find the **center** of that pentagon by the :just:`fourteenth of the fourth <IV.14>` (bisecting two adjacent angles of the pentagon; the intersection of the bisectors is the center of the pentagon), giving **twelve face-centers** in all (see the marginal diagram ``0040.g3.png`` on Folio 0040).
   2. Around each of the twenty solid angles (vertices) of the duodecedron, exactly **three** regular pentagonal faces meet (:ref:`Chapter XXV <compendio-cap_25-en>`). Join the three centers of the three pentagons meeting at each vertex of the duodecedron by three straight lines.
   3. Because the three pentagonal faces meeting at any vertex of the duodecedron are equal and equally inclined to one another, the three straight lines connecting their centers are mutually equal and form an **equilateral triangle** opposite that vertex.
   4. Carrying out this construction around all **twenty** vertices of the duodecedron produces **twenty equal equilateral triangles** bounded by thirty equal edges meeting five by five at the **twelve** centers of the pentagonal faces of the duodecedron.

Therefore the regular ycocedron is inscribed in the duodecedron, with its twelve solid angles touching the centers of the twelve pentagonal bases of the duodecedron.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0040 (``f. 12v``) displays diagram ``0040.g3.png`` illustrating the pentagonal faces of the dodecahedron and the equilateral triangles connecting their centers.""",
    },
    44: {
        "title_en": "How the Ycocedron Is Placed in the Cube.",
        "body_en": """Before completing the remaining inscriptions in the duodecedron, Campanus places as the tenth proposition of the fifteenth book (Campanus XV.10) the inscription of the **ycocedron** (20 triangular bases) inside the **cube** (6 square bases).

.. enunciation:: Inscribing the Icosahedron in the Cube (Campanus XV.10)

   In a given cube (*exacedron*), to inscribe the regular body of twenty equilateral triangular bases (*ycocedron*) so that the twelve vertices of the ycocedron stand in pairs along six median lines on the six square faces of the cube (or at the twelve centers via the inscribed octocedron/duodecedron).

.. assertion:: Construction and Proof (Campanus XV.10, via XV.3 and :just:`XIII.16`)

   1. Campanus demonstrates this inscription by first inscribing the **octocedron** in the given cube by the method of :ref:`Chapter XXXVII <compendio-cap_37-en>` (Campanus XV.3), so that the six vertices of the octocedron stand at the six centers of the square faces of the cube, and the three axes of the octocedron join the opposite face-centers of the cube (see the marginal diagram ``0041.g1.png`` on Folio 0041).
   2. Alternatively—and even more manifestly from the Divine Proportion—on the six square faces of the cube, draw six median lines through the six face-centers in three mutually perpendicular directions (so that on each pair of opposite square faces the medians are parallel, and on each adjacent face the median is perpendicular to the shared edge, just as we did in :ref:`Chapter XXX <compendio-cap_30-en>` when erecting the roofs of the duodecedron).
   3. Divide the half-median of each square face according to our **Divine Proportion**, and mark on each of the six face-medians two points equidistant from the face-center by half the lesser (or greater) segment so that six edges of the ycocedron lie flat on the six square faces of the cube, and all **twelve vertices** of the ycocedron touch the six square faces of the cube!
   4. In Campanus's construction (XV.10), the twelve vertices of the ycocedron lie on the circles inscribed in the faces (or along the twelve edges of the inscribed octocedron divided in extreme and mean ratio), forming twenty equilateral triangles whose twelve vertices touch the interior of the cube.

Thus the regular ycocedron is inscribed in the cube.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Two Ways to Inscribe the Icosahedron in the Cube**:
  1. **Edge-on-Face Inscription (Golden Rectangles)**: An icosahedron of edge :math:`a_{20}` has 12 vertices that form three mutually perpendicular golden rectangles of dimensions :math:`a_{20} \\times \\varphi\\,a_{20}`. Placing these three golden rectangles inside a cube of side :math:`s_{\\text{cube}} = \\varphi\\,a_{20}` puts 6 edges of the icosahedron (and all 12 of its vertices!) directly on the 6 square faces of the cube, with the cube edge and icosahedron edge in the **Divine Proportion** (:math:`s_{\\text{cube}} : a_{20} = \\varphi : 1`).
  2. **Campanus XV.10 Inscription**: Campanus routes the construction through the octahedron inscribed in the cube (XV.3) and the circles of :just:`XIII.16`.""",
    },
    45: {
        "title_en": "How the Octocedron Is Placed in the Duodecedron.",
        "body_en": """Returning now to the **duodecedron**, the eleventh proposition of the fifteenth book (Campanus XV.11) shows how to inscribe the **octocedron** (8 triangular bases) inside the **duodecedron** (12 pentagonal bases)—a construction of singular elegance because the six vertices of the octocedron do not touch the faces or vertices of the duodecedron, but rather the **midpoints of six of its thirty edges**!

.. enunciation:: Inscribing the Octahedron in the Dodecahedron (Campanus XV.11)

   In a given regular body of twelve pentagonal bases (*duodecedron*), to inscribe the regular body of eight equilateral triangular bases (*octocedron*) so that the six solid angles of the octocedron stand upon the midpoints of six opposite edges of the duodecedron.

.. assertion:: Construction and Proof (Campanus XV.11, via :just:`XIII.17` and :just:`XIII.14`)

   1. Recall from :ref:`Chapter XXX <compendio-cap_30-en>` (:just:`XIII.17`) how the duodecedron was built by erecting six hipped roofs over the **six square faces of an inscribed cube**: over each of the six square faces of that underlying cube there stands one **ridge edge** (*corausto* or roof-crest, such as :math:`vx` in ``0035.g1.png``) of the duodecedron, parallel to the median of that square face of the cube and lying directly above its center!
   2. Thus among the thirty edges of the duodecedron, there is a set of **six privileged edges**—three pairs of opposite, parallel roof-ridge edges—whose **six midpoints** lie directly on the three mutually perpendicular axes passing through the center of the duodecedron (and of the underlying cube) and perpendicular to the six faces of that cube (see the marginal diagram ``0041.g2.png`` on Folio 0041).
   3. Mark the midpoints :math:`f, g, h, k, l, m` of these six opposite edges of the duodecedron. The three straight lines joining the three opposite pairs of midpoints pass straight through the center of the duodecedron, are all equal in length (each being equal to the diameter of the sphere that touches those six edge-midpoints), and intersect one another at **right angles** at the center!
   4. Join the six midpoints :math:`f, g, h, k, l, m` to one another by twelve straight lines. By the exact same proof as in :ref:`Chapter XXVIII <compendio-cap_28-en>` (:just:`XIII.14`), because the three axes are mutually equal and bisect one another at right angles at the center, all twelve connecting edges are mutually equal (each having its square equal to half the square on the axis joining two opposite midpoints), and all eight faces are equilateral triangles!

Therefore the regular octocedron is inscribed in the duodecedron, with its six vertices standing at the midpoints of six opposite edges of the duodecedron.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Geometric Insight of Campanus XV.11**: In Euclid's construction of the dodecahedron (:just:`XIII.17`), 6 of the 30 edges of the dodecahedron are the roof ridges :math:`vx` centered over the 6 faces of the inscribed cube. The midpoints of those 6 edges lie on the 3 coordinate axes of the cube at distance :math:`\\frac{1}{2}s_{\\text{cube}} + \\text{lesser} = \\frac{\\varphi}{2}s_{\\text{cube}} = \\frac{\\varphi^{2}}{2}a_{12}` from the origin. Because the 3 coordinate axes are orthogonal and equal in length, those 6 edge-midpoints are the exact vertices of a **regular octahedron** of edge :math:`a_{8} = \\frac{\\varphi^{2}}{\\sqrt{2}}a_{12}`!""",
    },
    46: {
        "title_en": "How the Exacedron and the Tetracedron Are Placed in the Duodecedron, and Why Only Twelve Inscriptions Are Possible.",
        "body_en": """Now we complete the twelfth proposition of the fifteenth book (Campanus XV.12 and its corollary), showing how both the **cube** (*exacedron*) and the **tetracedron** are inscribed in the **duodecedron**, and explaining why only **twelve** of the twenty theoretical inscriptions can be regularly formed.

.. enunciation:: Inscribing the Cube and the Tetrahedron in the Dodecahedron (Campanus XV.12)

   In a given regular body of twelve pentagonal bases (*duodecedron*), to inscribe the cube (*exacedron*) and the pyramid of four triangular bases (*tetracedron*) so that their vertices stand at vertices of the duodecedron.

.. assertion:: Construction and Proof (:just:`XIII.17`, :just:`XIII.8`, Campanus XV.2)

   1. **Inscribing the Cube in the Duodecedron**: As was already demonstrated in :ref:`Chapter XXX <compendio-cap_30-en>` (:just:`XIII.17`) and used in :ref:`Chapter XLI <compendio-cap_41-en>`, across each of the twelve pentagonal faces of the given duodecedron draw one **pentagonal chord** (*corda pentagonica*, subtending one pentagonal angle) so that the twelve chords meet three by three at eight of the twenty solid angles (vertices) of the duodecedron (see the marginal diagram ``0041.g3.png`` on Folio 0041).
      - By :just:`XIII.8` and :just:`XIII.17`, all twelve pentagonal chords are equal, and they form six equal square faces bounding a **cube** whose eight vertices are eight of the twenty vertices of the duodecedron!
      - Furthermore, by :just:`XIII.8`, if the pentagonal chord (which is the edge of this inscribed cube) is divided according to our **Divine Proportion**, its greater segment is the edge of the duodecedron!
   2. **Inscribing the Tetracedron in the Duodecedron**: Having inscribed the cube in the duodecedron so that its eight vertices are eight vertices of the duodecedron, inscribe the **tetracedron** in that cube by the method of :ref:`Chapter XXXVI <compendio-cap_36-en>` (Campanus XV.2), joining four alternating corners of the cube by the six face diagonals of the cube's six squares.
      - Because the eight vertices of the cube are vertices of the duodecedron, the **four vertices of the tetracedron** are likewise four of the twenty vertices of the duodecedron (and its six edges are six interior diagonals of the duodecedron)!

.. rubric:: Why Only Twelve Inscriptions Are Regularly Assigned, and the Mystery of the Holy Cross in the Octocedron

Let Your Ducal Highness now consider why, out of the :math:`5 \\times 4 = 20` combinations that one might imagine by pairing each of the five regular bodies with the other four, our author and Campanus assign only these **twelve**:

- **The Duodecedron Receives All Four**: As the figure of the fifth essence and of the universal heaven (*il cielo*) which embraces all things created, the **duodecedron** alone receives all four of the other regular bodies within itself: the ycocedron at its 12 face-centers (:ref:`Cap. XLIII <compendio-cap_43-en>`), the octocedron at 6 of its 30 edge-midpoints (:ref:`Cap. XLV <compendio-cap_45-en>`), the cube at 8 of its 20 vertices (:ref:`Cap. XLVI <compendio-cap_46-en>`), and the tetracedron at 4 of its 20 vertices (:ref:`Cap. XLVI <compendio-cap_46-en>`).
- **Why the Ycocedron Receives Three, Denying Only the Octocedron**: In the **ycocedron** (20 triangular faces, 12 vertices, 30 edges), we inscribed the duodecedron (:ref:`Cap. XL <compendio-cap_40-en>`), the cube (:ref:`Cap. XLI <compendio-cap_41-en>`), and the tetracedron (:ref:`Cap. XLII <compendio-cap_42-en>`), because 20 face-centers accommodate the 20 vertices of the duodecedron, 8 of those 20 accommodate the cube, and 4 of those 8 accommodate the tetracedron. Why then does the ycocedron refuse to receive the **octocedron**?
  - Because the octocedron has **six** vertices at the ends of **three axes that intersect one another at right angles** (*ad angoli recti in croce*), forming the **glorious sign of the Holy Cross** (*el glorioso segno dela sancta Croce*)! Neither the 20 face-centers nor the 12 vertices of the ycocedron contain six points at the extremities of three mutually perpendicular diameters; and just as water (represented by the ycocedron) yields to the Cross, or as the devil flees the sign of the Cross, so the ycocedron cannot enclose the octocedron at its face-centers or vertices! (Though if one wished to use the midpoints of six opposite edges among the 30 edges of the ycocedron, just as we did in the duodecedron in :ref:`Chapter XLV <compendio-cap_45-en>`, three orthogonal axes do pass through six edge-midpoints of the ycocedron.)
- **Why the Other Eight Combinations Fail at Face-Centers or Vertices**: In the **tetracedron** (4 faces, 4 vertices, 6 edges), only the **octocedron** (6 vertices) can be inscribed using the 6 edge-midpoints (:ref:`Cap. XXXV <compendio-cap_35-en>`), for neither the cube (8 vertices), the ycocedron (12 vertices), nor the duodecedron (20 vertices) can fit symmetrically on 4 faces, 4 vertices, or 6 edges. Similarly, the **octocedron** (8 faces, 6 vertices, 12 edges) receives the cube (8 vertices at its 8 face-centers, :ref:`Cap. XXXVIII <compendio-cap_38-en>`) and the tetracedron (4 vertices at 4 of those 8 face-centers, :ref:`Cap. XXXIX <compendio-cap_39-en>`), but its 8 faces, 6 vertices, and 12 edges cannot symmetrically seat the 12 vertices of the ycocedron or the 20 vertices of the duodecedron.

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0041 (``f. 13r``) shows diagram ``0041.g3.png`` for Campanus XV.12 (the cube and tetrahedron inscribed in the dodecahedron).
- **Theological-Geometric Conceit of the Holy Cross**: Pacioli's explanation on Folio 0042 (``f. 13v``) of why Campanus inscribes all four solids in the dodecahedron (XV.9, 11, 12) but only three in the icosahedron (XV.6, 7, 8)—invoking the three mutually perpendicular axes of the octahedron as the *glorioso segno dela sancta Croce*—is a classic example of Franciscan mathematical theology. Ironically, from a purely group-theoretic standpoint, the icosahedron and dodecahedron share the exact same symmetry group :math:`A_5 \\times \\mathbb{Z}_2` and the exact same 30 edge-midpoints (which form the 30 vertices of an **icosidodecahedron**), so the 6 midpoints of three orthogonal pairs of opposite edges of the icosahedron *do* form a regular octahedron, just as in Campanus XV.11 for the dodecahedron!""",
    },
    47: {
        "title_en": "How the Sphere Is Placed and Inscribed in Each of the Said Five Regular Bodies.",
        "body_en": """To conclude the fifteenth book (Campanus XV.13), having shown how all five regular bodies are inscribed in the sphere and how they are inscribed in one another, we now demonstrate the converse: how a **sphere** is inscribed inside each of the five regular bodies so that it touches the center of every one of its faces.

.. enunciation:: Inscribing a Sphere in Any of the Five Regular Solids (Campanus XV.13)

   In any given one of the five regular bodies (*tetracedron*, *cubo*, *octocedron*, *ycocedron*, or *duodecedron*), to inscribe a sphere that touches all the plane bases (faces) of that body at their centers.

.. assertion:: Construction and Proof (:just:`III.14`, :just:`XI.11`, :just:`III.16`, :just:`XI.Def.14`)

   1. Every one of the five regular bodies can be inscribed in a circumscribing sphere (:just:`XIII.13`–:just:`XIII.17`), whose center :math:`a` is the common center of the regular body.
   2. From this center :math:`a` of the circumscribing sphere, draw perpendiculars (:just:`XI.11`) to all the plane bases (faces) of the regular body—namely 4 perpendiculars in the tetracedron, 6 in the cube, 8 in the octocedron, 20 in the ycocedron, and 12 in the duodecedron (see the marginal diagram ``0042.g1.png`` on Folio 0042).
   3. Each plane face of the regular body cuts the circumscribing sphere in a circle that circumscribes that face. Because all the faces of any single regular body are equal and equilateral polygons, all their circumscribing circles are **equal circles** in the circumscribing sphere.
   4. By the :just:`fourteenth of the third <III.14>`, equal circles (and equal chords) in the same sphere lie at **equal perpendicular distances** from the center of the sphere; and the perpendicular from the center of the sphere to the plane of each circle falls upon the exact **center** of that circle (and therefore the center of that regular face).
   5. Consequently, all the perpendiculars :math:`ab, ac, ad, \\dots` drawn from the center :math:`a` of the body to the centers :math:`b, c, d, \\dots` of its faces are **mutually equal**!
   6. With center :math:`a` and radius equal to one of these perpendiculars :math:`ab`, describe a semicircle in a plane passing through :math:`ab` and revolve it around its diameter (:just:`XI.Def.14`).
   7. As the semicircle revolves, its circumference passes through the center :math:`b, c, d, \\dots` of every face of the regular body; and because each face plane is perpendicular to the radius :math:`ab, ac, \\dots` at its extremity, by the :just:`sixteenth of the third <III.16>` the inscribed sphere **touches** (*continge*) every face at its center without cutting through any face!

And recall from :ref:`Chapter XXXII <compendio-cap_32-en>` and :ref:`Chapter XXXIII <compendio-cap_33-en>` that when all five regular bodies are inscribed in one and the same outer sphere, the inner sphere inscribed in the **duodecedron** is **equal** to the inner sphere inscribed in the **ycocedron**, and the inner sphere inscribed in the **cube** is **equal** to the inner sphere inscribed in the **octocedron**!

.. qed::""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagram**: Folio 0042 (``f. 13v``) includes diagram ``0042.g1.png`` illustrating the insphere construction of Campanus XV.13.
- **Completion of the Classical Corpus (Books I–XV)**: With ``Cap. XLVII`` (Campanus XV.13), Pacioli completes his exposition of the entire Euclidean-Campanian canon of the five regular solids (:just:`XIII.1`–:just:`XIII.18`, :just:`XIV.1`–:just:`XIV.10`, and Campanus XV.1–13). Chapters ``XLVIII``–``LV`` now transition directly to **Leonardo da Vinci's** woodcut plates (Plates I–XL) and the semi-regular and stellated **dependent bodies** (*corpi dependenti*).""",
    },
    48: {
        "title_en": "On the Form and Disposition of the Plane (Solid) and Hollow (Skeletal) Tetracedron, Regular and Truncated (Plates I–IV), and Elevated (Plates V–VI).",
        "body_en": """Having demonstrated the theoretical generation, proportions, and mutual inscriptions of all five regular bodies, we now present to Your Ducal Highness's eyes their true perspective images—drawn by the hand of our **Leonardo da Vinci**—together with their **truncated** (*abscisi* or *tagliati*) and **elevated** (*elevati* or *pontuti*) dependent bodies, beginning with the first regular body, the **tetracedron** (:ref:`Plates I–VI <plates-polyhedra-en>`).

.. rubric:: 1. The Regular Tetracedron — Solid (Plate I) and Hollow/Skeletal (Plate II)

- **Plate I (Folio 0187, Tetracedron Planum Solidu[m])** and **Plate II (Folio 0189, Tetracedron Planum Vacuum)**:
  This first figure is the **regular tetracedron** itself, whose formation in the sphere we proved in :ref:`Chapter XXVI <compendio-cap_26-en>` (:just:`XIII.13`). It has **4** equilateral triangular bases (faces), **4** solid angles (each contained by 3 plane angles of :math:`\\frac{2}{3}R`), and **6** equal edges.
  - Under number **I** it is shown **solid** (*piano solido*), so that only the front faces turned toward the eye are seen, while the back faces are hidden by its corporeal mass.
  - Under number **II** it is shown **hollow** or **skeletal** (*piano vacuo*), framed by solid ribs (*pilastrelli*) along its six edges with open windows in the middle of its faces, so that the eye sees simultaneously both the front and the back edges and vertices in true perspective.

.. rubric:: 2. The Truncated Tetracedron (*Tetracedron Abscisum*) — Solid (Plate III) and Hollow (Plate IV)

- **Plate III (Folio 0191, Tetracedron Abscisum Solidu[m])** and **Plate IV (Folio 0193, Tetracedron Abscisum Vacuum)**:
  This second body is derived (*dependente*) from the regular tetracedron by **truncation** (*abscissione* or *taglio*):
  - If each of the **6 edges** of the regular tetracedron is divided into **three equal parts** (:math:`\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}`), and the **4 solid angles** (corners) are sliced off by four plane cuts passing through those trisection points, then:
    1. In place of the **4 cut-off vertices** there appear **4 new equilateral triangles** (whose sides equal :math:`\\frac{1}{3}` of the original edge of the tetracedron).
    2. Each of the **4 original triangular faces** of the tetracedron loses its three corners and is transformed into an **equilateral and equiangular hexagon** (of side :math:`\\frac{1}{3}` of the original edge)!
  - Thus the *tetracedron absciso* has **8 plane bases** in all (**4 equilateral triangles** and **4 regular hexagons**), **12 solid angles** (each formed by two hexagons and one triangle), and **18 equal edges** (6 remaining middle thirds of the original edges plus 12 new edges formed by the 4 triangular cuts).
  - Note well: here the cut was made at **one-third** (:math:`\\frac{1}{3}`) of each edge. If instead the cut is carried all the way to the **midpoint** (:math:`\\frac{1}{2}`) of each edge, the hexagons vanish into triangles and the body becomes the regular **octocedron** of 8 triangular bases, exactly as we proved in :ref:`Chapter XXXV <compendio-cap_35-en>`!

.. rubric:: 3. The Elevated Tetracedron (*Tetracedron Elevatum*) — Solid (Plate V) and Hollow (Plate VI)

- **Plate V (Folio 0195, Tetracedron Elevatum Solidu[m])** and **Plate VI (Folio 0197, Tetracedron Elevatum Vacuum)**:
  This third body is derived from the regular tetracedron by **elevation** (*elevatione*):
  - Upon each of the **4 equilateral triangular bases** of the interior regular tetracedron, erect outward an **equilateral triangular pyramid** (a small *tetracedron*) whose base is that face of the tetracedron and whose three rising lateral faces are equilateral triangles.
  - The resulting star-like body is bounded externally by :math:`4 \\times 3 =` **12 equilateral triangular faces** (while the 4 bases of the inner tetracedron remain hidden inside, except in the hollow skeletal view of Plate VI where the interior frame is visible!).
  - It has **8 vertices** in all: **4 interior re-entrant vertices** (*angoli de dentro*, the 4 vertices of the core tetracedron) and **4 exterior projecting vertices or cones** (*coni / ponti de fore*, the 4 apices of the elevated pyramids), and **18 equal edges** (the 6 edges of the core tetracedron plus :math:`4 \\times 3 = 12` rising edges, called *corausti*).""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate I** (``0187.rst``, ``0187.g1.png``): *Tetracedron Planum Solidum* (Tetrahedron, solid).
  - **Plate II** (``0189.rst``, ``0189.g1.png``): *Tetracedron Planum Vacuum* (Tetrahedron, skeletal).
  - **Plate III** (``0191.rst``, ``0191.g1.png``): *Tetracedron Abscisum Solidum* (Truncated tetrahedron, Archimedean solid :math:`(3.6^2)`, solid).
  - **Plate IV** (``0193.rst``, ``0193.g1.png``): *Tetracedron Abscisum Vacuum* (Truncated tetrahedron, skeletal).
  - **Plate V** (``0195.rst``, ``0195.g1.png``): *Tetracedron Elevatum Solidum* (Triakis-like equilateral cumulation of the tetrahedron, solid).
  - **Plate VI** (``0197.rst``, ``0197.g1.png``): *Tetracedron Elevatum Vacuum* (Elevated tetrahedron, skeletal).""",
    },
    49: {
        "title_en": "On the Disposition of the Exacedron or Cube: Regular (Plates VII–VIII), Truncated (Plates IX–X), and Elevated (Plates XI–XII).",
        "body_en": """Following the same threefold order—regular, truncated (*absciso*), and elevated (*elevato*), each in solid (*solido*) and hollow (*vacuo*) perspective—we now describe the second regular body, the **exacedron** or **cube**, and its immediate dependents (:ref:`Plates VII–XII <plates-polyhedra-en>`).

.. rubric:: 1. The Regular Exacedron or Cube — Solid (Plate VII) and Hollow (Plate VIII)

- **Plate VII (Folio 0199, Exacedron Planum Solidu[m])** and **Plate VIII (Folio 0201, Exacedron Planum Vacuum)**:
  This is the second regular body, the **cube** (*cubo* or *exacedron*), whose construction in the sphere we proved in :ref:`Chapter XXVII <compendio-cap_27-en>` (:just:`XIII.15`). It has **6 equal square bases** (faces), **8 solid angles** (each contained by 3 right angles), and **12 equal edges**. Plate VII shows it solid, and Plate VIII shows it hollow in perspective.

.. rubric:: 2. The Truncated Cube (*Exacedron Abscisum* / Cuboctahedron) — Solid (Plate IX) and Hollow (Plate X)

- **Plate IX (Folio 0203, Exacedron Abscisum Solidu[m])** and **Plate X (Folio 0205, Exacedron Abscisum Vacuum)**:
  This dependent body is formed from the cube by **bisecting all 12 edges of the cube at their midpoints** and slicing off all **8 corner pyramids** by plane cuts passing through the midpoints of the three edges meeting at each corner:
  1. In place of the **8 sliced-off solid angles** of the cube, there arise **8 equilateral triangles** (whose sides equal half the face diagonal of the cube).
  2. Each of the **6 original square faces** of the cube, having its four corners cut off to the midpoints of its four sides, is reduced to an inscribed **square** (whose area is half the original square face and whose sides equal the sides of the 8 new equilateral triangles!).
  - Thus the *exacedron absciso* (the **cuboctahedron**) is bounded by **14 plane bases** in all—**6 squares** and **8 equilateral triangles**—all having equal edges! It has **12 solid angles** (at the 12 midpoints of the original cube's edges, each vertex surrounded by two squares and two equilateral triangles) and **24 equal edges**.

.. rubric:: 3. The Elevated Cube (*Exacedron Elevatum*) — Solid (Plate XI) and Hollow (Plate XII)

- **Plate XI (Folio 0207, Exacedron Elevatum Solidu[m])** and **Plate XII (Folio 0209, Exacedron Elevatum Vacuum)**:
  This body is formed by erecting upon each of the **6 square bases** of the core cube an **equilateral square pyramid** (each bounded by 4 equilateral triangles meeting at an outer apex or cone):
  - Externally it is bounded by :math:`6 \\times 4 =` **24 equilateral triangular faces** (while the 6 square faces of the interior cube are enclosed within, visible in the hollow skeletal perspective of Plate XII).
  - It has **14 vertices** in all (**8 interior re-entrant vertices** of the core cube and **6 exterior projecting cones** of the six pyramids) and **36 equal edges** (the 12 edges of the core cube plus :math:`6 \\times 4 = 24` rising edges).""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate VII** (``0199.rst``): *Exacedron Planum Solidum* (Cube, solid).
  - **Plate VIII** (``0201.rst``): *Exacedron Planum Vacuum* (Cube, skeletal).
  - **Plate IX** (``0203.rst``): *Exacedron Abscisum Solidum* (**Cuboctahedron**, Archimedean solid :math:`(3.4)^2`, solid).
  - **Plate X** (``0205.rst``): *Exacedron Abscisum Vacuum* (Cuboctahedron, skeletal).
  - **Plate XI** (``0207.rst``): *Exacedron Elevatum Solidum* (Equilateral cumulation of the cube, solid).
  - **Plate XII** (``0209.rst``): *Exacedron Elevatum Vacuum* (Elevated cube, skeletal).""",
    },
    50: {
        "title_en": "On the Disposition of the Octocedron: Regular (Plates XIII–XIV), Truncated (Plates XV–XVI), and Elevated (Plates XVII–XVIII).",
        "body_en": """Next we describe the third regular body, the **octocedron** of eight equilateral triangular bases, together with its truncated (*absciso*) and elevated (*elevato*) dependent bodies in solid and hollow perspective (:ref:`Plates XIII–XVIII <plates-polyhedra-en>`).

.. rubric:: 1. The Regular Octocedron — Solid (Plate XIII) and Hollow (Plate XIV)

- **Plate XIII (Folio 0217, Octocedron Planum Solidu[m])** and **Plate XIV (Folio 0219, Octocedron Planum Vacuum)**:
  This is the third regular body, whose construction in the sphere we demonstrated in :ref:`Chapter XXVIII <compendio-cap_28-en>` (:just:`XIII.14`). It has **8 equilateral triangular bases**, **6 solid angles** (each contained by 4 plane angles of :math:`\\frac{2}{3}R`), and **12 equal edges**.

.. rubric:: 2. The Truncated Octahedron (*Octocedron Abscisum*) — Solid (Plate XV) and Hollow (Plate XVI)

- **Plate XV (Folio 0221, Octocedron Abscisum Solidu[m])** and **Plate XVI (Folio 0223, Octocedron Abscisum Vacuum)**:
  This dependent body is formed from the regular octocedron:
  - Note carefully the two ways of truncating the octocedron:
    1. If the **12 edges** of the octocedron are divided into **three equal parts** (:math:`\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}`) and the **6 four-faced solid angles** are sliced off at those trisection points, then the **6 cut-off vertices** become **6 squares** (because 4 triangles meet at each vertex of the octocedron) and the **8 original triangular faces** become **8 regular hexagons**, producing a body of **14 faces (6 squares and 8 hexagons)**, 24 vertices, and 36 equal edges.
    2. If instead the cut is made at the **midpoints** (:math:`\\frac{1}{2}`) of the 12 edges of the octocedron, the 6 cut-off vertices become **6 squares** and the 8 original triangles are reduced to **8 equilateral triangles**, yielding the exact same **14-base body of 6 squares and 8 triangles** (the **cuboctahedron**) that was generated from the cube in Plates IX–X! (In Leonardo's Plates XV and XVI, the rectified 14-face cuboctahedron is drawn again from the dual octahedral perspective.)

.. rubric:: 3. The Elevated Octahedron (*Octocedron Elevatum* / Stella Octangula) — Solid (Plate XVII) and Hollow (Plate XVIII)

- **Plate XVII (Folio 0225, Octocedron Elevatum Solidu[m])** and **Plate XVIII (Folio 0227, Octocedron Elevatum Vacuum)**:
  This body is formed by erecting upon each of the **8 equilateral triangular bases** of the core octocedron an **equilateral triangular pyramid** (a small *tetracedron*):
  - Externally it is bounded by :math:`8 \\times 3 =` **24 equilateral triangular faces** (while the 8 triangular bases of the core octocedron lie within).
  - It has **14 vertices** in all (**6 interior re-entrant vertices** of the core octocedron and **8 exterior projecting cones** of the eight elevated pyramids—which 8 exterior cones stand at the 8 corners of a circumscribing cube!) and **36 equal edges** (the 12 edges of the core octocedron plus :math:`8 \\times 3 = 24` rising edges).""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XIII** (``0217.rst``): *Octocedron Planum Solidum* (Octahedron, solid).
  - **Plate XIV** (``0219.rst``): *Octocedron Planum Vacuum* (Octahedron, skeletal).
  - **Plate XV** (``0221.rst``): *Octocedron Abscisum Solidum* (Truncated/rectified octahedron, solid).
  - **Plate XVI** (``0223.rst``): *Octocedron Abscisum Vacuum* (Truncated/rectified octahedron, skeletal).
  - **Plate XVII** (``0225.rst``): *Octocedron Elevatum Solidum* (**Stella Octangula**, compound of two dual tetrahedra, solid).
  - **Plate XVIII** (``0227.rst``): *Octocedron Elevatum Vacuum* (Stella Octangula, skeletal).
- **First Depiction of the *Stella Octangula***: Plates XVII and XVIII (drawn by Leonardo da Vinci in 1497 and printed in 1509) are the earliest known perspective depictions of the **stellated octahedron** (later rediscovered by Johannes Kepler in *Harmonices Mundi*, 1619, who named it the *Stella Octangula*). Because the dihedral angle of an octahedron (:math:`\\arccos(-\\frac{1}{3}) \\approx 109.47^{\\circ}`) and the dihedral angle of a regular tetrahedron (:math:`\\arccos(\\frac{1}{3}) \\approx 70.53^{\\circ}`) are **supplementary** (:math:`109.47^{\\circ} + 70.53^{\\circ} = 180^{\\circ}`), erecting regular tetrahedra on the 8 faces of a regular octahedron makes the faces coplanar across the octahedral edges, forming two interpenetrating large regular tetrahedra of double the edge length!""",
    },
    51: {
        "title_en": "On the Disposition of the Ycocedron: Regular (Plates XIX–XX), Truncated (Plates XXI–XXII), and Elevated (Plates XXIII–XXIV).",
        "body_en": """We come now to the fourth regular body, the **ycocedron** of twenty equilateral triangular bases, and its truncated (*absciso*) and elevated (*elevato*) dependent bodies in solid and hollow perspective (:ref:`Plates XIX–XXIV <plates-polyhedra-en>`).

.. rubric:: 1. The Regular Ycocedron — Solid (Plate XIX) and Hollow (Plate XX)

- **Plate XIX (Folio 0229, Ycocedron Planum Solidu[m])** and **Plate XX (Folio 0231, Ycocedron Planum Vacuum)**:
  This is the fourth regular body, whose construction in the sphere by means of our Divine Proportion we demonstrated in :ref:`Chapter XXIX <compendio-cap_29-en>` (:just:`XIII.16`). It has **20 equilateral triangular bases**, **12 solid angles** (each contained by 5 plane angles of :math:`\\frac{2}{3}R`), and **30 equal edges**.

.. rubric:: 2. The Truncated Icosahedron (*Ycocedron Abscisum*) — Solid (Plate XXI) and Hollow (Plate XXII)

- **Plate XXI (Folio 0233, Ycocedron Abscisum Solidu[m])** and **Plate XXII (Folio 0235, Ycocedron Abscisum Vacuum)**:
  This celebrated body is derived from the regular ycocedron by **dividing each of its 30 edges into three equal parts** (:math:`\\frac{1}{3}, \\frac{1}{3}, \\frac{1}{3}`) and slicing off all **12 five-faced solid angles** at those trisection points:
  1. Because **5** triangular faces meet at each of the **12 vertices** of the ycocedron, slicing off the 12 vertices produces **12 equilateral and equiangular pentagons** (whose sides equal :math:`\\frac{1}{3}` of the original edge of the ycocedron).
  2. Each of the **20 original equilateral triangular faces** of the ycocedron, losing its three corners at the trisection points, is transformed into an **equilateral and equiangular hexagon** (of side :math:`\\frac{1}{3}` of the original edge)!
  - Thus the *ycocedron absciso* has **32 plane bases** in all (**12 regular pentagons** and **20 regular hexagons**), **60 solid angles** (each formed by two hexagons and one pentagon), and **90 equal edges** (30 remaining middle thirds of the original edges plus :math:`12 \\times 5 = 60` new pentagonal edges)!

.. rubric:: 3. The Elevated Icosahedron (*Ycocedron Elevatum*) — Solid (Plate XXIII) and Hollow (Plate XXIV)

- **Plate XXIII (Folio 0237, Ycocedron Elevatum Solidu[m])** and **Plate XXIV (Folio 0239, Ycocedron Elevatum Vacuum)**:
  This body is formed by erecting upon each of the **20 equilateral triangular bases** of the core ycocedron an **equilateral triangular pyramid** (whose three rising lateral edges or *corausti* are either equal to the edge of the ycocedron or, even more nobly, proportioned to it according to our Divine Proportion so that the twenty apices form a circumscribing duodecedron):
  - Externally it is bounded by :math:`20 \\times 3 =` **60 triangular faces** (while the 20 triangular bases of the core ycocedron lie within, visible in the hollow skeletal perspective of Plate XXIV).
  - It has **32 vertices** in all (**12 interior re-entrant vertices** of the core ycocedron and **20 exterior projecting cones** of the twenty elevated pyramids) and **90 edges** (the 30 edges of the core ycocedron plus :math:`20 \\times 3 = 60` rising edges).""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XIX** (``0229.rst``): *Ycocedron Planum Solidum* (Icosahedron, solid).
  - **Plate XX** (``0231.rst``): *Ycocedron Planum Vacuum* (Icosahedron, skeletal).
  - **Plate XXI** (``0233.rst``): *Ycocedron Abscisum Solidum* (**Truncated Icosahedron**, Archimedean solid :math:`(5.6^2)` of 12 pentagons and 20 hexagons, solid).
  - **Plate XXII** (``0235.rst``): *Ycocedron Abscisum Vacuum* (Truncated Icosahedron, skeletal).
  - **Plate XXIII** (``0237.rst``): *Ycocedron Elevatum Solidum* (Elevated/cumulated Icosahedron of 60 triangular faces, solid).
  - **Plate XXIV** (``0239.rst``): *Ycocedron Elevatum Vacuum* (Elevated Icosahedron, skeletal).""",
    },
    52: {
        "title_en": "On the Disposition of the Duodecedron: Regular (Plates XXV–XXVI), Truncated (Plates XXVII–XXVIII), Elevated (Plates XXIX–XXX), and the Elevated Truncated Bodies (Plates XXXI–XXXIV).",
        "body_en": """Now we describe the fifth and noblest regular body, the **duodecedron** of twelve regular pentagonal bases, together with its truncated (*absciso*) and elevated (*elevato*) dependents, as well as the further bodies formed by **elevating the truncated bodies** (*abscisi elevati*) (:ref:`Plates XXV–XXXIV <plates-polyhedra-en>`).

.. rubric:: 1. The Regular Duodecedron — Solid (Plate XXV) and Hollow (Plate XXVI)

- **Plate XXV (Folio 0241, Duodecedron Planum Solidu[m])** and **Plate XXVI (Folio 0243, Duodecedron Planum Vacuum)**:
  This is the fifth regular body, whose construction in the sphere by means of our Divine Proportion we demonstrated in :ref:`Chapter XXX <compendio-cap_30-en>` (:just:`XIII.17`). It has **12 equilateral and equiangular pentagonal bases**, **20 solid angles** (each contained by 3 pentagonal angles of :math:`1\\frac{1}{5}R`), and **30 equal edges**.

.. rubric:: 2. The Truncated Dodecahedron (*Duodecedron Abscisum* / Icosidodecahedron) — Solid (Plate XXVII) and Hollow (Plate XXVIII)

- **Plate XXVII (Folio 0245, Duodecedron Abscisum Solidu[m])** and **Plate XXVIII (Folio 0247, Duodecedron Abscisum Vacuum)**:
  This dependent body is formed from the regular duodecedron by **bisecting all 30 edges at their midpoints** and slicing off all **20 three-faced solid angles** by plane cuts passing through those midpoints:
  1. Because **3** pentagonal faces meet at each of the **20 vertices** of the duodecedron, slicing off the 20 vertices produces **20 equilateral triangles** (whose sides equal half the pentagonal chord of the original duodecedron, so that the original edge and the new edge stand in the Divine Proportion!).
  2. Each of the **12 original pentagonal faces**, having its five corners cut off at the midpoints of its five sides, is reduced to an inscribed **regular pentagon** sharing the exact same edges as the 20 new equilateral triangles!
  - Thus the *duodecedron absciso* (the **icosidodecahedron**) has **32 plane bases** in all (**12 regular pentagons** and **20 equilateral triangles**), **30 solid angles** (at the 30 midpoints of the original edges, each vertex surrounded by two pentagons and two triangles), and **60 equal edges**.

.. rubric:: 3. The Elevated Dodecahedron (*Duodecedron Elevatum*) — Solid (Plate XXIX) and Hollow (Plate XXX)

- **Plate XXIX (Folio 0249, Duodecedron Elevatum Solidu[m])** and **Plate XXX (Folio 0251, Duodecedron Elevatum Vacuum)**:
  This body is formed by erecting upon each of the **12 regular pentagonal bases** of the core duodecedron an **equilateral pentagonal pyramid** (each bounded by 5 equilateral triangles meeting at an outer apex or cone—recall that 5 equilateral triangles have angle sum :math:`5 \\times \\frac{2}{3}R = 3\\frac{1}{3}R < 4R`, so they form a genuine solid pyramid over a regular pentagon!):
  - Externally it is bounded by :math:`12 \\times 5 =` **60 equilateral triangular faces** (while the 12 pentagonal bases of the core duodecedron lie within, visible in the hollow skeletal perspective of Plate XXX).
  - It has **32 vertices** in all (**20 interior re-entrant vertices** of the core duodecedron and **12 exterior projecting cones** of the twelve pentagonal pyramids) and **90 equal edges** (the 30 edges of the core duodecedron plus :math:`12 \\times 5 = 60` rising edges).

.. rubric:: 4. The Elevated Truncated Cube (*Exacedron Abscisum Elevatum*) and Elevated Truncated Dodecahedron (*Duodecedron Abscisum Elevatum*) — Plates XXXI–XXXIV

By the same art, one can also **elevate the truncated bodies** (*abscisi elevati*) by erecting pyramids upon all the faces of a truncated body:

- **Plate XXXI (Folio 0253, Exacedron Abscisum Elevatum Solidu[m])** and **Plate XXXII (Folio 0255, Exacedron Abscisum Elevatum Vacuum)**:
  Formed by taking the 14-base *exacedron absciso* (the cuboctahedron of **6 squares** and **8 equilateral triangles**, Plates IX–X) and erecting **6 square pyramids** upon its 6 square bases (:math:`6 \\times 4 = 24` triangles) and **8 triangular pyramids** upon its 8 triangular bases (:math:`8 \\times 3 = 24` triangles), yielding a star-like body bounded externally by :math:`24 + 24 =` **48 triangular faces** and **14 projecting cones**!
- **Plate XXXIII (Folio 0257, Duodecedron Abscisum Elevatum Solidu[m])** and **Plate XXXIV (Folio 0259, Duodecedron Abscisum Elevatum Vacuum)**:
  Formed by taking the 32-base *duodecedron absciso* (the icosidodecahedron of **12 pentagons** and **20 equilateral triangles**, Plates XXVII–XXVIII) and erecting **12 pentagonal pyramids** upon its 12 pentagonal bases (:math:`12 \\times 5 = 60` triangles) and **20 triangular pyramids** upon its 20 triangular bases (:math:`20 \\times 3 = 60` triangles), yielding a magnificent star-like body bounded externally by :math:`60 + 60 =` **120 triangular faces** and **32 projecting cones**!""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XXV** (``0241.rst``): *Duodecedron Planum Solidum* (Dodecahedron, solid).
  - **Plate XXVI** (``0243.rst``): *Duodecedron Planum Vacuum* (Dodecahedron, skeletal).
  - **Plate XXVII** (``0245.rst``): *Duodecedron Abscisum Solidum* (**Icosidodecahedron**, Archimedean solid :math:`(3.5)^2` of 12 pentagons and 20 triangles, solid).
  - **Plate XXVIII** (``0247.rst``): *Duodecedron Abscisum Vacuum* (Icosidodecahedron, skeletal).
  - **Plate XXIX** (``0249.rst``): *Duodecedron Elevatum Solidum* (Equilateral pentagonal cumulation of the dodecahedron, solid—visually identical in vertex/face topology to Kepler's **Small Stellated Dodecahedron**!).
  - **Plate XXX** (``0251.rst``): *Duodecedron Elevatum Vacuum* (Elevated dodecahedron, skeletal).
  - **Plate XXXI–XXXII** (``0253.rst``, ``0255.rst``): *Exacedron Abscisum Elevatum Solidum / Vacuum* (Cumulated cuboctahedron, 48 triangular faces).
  - **Plate XXXIII–XXXIV** (``0257.rst``, ``0259.rst``): *Duodecedron Abscisum Elevatum Solidum / Vacuum* (Cumulated icosidodecahedron, 120 triangular faces).""",
    },
    53: {
        "title_en": "On the Formation and Origin of the Body of Twenty-Six Bases: Eighteen Squares and Eight Equilateral Triangles (Plates XXXV–XXXVIII).",
        "body_en": """Beyond the immediate truncations and elevations of the five regular bodies, another most noble and useful dependent body is generated from the **cube**, called the **Vigintisex Basium** (the **Body of Twenty-Six Bases**, modern **rhombicuboctahedron**), shown both plain and elevated in :ref:`Plates XXXV–XXXVIII <plates-polyhedra-en>`.

.. rubric:: 1. The Twenty-Six-Base Body (*Vigintisex Basium*) — Solid (Plate XXXV) and Hollow (Plate XXXVI)

- **Plate XXXV (Folio 0261, Vigintisex Basium Planum Solidu[m])** and **Plate XXXVI (Folio 0263, Vigintisex Basium Planum Vacuum)**:
  This body of **26 bases** arises from the regular **cube** by uniform beveling (*smussatura*) of **both its 12 edges and its 8 solid angles**:
  - Imagine a cube whose 6 square faces are cut parallel to its 12 edges at an equal depth on every face so that:
    1. In the middle of each of the **6 original square faces** of the cube there remains an inner **square** (*6 original squares*).
    2. Along each of the **12 bevelled edges** of the cube, where two adjacent square faces met at right angles, there is formed a new **square** inclined equally (:math:`45^{\\circ}`) to both adjacent faces (*12 edge squares*).
    3. At each of the **8 sliced-off corners** (solid angles) of the cube, where three bevelled edges meet, there is formed an **equilateral triangle** whose three sides are the ends of those three edge-squares (*8 corner equilateral triangles*).
  - Thus the whole body is bounded by **26 equilateral and equiangular plane bases** in all:
    - **18 equal squares** (:math:`6 + 12 = 18`);
    - **8 equal equilateral triangles**;
    all sharing the exact same edge length!
  - It has **24 solid angles** (each vertex surrounded by three squares and one equilateral triangle) and **48 equal edges**.
  - Notice also its admirable octogonal cross-sections: around the body run **three mutually perpendicular octogonal belts**, each consisting of **8 consecutive squares** (:math:`4` from the original cube faces alternating with :math:`4` from the bevelled edges), so that the cross-section is a **regular octagon**! And for this reason this body is of the greatest utility to **architects, sculptors, and perspective painters** (*architecti, scultori, e prospectivi*), since from a cubic block of marble or timber one immediately derives the regular octagon in three orthogonal planes for capitals, bases, lanterns, and cupolas.

.. rubric:: 2. The Elevated Twenty-Six-Base Body (*Vigintisex Basium Elevatum*) — Solid (Plate XXXVII) and Hollow (Plate XXXVIII)

- **Plate XXXVII (Folio 0265, Vigintisex Basium Elevatum Solidu[m])** and **Plate XXXVIII (Folio 0267, Vigintisex Basium Elevatum Vacuum)**:
  Formed by erecting **18 equilateral square pyramids** upon the 18 square bases of the 26-base body (:math:`18 \\times 4 = 72` triangular faces) and **8 equilateral triangular pyramids** upon its 8 triangular bases (:math:`8 \\times 3 = 24` triangular faces), producing a magnificent star-like polyhedron bounded externally by :math:`72 + 24 =` **96 equilateral triangular faces** and **26 projecting cones**!""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XXXV** (``0261.rst``): *Vigintisex Basium Planum Solidum* (**Rhombicuboctahedron**, Archimedean solid :math:`(3.4^3)` of 18 squares and 8 equilateral triangles, solid).
  - **Plate XXXVI** (``0263.rst``): *Vigintisex Basium Planum Vacuum* (Rhombicuboctahedron, skeletal).
  - **Plate XXXVII** (``0265.rst``): *Vigintisex Basium Elevatum Solidum* (Cumulated rhombicuboctahedron, 96 triangular faces, solid).
  - **Plate XXXVIII** (``0267.rst``): *Vigintisex Basium Elevatum Vacuum* (Cumulated rhombicuboctahedron, skeletal).
- **Jacopo de' Barbari's 1495 Portrait of Pacioli**: The glass *Vigintisex Basium* half-filled with water hanging from a thin cord in Jacopo de' Barbari's famous 1495 Capodimonte portrait of Fra Luca Pacioli (and the wooden dodecahedron resting on Pacioli's *Summa*) is this exact 26-base rhombicuboctahedron!""",
    },
    54: {
        "title_en": "On the Body of Seventy-Two Bases (*Septuaginta Duarum Basium*), Its Origin, and Its Architectural Use in Cupolas and Vaults (Plates XXXIX–XL).",
        "body_en": """Continuing further along this path toward the sphere, we arrive at the celebrated **Body of Seventy-Two Bases** (*Septuaginta Duarum Basium*), depicted in solid and hollow perspective in :ref:`Plates XXXIX and XL <plates-polyhedra-en>`, which is of supreme utility in **architecture** for the coffered vaults of round temples, tribunes, and cupolas.

.. rubric:: 1. Generation of the Seventy-Two-Base Body (Plates XXXIX–XL)

- **Plate XXXIX (Folio 0269, Septuagintaduarum Basium Planum Solidu[m])** and **Plate XL (Folio 0271, Septuagintaduarum Basium Vacuum)**:
  How is this body generated in the sphere? By the method of the :just:`seventeenth of the twelfth book <XII.17>` (which is the fourteenth of the twelfth in Campanus), where our philosopher teaches how to inscribe a polyhedral solid inside the outer of two concentric spheres by dividing the great circle of the sphere into equal parts (for instance into **12** or **16** or **24** equal arcs) and drawing parallel latitudinal circles (*paralleli*) and longitudinal meridians (*meridiani*) from pole to pole!
- Specifically, in the **72-base body**:
  - Dividing the equatorial circle into **12 equal parts** (dodecagon) and stepping in 3 latitudinal zones toward each pole produces:
    - **48 trapezoidal or quadrangular faces** (*48 basi quadrilatere / d'elmuariffe*, arranged in 4 latitudinal rings of 12 quadrangles each: 24 in the upper hemisphere and 24 in the lower hemisphere); and
    - **24 isosceles triangular faces** (*24 basi triangulari*, 12 meeting around the upper pole and 12 around the lower pole, closing the polar caps);
    making :math:`48 + 24 =` **72 plane bases** in all! (Or in the hollowed ring form known in Tuscany as the *mazzocchio*, the open faceted torus of quadrangular coffers.)

.. rubric:: 2. Architectural Application: The Pantheon in Rome, Santa Maria delle Grazie, and Bramante's Sacristy of San Satiro in Milan

This geometric generation is the very foundation of all round and polygonal vaulted architecture (*tribune, cupole, e volte a botta o a crosera*):

- **The Pantheon in Rome (*La Rotonda*)**: Thus the ancient Romans constructed thestupendous vault of that most famous temple called the **Pantheon** (today *Sancta Maria Rotonda* in Rome), originally dedicated to Cybele, Mother of all the Gods: its hemispherical dome is divided by meridians and parallels into stepped rings of **quadrangular coffers** (*quadri / lacunari*) diminishing proportionally toward the central oculus at the pole, exactly according to the zones of this 72-base body!
- **Milan — Santa Maria delle Grazie and San Satiro**: And in our own day in your renowned city of Milan, we see this same geometric art practiced in the magnificent tribune of **Santa Maria delle Grazie** (constructed under Your Ducal Highness's pious patronage) and in the admirable octagonal **Sacristy of San Satiro** designed by Maestro Donato Bramante, where the coffered vaults, pilasters, and perspective reliefs follow these exact circular and polygonal subdivisions.
- **Ludovico Sforza's Heraldic Devices (*Imprese*) and Pythagoras's Angle of Justice (*Angulus Iustitiae*)**:
  In the coffers and friezes of such vaults are carved roses, foliage, and Your Ducal Highness's own famous heraldic devices (*imprese*)—the **brush** (*la scopetta*) and the **axe** (*la cetta*)—symbolizing how Your Highness cleanses and prunes away all vice and superfluous disorder through **Justice** (*Iustitia*). And well did the ancient philosophers, above all **Pythagoras** (as Vitruvius also recalls), call the **right angle** (:math:`90^{\\circ}`, formed by the carpenter's square, *la squadra*) the **Angle of Justice** (*Angulus Iustitiae*): for just as the right angle inclines neither to the acute (deficiency) nor to the obtuse (excess), standing invariable and upright between both extremes, so true Justice gives to every person what is rightfully theirs without tilting to either side!""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Plates Referenced**:
  - **Plate XXXIX** (``0269.rst``): *Septuagintaduarum Basium Planum Solidum* (72-base faceted sphere, solid).
  - **Plate XL** (``0271.rst``): *Septuagintaduarum Basium Vacuum* (72-base faceted sphere, hollow/coffered).
- **Euclid Book XII, Proposition 17 (Campanus XII.14)**: Euclid's construction in :just:`XII.17` inscribes a polyhedron of quadrangular (trapezoidal) zones and polar triangles between two concentric spheres by subdividing the equator and meridians into :math:`4n` equal parts—the exact classical source for Renaissance perspective drawings of the *mazzocchio* (by Paolo Uccello, Piero della Francesca in *De Prospectiva Pingendi*, and Leonardo da Vinci) and for the coffered hemisphere of the **Pantheon** (*La Rotonda*) and Bramante's **Santa Maria presso San Satiro** and **Santa Maria delle Grazie** in Milan.
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2/54.txt`` draft omitted Pacioli's discussion of the Pantheon (*La Rotonda*), Santa Maria delle Grazie, San Satiro, Ludovico Sforza's devices (*la scopetta* and *la cetta*), and Pythagoras's *Angulus Iustitiae*. All are restored in full here (``0046.rst``–``0047.rst``, ``f. 15v``–``f. 16r``).""",
    },
    55: {
        "title_en": "On the Way to Know How to Form Still More Bodies Beyond Those Mentioned, How Their Forms Proceed to Infinity, and Why Plato Assigned the Five Regular Bodies to the Five Simple Bodies of the Universe.",
        "body_en": """From what has been shown in the preceding chapters, most lofty Duke, any speculative intellect can readily understand how **infinitely many more dependent bodies** (*in infinito*) can be formed beyond those already described, and why the divine philosopher **Plato** in his *Timaeus* assigned the five regular bodies alone to the five simple bodies of the universe.

.. rubric:: 1. How Dependent Bodies Proceed to Infinity

- Just as in plane geometry the number of equilateral and equiangular polygons increases without end—from the triangle (3 sides), square (4), pentagon (5), hexagon (6), heptagon (7), octagon (8), and so on *in infinito*—and just as in :just:`XII.17` (:ref:`Chapter LIV <compendio-cap_54-en>`) we divided the sphere by meridians and parallels to produce the 72-base body, so by continually bisecting the arcs of the sphere or by repeatedly truncating (*tagliando / abscindendo*) the solid angles and edges of any regular or dependent polyhedron, and again elevating pyramids upon the resulting faces, new polyhedral forms of 100, 200, or 1,000 bases can be generated **to infinity**, approaching ever closer to the roundness of the **sphere**!
- Yet none of these infinite dependent bodies can ever be **regular** in the strict sense (having all faces equal and of one single kind, all edges equal, and all solid angles equal), for as we proved demonstratively in :ref:`Chapter XXV <compendio-cap_25-en>` (:just:`XI.21`, :just:`I.32`), **only five** such bodies can exist in nature.

.. rubric:: 2. Why Plato in the *Timaeus* Assigned the Five Regular Solids to the Five Simple Elements

Because there are in the entire created universe **five simple bodies**—namely the four sublunary elements (**Earth**, **Fire**, **Air**, and **Water**) and the fifth essence, the **Universal Heaven** (*il Cielo / Quinta Essentia*)—Plato, arguing as a most profound geometer and mathematician, matched each of the five simple bodies to the one regular solid whose geometric properties correspond to its natural motion and character:

1. **The Cube (6 Square Faces, 8 Solid Angles) — Assigned to Earth (*Terra*)**:
   Among all the elements, **Earth** is the most immobile, fixed, heavy, and stable, resting at the center of the world. And among the five regular solids, none sits more firmly and immovably upon its base than the **cube** (*exacedron*), bounded by six flat square faces at right angles; whereas a sphere touches a plane at a single point and rolls at the slightest impulse, the cube rests flat and unshakable.
2. **The Tetracedron (4 Triangular Faces, 4 Solid Angles) — Assigned to Fire (*Fuoco*)**:
   **Fire** is the lightest, sharpest, most penetrating, and quickest to ascend of all the elements, rising upward into a sharp flame (whence the very name *pyramis* comes from the Greek *pyr*, meaning fire!). And among the five regular bodies, the **tetracedron** has the fewest faces (4), the smallest volume for its surface, and the sharpest, most acute solid angles (each contained by only three plane angles totaling two right angles, :math:`180^{\\circ}`), so that it pierces and divides all things.
3. **The Octocedron (8 Triangular Faces, 6 Solid Angles) — Assigned to Air (*Aria*)**:
   **Air** is next to fire in subtlety, mobility, and lightness. The **octocedron**, having 8 equilateral triangular faces and 6 four-triangle vertices (totaling :math:`2\\frac{2}{3}` right angles), is intermediate in mobility and acuteness between the sharp tetracedron of Fire and the rounder ycocedron of Water.
4. **The Ycocedron (20 Triangular Faces, 12 Solid Angles) — Assigned to Water (*Acqua*)**:
   **Water** is heavier and more fluid, flowing downward and spreading across the earth rather than ascending like flame. Accordingly, Plato assigned to Water the **ycocedron**, which has the greatest number of faces (20 triangles) and the most obtuse, rounded solid angles (each formed by 5 triangles totaling :math:`3\\frac{1}{3}` right angles) among the bodies bounded by triangles, so that it is closest to a rolling drop that flows and descends.
5. **The Duodecedron (12 Pentagonal Faces, 20 Solid Angles) — Assigned to the Heaven (*Il Cielo / Quinta Essentia*)**:
   Finally, Plato assigned the **duodecedron** of 12 regular pentagonal bases to the **Universal Heaven**:
   - First, because just as the Heaven is the **receptacle and lodging** (*receptaculo e albergo*) of all created things in the universe, so the duodecedron alone (as we proved in :ref:`Chapter XLVI <compendio-cap_46-en>`) is the receptacle of **all four** of the other regular bodies inscribed within it!
   - Second, as **Alcinous** (*Alcinovo*), **Calcidius** (*Calcidio*), **Macrobius**, and **Apuleius** observe in their commentaries on Plato's *Timaeus*: just as the celestial **Zodiac** is divided into **12 Signs** (*12 segni*), and each of the 12 Signs is divided into **30 degrees** (*30 gradi*), making **360 degrees** in the entire annual revolution of the sun through the heaven, so the **duodecedron** has **12 pentagonal bases**, and when each pentagon is resolved from its center into **5 isosceles triangles** and each of those 5 triangles is subdivided by its three medians/altitudes into **6 scalene right triangles**, each pentagonal face contains :math:`5 \\times 6 =` **30 elementary triangles**, and all **12 pentagonal faces** together contain:

     .. math::

        12 \\times 5 \\times 6 = 12 \\times 30 = 360\\text{ triangles}

     matching the **360 degrees of the Zodiac**! (See the two marginal woodcut diagrams ``0049.g1.png`` and ``0049.g2.png`` on Folio 0049.)

And if a sixth simple element could have existed in nature without a corresponding sixth regular solid, the Supreme Artificer (*el summo Opefice*) would have seemed lacking in foresight—which is impossible. Nor is the **sphere** excluded from perfection because only these five are called regular polyhedra: rather, the sphere is **most regular above all** (*sopra tutti regularissima*), having no diversity of faces or angles at all, but absolute uniformity everywhere, being the sublime cause and container from which all the other bodies derive!""",
        "notes": """Historical & Mathematical Commentary
------------------------------------

- **Paganini 1509 Marginal Diagrams**: Folio 0049 (``f. 17r``) contains two woodcut diagrams (``0049.g1.png`` and ``0049.g2.png``) illustrating the subdivision of the regular pentagon into 5 central triangles and each triangle into 6 scalene right triangles (:math:`5 \\times 6 = 30` per pentagon, :math:`12 \\times 30 = 360` over the whole dodecahedron).
- **Philosophical Authorities Cited**:
  - **Plato**, *Timaeus* 53c–56c (the geometric atomism of the four elements and the cosmos).
  - **Alcinous** (*Didaskalikos* / *Epitome doctrinae Platonicae*, 13, translated into Latin by Marsilio Ficino and Pietro Balbi), source of the 12 signs / 360 triangles zodiacal correspondence (:math:`12 \\times 5 \\times 6 = 360`).
  - **Calcidius** (4th-century Latin translator and commentator on the *Timaeus*), **Macrobius** (*Commentarii in Somnium Scipionis*), and **Apuleius** (*De Platone et eius dogmate*).
- **Comparison with Earlier Draft Track**: The earlier ``divina_en_2/55.txt`` draft compressed this major cosmological and Neoplatonic chapter into four short paragraphs and omitted the citations of Alcinous, Calcidius, Macrobius, and Apuleius as well as the :math:`12 \\times 5 \\times 6 = 360` Zodiacal triangulation explained by diagrams ``0049.g1.png`` and ``0049.g2.png``.""",
    },
}
