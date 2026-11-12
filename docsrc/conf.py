"""Sphinx configuration for GEOMETOR Pacioli."""
from __future__ import annotations

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403
import geometor.pacioli as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "geometor"

repo = "pacioli"
repo_name = "pacioli"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405
