
0.2.0 (2026-10-16)
------------------

*   Added high-resolution folio extraction for the 1509 Paganini edition of *De Divina Proportione* (`pacioli-extract`).
*   Implemented automated woodcut diagram and polyhedron detection, bounding-box calibration, and image cropping via OpenCV (`pacioli-graphics`).
*   Extracted all 202 folios and 374 graphics with structured JSON manifests (`<folio>.json` and centralized `graphics_index.json`).
*   Removed legacy inverted graphics in favor of standardized light-mode digital assets.
*   Added CLI commands `pacioli-extract` and `pacioli-graphics`.

0.1.0 (2025-12-10)
------------------

*   Synthesized English translations of *De Divina Proportione* (Book I) Chapters I-LXXI.
*   Implemented `winterberg-parser` to process the 1896 Winterberg bilingual edition.
*   Established file structure for parsed chapters (Italian, German, English).
*   Added `winterberg_en/divina_en_2` directory for synthesized "Euclid-like" translations.
*   Added `PacioliParser` class for text extraction and cleaning.

0.0.2 (2025-??-??)
------------------
*   Initial project setup.
