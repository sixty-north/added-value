from __future__ import division

import re

import natsort
from docutils import nodes

from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives import unchanged_required, unchanged
from docutils.parsers.rst.states import Body
from sphinx.ext.autosummary import import_by_name

from added_value.grammatical_conjunctions import list_conjunction
from added_value.multisort import asc, dec, as_is

FORMAT_OPTION = "format"
SORT_ORDERS_OPTION = "sort-order"
ENUMERATOR_OPTION = "enumerator"


_natural = natsort.natsort_keygen()

SORT_ORDERS = {"asc": asc(_natural), "dec": dec(_natural), "as-is": as_is()}

ENUMERATOR_PATTERN = Body.patterns["enumerator"]


class EnumeratedItemsListDirective(Directive):
    """Format a sequence as an unordered list.

    The items themselves must.
    """

    required_arguments = 1
    has_content = False
    option_spec = {
        FORMAT_OPTION: unchanged,
        SORT_ORDERS_OPTION: unchanged,
        ENUMERATOR_OPTION: unchanged,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._body = Body(None)

    @property
    def sort_order(self):
        key = self.options.get(SORT_ORDERS_OPTION, "as-is")
        if key not in SORT_ORDERS:
            raise self.error(
                "Could not interpret option {} {!r}. Value must be one of {}".format(
                    SORT_ORDERS_OPTION, key, list_conjunction(list(map(repr, SORT_ORDERS.keys())), "or")
                )
            )
        return SORT_ORDERS[key]

    @property
    def format(self):
        text = self.options.get(FORMAT_OPTION, "{!s}")
        return text

    @property
    def enumerator(self):
        e = self.options.get(ENUMERATOR_OPTION, "#.")
        return e


    def render_iterable(self, iterable, key, format_string):
        items = sorted(iterable, key=key.func, reverse=key.reverse)
        text_items = [format_string.format(item) for item in items]
        return text_items

    def run(self):

        obj_name = self.arguments[0]

        try:
            prefixed_name, obj, parent, modname = import_by_name(obj_name)
        except ImportError:
            raise self.error(
                "Could not locate Python object {} ({} directive).".format(obj_name, self.name)
            )

        items = self.render_iterable(
            obj,
            key=self.sort_order,
            format_string=self.format
        )

        m = re.match(ENUMERATOR_PATTERN, self.enumerator)
        fmt, sequence, text, ordinal = self._body.parse_enumerator(m)
        print(f"fmt = {fmt}")
        print(f"sequence = {sequence}")
        print(f"text = {text}")
        print(f"ordinal = {ordinal}")

        list_node = nodes.enumerated_list()

        if sequence == '#':
            list_node['enumtype'] = 'arabic'
        else:
            list_node['enumtype'] = sequence

        list_node['prefix'] = self._body.enum.formatinfo[fmt].prefix
        list_node['suffix'] = self._body.enum.formatinfo[fmt].suffix

        if ordinal != 1:
            list_node['start'] = ordinal

        for item_text in items:
            item_node = nodes.list_item()
            list_node += item_node
            item_node += nodes.paragraph(text=item_text)

        list_node["classes"] += self.options.get("class", [])
        if "align" in self.options:
            list_node["align"] = self.options.get("align")
        self.add_name(list_node)

        return [list_node]
