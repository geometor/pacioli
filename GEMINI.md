# GEOMETOR Pacioli

A system for tracking and analyzing the works of Fra Luca Pacioli.

## Mission

To provide a structured, digital environment for studying the works of Fra Luca Pacioli, integrating text analysis with the geometric and mathematical insights found in his treatises.

## Overview

`geometor.pacioli` combines text processing with a modern terminal user interface (TUI) to facilitate the study of historical texts. It handles the ingestion, parsing, and structured display of these works.


## Key Outcomes
- **Synthesized Translation**: A complete, modernized English translation of Book I (Chapters I-LXXI) in "Euclid-like" style, located in `resources/de_divina_proportione/winterberg_en/divina_en_2/`.
- **1509 Paganini Edition Graphics**: Complete extraction and indexing of 202 folios and 374 diagrams and polyhedra in `resources/de_divina_proportione/paganini_1509/`.

## Key Modules
-   `parser.py`: Core logic for parsing text and extracting structure.
-   `parse_winterberg.py`: Specialized parser for the Winterberg edition.
-   `extraction.py`: Extraction of high-resolution folio pages from PDF editions (`pacioli-extract`).
-   `graphics.py`: Automated detection, calibration, cropping, and indexing of woodcut illustrations (`pacioli-graphics`).
-   `app.py`: Entry point for the Textual-based TUI.
-   `run_parse.py`: Script for executing parse routines.



-   **Source Code**: https://github.com/geometor/pacioli
-   **Issues**: https://github.com/geometor/pacioli/issues
