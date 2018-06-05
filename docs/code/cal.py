from collections import OrderedDict

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

month_of_weeks = [
    ["29 Jan", "30 Jan", "31 Jan", "1 Feb", "2 Feb", "3 Feb", "4 Feb"],
    ["5 Feb", "6 Feb", "7 Feb", "8 Feb", "9 Feb", "10 Feb", "11 Feb"],
    ["12 Feb", "13 Feb", "14 Feb", "15 Feb", "16 Feb", "17 Feb", "18 Feb"],
    ["19 Feb", "20 Feb", "21 Feb", "22 Feb", "23 Feb", "24 Feb", "25 Feb"],
    ["26 Feb", "27 Feb", "28 Feb", "1 Mar", "2 Mar", "3 Mar", "4 Mar"],
]

month_lengths = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 31,
    'December': 31,
}

ordered_month_lengths = OrderedDict([
    ('January', 31),
    ('February', 28),
    ('March', 31),
    ('April', 30),
    ('May', 31),
    ('June', 30),
    ('July', 31),
    ('August', 31),
    ('September', 30),
    ('October', 31),
    ('November', 31),
    ('December', 31),
])
