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
from .extraction import extract_all
from .graphics import clean_image, detect_graphics_cv, extract_from_json

__all__ = [
    "PacioliParser",
    "extract_all",
    "clean_image",
    "detect_graphics_cv",
    "extract_from_json",
]
__version__ = "0.1.0"
