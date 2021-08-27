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


Role: literal-any-items – embed a series of alternative items as literals
-------------------------------------------------------------------------

To embed a series of alternative items in a sentence, use the ``:literal-any-items`` role:

::

  You must select :literal-any-items:`materials.metals` when specifying a material.

which gives:

  You must select :literal-any-items:`materials.metals` when specifying a material.


Note that ``:literal-any-items:`` uses the English "or" as the coordinating conjunction between the
final two items.  Each item is rendered by conversion to string using the string constructor
``str()`` which ultimately called the ``__str_()`` special method on the item. If you want to use
the ``repr()`` instead, do the conversion in Python code to generate a collection of strings
containing what you want.


Directive: items-list – embed collections as lists
--------------------------------------------------

Bullet lists
~~~~~~~~~~~~

The ``items-list::`` directive can be used to represent collections as lists. The ``:list-type:``
option is mandatory. For a flat bullet list, specify ``:list-types: bullet`` like this:

::

    Precious metals include:

    .. items-list:: materials.metals
       :list-types: bullet

which gives:

Precious metals include:

.. items-list:: materials.metals
   :list-types: bullet


Enumerated lists
~~~~~~~~~~~~~~~~

For an enumerated list, specify ``:list-types: enumerated``

::

    Precious metals include:

    .. items-list:: materials.metals
       :list-types: bullet

which gives:

Precious metals include:

.. items-list:: materials.metals
   :list-types: bullet

Definition lists
~~~~~~~~~~~~~~~~

Definition lists are designed to display a *term* and its definition, and so must be used with a
*mapping* type, such as a dictionary, and cannot be used with other iterable types, such as a
list or set. For example, given the dictionary:

.. literalinclude:: ../code/cal.py
   :lines: 36-49

using the follow directive,

::

    Abbreviations of months and their definitions:

    .. items-list:: cal.month_abbreviations
       :list-types: definition

we can render a definition list:

Abbreviations of months and their definitions:

.. items-list:: cal.month_abbreviations
   :list-types: definition

Sorting lists
~~~~~~~~~~~~~

The order of display of items can be controlled using the ``:sort-orders:`` option, which accepts
three values: ``asc`` for ascending natural sort, ``dec`` for descending natural sort, or ``as-is``
for displaying the values in their original order.

::

    Precious metals include:

    .. items-list:: materials.metals
       :list-types: bullet
       :sort-orders: asc

which gives:

Precious metals include:

.. items-list:: materials.metals
   :list-types: bullet
   :sort-orders: asc


Nested lists from nested data structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``items-list::`` directive can be used to represent hierarchical data structures.
Consider the following, dictionary of dictionaries of dictionaries:

.. literalinclude:: ../code/economy.py
   :language: python

When displaying, data structures with multiple levels, the type of list to be used at each level
must be specified as a comma-separated list. In this case the outer list will be a bullet list,
the intermediate lists will be enumerated lists, and the innermost lists will be definition lists:

::

    .. items-list:: economy.economic_data
       :list-types: bullet, enumerated, definition

which is displayed as:

.. items-list:: economy.economic_data
   :list-types: bullet, enumerated, definition

Notice how the dictionary keys are used for headings before each nested list.


Formatting control
~~~~~~~~~~~~~~~~~~

The formatting of lists is controlled with various additional format options.

Controlling bullets, enumerator and terms with key-formats
##########################################################

The ``:key-formats:`` option controls how bullets, enumerators and terms are displayed for bullet
lists, enumerated lists, and definition lists respectively.

::

    .. items-list:: economy.usa_economic_data
       :list-types: bullet, enumerated, definition
       :key-formats: •, i), {k}:-

.. items-list:: economy.usa_economic_data
   :list-types: bullet, enumerated, definition
   :key-formats: •, i), {k}:-

Above, the bullet list has a disc bullet, the enumerated lists use lower-case roman numerals, and
the term for the definition list is terminated by a colon and hypen.

For *bullet lists* the options are ``*``, ``+``, ``-``, ``•``, ``‣``, or ``⁃``. Note that while this information
is passed through the documentation rendering pipeline, few renderers or styles respect this option,
so it's usually easiest to stay with a asterisk ``*``.  The default is ``*``.

For *enumerated lists*, the options are arabic numerals ``1``, upper-case letters ``A``,
lower-case letters ``A``, lower-case Roman numerals ``i``, upper-case Roman numerals ``I``. These
can be combined with various prefix and suffix puncuation, so ``(A)``, ``1.`` ``i:`` are all valid.
Furthermore, the starting value can be specified with, for example, ``iv.``. The extent to which
the enumerator format is respected is very much a function of the theme or stylesheets in use, and
some popular themes, such as the Read The Docs theme, are somewhat defective in this area. The
default is ``1.``

For *definition lists*, the key-format is a string containing Python-style replacement fields
delimited by curly braces. Three replacement values are supported: ``{k}`` is the key of the
current item from the mapping; the ``{v}`` replacement field is the value of the current item from
the mapping. These may be used in any combination and the format specifiers support any options
supported by the underlying key and value types in the dictionary. The ``{o}`` replacement field
is the one-based integer ordinal *after sorting*. Any features from the Python format specifier
mini-language can be used. See the Python documentation for more details. The default is key format
for defintion lists is ``{k}``.


Controlling internal and leaf node formats
##########################################

We can consider a nested hierarchy of dictionaries to consist of *internal* nodes and *leaf*
nodes. The dictionary keys (or sequence indexes) at all levels represent the *internal* nodes,
and the values of the innermost collections represent the *leaf* nodes.

The formats of the internal nodes are controlled by the ``:internal-formats:`` option, which accepts
a comma-separated list of formats, one for each level. Each value format is a string containing
Python-style replacement fields delimited by curly braces. Three replacement values are supported:
``{k}`` is the key of the current item from the mapping, or for sequences and other iterables, a
zero-based index *before sorting*; the ``{v}`` replacement field is the value of the current item
from the collection; the ``{o}`` replacement field is the one-based ordinal integer *after sorting*.
The default *internal* format for mapping collections such as ``dict`` is ``{k}``, whereas the
default for other collections such as ``list`` is empty.

::

    .. items-list:: economy.usa_economic_data
       :list-types: bullet, enumerated, bullet
       :internal-formats: "Country: {k}", "Statistic: {k}", "Period: {k}"

.. note::

   We have used a bullet list at the third-level here, as ``:internal-format:`` has no effect on
   definition lists at the innermost level, as the corresponding ``:key-format:`` will be used
   instead to format the *term*.

.. items-list:: economy.usa_economic_data
   :list-types: bullet, enumerated, bullet
   :internal-formats: "Country: {k}", "Statistic: {k}", "Period: {k}"

The leaf-node formats are controlled with the ``:leaf-format:`` option. This accepts a single
Python style format-string containing curly-brace delimited replacements fields. Three replacement
values are supported: ``{k}`` is the key of the current item from the mapping, or for sequences and
other iterables, a zero-based index *before sorting*; the ``{v}`` replacement field is the value of
the current item from the collection; the ``{o}`` field is the integer ordinal *after sorting*.
The default *leaf* format is ``{v}``.

::

    .. items-list:: economy.usa_economic_data
       :list-types: bullet, enumerated, bullet
       :internal-formats: "Country: {k}", "Statistic: {k}", "Period: {k}"
       :leaf-format: {v:.1f}%

The leaf values are floating point numbers, and here the ``:leaf-format:`` option is used to display
those values with one decimal place and append a percentage symbol.

.. items-list:: economy.usa_economic_data
   :list-types: bullet, enumerated, bullet
   :internal-formats: "Country: {k}", "Statistic: {k}", "Period: {k}"
   :leaf-format: {v:.1f}%

By means of creative combination of these options various effects can be achieved. In this economic
dataset the innermost dictionaries each contain only one item. By using an combining the leaf value
into the *internal-format* and specifying an empty *leaf-format* the innermost structure can be
flattened:

::

    .. items-list:: economy.usa_economic_data
       :list-types: bullet, enumerated, bullet
       :key-formats: *, i., *
       :internal-formats: "Country: {k}", {k}, "{k} – {v:.1f}%"
       :leaf-format:
       :sort-orders: as-is, asc, as-is

.. items-list:: economy.usa_economic_data
   :list-types: bullet, enumerated, bullet
   :key-formats: *, i., *
   :internal-formats: "Country: {k}", {k}, "{k} – {v:.1f}%"
   :leaf-format:
   :sort-orders: as-is, asc, as-is

Using iterables and sequences with ``items-list::``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The examples so far have used nested collections which support the *Mapping* protocol, specifically
dictionaries. The ``items-list::`` directive can be used with other collections which support the
*Iterable* or *Sequence* protocols, and in any combination.

Consider the following list of lists:

.. literalinclude:: ../code/cal.py
   :lines: 51-56

Without specifying any options,

::

    .. items-list:: cal.quarter_months


this is displayed as a single-level bullet list:

.. items-list:: cal.quarter_months

Not very useful.

By specifying two list types, like this,

::

    .. items-list:: cal.quarter_months
       :list-types: bullet, bullet

we get this:

.. items-list:: cal.quarter_months
   :list-types: bullet, bullet

Notice that the *internal-format* for non-mapping types defaults to being empty, so the list indexes
not displayed.  Using the ``{o}`` format-specifier in the *internal-format* for the outer list, we
can include the one-based ordinal number in the string.

.. items-list:: cal.quarter_months
   :list-types: bullet, bullet
   :internal-formats: "Quarter {o}", ""

Indexes, keys and ordinals
~~~~~~~~~~~~~~~~~~~~~~~~~~

Various numbering systems are in play with lists of sequences, which can make things confusing.
Let's return to our list of metals:

.. literalinclude:: ../code/materials.py

This simple list contains three items at indexes zero, one and two.

We can configure an items list to display the various numbering systems in play:

::

    .. items-list:: materials.metals
       :list-types: enumerated
       :key-formats: iv.
       :leaf-format: value={v}, ordinal={o}, key={k}

.. items-list:: materials.metals
   :list-types: enumerated
   :key-formats: iv.
   :leaf-format: value={v}, ordinal={o}, key={k}

Here we have the *enumerator* values starting with Roman numeral ``iv``, the *ordinal* values
which give a one-based position in the list (for display purposes we usually want one-based indexes)
and the *key*, which is the original list index (or dictionary key).

The ordinal *always* increases from top to bottom, but the key is preserved, even if we sort the
items.

::

    .. items-list:: materials.metals
       :list-types: enumerated
       :key-formats: iv.
       :leaf-format: value={v}, ordinal={o}, key={k}
       :sort-orders: asc

.. items-list:: materials.metals
   :list-types: enumerated
   :key-formats: iv.
   :leaf-format: value={v}, ordinal={o}, key={k}
   :sort-orders: asc

The ordinal base can be modified independently using the ``ordinal-bases`` option, which defaults
to one. Here we set it to zero:

::

    .. items-list:: materials.metals
       :list-types: enumerated
       :key-formats: iv.
       :leaf-format: value={v}, ordinal={o}, key={k}
       :sort-orders: asc
       :ordinal-bases: 0

.. items-list:: materials.metals
   :list-types: enumerated
   :key-formats: iv.
   :leaf-format: value={v}, ordinal={o}, key={k}
   :sort-orders: asc
   :ordinal-bases: 0


