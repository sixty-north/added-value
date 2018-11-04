======
Tables
======

Directive: items-table - embed sequences and mappings as tables
===============================================================

Added value includes powerful facilities for creating tabular presentations of single- and
multi-dimensional data structures, such as lists of lists and lists of dictionaries. We'll start
with a few basic examples of the ``items-table::` directive, before explaining all various
configuration options.

Basic Examples
--------------

Table from a list
~~~~~~~~~~~~~~~~~

Python sequences, such as a lists, can be represented as tables. Consider the following Python
data structure, which is a list of strings containing the names of the days of the week:

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 3

This is how we would refer to that table using an ``items-table::`` directive:

::

  .. items-table:: cal.days_of_the_week

which will be rendered like this:

.. items-table:: cal.days_of_the_week

Notice that the list indexes are included in the table data.


Table from a dictionary
~~~~~~~~~~~~~~~~~~~~~~~

Python mappings, such as a dictionaries, can be represented as a tables. Consider the following
Python data structure, which is a dictionary mapping the names of the months as strings, to the
number of days in those months as an integer:

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 13-26

This is how we would refer to that table using an ``items-table::`` directive:

::

  .. items-table:: cal.month_lengths

which will be rendered like this:

.. items-table:: cal.month_lengths

Notice that the dictionary keys are included in the table data.


Table from list of lists
------------------------

Arbitrarily nested combinations of sequences and mappings (*e.g.* lists and dictionaries).

.. literalinclude:: ../code/elements.py
   :language: python
   :lines: 6-32

This is how we would refer to that table using an ``items-table::`` directive:

::

  .. items-table:: elements.elements

which will be rendered like this:

.. items-table:: elements.elements