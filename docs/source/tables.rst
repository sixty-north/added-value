======
Tables
======

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
