"""
Props utility module.

A module that contains a single utility function used to
filter out default instance attributes and returns a dictionary
of user defined attributes.
"""


# Python 3 classes
class _NewClass:
    pass


# Python 2 classes
class _OldClass(object):
    pass


_all_vars = set(dir(_OldClass) + dir(_NewClass))


def props(x):
    """Return user defined instance attributes."""
    return {
        key: value for key, value in vars(x).items() if key not in _all_vars
    }
