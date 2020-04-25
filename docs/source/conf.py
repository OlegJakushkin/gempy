#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GemPy documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  4 10:28:52 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys
import warnings

import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey
import gempy

import IPython.sphinxext
from pygments.plugin import find_plugin_lexers
sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('../../gempy/plot/'))


# from unittest.mock import MagicMock
#
#
# class Mock(MagicMock):
#     @classmethod
#     def __getattr__(cls, name):
#             return MagicMock()
#
#
# MOCK_MODULES = ['IPython', 'git+git://github.com/Leguark/scikit-image@master']
# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
  #  'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',

    'sphinx_gallery.gen_gallery'
]



intersphinx_mapping = {
    'numpy': ('https://numpy.org/doc/stable/', None),
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'matplotlib': ('https://matplotlib.org/', None),
    'mayavi': ('http://docs.enthought.com/mayavi/mayavi', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}


napoleon_google_docstring = True

# nbsphinx_execute = 'never'
# nbsphinx_allow_errors = True

# autodoc_default_flags = ['members']

autodoc_default_options = {
    'autodoc_default_flags' : ['members'],
    'members': None,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}
autosummary_generate = True
autosummary_imported_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'GemPy'
year = datetime.date.today().year
copyright = u'2017-{}, CGRE-Aachen Team'.format(year)
author = 'Miguel de la Varga'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = gempy.__version__
# The full version, including alpha/beta/rc tags.
release = gempy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'python3'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Example configuration for intersphinx: refer to the Python standard library.


# -- Sphinx Gallery Options
from sphinx_gallery.sorting import FileNameSortKey

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": ["../../examples/getting_started", "../../examples/tutorials"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": 'gen_modules/backreferences',
    # Modules for which function level galleries are created.  In
    "doc_module": ("gempy", 'numpy', 'pandas', 'matplotlib'),
    "image_scrapers": ('matplotlib'),
    'first_notebook_cell': ("%matplotlib inline\n"
                            "from pyvista import set_plot_theme\n"
                            "set_plot_theme('document')"),
    'reference_url': {
        # The module you locally document uses None
        'gempy': None,
        'numpy': 'https://numpy.org/doc/stable/'

    },

}


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'alabaster'
#html_theme = 'bootstrap'
#html_theme_path = [sphinx_bootstrap_theme.get_html_theme_path()[0]+'/bootsrap']
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'github_user': 'cgre-aachen',
                        'github_repo': 'gempy',
                        'github_type': 'star',
                        'logo': './logos/gempy.png',
                        'logo_name': True,
                        'travis_button': True,
                        'page_width': '1200px',
                        'fixed_sidebar': True,
                        }


# Custom sidebar templates, maps document names to template names.
#html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}

html_sidebars = {'**': [ 'about.html', 'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_favicon = '_static/logos/favicon.ico'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GemPydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GemPy.tex', 'GemPy Documentation',
     'Miguel de la Varga, CGR-Aachen Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gempy', 'GemPy Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GemPy', 'GemPy Documentation',
     author, 'Miguel de la Varga', '3D Implicit geomodeling.',
     'Geomodelling'),
]

# Remove matplotlib agg warnings from generated doc when using plt.show
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')
