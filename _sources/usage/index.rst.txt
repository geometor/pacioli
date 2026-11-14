:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive GEOMETOR Digital Edition

Welcome to the GEOMETOR critical digital edition of Fra Luca Pacioli's *De Divina Proportione* (1509) and *Summa de Arithmetica, Geometria, Proportioni et Proportionalita* (1494). This edition integrates high-resolution incunable folios, recalibrated Renaissance woodcut graphics, and synchronized multilingual parallel translations.

Reader's Guide
--------------

Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every chapter and canonical unit in the Book Codices provides synchronized companion tracks selectable from the book header bar:

* **De Divina Proportione Tracks**: Switch seamlessly between:
  
  1. **English**: Unabridged modern English translation equipped with Euclidean justification pills (``:just:``), geometric highlights (``:g:``), and diplomatic line markers.
  2. **Italiano (1509)**: Diplomatic transcription of the original Renaissance Italian *volgare* printed by Paganino de' Paganini in Venice.
  3. **Deutsch (1889)**: Constantin Winterberg's landmark German critical translation (*Quellenschriften für Kunstgeschichte*).
  4. **Notes**: Historical, philological, and mathematical commentary including Winterberg's *Sachliche Anmerkungen*.

* **Summa (1494) Tracks**: Switch between **English**, **Italiano (1494)**, **Summary** (symbolic algebraic signatures and conservation laws), and **Notes** (tracing Pacioli's classical, Arabic, and medieval sources).

Primary-Source Folio Milestones & Archival Scans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The edition indexes hundreds of primary incunable folios:

* Click any marginal **[f. N]** or **[p. N]** milestone link within the text to reference the corresponding page in the primary witness.
* Click the **Folio** badge in the header bar to inspect the uncropped high-resolution scan from the 1509 Venice Paganini edition or 1494 *Summa*.

Renaissance Woodcuts & Interactive Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Over **482 recalibrated woodcut illustrations** and vector diagrams are integrated into the reading experience:

* **Leonardo da Vinci's Polyhedra**: High-resolution, dual-theme transparent renderings of Leonardo's sixty perspective solids (Plates I–LIX), available in both solid (*vacui*) and hollowed-out skeletal (*pertusati*) views.
* **Marginal Figures & Initial Letters**: Recalibrated Venetian woodcuts with dynamic dark/light mode optimization.
* **Interactive Geometry (``:g:``)**: In the *Summa*, interactive ``.euclid-graphic`` SVGs highlight corresponding geometric lines, points, and surfaces on hover.

Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The site-wide search index provides rapid full-text discovery across English, Italian, Latin, and German texts:

* Enter queries in the search field to find mathematical concepts, historical names, or bookkeeper's terminology.
* Search results link directly to matched passages and automatically highlight search terms in yellow (``?highlight=``).

Taxonomy, Facets & Collection Layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Browse the corpus by structural classifications and thematic facets:

* **Sidebar Facets**: Filter chapters and documents by category, topic tag, or document type.
* **Collection View Toggles**: On collection index pages, switch easily between **Cards**, **Banners**, and **List** views using the interactive view buttons.

Scholarly Apparatus Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interactive popups annotate entities throughout the text:

* Hover over any :person:`person name` to view dates, roles, and historical biographies.
* Hover over any :cite:`citation` to preview bibliographic information and source locus.
* Hover over any :term:`glossary term` for historical Italian and Latin definitions.
* Use the **Theme Toggle** button in the upper header to switch between light and dark modes.

CLI & Build Pipeline
--------------------

For researchers and contributors running ``geometor.pacioli`` tools locally:

.. code-block:: bash

   # Extract high-resolution folio pages from archival PDFs
   pacioli-extract

   # Detect, normalize, and crop woodcut graphics across the 1509 Paganini folios
   pacioli-graphics
   python3 scripts/recalibrate_graphics.py

   # Build apparatus registries (citations.json, persons.json, glossary.json)
   python3 scripts/build_apparatus_registry.py

   # Build the Sphinx HTML documentation
   publish build

Guides & Demos
--------------

.. collection::
   :sort: order
