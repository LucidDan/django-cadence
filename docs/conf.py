# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# theme
import alabaster

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'django-cadence'
copyright = '2020, Daniel Sloan, Lucid Horizons'
author = 'Dan Sloan <dan@luciddan.com>'

# The full version, including alpha/beta/rc tags
version = '0.1.0'
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'alabaster',
#    'sitemap',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_context = {}

html_theme_options = {
    'logo_name': False,
    'code_font_family': '"SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace',
    'code_font_size': '0.8em',
    'show_related': False,
    'fixed_sidebar': False,
    'github_banner': True,
    'github_button': True,
    'github_type': 'star',
    'github_user': 'LucidDan',
    'github_repo': 'django-cadence',
}

# html_sidebars = {
#     '**': [
#         'sidebarlogo.html',
#         'navigation.html',
#         'searchbox.html',
#         'versions.html',
#         'analytics.html',
#     ]
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# intersphinx options

intersphinx_mapping = {
    'https://docs.python.org/3/': None,
}
