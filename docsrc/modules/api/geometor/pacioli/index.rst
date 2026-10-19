geometor.pacioli
================

.. py:module:: geometor.pacioli

.. autoapi-nested-parse::

   Tools for parsing and processing "De :term:`Divina Proportione <divina-proportione>`" by :person:`Luca Pacioli <pacioli>`.

   Key Components:
   ---------------
   - **Parser**: The :class:`PacioliParser` class extracts chapters and content from the transcribed text.
   - **Execution**: The `run_parse.py` script executes the parsing process.

   Usage:
   ------
   Initialize :class:`PacioliParser` with resources and output directories, then call `parse()`.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/pacioli/__main__/index
   /modules/api/geometor/pacioli/app/index
   /modules/api/geometor/pacioli/extraction/index
   /modules/api/geometor/pacioli/graphics/index
   /modules/api/geometor/pacioli/pacioli/index
   /modules/api/geometor/pacioli/parse_winterberg/index
   /modules/api/geometor/pacioli/parser/index
   /modules/api/geometor/pacioli/run_parse/index
   /modules/api/geometor/pacioli/run_winterberg_parse/index


Classes
-------

.. autoapisummary::

   geometor.pacioli.PacioliParser


Functions
---------

.. autoapisummary::

   geometor.pacioli.extract_all
   geometor.pacioli.build_graphics_index
   geometor.pacioli.clean_image
   geometor.pacioli.detect_graphics_cv
   geometor.pacioli.detect_initials
   geometor.pacioli.detect_margin_figures
   geometor.pacioli.extract_from_json


Package Contents
----------------

.. py:class:: PacioliParser(resources_dir: pathlib.Path, output_dir: pathlib.Path)

   .. py:attribute:: resources_dir


   .. py:attribute:: output_dir


   .. py:attribute:: transcribed_file


   .. py:method:: parse()

      Execute the parsing process.

      This method orchestrates the extraction of TOC and text chapters,
      merges them, and generates the RST output structure.



   .. py:method:: create_root_index(book_names: List[str])


   .. py:method:: process_book(lines: List[str], book_config: Dict)


   .. py:method:: extract_chapters(lines: List[str], start_marker: str, end_marker: str, prefix: str) -> Dict[str, Dict]

      Extract chapters from a section of lines.

      :param lines: The list of lines to process.
      :param start_marker: The string marking the start of the section.
      :param end_marker: The string marking the end of the section.
      :param prefix: The prefix for chapter headers (e.g., "Cap", "Gap").

      :returns: A dictionary of chapters keyed by Roman Numeral ID.
      :rtype: dict



   .. py:method:: merge_chapters(toc_chapters: Dict, text_chapters: Dict) -> List[Dict]

      Merge TOC and Text chapters into a single list.

      :param toc_chapters: Dictionary of chapters extracted from the TOC.
      :param text_chapters: Dictionary of chapters extracted from the text.

      :returns: A list of merged chapter dictionaries, sorted by Roman Numeral ID.
      :rtype: list



   .. py:method:: generate_rst_structure(chapters: List[Dict], output_dir: pathlib.Path)

      Generate the RST folder structure and files for the chapters.

      :param chapters: List of chapter dictionaries.
      :param output_dir: The directory where RST files will be generated.



   .. py:method:: create_main_index(chapters: List[Dict], output_dir: pathlib.Path)


   .. py:method:: create_chapter_files(chapter_dir: pathlib.Path, chapter: Dict)


   .. py:method:: indent_text(text: str, indent: str = '   ') -> str


.. py:function:: extract_all(pdf_path: pathlib.Path, output_dir: pathlib.Path, start_page: int = 1, end_page: int = 318, dpi: int = 150, max_workers: int = 6, force: bool = False) -> None

   Extract page images and text for the entire volume in parallel.


.. py:function:: build_graphics_index(directory: pathlib.Path) -> pathlib.Path

   Compile all per-folio <folio>.json files into graphics_index.json.


.. py:function:: clean_image(pil_image: PIL.Image.Image, white_point: int = 226) -> PIL.Image.Image

   Applies a linear levels adjustment to the image, mapping white_point to pure white (255).

   Effectively eliminates bleed-through, yellowed paper background, and scanning artifacts.


.. py:function:: detect_graphics_cv(image_path: pathlib.Path) -> List[Dict[str, Any]]

   Detect full-page plate graphics using OpenCV if available, falling back to SciPy.


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


.. py:function:: extract_from_json(json_path: pathlib.Path, no_clean: bool = False) -> None

   Extract all margin graphics and illuminated initial caps defined in <folio>.json.


