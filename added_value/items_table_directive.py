import csv
from collections import Mapping

from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives import flag, unchanged_required, unchanged
from docutils.statemachine import StringList
from six import StringIO
from sphinx.ext.autosummary import import_by_name

from added_value.non_string_iterable import NonStringIterable
from added_value.tabulator import tabulate, is_rectangular, size
from added_value.util import pad


class ItemsTableDirective(Directive):
    """Format a sequence as a table.

    If the items of the sequence are themselves sequences, they will formatted as rows.
    """

    required_arguments = 1
    has_content = False
    option_spec = {
        'title': unchanged_required,
        'header-rows': directives.nonnegative_int,
        'stub-columns': directives.nonnegative_int,
        'header': unchanged,
        'h_level_indexes': unchanged_required,
        'v_level_indexes': unchanged_required,
        'show-row-index-with-base': int,
        'show-column-index-with-base': int,
        'cell-formats': unchanged_required,
        'widths': directives.value_or(
            ('auto', 'grid'),
            directives.positive_int_list)
    }

    @property
    def widths(self):
        return self.options.get('widths', '')

    @property
    def header_rows(self):
        return self.options.get('header-rows', 0)

    @property
    def stub_columns(self):
        return self.options.get('stub-columns', 0)

    @property
    def v_level_indexes(self):
        text = self.options.get('v-level-indexes', '')
        try:
            items = map(int, filter(None, text.split(',')))
            return items or None
        except ValueError:
            raise self.error(
                "Could not interpret option v-level-indexes {!r}".format(text)
            )

    @property
    def h_level_indexes(self):
        text = self.options.get('h-level-indexes', '')
        try:
            items = map(int, filter(None, text.split(',')))
            return items or None
        except ValueError:
            raise self.error(
                "Could not interpret option h-level-indexes {!r}".format(text)
            )

    def get_column_widths(self, max_cols):
        if isinstance(self.widths, list):
            if len(self.widths) != max_cols:
                raise self.error(
                    "{!s} widths tabulate not match the number of columns {!s} in table. ({} directive)."
                        .format(self.widths, max_cols, self.name))
            col_widths = self.widths
        elif max_cols:
            col_widths = [100 // max_cols] * max_cols
        else:
            raise self.error(
                "Something went wrong calculating column widths. ({} directive).".format(self.name)
            )
        return col_widths

    def process_header_option(self):
        table_head = []
        max_header_cols = 0
        if 'header' in self.options:
            # TODO: Have the option for this to be a Python object too.
            header = self.options['header']
            header_stream = StringIO(header)
            reader = csv.reader(header_stream, delimiter=',', quotechar='"')
            header_row = next(reader)
            stripped_header_row = [cell.strip() for cell in header_row]
            table_head.append(stripped_header_row)
            max_header_cols = len(header_row)
        return table_head, max_header_cols

    def interpret_obj(self, obj, v_level_indexes, h_level_indexes):
        """Interpret the given Python object as a table.

        Args:
            obj: A sequence (later a mapping, too)

        Returns:
            A list of lists represents rows of cells.

        Raises:
            TypeError: If the type couldn't be interpreted as a table.
        """
        if not isinstance(obj, NonStringIterable):
             raise self.error("Cannot make a table from object {!r}".format(obj))

        rectangular_rows = tabulate(obj, v_level_indexes, h_level_indexes)
        assert is_rectangular(rectangular_rows)
        num_rows, num_cols = size(rectangular_rows)
        return rectangular_rows, num_cols

    def augment_cells(self, rows, source):
        """Convert each cell into a tuple suitable for consumption by build_table.

        I think this has to tabulate with cell spans, but I'm not sure, and we don't need it.
        """
        # TODO: Hardwired str transform.
        return [[(0, 0, 0, StringList(str(cell).splitlines(), source=source))
                 for cell in row] for row in rows]

    def run(self):

        obj_name = self.arguments[0]

        try:
            prefixed_name, obj, parent, modname = import_by_name(obj_name)
        except ImportError:
            raise self.error(
                "Could not locate Python object {} ({} directive).".format(obj_name, self.name))
        table_head, max_header_cols = self.process_header_option()
        rows, max_cols = self.interpret_obj(obj, self.v_level_indexes, self.h_level_indexes)
        max_cols = max(max_cols, max_header_cols)
        col_widths = self.get_column_widths(max_cols)
        table_head.extend(rows[:self.header_rows])
        table_body = rows[self.header_rows:]

        table_head = self.augment_cells(table_head, source=prefixed_name)
        table_body = self.augment_cells(table_body, source=prefixed_name)

        table = (col_widths, table_head, table_body)
        table_node = self.state.build_table(table, self.content_offset,
                                            self.stub_columns, widths=self.widths)
        table_node['classes'] += self.options.get('class', [])
        if 'align' in self.options:
            table_node['align'] = self.options.get('align')
        self.add_name(table_node)

        return [table_node]
