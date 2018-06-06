from itertools import chain, repeat, islice, izip_longest, tee


def pad_infinite(iterable, padding=None):
    return chain(iterable, repeat(padding))


def pad(iterable, size, padding=None):
    return islice(pad_infinite(iterable, padding), size)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def pairwise_longest(iterable, fillvalue=None):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip_longest(a, b, fillvalue=fillvalue)