# GEOMETOR Pacioli

A system for tracking and analyzing the works of Fra Luca Pacioli.

## Mission

To provide a structured, digital environment for studying the works of Fra Luca Pacioli, integrating text analysis with the geometric and mathematical insights found in his treatises.

## Overview

`geometor.pacioli` combines text processing with a modern terminal user interface (TUI) to facilitate the study of historical texts. It handles the ingestion, parsing, and structured display of these works.


## Key Outcomes
- **Multi-Track Book Codex (`docsrc/de_divina_proportione/`)**: Complete multi-language Book Codex edition of *De Divina Proportione* (Winterberg's 1889 *Critical Introduction*, Part I *Compendio* Cap. I–LXXI, Part II *Architectura* Prohemio & Cap. I–XX, and Appendices I–IV including Winterberg's 17 *Sachliche Anmerkungen*) with synchronized **English**, **Italiano (1509)**, **Deutsch (1889)**, **Latin / Greek (1509)**, and **Critical Notes** tracks and scholarly apparatus (`bibliography.rst`, `persons.rst`, `glossary.rst`).
- **1509 Paganini Edition Folios & Graphics**: Complete extraction, neutral-white paper normalization, and bounding-box calibration of 318 folios and 482 woodcut graphics (214 illuminated initial caps, 180 marginal geometric diagrams, and 88 full-page alphabet, architectural, and Leonardo da Vinci polyhedra plates) in `resources/de_divina_proportione/paganini_1509/`.

## Key Modules
-   `parser.py`: Core logic for parsing text and extracting structure.
-   `parse_winterberg.py`: Specialized parser for the Winterberg edition.
-   `extraction.py`: Extraction of high-resolution folio pages from PDF editions (`pacioli-extract`).
-   `graphics.py`: Automated detection, background normalization (`clean_image`), calibration, cropping, and indexing of woodcut illustrations (`pacioli-graphics`).
-   `scripts/recalibrate_graphics.py`: Bounding-box recalibrator and false-positive filter for all 482 woodcut graphics across the 318 Paganini folios.
-   `scripts/build_docsrc.py`: Compiler for the multi-language Book Codex (`docsrc/de_divina_proportione/`).
-   `scripts/winterberg_commentary.py`: Bilingual English/German module for Constantin Winterberg's 1889 *Vorwort & Einleitung*, 17 *Sachliche Anmerkungen*, and critical chapter/plate footnotes.
-   `scripts/build_apparatus_registry.py`: Generator for `citations.json`, `persons.json`, `glossary.json`, and `:cite:` / `:person:` / `:term:` role injection.
-   `app.py`: Entry point for the Textual-based TUI.
-   `run_parse.py`: Script for executing parse routines.

-   **Source Code**: https://github.com/geometor/pacioli
-   **Issues**: https://github.com/geometor/pacioli/issues
