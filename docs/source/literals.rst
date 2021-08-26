==================
Embedding Literals
==================

Directive: literal-block – embed blocks of text
===============================================

Added value includes facilities for rendering mutliline strings as blocks of text, with optional
syntax highlighting.

The directive accepts two arguments:

::

  .. literal-block:: module.data
     :language: yaml


Other options include the ``:linenos:`` flag to show line numbers:

::

  .. literal-block:: module.data
     :language: json
     :linenos:

and highlighting of optional lines using ``:highlight-lines:``:

::

  .. literal-block:: module.data
     :language: toml
     :emphasize-lines: 8, 10, 16



Basic Examples
--------------

JSON literal
~~~~~~~~~~~~

Consider the following Python data structure representing some facts about a few Nordic countries,
and the code to render it into a string as a JSON literal:

.. literalinclude:: ../code/countries.py
   :language: python3

This is how we would refer to that this JSON literal using a  ``literal-block::`` directive:

::

  .. literal-block:: countries.json_countries
     :language: json

which will be rendered like this:

.. literal-block:: countries.json_countries
   :language: json


