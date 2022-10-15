#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):

    """ Returns the integer addition of a and b

    Float arguments are typecasted into int before addition is performed

    Raises:
        TypeError if either a or b is non-integer and non-float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

