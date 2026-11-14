geometor.pacioli.svg_woodcut
============================

.. py:module:: geometor.pacioli.svg_woodcut

.. autoapi-nested-parse::

   Deterministic `.euclid-graphic` SVG generator for Pacioli's *Summa* (1494) codex.

   Generates nine theme-adaptive, interactive ``.euclid-graphic`` SVGs directly from
   exact ``SymPy`` and ``geometor.model`` coordinates (converting symbolic expressions
   to pixel coordinates strictly at SVG serialization time). Every generated SVG adheres
   to the ``photon-platform/publish`` five-layer contract (``#elements``, ``#graphics``,
   ``#highlights``, ``#points``, ``#labels``), 3-vertex midpoint segment paths for
   congruence tick markers (``#geom-tick-1..3``), and canonical ``data-ref`` wiring for
   ``:g:`` and ``:eq:`` interactive highlighting.



Classes
-------

.. autoapisummary::

   geometor.pacioli.svg_woodcut.SVGSpec
   geometor.pacioli.svg_woodcut.EuclidGraphicCanvas


Functions
---------

.. autoapisummary::

   geometor.pacioli.svg_woodcut.generate_all_summa_svgs


Module Contents
---------------

.. py:class:: SVGSpec

   Metadata describing a generated *Summa* ``.euclid-graphic`` SVG plate.


   .. py:attribute:: graphic_id
      :type:  str


   .. py:attribute:: unit_dir
      :type:  str


   .. py:attribute:: filename
      :type:  str


   .. py:attribute:: folio
      :type:  str


   .. py:attribute:: proposition
      :type:  str


   .. py:attribute:: path
      :type:  pathlib.Path


.. py:class:: EuclidGraphicCanvas(*, width: int, height: int, graphic_id: str, folio: str, proposition: str, scale: float = 1.0, origin_x: float = 0.0, origin_y: float = 0.0)

   Builder for standard 5-layer ``.euclid-graphic`` interactive SVGs.


   .. py:attribute:: width


   .. py:attribute:: height


   .. py:attribute:: graphic_id


   .. py:attribute:: folio


   .. py:attribute:: proposition


   .. py:attribute:: scale
      :value: 1.0



   .. py:attribute:: origin_x
      :value: 0.0



   .. py:attribute:: origin_y
      :value: 0.0



   .. py:method:: to_px(x: float | int | sympy.Expr, y: float | int | sympy.Expr) -> tuple[float, float]

      Map exact mathematical ``(x, y)`` (y-up) to SVG screen coordinates (y-down).



   .. py:method:: add_circle(el_id: str, cx: float | int | sympy.Expr, cy: float | int | sympy.Expr, r: float | int | sympy.Expr, *, data_ref: str = '', css_class: str = 'geom-circle') -> None

      Add a circle to ``#elements`` and ``#highlights``.



   .. py:method:: add_arc(el_id: str, cx: float | int | sympy.Expr, cy: float | int | sympy.Expr, r: float | int | sympy.Expr, deg_start: float, deg_end: float, *, data_ref: str = '', css_class: str = 'geom-arc') -> None

      Add a circular arc (math degrees counter-clockwise from +x) to ``#elements``.



   .. py:method:: add_polygon(el_id: str, vertices: list[tuple[float | int | sympy.Expr, float | int | sympy.Expr]], *, data_ref: str = '', css_class: str = 'geom-polygon') -> None

      Add a filled polygon to ``#graphics`` and ``#highlights``.



   .. py:method:: add_segment(el_id: str, p1: tuple[float | int | sympy.Expr, float | int | sympy.Expr], p2: tuple[float | int | sympy.Expr, float | int | sympy.Expr], *, data_ref: str = '', css_class: str = 'geom-line') -> None

      Add a 3-vertex midpoint segment path ``M x1 y1 L xm ym L x2 y2`` to ``#graphics``.



   .. py:method:: add_point(pt_id: str, x: float | int | sympy.Expr, y: float | int | sympy.Expr, *, label: str | None = None, dx: float = 0.0, dy: float = -10.0, anchor: str = 'middle', radius: float = 3.4) -> None

      Add a point circle in ``#points`` and optional label in ``#labels``.



   .. py:method:: add_annotation(ann_id: str, x: float | int | sympy.Expr, y: float | int | sympy.Expr, text: str, *, anchor: str = 'middle', data_ref: str = '') -> None

      Add a compact mathematical or woodcut caption inside ``#labels``.



   .. py:method:: render() -> str

      Serialize the complete 5-layer ``.euclid-graphic`` SVG XML string.



.. py:function:: generate_all_summa_svgs(summa_docsrc_dir: pathlib.Path | str) -> list[SVGSpec]

   Generate and write all nine ``.euclid-graphic`` SVGs into ``docsrc/summa_1494/``.

   :param summa_docsrc_dir: Target root directory (typically ``<repo>/docsrc/summa_1494``).

   :returns: Ordered list of :class:`SVGSpec` records written to disk.


