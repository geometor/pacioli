geometor.pacioli.parse_winterberg
=================================

.. py:module:: geometor.pacioli.parse_winterberg


Functions
---------

.. autoapisummary::

   geometor.pacioli.parse_winterberg.clean_lines
   geometor.pacioli.parse_winterberg.parse_winterberg
   geometor.pacioli.parse_winterberg.split_intro
   geometor.pacioli.parse_winterberg.split_book_into_chapters
   geometor.pacioli.parse_winterberg.extract_trailing_title


Module Contents
---------------

.. py:function:: clean_lines(lines: List[str]) -> List[str]

   Remove page artifacts and clean text.


.. py:function:: parse_winterberg()

   Parses the :person:`Winterberg <winterberg>` text file into top-level sections.


.. py:function:: split_intro(lines: List[str], output_dir: pathlib.Path)

   Splits the intro file into metadata, title page, and introduction.


.. py:function:: split_book_into_chapters(lines: List[str], output_dir: pathlib.Path, filename: str)

   Split book lines into chapter files.


.. py:function:: extract_trailing_title(lines: List[str])

   Looks for a parenthetical block at the end of lines.
   Returns (subtitle_lines, remaining_lines).
   Subtitle lines include the parentheses.


