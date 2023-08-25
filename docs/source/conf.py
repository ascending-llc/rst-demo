# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from importlib import import_module
from inspect import getsourcelines
from pathlib import Path

project = "reStructuredText Demo"
copyright = "2023, Ke Xue"
author = "Ke Xue"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    # "sphinx.ext.viewcode",
    "sphinx.ext.linkcode",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.confluencebuilder",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Options for autodoc extension -------------------------------------------------
autodoc_typehints = "none"
autodoc_member_order = "bysource"

# -- Options for sphinx_autodoc_typehints extension -------------------------------------------------

# -- Options for intersphinx extension -------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sceptre": ("https://docs.sceptre-project.org/4.2.2/", None),
}

# -- Options for Confluence builder -------------------------------------------------
confluence_publish = True
confluence_server_url = "https://ascending.atlassian.net/wiki/"
confluence_space_key = "ASC"
confluence_server_user = "kent.xue@ascendingdc.com"
confluence_parent_page = 141524993
# confluence_parent_page = 'reStructuredText demo'

# -- Options for sphinx-copybutton -------------------------------------------------
copybutton_prompt_text = "$ "
copybutton_line_continuation_character = "\\"
copybutton_here_doc_delimiter = "EOF"


# -- Options for sphinx.ext.linkcode -------------------------------------------------
def linkcode_resolve(domain, info):
    file_dir = Path(__file__).parent
    src_dir = file_dir.parent.joinpath("src")
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    if src_dir.joinpath(filename).is_dir():
        filename = f"{filename}/__init__"
    filename = "src/" + filename
    if "fullname" in info:
        module = import_module(info["module"])
        obj = getattr(module, info["fullname"])
        anchor = f"#L{getsourcelines(obj)[1]}"
    else:
        anchor = ""

    result = (
        f"https://github.com/ascending-llc/rst-demo/blob/master/{filename}.py{anchor}"
    )
    return result
