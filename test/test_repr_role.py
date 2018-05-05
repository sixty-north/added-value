from sphinx_testing import with_app


@with_app(
    srcdir='test/examples/source',
    confdir='test/examples/source',
    copy_srcdir_to_tmpdir=True)
def test_smoke(app, status, warning):
    app.build()
    html = (app.outdir / 'index.html').read_text()
    assert "Examples for added-value" in html
