#!/usr/bin/python3
# 0-add_integer.py
"""An integer addition function is defined."""

def add_integer(a, b=98):
    """The integer addition of a and b is returned.

    Float arguments are typecasted to ints before addition is performed.

    Note:
        a and b must be integers or floats, otherwise raise a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

