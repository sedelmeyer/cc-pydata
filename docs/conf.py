# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'cc-pydata'
copyright = '2020, Michael Sedelmeyer'
author = 'Michael Sedelmeyer'

# The full version, including alpha/beta/rc tags
release = 'v0.1.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
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

# If using alabaster theme and hiding 'logo_name', use the 'logo' setting
# in html_theme_options, otherwise, uncomment html_logo to activate the logo
# html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html theme options for alabaster
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': 'false',
    'github_user': 'sedelmeyer',
    'github_repo': 'cc-pydata',
    'fixed_sidebar': 'false',
    'description': 'Cookiecutter PyData (cc-pydata) is a template for '
            'generating "reasonably standardized" skeletons for Python-based '
            'data science projects.',
    'badge_branch': 'master',
    'github_banner': 'true',
    'github_button': 'true',
    'travis_button': 'true',
    'show_powered_by': 'true',
    'show_relbar_bottom': 'true',
    'extra_nav_links': {
        'Find me online at sedelmeyer.net': 'https://www.sedelmeyer.net/',
        'GitHub': 'https://github.com/sedelmeyer',
        'LinkedIn': 'https://www.linkedin.com/in/sedelmeyer/'
    }
}

# -- Extension configuration -------------------------------------------------

todo_include_todos = True
