.. Added Value documentation master file, created by
   sphinx-quickstart on Tue Jun  5 19:36:38 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Added Value
===========

Added Value is a tool which makes it easy to embed *values* extracted from Python modules in Sphinx
documentation. This allows important constants, collections and tables to have a *single source of
truth* in the software, so that documentation always faithfully represents the underlying values
used by the software.  Uses of Added Value are not specific to documenting source code, although it
can help in that task in conjunction with Sphinx' tools for such at the roles and directives in the
Python, and other language domains.

Some Quick Examples
===================

Using added value we can extract the value of pi from the Python Standard Library ``math`` module,
and embed it in a sentence, using Added Values's ``format`` role:

::

    The ratio of the circumference to the diameter of a circle is :format:`math.pi, .3f` to three
    decimal places.

Which gives:

    The ratio of the circumference to the diameter of a circle is :format:`math.pi, .3f` to three
    decimal places.

Added value is powerful, and allows lists, dictionaries, and even complex data structures such as
lists of lists of dictionaries to be rendered into text in various ways. Consider the following
dictionary of dictionaries of dictionaries:

.. literalinclude::  ../code/economy.py

Using Added Value's ``items-table`` directive, we can embed this into the documentation as a table:

::

   .. items-table:: economy.economic_data
      :title: **Economic Data**
      :v-level-indexes: 0
      :h-level-indexes: 1, 2
      :header-rows: 2
      :stub-columns: 1

which when rendered, looks like this:

.. items-table:: economy.economic_data
   :title: **Economic Data**
   :v-level-indexes: 0
   :h-level-indexes: 1, 2
   :header-rows: 2
   :stub-columns: 1


Reference Documentation
=======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   single_items
   series_of_items
   tables

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
