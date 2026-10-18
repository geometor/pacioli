GEOMETOR • pacioli
==================

.. image:: https://img.shields.io/github/license/geometor/pacioli.svg
   :target: https://github.com/geometor/pacioli/blob/main/LICENSE

**A system for tracking and analyzing the works of Fra Luca Pacioli.**

Overview
--------

To provide a structured, digital environment for studying the works of Fra Luca Pacioli, integrating text analysis with the geometric and mathematical insights found in his treatises.

Current Status
--------------

- **318 Paganini (1509) Folios & 510 Extracted Woodcuts/Initials**: High-resolution folio scans (``0001.png``–``0318.png``), 510 extracted marginal diagrams, polyhedra plates, and illuminated initial caps (``g1``, ``c1``), and structured ``<NNNN>.rst`` + ``<NNNN>.notes.rst`` files in ``resources/de_divina_proportione/paganini_1509/``.
- **Paganini (1509) ↔ Winterberg (1889) Concordance**: Complete mapping (``concordance.json``) aligning all 318 folios of the 1509 Venice edition with Constantin Winterberg's 1889 Vienna critical edition (Italian and German).
- **Multi-Track Scholarly Edition (``docsrc/``)**: Complete RST edition across all 71 chapters of Part I (*Compendio de Divina Proportione*) and 20 chapters of Part II (*Tractato de l'Architectura*) with Italian (``_it.rst``), German (``_de.rst``), complete English translation (``_en.rst``), and critical commentary (``_notes.rst``).

Textual Foundation: Why We Use Winterberg's Expanded Italian Transcription
--------------------------------------------------------------------------

The 1509 Venice *editio princeps* printed by Paganino de' Paganini uses dense Renaissance scribal and typographical abbreviations throughout the Italian text—including nasal macrons (``ō``, ``ū``, ``ē``), ``p̄`` (*pro-* / *per-*), ``q̄`` (*que-* / *qua-*), ``qđ`` (*quod*), and courtly or titular suspensions (such as ``de. v. D. celſi.`` for *de vostra Ducal celsitudine* or ``Reuereñ. P. M.`` for *reuerendissimo Padre Maestro*). Direct OCR on the 1509 letterpress produces unusable garbage because of these contractions and ligatures.

In his 1889 Vienna critical edition (*Fra Luca Pacioli: Divina Proportione*, Quellenschriften für Kunstgeschichte), **Constantin Winterberg systematically expanded all of the 1509 abbreviations while preserving Pacioli's authentic 15th-century Northern/Tuscan-Lombard Italian orthography** (``glianni``, ``commo``, ``parolle``, ``auenga``). As Winterberg notes in his *Einleitung* (``resources/de_divina_proportione/winterberg/00_intro.txt``):

    *„Die Neuausgabe der Divina proportione stellte sich zwar zunächst den Zweck, den alterthümlichen, durch Abkürzungen aller Art fast ungeniessbar gewordenen Text der früheren Ausgabe wieder lesbar zu machen und zugleich die sachlichen Mängel und Ungenauigkeiten zu berichtigen…“*

    *(“The new edition of the Divina Proportione set itself first of all the goal of making readable again the archaic text of the earlier [1509] edition, which had become almost unreadable through abbreviations of every kind, and at the same time correcting factual defects and inaccuracies…”)*

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
   * - ``cōmo``, ``habūda``, ``cōuento``, ``Fiorētino``
     - Nasal macron (``ō``, ``ū``, ``ē`` for *m/n*)
     - ``commo``, ``habunda``, ``conuento``, ``Fiorentino``
   * - ``tāti dela q̄ p̄nte līea. a. b.``
     - Multiple scribal contractions
     - ``tanti dela qui presente linea ab.``
   * - ``Illuſtre. S. Galeazzo ſfor. VI. S. Seuerino``
     - Titular suspension
     - ``Illustre Signore Galeazzo Sforza VI. San Seuerino``
   * - ``de. v. D. celſi.``
     - Courtly formula suspension
     - ``de vostra Ducal celsitudine``

By seeding our folio transcriptions (``resources/de_divina_proportione/paganini_1509/<NNNN>.rst``) from Winterberg's expanded Italian text rather than raw 1509 OCR, we gain an enormous head start: all Renaissance abbreviations are already expanded into readable Italian, leaving ``publish folio`` focused on verifying folio boundary alignment, calibrating the 510 woodcut graphics (``g1``, ``c1``), and cleaning up occasional 19th-century OCR artifacts against the 1509 scan.

Features
--------

- **Folio Review (``publish folio``)**: Interactive side-by-side review of the 1509 Paganini scans, expanded Italian folio transcriptions (``<NNNN>.rst``), transcription & graphic calibration notes (``<NNNN>.notes.rst``), and woodcut/initial crops (``<NNNN>.json``).
- **Folio & Graphic Ingestion**: High-resolution folio rendering and computer vision graphic extraction for the 1509 Paganini edition (``pacioli-extract``, ``pacioli-graphics``).
- **Multi-Track Sphinx Edition (``publish build`` / ``publish test``)**: Builds the de-paginated multi-language edition in ``docsrc/`` with Italian, German, English, and Commentary tracks.

Installation & Usage
--------------------

.. code-block:: bash

    # Launch the interactive Folio Reviewer on resources/de_divina_proportione/
    publish folio

    # Build and serve the multi-track Sphinx edition from docsrc/
    publish test

    # Launch the TUI
    pacioli

Resources
---------

- **Source Code**: https://github.com/geometor/pacioli
- **Issues**: https://github.com/geometor/pacioli/issues

