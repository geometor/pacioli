geometor.pacioli.parser
=======================

.. py:module:: geometor.pacioli.parser


Classes
-------

.. autoapisummary::

   geometor.pacioli.parser.PacioliParser


Module Contents
---------------

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


