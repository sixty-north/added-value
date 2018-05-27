from collections import Mapping, deque
from itertools import count, chain, product

import operator

from added_value.items_table_directive import NonStringIterable
from added_value.sorted_frozen_set import SortedFrozenSet


depth_marker = object()
ROOT = object()
LEAF = object()

def breadth_first(obj, leaves=False):
    queue = deque()
    queue.append(obj)
    queue.append(None)
    level_keys = []
    current_level_keys = set()
    while len(queue) > 0:
        node = queue.popleft()
        if node is None:
            level_keys.append(current_level_keys)
            current_level_keys = set()
            queue.append(None)
            if queue[0] is None:
                break
            else:
                continue
        if isinstance(node, Mapping):
            current_level_keys.update(node.keys())
            for value in node.values():
                queue.append(value)
        elif isinstance(node, NonStringIterable):
            current_level_keys.update(range(len(node)))
            for value in node:
                queue.append(value)
        else:
            if leaves:
                current_level_keys.add(node)
    return level_keys[:-1]

class Missing(object):

    def __str__(self):
        return ''

    def __repr__(self):
        return self.__class__.__name__

MISSING = Missing()


def tabulate_body(obj, v_level_indexes, h_level_indexes):
    """
    Args:
        v_level_indexes: A sequence of level indexes.
        h_level_indexes: A sequence of level indexes.
    """
    level_keys = breadth_first(obj)
    h_level_set = SortedFrozenSet(h_level_indexes)
    if len(h_level_indexes) != len(h_level_set):
        raise ValueError("h_level_indexes contains duplicate values")
    if h_level_set and (h_level_set[0] < 0 or h_level_set[-1] >= len(level_keys)):
        raise ValueError("h_level_indexes contains out of range values")

    v_level_set = SortedFrozenSet(v_level_indexes)
    if len(v_level_indexes) != len(v_level_set):
        raise ValueError("v_level_indexes contains duplicate values")
    if v_level_set and v_level_set[0] < 0 or v_level_set[-1] >= len(level_keys):
        raise ValueError("v_level_indexes contains out of range values")

    all_levels = SortedFrozenSet(range(len(level_keys)))
    unmentioned_levels = all_levels - v_level_set - h_level_set
    if len(unmentioned_levels) > 0:
        raise ValueError("v_level_indexes and h_level_indexes tabulate not include levels {}".format(', '.join(map(str, unmentioned_levels))))

    if not h_level_set.isdisjoint(v_level_set):
        raise ValueError("h_level_indexes and v_level_indexes are not disjoint")

    h_level_keys = [level_keys[level] for level in h_level_indexes]
    v_level_keys = [level_keys[level] for level in v_level_indexes]

    h_key_tuples = list(product(*h_level_keys))  # Use sorted?
    v_key_tuples = list(product(*v_level_keys))  # Use sorted?

    h_size = len(h_key_tuples)
    v_size = len(v_key_tuples)

    table = [[MISSING for _ in range(h_size)] for _ in range(v_size)]

    for h_index, h_keys in enumerate(h_key_tuples):
        for v_index, v_keys in enumerate(v_key_tuples):
            key_path = [None] * len(level_keys)
            merge_into_by_index(key_path, h_level_indexes, h_keys)
            merge_into_by_index(key_path, v_level_indexes, v_keys)
            for v_level, v_key in zip(v_level_indexes, v_keys):
                key_path[v_level] = v_key

            item = obj
            for key in key_path:
                try:
                    item = item[key]
                except (IndexError, KeyError):
                    break
            else:  # no-break
                table[v_index][h_index] = item

    return table, v_key_tuples, h_key_tuples


def strip_missing_rows(table, row_keys):
    stripped_table = []
    stripped_v_key_tuples = []
    for row, v_key_tuple in zip(table, row_keys):
        if any(cell is not MISSING for cell in row):
            stripped_table.append(list(row))
            stripped_v_key_tuples.append(v_key_tuple)
    return stripped_table, stripped_v_key_tuples


def strip_missing_columns(table, h_key_tuples):
    transposed_table = transpose(table)
    stripped_transposed_table, stripped_h_key_tuples = strip_missing_rows(transposed_table, h_key_tuples)
    stripped_table = transpose(stripped_transposed_table)
    return stripped_table, stripped_h_key_tuples


def merge_into_by_index(sequence, indexes, values):
    for index, value in zip(indexes, values):
        sequence[index] = value

def is_rectangular(seq_of_seqs):
    return len(set(map(len, seq_of_seqs))) <= 1

def size_h(rows_of_columns):
    try:
        first_row = rows_of_columns[0]
    except IndexError:
        return 0
    else:
        return len(first_row)

def size_v(rows_of_columns):
    return sum(1 for row in rows_of_columns if len(row) != 0)


def transpose(rows_of_columns):
    return list(map(list, zip(*rows_of_columns)))


def assemble_table(table_body, v_key_tuples, h_key_tuples, empty=''):
    if not is_rectangular(table_body):
        raise ValueError("table_body {} is not rectangular".format(table_body))
    if not is_rectangular(v_key_tuples):
        raise ValueError("v_key_tuples {} is not rectangular".format(v_key_tuples))
    if not is_rectangular(h_key_tuples):
        raise ValueError("h_key_tuples {} is not rectangular".format(h_key_tuples))
    if size_v(v_key_tuples) > 0 and (size_v(table_body) != size_v(v_key_tuples)):
        raise ValueError("table body and v_key_tuples have incompatible dimensions")
    h_key_tuples_transposed = transpose(h_key_tuples)
    if size_h(h_key_tuples_transposed) > 0 and (size_h(table_body) != size_h(h_key_tuples_transposed)):
        raise ValueError("table body and h_key_tuples have incompatible dimensions")

    num_stub_columns = size_h(v_key_tuples)
    num_header_rows = size_v(h_key_tuples_transposed)
    table = []

    for h_key_row in h_key_tuples_transposed:
        row = [empty] * num_stub_columns
        row.extend(h_key_row)
        table.append(row)

    for v_key_row, table_row in zip(v_key_tuples, table_body):
        row = list(v_key_row)
        row.extend(table_row)
        table.append(row)

    assert is_rectangular(table)
    return table


def tabulate(obj, v_level_indexes, h_level_indexes, v_level_visibility=None, h_level_visibility=None):
    """Render a nested data structure into a two-dimensional table.

    Args:
        obj: The indexable data structure to be rendered, which can
            either be a non-string sequence or a mapping containing other
            sequences and mappings nested to arbitrarily many levels,
            with all the leaf items (which are neither sequences nor
            mappings, excluding strings).

        v_level_indexes: An iterable of the zero-based indexes of
            the levels for which the keys/indexes will be displayed
            along the vertical axis of the table. Taken together
            with the levels in h_levels these must represent the
            complete set of levels in the obj data structure. No
            level index should appear in both v_level_indexes and
            h_level_indexes, but all level indexes must appear in
            either v_level_indexes or h_level_indexes.

        h_level_indexes: An iterable of the zero-based indexes of
            the levels for which the keys/indexes will be displayed
            along the horizontal axis of the table. Taken together
            with the levels in v_levels these must represent the
            complete set of levels in the obj data structure. No
            level index should appear in both h_level_indexes and
            v_level_indexes, but all level indexes must appear in
            either h_level_indexes or v_level_indexes.

        v_level_visibility: An iterable of booleans, where each
            item corresponds to a level in v_level_indexes, and
            controls whether than level of index is included in
            the table stub columns. This iterable must contain
            the same number of items as v_level_indexes.

        h_level_visibility: An iterable of booleans, where each
            item corresponds to a level in h_level_indexes, and
            controls whether than level of index is included in
            the table header rows. This iterable must contain
            the same number of items as h_level_indexes.


    Returns:
        A list of lists representing the rows of cells.

    Example:

        tabulate(dict_of_dicts, [0, 1], [])

    """
    v_level_indexes = list(v_level_indexes)
    h_level_indexes = list(h_level_indexes)
    if v_level_visibility is None:
        v_level_visibility = [True] * len(v_level_indexes)
    if h_level_visibility is None:
        h_level_visibility = [True] * len(h_level_indexes)
    table, v_key_tuples, h_key_tuples = tabulate_body(obj, v_level_indexes, h_level_indexes)
    table, v_key_tuples = strip_missing_rows(table, v_key_tuples)
    table, h_key_tuples = strip_missing_columns(table, h_key_tuples)
    v_key_tuples = strip_hidden(v_key_tuples, v_level_visibility)
    h_key_tuples = strip_hidden(h_key_tuples, h_level_visibility)
    return assemble_table(table, v_key_tuples, h_key_tuples)


def strip_hidden(key_tuples, visibilities):
    """Filter each tuple according to visibility.

    Args:
        key_tuples: A sequence of tuples of equal length (i.e. rectangular)
        visibilities: A sequence of booleans equal in length to the tuples contained in key_tuples.

    Returns:
        A sequence equal in length to key_tuples where the items are tuples with a length corresponding
        to the number of items in visibility which are True.
    """
    result = []
    for key_tuple in key_tuples:
        if len(key_tuple) != len(visibilities):
            raise ValueError("length of key tuple {} is not equal to length of visibilities {}".format(key_tuple, visibilities))
        filtered_tuple = tuple(item for item, visible in zip(key_tuple, visibilities) if visible)
        result.append(filtered_tuple)
    return result

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

b = [
    [[5, 6], [1, 9], [3, 5]],
    [[7, 2], [4], [5, 6]],
    [[7, 8], [9, 3],],
    [[1, 9], [2, 9], [3, 6]],
]

c = {
    'alpha': 5,
    'bravo': 5,
    'charlie': 6,
    'delta': 5,
    'foxtrot': 6,
    'golf': 4,
}

d = {
    'alpha': "Fox base alpha".split(),
    'bravo': "Rio bravo".split(),
    'charlie': "Charlie says".split(),
    'delta': "Concorde has a delta wing".split(),
    'foxtrot': "The foxtrot was a popular dance".split(),
    'golf': "Golf spoils a walk in the countryside".split(),
}

e = [
    {'set': 3,
     'pour': 4,
     'serve': 5
     },
    {'serve': 19,
     'set': 12,
     'volley': 9
     },
    {'set': 98,
     'pour': 1,
     'cast': 14
     },
    {'cast': 34,
     'line': 18,
     'fish':8
     }
]

# TODO: Multidimensional arrays. e.g. ndarray

