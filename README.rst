.. image:: docsrc/_static/logo.png
   :alt: GEOMETOR • pacioli Medallion
   :target: https://geometor.github.io/pacioli/
   :width: 150px
   :align: right

GEOMETOR • pacioli
==================

**Visit the Online Archive:** https://geometor.github.io/pacioli/

.. image:: docsrc/summa_1494/dist_01_dedication_arithmetica/fig_01_figurate_perfect.svg
   :alt: GEOMETOR • pacioli featured geometric construction
   :target: https://geometor.github.io/pacioli/
   :align: center

**Fra Luca Pacioli • De Divina Proportione, Summa de Arithmetica • semantic digital archive**

Mission
-------

``geometor/pacioli`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It preserves and formalizes Fra Luca Pacioli's twin Renaissance masterpieces—*De Divina Proportione* (1509), illustrated with Leonardo da Vinci's sixty polyhedral woodcut plates, and *Summa de Arithmetica, Geometria, Proportioni et Proportionalita* (1494). Through addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance across all 318 folios, and exact SymPy symbolic models, Pacioli's synthesis of Euclidean proportion, practical geometry, and algebraic method speaks directly to the wider GEOMETOR corpus.

Books in This Archive
---------------------

- `On the Divine Proportion <https://geometor.github.io/pacioli/de_divina_proportione/>`_ — *De Divina Proportione*, master treatise on the golden proportion, regular and semi-regular polyhedra illustrated with Leonardo da Vinci's sixty woodcut plates (Venice, 1509).
- `Summary of Arithmetic, Geometry, Proportions and Proportionality <https://geometor.github.io/pacioli/summa_1494/>`_ — *Summa de Arithmetica, Geometria, Proportioni et Proportionalita*, encyclopedic compendium of Renaissance arithmetic, Cossic algebra, practical geometry, proportion theory, and double-entry bookkeeping (Venice, 1494).


Repository Contents
-------------------

- ``docsrc/`` — RST documentation source, 5-track *De Divina Proportione* and 4-track *Summa* study codices compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary-source folios, 482 recalibrated 1509 Venetian woodcuts, and apparatus manifests.
- ``src/geometor/pacioli/`` — Exact SymPy engines for Boethian proportions, Euclidean solids, Venetian ledger conservation, and woodcut vector graphics.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
