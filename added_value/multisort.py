class Key(object):

    def __init__(self, func, reverse=False):
        self._func = func
        self._reverse=reverse

    @property
    def func(self):
        return self._func

    @property
    def reverse(self):
        return self._reverse

def identity(x):
    return x

def asc(func=identity):
    return Key(func, reverse=False)

def dec(func=identity):
    return Key(func, reverse=True)

_asis = Key(func=lambda x: None)

def asis():
    return _asis

def multisorted(items, *keys):
    if len(keys) == 0:
        keys = [asc(func=lambda x: x)]
    for key in reversed(keys):
        items = sorted(items, key=key.func, reverse=key.reverse)
    return items
