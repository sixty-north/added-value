=========================
Embedding Series of Items
=========================

Series of values (*e.g.* Python lists, tuples and other iterables) may be incorporated into the
documentation using the roles described below.

For the examples below, assume the existence of a Python module called ``materials`` with the
following contents:

.. literalinclude:: ../code/materials.py

Role: any-items – embed a series of alternative items
-----------------------------------------------------

To embed a series of alternative items in a sentence, use the ``:any-items`` role:

::

  You must select :any-items:`materials.metals` when specifying a material.

which gives:

  You must select :any-items:`materials.metals` when specifying a material.


Note that ``:any-items:`` uses the English "or" as the coordinating conjunction between the final
two items.  Each item is rendered by conversion to string using the string constructor ``str()``
which ultimately called the ``__str__()`` special method on the item.


Role: all-items - embed a series of non-contrasting items
---------------------------------------------------------


To embed a series of non-contrasting items in a sentence, use the ``:all-items`` role:

::

    Precious metals include :all-items:`materials.metals`.

which gives:

    Precious metals include :all-items:`materials.metals`.

Note that ``:all-items:`` uses the English "and" as the coordinating conjunction between the final
two items.  Each item is rendered by conversion to string using the string constructor ``str()``
which ultimately called the ``__str__()`` special method on the item.
