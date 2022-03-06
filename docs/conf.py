# pylint: disable=invalid-name
import os
import sys

from hypixelio import __version__ as hypixelio_version

# Sphinx path setup
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

# Project info configuration
project = "HypixelIO"
copyright = "Copyright 2021-present, Sunrit Jana"  # pylint: disable=redefined-builtin
author = "Sunrit Jana"

release = hypixelio_version
branch = (
    "main"
    if hypixelio_version.endswith("a")  # noqa: W503
    or hypixelio_version.endswith("b")  # noqa: W503
    or hypixelio_version.endswith("rc")  # noqa: W503
    else "v" + hypixelio_version  # noqa: W503
)

# General configuration
extensions = [
    "myst_parser",
    "resourcelinks",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
]

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# Warnings
suppress_warnings = ["myst.header"]

extlinks = {
    "issue": ("https://github.com/janaSunrise/HypixelIO/issues/%s", "GH-"),
}

source_suffix = {".rst": "restructuredtext", ".md": "markdown", ".txt": "markdown"}

master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_STORE"]

# Links for the RST
resource_links = {
    "repo": "https://github.com/janaSunrise/HypixelIO/",
    "issues": "https://github.com/janaSunrise/HypixelIO/issues",
    "discussions": "https://github.com/janaSunrise/HypixelIO/discussions",
    "examples": f"https://github.com/janaSunrise/HypixelIO/tree/{branch}/examples",
}

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
