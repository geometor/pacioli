"""
Tools for parsing and processing "De Divina Proportione" by Luca Pacioli.

Key Components:
---------------
- **Parser**: The :class:`PacioliParser` class extracts chapters and content from the transcribed text.
- **Execution**: The `run_parse.py` script executes the parsing process.

Usage:
------
Initialize :class:`PacioliParser` with resources and output directories, then call `parse()`.
"""
from __future__ import annotations

from .parser import PacioliParser

__all__ = [
    "PacioliParser",
]
__author__ = "PHOTON platform"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.2"
__licence__ = "MIT"
