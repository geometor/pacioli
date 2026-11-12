"""Master CLI runner executing all three *Summa* (1494) symbolic demonstrations."""

from __future__ import annotations

import sys
from pathlib import Path

_DEMOS_DIR = Path(__file__).resolve().parent
if str(_DEMOS_DIR) not in sys.path:
    sys.path.insert(0, str(_DEMOS_DIR))

import summa_geometria  # noqa: E402
import summa_proportions  # noqa: E402
import summa_quaderno  # noqa: E402


def main() -> None:
    """Run proportions, *Tractatus Geometriae*, and *Quaderno* conservation demos."""
    summa_proportions.run_demo()
    summa_geometria.run_demo()
    summa_quaderno.run_demo()


if __name__ == "__main__":
    main()
