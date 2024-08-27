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


# -- Project information -----------------------------------------------------

project = 'AI Vision Library Documentation'
copyright = '2024, Griffin Thompson'
author = 'Griffin Thompson'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.todo',  # Support for todo items
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'  # Using Read the Docs theme for better navigation

# Theme options to customize the look and feel
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'style_nav_header_background': '#003366',  # Dark blue header background
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS file
html_css_files = [
    'custom.css',  # Your custom styles
]

# -- Extension configuration -------------------------------------------------

# Enable todo directives
todo_include_todos = True

# Autodoc options
autodoc_member_order = 'bysource'

# Napoleon settings for NumPy and Google style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# -- Custom options ----------------------------------------------------------

# Add a favicon to the documentation
html_favicon = '_static/favicon.ico'

# Add a custom logo
html_logo = '_static/images.png'

# Modify the sidebar
html_sidebars = {
    '**': [
        'globaltoc.html',  # Global table of contents
        'relations.html',  # Previous/Next links
        'sourcelink.html',  # Link to the source code
        'searchbox.html',  # Search box
    ]
}
