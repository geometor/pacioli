geometor.pacioli.graphics
=========================

.. py:module:: geometor.pacioli.graphics

.. autoapi-nested-parse::

   Module and CLI utility for graphic, initial cap, and content metadata extraction for Pacioli.



Attributes
----------

.. autoapisummary::

   geometor.pacioli.graphics.cv2
   geometor.pacioli.graphics.scipy
   geometor.pacioli.graphics.ROMAN_MAP


Functions
---------

.. autoapisummary::

   geometor.pacioli.graphics.clean_image
   geometor.pacioli.graphics.find_text_column_bounds
   geometor.pacioli.graphics.detect_initials
   geometor.pacioli.graphics.detect_margin_figures
   geometor.pacioli.graphics.detect_graphics_scipy
   geometor.pacioli.graphics.detect_graphics_cv
   geometor.pacioli.graphics.detect_graphics_folio
   geometor.pacioli.graphics.load_winterberg_chapters
   geometor.pacioli.graphics.extract_folio_content_info
   geometor.pacioli.graphics.detect_single_image
   geometor.pacioli.graphics.extract_from_json
   geometor.pacioli.graphics.build_graphics_index
   geometor.pacioli.graphics.main


Module Contents
---------------

.. py:data:: cv2
   :value: None


.. py:data:: scipy
   :value: None


.. py:data:: ROMAN_MAP

.. py:function:: clean_image(pil_image: PIL.Image.Image, white_point: int = 226) -> PIL.Image.Image

   Applies a linear levels adjustment to the image, mapping white_point to pure white (255).

   Effectively eliminates bleed-through, yellowed paper background, and scanning artifacts.


.. py:function:: find_text_column_bounds(gray: numpy.ndarray, is_recto: bool) -> Tuple[int, int]

   Dynamically locate the horizontal [x_left, x_right] bounds of the main printed text column.


.. py:function:: detect_initials(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect woodcut illuminated initial caps by finding 2D ink-density centers along the text column edge.

   Woodcut initials in the 1509 Paganini edition have consistent square dimensions:
   - Standard chapter initials: 120x132 px (padded around the ~112x118 woodcut frame)
   - Large treatise-opening initials (folios 0017 and 0085): 260x304 px
   - Title-page red initial D (folio 0005): 184x188 px


.. py:function:: detect_margin_figures(image_path: pathlib.Path, is_recto: bool) -> List[Dict[str, Any]]

   Detect geometric diagrams and marginalia strictly in the outer margin of a text folio.

   - Odd (recto) folios: right outer margin (to the right of the main text column).
   - Even (verso) folios: left outer margin (to the left of the main text column).
   Never falls back to full-page text blocks.


.. py:function:: detect_graphics_scipy(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect full-page plate woodcuts on a folio (137-309) using NumPy and SciPy.


.. py:function:: detect_graphics_cv(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect full-page plate graphics using OpenCV if available, falling back to SciPy.


.. py:function:: detect_graphics_folio(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Context-aware graphic detection based on folio page number and book section.


.. py:function:: load_winterberg_chapters(resources_root: pathlib.Path) -> Dict[Tuple[int, int], Dict[str, Any]]

   Load clean Italian, German, and English chapter titles and file links from Winterberg resources.


.. py:function:: extract_folio_content_info(folio_num: int, folio_dir: pathlib.Path, wb_map: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None) -> Dict[str, Any]

   Determine book part, recto/verso side, running header, and chapters/cases on a folio.


.. py:function:: detect_single_image(img_path: pathlib.Path, save: bool = False, force: bool = False, wb_map: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]

   Detect margin graphics, illuminated initial caps, and content info on a single folio scan.


.. py:function:: extract_from_json(json_path: pathlib.Path, no_clean: bool = False) -> None

   Extract all margin graphics and illuminated initial caps defined in <folio>.json.


.. py:function:: build_graphics_index(directory: pathlib.Path) -> pathlib.Path

   Compile all per-folio <folio>.json files into graphics_index.json.


.. py:function:: main() -> None

   CLI for managing graphics and illuminated initials in Pacioli folios.


