GEOMETOR • pacioli
==================

.. image:: https://img.shields.io/github/license/geometor/pacioli.svg
   :target: https://github.com/geometor/pacioli/blob/main/LICENSE

**Digital critical edition, multi-language parallel translations, recalibrated 1509 woodcuts, and Euclidean apparatus for Fra Luca Pacioli's *De Divina Proportione* (Venice, 1509 / Vienna, 1889).**

Overview
--------

``geometor.pacioli`` provides a structured digital scriptorium for studying the mathematical, proportional, and architectural treatises of **Fra Luca Pacioli of Borgo Sansepolcro, O.F.M. (c. 1447–1517)**, illustrated with perspective polyhedra by **Leonardo da Vinci**. It unites the 1509 Venice *editio princeps* printed by Paganino de' Paganini with Constantin Winterberg's 1889 Vienna critical edition into a 5-track **Book Codex** powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_.

Process & Pipeline
------------------

1. **Archival Folio Extraction & Woodcut Recalibration (`extraction.py`, `graphics.py`, `scripts/recalibrate_graphics.py`)**:
   - Extracts all 318 folios (`0001.png`–`0318.png`) of the 1509 Paganini edition and detects, normalizes (neutral-white paper background cleaning), and calibrates bounding boxes for **482 woodcut graphics**:
     - **214** illuminated Renaissance woodcut initial drop-caps (`c1`)
     - **180** marginal geometric diagrams (`g1`–`g6`)
     - **23** geometric Roman alphabet plates (*Alphabetum Dignissimum*)
     - **5** Vitruvian architectural and *Arbor Proportio et Proportionalitas* plates
     - **60** full-page Leonardo da Vinci polyhedra plates (*Corpora Regularia et Dependentia*, solid and *vacua* skeletal frames)

2. **Paganini (1509) ↔ Winterberg (1889) Concordance & Diplomatic Seeding**:
   - The 1509 Venice letterpress uses dense Renaissance scribal contractions (`ō`, `ū`, `ē`, `p̄`, `q̄`, `qđ`, and titular suspensions) that defeat raw OCR.
   - In his 1889 Vienna critical edition (*Quellenschriften für Kunstgeschichte*), Constantin Winterberg systematically expanded all 1509 abbreviations while preserving Pacioli's authentic 15th-century Northern/Tuscan-Lombard Italian orthography (`commo`, `parolle`, `glianni`).

   .. list-table:: Examples from Folio ``0017`` (``f. 1r``, Dedication to Ludovico Sforza)
      :header-rows: 1

      * - 1509 Paganini Print (``0017.png``)
        - Abbreviation Type
        - 1889 Winterberg Expansion (``0017.rst``)
      * - ``p̄fessoris``, ``p̄fessioni``, ``p̄ximo``
        - ``p̄`` (*pro-* / *pre-*)
        - ``professoris``, ``professioni``, ``proximo``
      * - ``p̄ſpicaciſſimi``, ``p̄cuffiōi``
        - ``p̄`` (*per-*)
        - ``perspicacissimi``, ``percussioni``
      * - ``q̄lla``, ``q̄ſte``, ``eq̄ſtre``
        - ``q̄`` (*que-* / *qua-*)
        - ``quella``, ``queste``, ``equestre``
      * - ``cōmo``, ``habūda``, ``cōuento``
        - Nasal macron (``ō``, ``ū``, ``ē``)
        - ``commo``, ``habunda``, ``conuento``
      * - ``tāti dela q̄ p̄nte līea. a. b.``
        - Multiple scribal contractions
        - ``tanti dela qui presente linea ab.``
      * - ``de. v. D. celſi.``
        - Courtly formula suspension
        - ``de vostra Ducal celsitudine``

   - By aligning all 318 folios (`concordance.json`) with Winterberg's expanded Italian transcription and German critical translation, ``publish folio`` verifies exact folio boundaries, marginal graphics, and illuminated initials against the 1509 scan.

3. **5-Track Book Codex Compilation (`scripts/build_docsrc.py`, `scripts/winterberg_commentary.py`, `scripts/build_apparatus_registry.py`)**:
   - Compiles *Winterberg's Critical Introduction (1889)*, *Part I: Compendio de Divina Proportione (Cap. I–LXXI)*, *Part II: Tractato de l'Architectura (Prohemio & Cap. I–XX)*, and *Appendices I–IV* into `docsrc/de_divina_proportione/` with five synchronized tracks:
     - **English (`_en.rst`)**: Complete modern English translation with floated 1509 woodcut initials (`.. folio:: :initial:`), marginal geometric diagrams, and Euclidean proposition cross-references.
     - **Italiano 1509 (`_it.rst`)**: Diplomatic 1509 Italian text with expanded scribal abbreviations and original woodcut placement.
     - **Deutsch 1889 (`_de.rst`)**: Constantin Winterberg's 1889 German critical translation.
     - **Latin / Greek 1509 (`_la.rst`)**: Dedicated track for chapters containing Latin epigrams, colophons, Campanus/Euclid Latin propositions, and Greek architectural etymologies.
     - **Critical Notes (`_notes.rst`)**: Bilingual English/German philological notes, Euclidean Book XIII/XIV derivations, and Winterberg's 17 *Sachliche Anmerkungen*.

Coordination with ``publish``
-----------------------------

- Uses `:layout: book` in `photon-platform/publish <https://github.com/photon-platform/publish>`_ for automatic companion-track detection (`_en`, `_it`, `_de`, `_la`, `_notes`) and track-preserving `Prev` / `Next` chapter navigation.
- Uses `.. folio:: <id>` with `:initial:` to float authentic 1509 woodcut drop-caps into paragraph openings alongside marginal page/folio badges.
- Connects `:cite:` (113 bibliographic loci), `:person:` (98 historical figures), and `:term:` (160 Renaissance mathematical/architectural terms) to interactive hover cards, while linking Pacioli's Euclidean citations via `intersphinx` to `geometor/euclid <https://geometor.github.io/euclid>`_ and `geometor/elements <https://geometor.github.io/elements>`_.

Installation & Usage
--------------------

.. code-block:: bash

   # Launch the interactive Folio Reviewer on resources/de_divina_proportione/
   publish folio

   # Rebuild apparatus registries and the 5-track Book Codex in docsrc/
   python3 scripts/build_apparatus_registry.py
   python3 scripts/build_docsrc.py

   # Build and serve the multi-track Sphinx edition locally
   publish test

Resources & Related Projects
----------------------------

- **Live Edition**: https://geometor.github.io/pacioli
- **Source Code**: https://github.com/geometor/pacioli
- `GEOMETOR • euclid <https://github.com/geometor/euclid>`_ & `GEOMETOR • elements <https://github.com/geometor/elements>`_: Euclid's *Elements* and the G-Index.
- `PHOTON • publish <https://github.com/photon-platform/publish>`_: Sphinx Book Codex publishing engine and theme.
