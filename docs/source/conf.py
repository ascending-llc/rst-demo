# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'reStructuredText Demo'
copyright = '2023, Ke Xue'
author = 'Ke Xue'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.confluencebuilder'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for autodoc extension -------------------------------------------------
autodoc_typehints = 'none'
autodoc_member_order = 'bysource'

# -- Options for intersphinx extension -------------------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for Confluence builder -------------------------------------------------
confluence_publish = True
confluence_server_url = 'https://ascending.atlassian.net/wiki/'
confluence_space_key = 'ASC'
confluence_server_user = 'kent.xue@ascendingdc.com'
confluence_parent_page = 141524993
# confluence_parent_page = 'reStructuredText demo'
