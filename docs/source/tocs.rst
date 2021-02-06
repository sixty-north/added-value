============================
Embedding Tables of Contents
============================

Tables of contents directives are fundamental to the way Sphinx connects otherwise separate
documents. The standard ``toctree`` directive permits hard-wired lists of linked documents with
optional titles, but it's not possible to easily generate a table of contents dynamically based on
data from a program. It is particularly useful to be able to do so with plug-in architectures so
that a program can report the location of each plugin's documentation, allowing each plug-in to
remain cohesive in the source code directory structure, rather than with documentation placed
elsewhere.

The ``items-toc`` directive allows the list of references to be retrieved from a Python object,
which must be provided as the only argument to the directive. The provided object can be an iterable
series of strings, in which case each string is treated as a reference to another page where the
title for each entry is extracted from the linked page. Alternatively it can be a mapping from page
title strings to page references.

Building a table-of-contents from a list of references
------------------------------------------------------

So given this code in ``pages.py``,

.. literalinclude:: ../code/pages.py
   :lines: 1-6


So given the directory structure and this file ``tocs.rst``::

    ├── chemistry
    │   ├── Be.rst
    │   ├── H.rst
    │   ├── He.rst
    │   └── Li.rst
    └── tocs.rst

the following ``items-toc`` directive

::

  .. items-toc:: pages.references

gives the following table of contents,

.. items-toc:: pages.references

All of the normal ``toctree`` options are supported. For example, to reverse the table of contents
and limit its depth to one, use:

::

  .. items-toc:: pages.references
     :maxdepth: 1
     :reversed:

to give,

.. items-toc:: pages.references
   :maxdepth: 1
   :reversed:

See the Sphinx documentation for ``toctree`` for a full list of the supported options.

Building a table-of-contents from a mapping of titles to references
-------------------------------------------------------------------

So given this code in ``pages.py``,

.. literalinclude:: ../code/pages.py
   :lines: 9-14


And given the same directory structure as before alogside this file ``tocs.rst``::

    ├── chemistry
    │   ├── Be.rst
    │   ├── H.rst
    │   ├── He.rst
    │   └── Li.rst
    └── tocs.rst

the following ``items-toc`` directive

::

  .. items-toc:: pages.titled_references

gives the following table of contents,

.. items-toc:: pages.titled_references
