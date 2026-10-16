GEOMETOR • pacioli
==================

.. image:: https://img.shields.io/github/license/geometor/pacioli.svg
   :target: https://github.com/geometor/pacioli/blob/main/LICENSE

**A system for tracking and analyzing the works of Fra Luca Pacioli.**

Overview
--------

To provide a structured, digital environment for studying the works of Fra Luca Pacioli, integrating text analysis with the geometric and mathematical insights found in his treatises.

Current Status (v0.2.0)
-----------------------
- Completed synthesis of *De Divina Proportione* (Book I) English translation.
- Extracted and indexed 202 folios and 374 woodcut diagrams and polyhedra from the 1509 Paganini edition.
- Implemented automated computer vision extraction pipeline (``pacioli-extract``, ``pacioli-graphics``).

Features
--------

- **Folio & Graphic Ingestion**: High-resolution folio rendering and computer vision graphic extraction for the 1509 Paganini edition.
- **Text Parsing**: Tools to digest and structure Pacioli's writings.
- **TUI Interface**: A Textual-based interface for interactive exploration.
- **Analysis**: Foundations for analyzing the geometric and accounting principles within the works.

Installation
------------

.. code-block:: bash

    pip install geometor-pacioli

Usage
-----

.. code-block:: bash

    # Launch the TUI
    pacioli

Resources
---------

- **Source Code**: https://github.com/geometor/pacioli
- **Issues**: https://github.com/geometor/pacioli/issues
