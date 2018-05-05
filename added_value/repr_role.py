from docutils import nodes
from sphinx.ext.autosummary import import_by_name


def repr_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Include Python object value.

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """
    if options is None:
        options = {}

    if content is None:
        content = []

    try:
        prefixed_name, obj, parent, modname = import_by_name(text)
    except ImportError:
        msg = inliner.reporter.error(
            "Could not locate Python object {}".format(text), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    app = inliner.document.settings.env.app
    node = make_repr_node(rawtext, app, prefixed_name, obj, parent, modname, options)
    return [node], []


def make_repr_node(rawtext, app, prefixed_name, obj, parent, modname, options):
    """Render a Python object to text using the repr() function.

    :param rawtext: Text being replaced with link node.
    :param app: Sphinx application context
    :param prefixed_name: The dotted Python name for obj.
    :param obj: The Python object to be rendered to text.
    :param parent: The parent Python object of obj.
    :param module: The name of the module containing obj.
    :param options: Options dictionary passed to role func.
    """
    text = repr(obj)
    node = nodes.Text(text, rawsource=rawtext)
    return node
