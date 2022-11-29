import os
import shutil
import sys
import importlib.util

pytest_plugins = [
    'sphinx.testing.fixtures',
]

from pytest import fixture

from sphinx.testing.path import path

this_dirpath = os.path.dirname(__file__)

source_dirpath = os.path.join(this_dirpath, "examples/source")
build_dirpath = os.path.join(this_dirpath, "examples/build")
code_dirpath = os.path.join(this_dirpath, "examples/code")

@fixture
def app(make_app):
    src_dir = path(source_dirpath).abspath()
    assert src_dir.isabs(), f"{src_dir} is not an absolute srcdir path as required by the Sphinx make_app() fixture"
    build_dir = path(build_dirpath).abspath()
    assert build_dir.isabs(), f" is not an absolute builddir path as required by the Sphinx make_app() fixture"
    shutil.rmtree(build_dirpath)
    return make_app(srcdir=src_dir, builddir=build_dir)


@fixture
def values():
    spec = importlib.util.spec_from_file_location("values", os.path.join(code_dirpath, "values.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["values"] = mod
    spec.loader.exec_module(mod)
    return mod