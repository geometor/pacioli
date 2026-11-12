# GEOMETOR Pacioli

A system for tracking and analyzing the works of Fra Luca Pacioli.

## Mission

To provide a structured, digital environment for studying the works of Fra Luca Pacioli, integrating text analysis with the geometric and mathematical insights found in his treatises.

## Overview

`geometor.pacioli` combines text processing with a modern terminal user interface (TUI) to facilitate the study of historical texts. It handles the ingestion, parsing, and structured display of these works.


## Key Outcomes
- **Multi-Track Book Codex of *De Divina Proportione* (`docsrc/de_divina_proportione/`)**: Complete multi-language Book Codex edition of *De Divina Proportione* (Winterberg's 1889 *Critical Introduction*, Part I *Compendio* Cap. I–LXXI, Part II *Architectura* Prohemio & Cap. I–XX, and Appendices I–IV including Winterberg's 17 *Sachliche Anmerkungen*) with synchronized **English**, **Italiano (1509)**, **Deutsch (1889)**, **Latin / Greek (1509)**, and **Critical Notes** tracks and scholarly apparatus (`bibliography.rst`, `persons.rst`, `glossary.rst`).
- **1509 Paganini Edition Folios & Graphics**: Complete extraction, neutral-white paper normalization, and bounding-box calibration of 318 folios and 482 woodcut graphics (214 illuminated initial caps, 180 marginal geometric diagrams, and 88 full-page alphabet, architectural, and Leonardo da Vinci polyhedra plates) in `resources/de_divina_proportione/paganini_1509/`.
- **Multi-Track Book Codex & Symbolic Engine of *Summa* (1494) (`docsrc/summa_1494/`, `resources/summa_1494/`)**: Folio-verified 4-track Book Codex (**English**, **Italiano 1494**, **Summary**, **Notes**) of *Summa de arithmetica, geometria, proportioni et proportionalita* (Venice: Paganino de' Paganini, Nov. 10–20, 1494) across 5 canonical units with 9 interactive `.euclid-graphic` vector SVGs, dedicated apparatus registries (`sources_manifest.json`, `concordance.json`, `persons.json`, `citations.json`, `glossary.json`), exact `SymPy` / `geometor.model` modules, `pytest` unit suite, and CLI demonstrations (`demos/`).

## Key Modules
-   `proportions.py`: Exact Boethian five-genus ratio taxonomy, Euclidean six *modi arguendi*, semicircle construction of arithmetic/geometric/harmonic means (`Part I, Dist. VI, fol. 73v`), and Euclid `II.11` extreme-and-mean division of $10$ (`XIII.1`).
-   `tractatus_geometriae.py`: Exact `geometor.model` constructions (`auto_intersect=False`, `@proposition`) for Heron's `(13, 14, 15)` triangle (`Part II, fol. 9v`), *De divisione superficierum*, Cossic quadratic gnomons (`Part I, fols. 145r–146r`), Archimedes's $96$-gon circle bounds (`fol. 31r`), and regular/Archimedean solids inscribed in a sphere (`fols. 68v–70r`).
-   `ledger_conservation.py`: Exact Venetian `l. s. g. p.` money-of-account arithmetic, `Per // A` double-entry ledger conservation ($F^T = -F$), *Cassa* non-negativity, *Bilancio del Libro*, and *Problem of Points* (`fol. 197r`).
-   `svg_woodcut.py`: Exact symbolic generator for the 9 theme-adaptive `.euclid-graphic` SVGs in `docsrc/summa_1494/`.
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
