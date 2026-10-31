:navigation: header
:order: 20

=====
usage
=====

``geometor.pacioli`` provides CLI tools and build scripts to extract archival folios, isolate and calibrate woodcut illustrations, compile scholarly apparatus registries, and build the 5-track Book Codex of :person:`Fra Luca Pacioli's <pacioli>` :cite:`*De Divina Proportione* <pacioli:divina-proportione>` (1509 / 1889).

CLI & Build Pipeline
--------------------

.. code-block:: bash

   # Extract high-resolution folio pages from archival PDFs
   pacioli-extract

   # Detect, normalize, and crop woodcut graphics across the 1509 Paganini folios
   pacioli-graphics
   python3 scripts/recalibrate_graphics.py

   # Build apparatus registries (citations.json, persons.json, glossary.json)
   python3 scripts/build_apparatus_registry.py

   # Compile the 5-track Book Codex into docsrc/de_divina_proportione/
   python3 scripts/build_docsrc.py

   # Build the Sphinx HTML documentation
   publish build
