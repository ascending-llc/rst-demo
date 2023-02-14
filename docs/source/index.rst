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
  for the codebase. See :doc:`apidoc/modules` under the **API** section as an example.

* We can also use ``Sphinx`` to "build" the :abbr:`rst (reStructuredText)` based documentations and API docs into
  a set of static ``HTML`` pages and host them on Confluence, GitHub Pages, `Read the Docs <https://readthedocs.org/>`_,
  or any other hosting alternatives.

* There is also the option of building into printable formats such as ``LaTeX`` and ``ePub``.

For demonstration purpose, we use :abbr:`rst (reStructuredText)` to document an existing 
`public project <https://github.com/xueke477/scaffold>`_ on GitHub. The public project provides a Python package
and CLI executable named ``scaffold`` that helps its users bootstrap a new Python project in the "src layout".

.. toctree::
   :maxdepth: 2
   :caption: Demo Project

   project

.. toctree::
   :maxdepth: 3
   :caption: API

   apidoc/modules
