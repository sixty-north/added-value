from sphinx_testing import with_app

with_test_examples_source = with_app(
    srcdir='test/examples/source',
    confdir='test/examples/source',
    copy_srcdir_to_tmpdir=True)