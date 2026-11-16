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
org_name = "GEOMETOR"

repo = "pacioli"
repo_name = "pacioli"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

site_title = "Fra Luca Pacioli"
html_static_path = ["_static"]
html_css_files = [*globals().get("html_css_files", []), "css/custom.css"]

autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]

# Restrict intersphinx_mapping strictly to offline local inventories present on disk:
for _key in list(intersphinx_mapping.keys()):  # noqa: F405
    _entry = intersphinx_mapping[_key]  # noqa: F405
    _target = _entry[1] if isinstance(_entry, tuple) and len(_entry) >= 2 else None
    _local_file = _target[0] if isinstance(_target, tuple) and _target else _target
    if not (isinstance(_local_file, str) and Path(_local_file).is_file()):
        intersphinx_mapping.pop(_key, None)  # noqa: F405

if "intro.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("intro.rst")  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

