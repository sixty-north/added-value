===========
Added Value
===========

A Sphinx extension for embedded representations of Python object values into documentation.

Added-value allows the *values* of Python objects to be incorporated into documentation.
This is achieved by adding new roles and directives which refer to Python objects in the
code being documented, much in the same way as the standard autodoc and autosummary
extensions work.

Status
======

Build status:

.. image:: https://travis-ci.org/sixty-north/added-value.svg?branch=master
    :target: https://travis-ci.org/sixty-north/added-value

.. image:: https://readthedocs.org/projects/added-value/badge/?version=latest
    :target: http://segpy.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/sixty-north/added-value/badge.svg?branch=master
    :target: https://coveralls.io/github/sixty-north/segpy?branch=master

Installation
============

The ``added-value`` package is available on the Python Package Index (PyPI):

.. image:: https://badge.fury.io/py/added-value.svg
    :target: https://badge.fury.io/py/added-value

The package supports Python 3 only. To install::

  $ pip install added-value


What is Added Value?
====================

Added value is a plugin to the Sphinx documentation tools which adds roles and directive for
embedding the *values* of Python objects into the documentation. This allows numbers, strings,
lists and more complex data structures to be rendered as text or tables.

For full details, see the documentation.
