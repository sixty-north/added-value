from __future__ import division

import natsort
from docutils import nodes
from docutils.nodes import Text

from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged_required, unchanged
from sphinx.ext.autosummary import import_by_name

from added_value.grammatical_conjunctions import list_conjunction
from added_value.multisort import asc, dec, as_is

KEY_FORMAT_OPTION = "key-format"
VALUE_FORMAT_OPTION = "value-format"
SORT_ORDER_OPTION = "sort-order"


_natural = natsort.natsort_keygen()

SORT_ORDERS = {"asc": asc(_natural), "dec": dec(_natural), "as-is": as_is()}


class DefinitionItemsListDirective(Directive):
    """Format a sequence as a definition list.

    """

    required_arguments = 1
    has_content = False
    option_spec = {
        KEY_FORMAT_OPTION: unchanged,
        VALUE_FORMAT_OPTION: unchanged,
        SORT_ORDER_OPTION: unchanged,
    }

    @property
    def sort_order(self):
        key = self.options.get(SORT_ORDER_OPTION, "as-is")
        if key not in SORT_ORDERS:
            raise self.error(
                "Could not interpret option {} {!r}. Value must be one of {}".format(
                    SORT_ORDER_OPTION, key, list_conjunction(list(map(repr, SORT_ORDERS.keys())), "or")
                )
            )
        return SORT_ORDERS[key]

    @property
    def key_format(self):
        text = self.options.get(KEY_FORMAT_OPTION, "{!s}")
        return text

    @property
    def value_format(self):
        text = self.options.get(KEY_FORMAT_OPTION, "{!s}")
        return text

    def render_mapping(self, mapping, key, key_format_string, value_format_string):
        keys = sorted(mapping.keys(), key=key.func, reverse=key.reverse)
        text_items = [(key_format_string.format(key), value_format_string.format(mapping[key]))
                      for key in keys]
        return text_items

    def run(self):

        obj_name = self.arguments[0]

        try:
            prefixed_name, obj, parent, modname = import_by_name(obj_name)
        except ImportError:
            raise self.error(
                "Could not locate Python object {} ({} directive).".format(obj_name, self.name)
            )

        items = self.render_mapping(
            obj,
            key=self.sort_order,
            key_format_string=self.key_format,
            value_format_string=self.value_format,
        )

        list_node = nodes.definition_list()
        for term, definition in items:

            term_node = nodes.term('', '', Text(term))

            definition_node = nodes.definition()
            definition_node += nodes.paragraph(text=definition)

            item_node = nodes.definition_list_item('', term_node, definition_node)
            list_node += item_node


        list_node["classes"] += self.options.get("class", [])
        if "align" in self.options:
            list_node["align"] = self.options.get("align")
        self.add_name(list_node)

        return [list_node]
