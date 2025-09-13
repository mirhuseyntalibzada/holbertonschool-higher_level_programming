#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Parameters:
    a (int/float): first number
    b (int/float, optional): second number (default is 98)

    Returns:
    int: the addition of a and b

    Raises:
    TypeError: if a or b are not integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
