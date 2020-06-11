# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#########################################################################
# NOTE: RUN NPM INSTALL JSDOC TO AVOID BUILD ERRORS
#########################################################################

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('src'))


# -- Project information -----------------------------------------------------

project = 'SANITISE.media'
copyright = '2020, Albert Ferguson, Jayden Lee, Joel Morrison, Cohen Bosworth'
author = 'Albert Ferguson, Jayden Lee, Joel Morrison, Cohen Bosworth'

# The short X.Y version.
version = '1.2'
# The full version including release/feature release/hot fix patch release
release = '1.2.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for PDF output --------------------------------------------------
extensions.append('rst2pdf.pdfbuilder') # PDF module plugin
pdf_documents = [('index', u'Final Product Proposal', project, author),]


# -- Options for HTML output -------------------------------------------------

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_logo = "_static/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

autosummary_generate = True
numfig = True
# Module names always prefix files.
# add_module_names = True
# Authors per module are shown.
show_authors = True
# Don't include TODO notes into documentation renderings.
todo_include_todos = False

# -- Enabling Extensions -----------------------------------------------------

extensions.append('sphinx_js')          # JS documentation
extensions.append('sphinx.ext.autodoc') # Python Autodoc feature enable.

# -- Setting Source Paths ----------------------------------------------------

this_path = os.path.dirname(os.path.abspath(__file__))
this_path = os.path.dirname(this_path)
this_path = os.path.dirname(this_path)

js_root = os.path.abspath(os.path.join(this_path, 'src', 'sanitise', 'src'))
js_pages = os.path.abspath(os.path.join(js_root, 'pages'))
js_components = os.path.abspath(os.path.join(js_root, 'components'))
# Paths that containg JS source code.
js_source_path = [js_root, js_pages, js_components]
js_language = "javascript" # change to Typescript if need be.
root_for_relative_js_paths = js_root

python_package_source = os.path.abspath(os.path.join(this_path, 'src', 'backend'))
