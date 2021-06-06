from collections.abc import Sequence

@dispatch(Sequence, (str, int))
def concatenate(a, b):
    return list(a) + [b]