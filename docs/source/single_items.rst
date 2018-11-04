=====================
Embedded Single Items
=====================

Role: str – embed the string conversion of an object
----------------------------------------------------

Single values from Python code may be included in this documentation using the ``:str:`` role, like
this:

::

  The atomic weight of carbon-12 is :str:`elements.CARBON_WEIGHT`.

which gives:

  The atomic weight of carbon-12 is :str:`elements.CARBON_WEIGHT`.


The value here is a float, but any Python object which can be converted to a string using the built
string constructor ``str(obj)`` is suitable, which will ultimately invoke the ``__str__()`` special
method of the object being formatted.


Role: repr – embed the string representation of an object
---------------------------------------------------------

By using the ``:repr:`` role instead, the alternative Python string representation (usually intended
for consumption by developers) can be inserted:

::

  By passing the string key, such as :repr:`elements.SILICON_SYMBOL`, to the function the
  corresponding element name can be retrieved.

which gives:

  By passing the string key, such as :repr:`elements.SILICON_SYMBOL`, to the function the
  corresponding element name can be retrieved.

Note that the quotes now included in the string, as they are part of the representation of the
object returned by the built-in ``repr(obj)`` function, which will ultimately invoke the
``__repr__()`` special method of the object being embedded.


Role: format – embed a formatted string representation of an object
-------------------------------------------------------------------

By using the ``:format:`` role, you can gain control over the formatting of Python objects.

::

  The value of the mathematic constamt *e* is :format:`math.e, .3f` to three decimal places.

which gives:

  The value of the mathematic constamt *e* is :format:`math.e, .3f` to three decimal places.

The role accepts two items separated by a comma. The first is a reference to the object to be
embedded. The second is a format specifier. The object being embedded here is a float, but any
Python object which can be passed to the built-in ``format()`` function can be used. The allowable
values for the format specifier depend on the type of the object being formatted.