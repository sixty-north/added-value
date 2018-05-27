from added_value.tabulator import tabulate

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


def test_tabulate_list_of_dicts_with_keys_zero_and_one_on_the_vertical_axis_has_three_columns():
    table = tabulate(e, [0, 1], [])
    assert len(table[0]) == 3

def test_tabulate_list_of_dicts_with_keys_zero_and_one_on_the_vertical_axis_has_twelve_rows():
    table = tabulate(e, [0, 1], [])
    assert len(table) == 12

def test_tabulate_list_of_dicts_with_keys_zero_and_one_on_the_vertical_axis_has_expected_column_0():
    table = tabulate(e, [0, 1], [])
    assert all(row[0] in range(4) for row in table)

def test_tabulate_list_of_dicts_with_keys_zero_and_one_on_the_vertical_axis_has_expected_column_1():
    table = tabulate(e, [0, 1], [])
    assert all(row[1] in {'set', 'pour', 'serve', 'volley', 'cast', 'line', 'fish'} for row in table)

# TODO: Sorting of keys
# TODO: str/repr/format of cells.
# TODO: Formatting of heterogeneous tuples e.g. ("Norway", 345, 12.45)  Maybe a sort of x-path syntax?

