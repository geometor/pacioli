geometor.pacioli.extraction
===========================

.. py:module:: geometor.pacioli.extraction

.. autoapi-nested-parse::

   Module for extracting folios (images, text, manifests) from De Divina Proportione scans.



Attributes
----------

.. autoapisummary::

   geometor.pacioli.extraction.DEFAULT_PDF_PATH
   geometor.pacioli.extraction.DEFAULT_OUTPUT_DIR
   geometor.pacioli.extraction.EDITION_SECTIONS


Functions
---------

.. autoapisummary::

   geometor.pacioli.extraction.ensure_dir
   geometor.pacioli.extraction.extract_single_image
   geometor.pacioli.extraction.extract_single_text
   geometor.pacioli.extraction.extract_all
   geometor.pacioli.extraction.generate_manifest
   geometor.pacioli.extraction.generate_sections_index
   geometor.pacioli.extraction.main


Module Contents
---------------

.. py:data:: DEFAULT_PDF_PATH

.. py:data:: DEFAULT_OUTPUT_DIR

.. py:data:: EDITION_SECTIONS

.. py:function:: ensure_dir(path: pathlib.Path) -> None

   Ensure directory exists.


.. py:function:: extract_single_image(pdf_path: pathlib.Path, page_num: int, output_dir: pathlib.Path, dpi: int = 150, force: bool = False) -> pathlib.Path

   Extract a single page from PDF as a PNG image.


.. py:function:: extract_single_text(pdf_path: pathlib.Path, page_num: int, output_dir: pathlib.Path, force: bool = False) -> pathlib.Path

   Extract text from a single page of PDF.


.. py:function:: extract_all(pdf_path: pathlib.Path, output_dir: pathlib.Path, start_page: int = 1, end_page: int = 318, dpi: int = 150, max_workers: int = 6, force: bool = False) -> None

   Extract page images and text for the entire volume in parallel.


.. py:function:: generate_manifest(output_dir: pathlib.Path, start_page: int, end_page: int) -> None

   Generate pages.json manifest matching the Euclid format.


.. py:function:: generate_sections_index(output_dir: pathlib.Path) -> None

   Generate sections.json index mapping sections and page ranges.


.. py:function:: main() -> None

   CLI entry point for folio extraction.


