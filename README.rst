GEOMETOR • pacioli
==================

.. image:: https://img.shields.io/github/license/geometor/pacioli.svg
   :target: https://github.com/geometor/pacioli/blob/main/LICENSE

**Digital critical editions, multi-language parallel translations, recalibrated Venetian woodcuts, interactive Euclidean vector graphics, and exact symbolic constructions for Fra Luca Pacioli's *Summa de Arithmetica, Geometria, Proportioni et Proportionalita* (Venice, 1494) and *De Divina Proportione* (Venice, 1509 / Vienna, 1889).**

Overview
--------

``geometor.pacioli`` provides a structured digital scriptorium and exact symbolic laboratory (`SymPy` + `geometor.model`) for studying the two Venetian masterpieces of **Fra Luca Pacioli of Borgo Sansepolcro, O.F.M. (c. 1447–1517)** printed by **Paganino de' Paganini**:

1. **Summa de Arithmetica, Geometria, Proportioni et Proportionalita (Venice, Nov. 10–20, 1494)**: A folio-verified 4-track **Book Codex** (`docsrc/summa_1494/`) spanning speculative arithmetic, syncopated Cossic algebra (*Regola dela Cosa*), Boethian and Euclidean proportion theory, the *Problem of Points*, the first printed treatise on Venetian double-entry bookkeeping (*Particularis de computis et scripturis*), practical mensuration, and regular/Archimedean stereometry—paired with 9 interactive ``.euclid-graphic`` SVGs and exact ``SymPy`` / ``geometor.model`` proof modules.
2. **De Divina Proportione (Venice, June 1, 1509 / Vienna, 1889)**: A 5-track **Book Codex** (`docsrc/de_divina_proportione/`) uniting all 318 folios and 482 recalibrated woodcuts of the 1509 *editio princeps*—including **Leonardo da Vinci's** 60 perspective polyhedra plates—with Constantin Winterberg's 1889 Vienna critical edition, powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_.

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

3. **5-Track Book Codex of *De Divina Proportione* (`docsrc/de_divina_proportione/`)**:
   - Compiles *Winterberg's Critical Introduction (1889)*, *Part I: Compendio de Divina Proportione (Cap. I–LXXI)*, *Part II: Tractato de l'Architectura (Prohemio & Cap. I–XX)*, and *Appendices I–IV* into five synchronized tracks (**English**, **Italiano 1509**, **Deutsch 1889**, **Latin / Greek 1509**, and **Critical Notes**).

4. **4-Track Book Codex & Exact Symbolic Engine for *Summa* (1494) (`docsrc/summa_1494/`, `src/geometor/pacioli/`)**:
   - Visually verified against the November 10–20, 1494 Paganini *editio princeps* across 5 canonical units with **English**, **Italiano (1494)**, **Summary**, and **Notes** tracks and dedicated apparatus registries (`resources/summa_1494/{sources_manifest,concordance,persons,citations,glossary}.json`).
   - Exact symbolic verification over ``SymPy`` and ``geometor.model`` (``auto_intersect=False``, zero floating-point coordinates):

     - ``proportions.py``: Boethian five-genus classification (*multiplex*, *superparticularis*, *superpartiens*, and compounds), Euclidean six *modi arguendi*, semicircle construction of the arithmetic/geometric/harmonic means (``fol. 73v``), and Euclid ``II.11`` division of ``10`` into :math:`\sqrt{125}-5` and :math:`15-\sqrt{125}` (``XIII.1`` identity).
     - ``tractatus_geometriae.py``: Heron ``(13, 14, 15)`` triangle with altitude ``12``, area :math:`\sqrt{7056} = 84`, inradius ``4``, and circumradius ``65/8`` (``Part II, fol. 9v``), *De divisione superficierum* parallel chords, Cossic quadratic gnomons (``Part I, fols. 145r–146r``), Archimedes's 96-gon bounds :math:`223/71 < \pi < 22/7` (``fol. 31r``), and exact edge/volume expressions for regular and Archimedean solids inscribed in a sphere of diameter ``6`` (``fols. 68v–70r``).
     - ``ledger_conservation.py``: Exact Venetian money-of-account arithmetic (``1 lira = 20 soldi = 240 grossi = 7680 piccoli``), ``Per // A`` double-entry ledger graph with skew-symmetric flow matrix :math:`F^T = -F`, *Cassa* non-negativity, *Bilancio del Libro* trial balance, and Pacioli's *Balla* (``fol. 197r``, ``2 : 1``) vs. Pascal–Fermat (``11 : 5``) stake division.
     - ``svg_woodcut.py``: Exact generator for all 9 theme-adaptive ``.euclid-graphic`` SVGs in ``docsrc/summa_1494/``.

Coordination with ``publish``
-----------------------------

- Uses `:layout: book` in `photon-platform/publish <https://github.com/photon-platform/publish>`_ for automatic companion-track detection and track-preserving `Prev` / `Next` chapter navigation across both codices.
- Uses `.. folio:: <id>` with `:initial:` to float authentic 1509 woodcut drop-caps into paragraph openings alongside marginal page/folio badges.
- Connects `:cite:`, `:person:`, and `:term:` to per-codex interactive hover cards and apparatus registries, while linking Pacioli's Euclidean citations via `intersphinx` to `geometor/euclid <https://geometor.github.io/euclid>`_ and `geometor/elements <https://geometor.github.io/elements>`_.

Installation & Usage
--------------------

.. code-block:: bash

   # Run exact symbolic unit tests and lint checks
   uv run --no-sync pytest
   ruff check src tests demos

   # Run the Summa (1494) symbolic CLI demonstrations
   uv run --no-sync python demos/summa_proportions.py
   uv run --no-sync python demos/summa_geometria.py
   uv run --no-sync python demos/summa_quaderno.py

   # Build the multi-book Sphinx site into docs/
   publish build

Resources & Related Projects
----------------------------

- **Live Edition**: https://geometor.github.io/pacioli
- **Source Code**: https://github.com/geometor/pacioli
- `GEOMETOR • euclid <https://github.com/geometor/euclid>`_ & `GEOMETOR • elements <https://github.com/geometor/elements>`_: Euclid's *Elements* and the G-Index.
- `PHOTON • publish <https://github.com/photon-platform/publish>`_: Sphinx Book Codex publishing engine and theme.
