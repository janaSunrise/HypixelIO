import os
import re
import sys


from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks"
]

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

suppress_warnings = ["myst.header"]

extlinks = {
    'issue': ('https://github.com/janaSunrise/HypixelIO/issues/%s', 'GH-'),
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'

# -- Project information -----------------------------------------------------

project = 'HypixelIO'
copyright = '2021, Sunrit Jana'
author = 'Sunrit Jana'

version = ''

# -- Version config --
with open('../hypixelio/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
release = version

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'insegel'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'


github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'


def setup(app) -> None:  # noqa: ANN001
    app.add_config_value(
        'recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
        }, True
    )
    app.add_transform(AutoStructify)
