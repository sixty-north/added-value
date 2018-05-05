from added_value.str_role import str_role
from added_value.repr_role import repr_role
from added_value.version import __version__


def setup(app):
    if not hasattr(app, 'add_config_value'):
        return  # probably called by nose, better bail out

    app.add_role('repr', repr_role)
    app.add_role('str', str_role)

    return {'version': __version__}