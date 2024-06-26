# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Virtual Brain Lab'
copyright = '2022 - Present, Daniel Birman'
author = 'Daniel Birman, Kenneth Yang'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    "nbsphinx",
    "sphinx_gallery.load_style"
]

# nbsphinx settings
nbsphinx_execute = 'never'  # Set to 'never' to avoid notebook execution
nbsphinx_allow_errors = True  # Allow notebooks with errors to be included

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['urchin/tutorials/urchin-examples/allen_institute/*',
    'urchin/tutorials/urchin-examples/bwm_coverage/*',
    'urchin/tutorials/urchin-examples/gallery/*',
    'urchin/tutorials/urchin-examples/histology/*',
    'urchin/tutorials/urchin-examples/ottenheimer_hjor_bowen_2022/*',
    'urchin/tutorials/urchin-examples/repro_ephys/*',
    'urchin/tutorials/urchin-examples/samuel/*',
    'urchin/tutorials/urchin-examples/shaker_2023/*',
    'urchin/tutorials/urchin-examples/steinmetz_2019/*',
    'urchin/tutorials/urchin-examples/yu_2023/*']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Include your custom CSS file
html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = '_static/favicon.ico'

# -- Options for autosummary and autodoc ------------------------------------
autosummary_generate = True
# Don't add module names to function docs
add_module_names = False

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'show-inheritance': False
}