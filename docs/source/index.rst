.. scaffold documentation master file, created by
   sphinx-quickstart on Fri Feb  3 12:14:51 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Document Writing with reStructuredText
======================================

Introduction
------------

This project shows how to use `reStructuredText <https://docutils.sourceforge.io/rst.html>`_, a markup language
slightly more complex than Markdown, to document a Python project. The benefits are:

* If dosctrings of the Python code are written in :abbr:`rst (reStructuredText)`, we can use
  `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ to automatically generate API documents
  for the codebase. See :doc:`apidoc/modules` under the
  :ref:`api_doc` section as an example.

* We can also use ``Sphinx`` to "build" the :abbr:`rst (reStructuredText)` based documentations and API docs into
  a set of static ``HTML`` pages and host them on Confluence, GitHub Pages, `Read the Docs <https://readthedocs.org/>`_,
  or any other hosting alternatives.

* There is also the option of building into printable formats such as ``LaTeX`` and ``ePub``.

For demonstration purpose, we use :abbr:`rst (reStructuredText)` to document an existing 
`public project <https://github.com/xueke477/scaffold>`_ on GitHub. The public project provides a Python package
and CLI executable named ``scaffold`` that helps its users bootstrap a new Python project in the "src layout".

Hands-on
--------

To try building the docs by ``Sphinx`` for oneself, use the following steps to set up the necessary local environment.

* Git clone the Ascending-private repo at https://github.com/ascending-llc/rst-demo.

* If ``pyenv`` is used for managing Python versions, do a :command:`pyenv local ***` to pin a Python version >= 3.8

* Run :command:`poetry install` to install dependencies, and :command:`poetry shell` to activate a virtual environment.
  All subsequent steps are carried out in this virtual environment.

* Run :command:`cd docs` --- all ``Sphinx`` related operations should be done with :file:`docs` as the current working
  directory.

To actually build the documentations:

* Run :command:`sphinx-apidoc -o ./source/apidoc ../src/scaffold` to generate API documentations and place them in the
  :file:`docs/source/apidoc` folder.

* Run :command:`make clean && make html` to generate static ``HTML`` pages. Then open :file:`docs/build/html/index.html`
  with a browser to view them.

* To publish to Confluence, edit :file:`docs/source/conf.py` according to the
  `Atlassian Confluence Builder <https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/configuration/>`_
  documentation, and then run :command:`make clean && make confluence`.

Demo Project
------------

.. toctree::
   :maxdepth: 2

   project

.. _api_doc:

API Documentation
-----------------

.. toctree::
   :maxdepth: 3

   apidoc/modules
