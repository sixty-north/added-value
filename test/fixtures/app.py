from pytest import fixture

from sphinx.testing.path import path

@fixture()
def app(make_app):
    src_dir = path('test/examples/source').abspath()
    assert src_dir.isabs(), "make_app() requires an absolute path"
    return make_app(srcdir=src_dir)

