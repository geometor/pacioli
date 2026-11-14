:navigation: header
:order: 25
:nav_title: Demos

.. _demos-index:

Symbolic Demonstrations
=======================

Executable Python 3.13 CLI demonstrations backed by :mod:`sympy` and :mod:`geometor.model`
for :person:`Fra Luca Pacioli's <pacioli>` *Summa de arithmetica, geometria, proportioni et proportionalita*
(Venice, 1494) and *De Divina Proportione* (Venice, 1509).

Run any demonstration inside the offline ``uv`` environment:

.. code-block:: bash

   uv run --no-sync python demos/summa_proportions.py
   uv run --no-sync python demos/summa_geometria.py
   uv run --no-sync python demos/summa_quaderno.py

.. toctree::
   :maxdepth: 1
   :caption: Runnable Demonstrations

   summa_proportions
   summa_geometria
   summa_quaderno
   demo