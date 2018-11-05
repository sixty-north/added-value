======
Tables
======

Directive: items-table – embed sequences and mappings as tables
===============================================================

Added value includes powerful facilities for creating tabular presentations of single- and
multi-dimensional data structures, such as lists of lists and lists of dictionaries. We'll start
with a few basic examples of the ``items-table::`` directive, before explaining all various
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
~~~~~~~~~~~~~~~~~~~~~~~~

Arbitrarily nested combinations of sequences and mappings (*e.g.* lists and dictionaries).

.. literalinclude:: ../code/elements.py
   :language: python
   :lines: 6-32

This is how we would refer to that table using an ``items-table::`` directive:

::

  .. items-table:: elements.elements

which will be rendered like this:

.. items-table:: elements.elements


Projecting multi-level data structures into tables
--------------------------------------------------

Data structures such a list-of-lists or list-of-dictionaries can be considered as being
*multi-level*. For example, a list of integers is a single-level data
structure, a list of list of integers is a two-level data structure, and a list of lists of lists
is a three- level data structure. Each of these levels can be given a zero-based indexed, called the
*level index*. So in the case of a list of lists of dictionarues, the outer list has indexes at
level zero, the inner lists have indexes at level one, and the dictionaties contained within those
inner lists have indexes at level two.

One easy way to see this is to think about how many successive applications of Python's indexing
operator are required to access an item.


::

                                     ┌────────── level 0 (outer list index)
                                     │   ┌────── level 1 (inner list index)
                                     │   │    ┌─ level 2 (dictionary key)
                                     │   │    │
   item = list_of_lists_dictionaries[12][32]["red"]


Tables can be no more than two dimensional, so when projecting multi-level data structures into a
table some decisions have to be be made. By default, even levels are projected to the vertical axis
of the table, and odd levels are projected to the horizontal axis of the table. This works well for
the common cases of single level and double-level data structures.  For more than two levels, it
will likely to necessary to exercise greater control over which levels are projected onto which
table axes using options to the ``items-table::`` directive.


Options to control items-table
------------------------------

The ``items-table::`` directive support the following options:

:header-rows: The number of leading rows to be formatted as the header.
:stub-columns: The number of leading columns to be formatted as header.
:header: A comma-separated list of strings to be used as a header row.
:widths: A comma-separated list of column widths
:title: A title for the table.
:v-level-indexes: A comma-separated list of level indexes for the vertical axis of the table (row
    indexes). Defaults to even level indexes. Must be disjoint with h-level-indexes.
:h-level-indexes: A comma-separated list of level indexes for the horizontal axis of the table
    (column indexes). Defaults to odd level indexes. Must be disjoint with v-level-indexes.
:v-level-visibility: A comma-separated list of ``true`` or ``false`` values controlling index
    visibility for the vertical axis of the table. Useful for hiding unwanted sequence indexes.
:h-level-visibility: A comma-separated list of ``true`` or ``false`` values controlling index
    visibility for the horizontal axis of the table. Useful for hiding unwanted sequence indexes.
:h-level-titles: A comma-separated list of names to be associated with each level for the horizontal
    axis of the table (column indexes).
:v-level-titles: A comma-separated list of names to be associated with each level for the vertical
    axis of the table (column indexes).
:v-level-sort-orders: A comma-separated list of ``asc``, ``dec`` or ``as-is`` values, controlling
    whether the corresponding indexes are sorted in ascending natural order, descending natural order, or taken as-is.
:h-level-sort-orders: A comma-separated list of ``asc``, ``dec`` or ``as-is`` values, controlling
    whether the corresponding indexes are sorted in ascending natural order, descending natural
    order, or taken as-is.
:cell-formats: TODO


Examples
--------

Specify the number of header rows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``:header-rows:`` option to specify the number of leading rows of the table which are to be
considered as column headers:

::

  .. items-table:: elements.elements
     :header-rows: 1

which will be rendered like this:

.. items-table:: elements.elements
   :header-rows: 1

The exact style of header rows depends on the theme in use.


Specify the number of stub columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``:stb-columms:`` option to specify the number of leading columns of the table which are to
be considered as row headers:

::

  .. items-table:: elements.elements
     :stub-columns: 1

which will be rendered like this:

.. items-table:: elements.elements
   :stub-columns: 1

The exact style of stub columns depends on the theme in use.


Control the assignment of level indexes to tables axes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default even-numbered levels are projected on to the vertical tables axis, and odd-numbered
levels projected to horizontal table axis. To gain more control over which levels of the data
structure are projected onto which table axis, use the ``:v-level-indexes`` and ``:h-level-indexes``
options to the ``items-table::`` directive.

Consider the following three-level economic data stored in a dictionary of dictionaries of
dictionaries:

.. literalinclude:: ../code/economy.py
   :language: python

The default view is equivalent to this, with even-numbered ``:v-level indexes:``, and odd-numbered
``:h-level-indexes:``:

::

  .. items-table:: economy.economic_data
     :v-level-indexes: 0, 2
     :h-level-indexes: 1

which will be rendered like this:

.. items-table:: economy.economic_data
   :v-level-indexes: 0, 2
   :h-level-indexes: 1


.. note::

   Tables cells for which there is no corresponding data will be left empty.

A more useful presentation would be to put only the country (level zero) on the vertical table axis,
and both catgeory and timing information on the horizontal axis:

::

  .. items-table:: economy.economic_data
     :v-level-indexes: 0
     :h-level-indexes: 1, 2

which will be rendered like this:

.. items-table:: economy.economic_data
   :v-level-indexes: 0
   :h-level-indexes: 1, 2





Hide a level of indexes
~~~~~~~~~~~~~~~~~~~~~~~

Particularly when dealing with sequences (*e.g.* lists) of data, we don't wish to see the zero-based
indexes. To disable