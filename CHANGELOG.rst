0.3.2 (2026-10-29)
------------------

*   Enabled intersphinx cross-referencing to ``geometor/euclid`` across all Euclid proposition, definition, postulate, and common-notion citations (``:just:`` and ``:ref:``):
    *   Added ``resources/de_divina_proportione/enunciations.json`` combining all 642 Euclid Books I–XIII enunciations with Campanus/Hypsicles Books XIV and XV propositions (``XIV.1``–``XIV.10``, ``XV.1``–``XV.12``) for rich hover tooltips.
    *   Expanded rubric-style ``.. assertion::`` step headings in ``scripts/build_docsrc.py`` so inline ``:just:`` roles render as individual interactive intersphinx links to ``https://geometor.github.io/euclid/``.

0.3.1 (2026-10-29)
------------------

*   Integrated Constantin Winterberg's 1889 critical commentary (*Quellenschriften für Kunstgeschichte*, Vienna, 1889) across the Book Codex:
    *   Added Winterberg's *Vorwort & Einleitung* (Preface and Historical-Mathematical Introduction, pp. III–V, 1–15) in synchronized **English** and **Deutsch (1889)** companion tracks (`docsrc/de_divina_proportione/intro/intro_en.rst`, `intro_de.rst`).
    *   Added **Appendix IV: Winterberg's Substantive Mathematical Notes (*Sachliche Anmerkungen* 1–17, pp. 338–352)** (`docsrc/de_divina_proportione/plates/anmerkungen_en.rst`, `anmerkungen_de.rst`), including restored algebraic proofs of the Thirteen Effects, the refutation of Pacioli's Chapter XLVI claim on inscribing the octahedron in the icosahedron, and the polar-reciprocity treatise classifying all 21 mutual inscriptions of the five Platonic solids.
    *   Injected Winterberg's 17 *Sachliche Anmerkungen* and philological chapter footnotes directly into the corresponding `_notes.rst` tracks across Part I (*Compendio*) and Part II (*Architectura*), plus Alphabet plate footnotes on Letters **H**, **N**, and **S**.

0.3.0 (2026-10-29)
------------------

*   Restructured ``docsrc/de_divina_proportione/`` as a ``photon_platform.publish`` Book Codex (``:layout: book``) with synchronized companion language tracks (**English**, **Italiano 1509**, **Deutsch 1889**, **Latin / Greek 1509**, and **Critical Notes**) and track-preserving ``Prev`` / ``Next`` navigation.
*   Built scholarly apparatus registries and RST index pages (``bibliography.rst`` with 113 cited loci, ``persons.rst`` with 98 historical persons, and ``glossary.rst`` with 160 technical terms) with interactive ``:cite:``, ``:person:``, ``:term:``, ``:just:``, and ``:g:`` cross-references across all 318 folios and chapters.
*   Upgraded ``clean_image()`` in ``geometor.pacioli.graphics`` to normalize aged paper and gutter shadows into pure neutral white while preserving woodcut ink and red rubrication on Folios ``0005`` and ``0311``.
*   Recalibrated all 482 woodcut graphics across the 1509 Paganini edition (214 illuminated initial caps, 180 marginal geometric diagrams, and 88 full-page alphabet, architectural, and Leonardo polyhedra plates), removing 28 false-positive detections and mapping initials and diagrams to their exact chapters.

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
