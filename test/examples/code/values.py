from collections import OrderedDict

the_answer = 42

tricolon = [
    'life',
    'the Universe',
    'everything',
]

flavors = [
    'cherry',
    'chocolate',
    'pear',
]

month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

month_lengths = [
    ['January', 31],
    ['February', 28],
    ['March', 31],
    ['April', 30],
    ['May', 31],
    ['June', 30],
    ['July', 31],
    ['August', 31],
    ['September', 30],
    ['October', 31],
    ['November', 31],
    ['December', 31],
]

month_day_ranges = OrderedDict((name, list(range(1, length+1))) for name, length in month_lengths)

