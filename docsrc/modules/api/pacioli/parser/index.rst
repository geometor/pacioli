pacioli.parser
==============

.. py:module:: pacioli.parser


Classes
-------

.. autoapisummary::

   pacioli.parser.PacioliParser


Module Contents
---------------

.. py:class:: PacioliParser(resources_dir: pathlib.Path, output_dir: pathlib.Path)

   .. py:attribute:: resources_dir


   .. py:attribute:: output_dir


   .. py:attribute:: transcribed_file


   .. py:method:: parse()

      Main execution method.



   .. py:method:: create_root_index(book_names: List[str])


   .. py:method:: process_book(lines: List[str], book_config: Dict)


   .. py:method:: extract_chapters(lines: List[str], start_marker: str, end_marker: str, prefix: str) -> Dict[str, Dict]

      Extracts chapters from a section of lines.
      Returns a dict keyed by Roman Numeral ID.



   .. py:method:: merge_chapters(toc_chapters: Dict, text_chapters: Dict) -> List[Dict]

      Merges TOC and Text chapters.



   .. py:method:: generate_rst_structure(chapters: List[Dict], output_dir: pathlib.Path)

      Generates the RST folder structure and files.



   .. py:method:: create_main_index(chapters: List[Dict], output_dir: pathlib.Path)


   .. py:method:: create_chapter_files(chapter_dir: pathlib.Path, chapter: Dict)


   .. py:method:: indent_text(text: str, indent: str = '   ') -> str


