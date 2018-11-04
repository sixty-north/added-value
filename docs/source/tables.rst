======
Tables
======

Standard table
==============

+-----------+------------+------------+----------+----------+
| Column    | Header     | Header 2   | Header 3 | Header 4 |
| Title     | Title      |            |          |          |
+===========+============+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+


Table from list
===============

Here is an example table made from a list:

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 1

.. items-table:: cal.days_of_the_week


Table from list of lists
========================

Here is an example table made from a list of lists:

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 3-9

.. items-table:: cal.month_of_weeks


Table from a dictionary
=======================

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 13-26

Notice that as dictionaries are unordered prior to Python 3.7, the resulting table may be in a random order.

.. items-table:: cal.month_lengths


To get a predictable order, use an ordered mapping collection, such as an ``OrderedDict``, like this:

.. literalinclude:: ../code/cal.py
   :language: python
   :lines: 28-41

.. items-table:: cal.ordered_month_lengths

Table from a dictionary with title
==================================

.. items-table:: cal.month_lengths
   :title: Month length in days

Table from a dictionary with header
===================================

.. items-table:: cal.month_lengths
   :header: Month, Length


Table from a dictionary of dictionaries
=======================================

.. items-table:: opcodes.OPCODES


Table from a dictionary of dictionaries with transposition
==========================================================

.. items-table:: opcodes.OPCODES
   :v-level-indexes: 1
   :h-level-indexes: 0


Table from a dictionary of dictionaries with transposition
==========================================================

.. items-table:: opcodes.OPCODES
   :v-level-indexes: 1
   :h-level-indexes: 0

Table from a dictionary of dictionaries with descending sort on vertical axis
=============================================================================

.. items-table:: opcodes.OPCODES
   :v-level-sort-orders: dec

Table from a dictionary of dictionaries with ascending sort on horizontal axis
==============================================================================

.. items-table:: opcodes.OPCODES
   :h-level-sort-orders: asc

Table from a dictionary of dictionaries with both levels on vertical axis
=========================================================================

.. items-table:: opcodes.OPCODES
   :v-level-indexes: 0, 1
   :v-level-sort-orders: asc, as-is

Table from a dictionary of dictionaries with both levels on vertical axis with two stub columns
===============================================================================================

.. items-table:: opcodes.OPCODES
   :v-level-indexes: 0, 1
   :v-level-sort-orders: asc, as-is
   :stub-columns: 2

Table from a dictionary of dictionaries with ascending sort on horizontal axis and one header row and one stub column
=====================================================================================================================

.. items-table:: opcodes.OPCODES
   :h-level-sort-orders: asc
   :header-rows: 1
   :stub-columns: 1


Table from a dictionary of dictionaries with both levels on vertical axis
=========================================================================

.. items-table:: opcodes.OPCODES
   :v-level-indexes: 0, 1
   :v-level-sort-orders: asc, as-is
   :v-level-visibility: show, show


Table from a stress table
=========================

.. items-table:: steel.en13445_docs
   :title: EN 13445 Material Stresses
   :header-rows: 1
   :stub-columns: 1
   :v-level-indexes: 0
   :h-level-indexes: 1
   :v-level-titles: Materials
   :h-level-titles: Temperature °C︎
   :v-level-sort-orders: as-is
   :h-level-sort-orders: asc