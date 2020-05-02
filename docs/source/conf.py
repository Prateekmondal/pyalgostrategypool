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
import os
import sys

# package_parent_path = os.path.dirname(os.path.dirname(__file__))
# sys.path.insert(0, package_parent_path)
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'pyalgostrategypool'
copyright = '2020, AlgoBulls'
author = 'Pushpak Dagade'

# The full version, including alpha/beta/rc tags
with open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'VERSION')) as f:
    release = f.read()

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

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
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Alabaster Related Customiation
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

html_theme_options = {
    # 'logo': 'logo.svg',       # TODO: Enable this when there is a logo for this package
    # 'touch_icon': 'favicon.svg',  # TODO: Enable this when there is a logo for this package
    'description': 'Official pool of Algorithmic Trading Strategies for the AlgoBulls Platform',
    'fixed_sidebar': 'fixed',
    'logo_name': 'true',
    'show_related': 'true',
    'show_relbars': 'true',

    'extra_nav_links': {'pyalgotrading': 'https://github.com/algobulls/pyalgotrading',
                        'algobulls': 'https://algobulls.com'},
    'analytics_id': 'UA-147658856-5',
    'github_button': 'true',
    'github_user': 'algobulls',
    'github_repo': 'pyalgostrategypool',
}

# Trying a ReadtheDocs fix from - https://stackoverflow.com/questions/56336234/build-fail-sphinx-error-contents-rst-not-found
master_doc = 'index'
