===============
Series of Items
===============

Series of values (*e.g.* Python lists, tuples and other iterables) may be incorporated into the
documentation using the roles described below.

Role: any-items – embed a series of alternative items
-----------------------------------------------------

For example:

::

  You must select :any-items:`materials.metals` when specifying a material.

which gives:

  You must select :any-items:`materials.metals` when specifying a material.


Note that ``:any-items:`` uses the English "or" as the coordinating conjunction between the final
two items.


Role: all-items - embed a series of non-contrasting items
---------------------------------------------------------

On the other hand ``:all-items:`` uses the English word "and" between the final two items:

::

    Precious metals include :all-items:`materials.metals`.

which gives:

    Precious metals include :all-items:`materials.metals`.

