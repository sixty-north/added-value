import os
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup
from natsort import natsort
from sphinx_testing import with_app

from added_value.util import is_sorted

dir_name = "test_items_table_two_v_columns"
html_filename = "index.html"


def test_base_name_in_html(app):
    app.build()
    html_doc = Path(app.outdir / dir_name / html_filename).read_text()
    rows = extract_table_body_from_html(html_doc)
    column = extract_column_from_rows(rows, 0)
    assert is_sorted(column, key=natsort.natsort_keygen())


def extract_column_from_rows(rows, column_index):
    return [row[column_index] for row in rows]


def extract_table_body_from_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('table', attrs={"class": "docutils"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    cells = []
    for row in rows:
        cols = row.find_all('td')
        elements = [element.text for element in cols]
        cells.append(elements)
    return cells

