#!/usr/bin/python3
"""Module to return a list of attributes and methods of a given object.

This module contains a function `lookup()` that takes an object as input
and returns a list of all the attributes and methods in the object.

Example:
    >>> lookup(5)
    ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', ...]
"""


def lookup(obj):
    """Returns a list of attributes and methods of the given object.

    Args:
        obj: The object whose attributes and methods are to be looked up.

    Returns:
        list: representing the names of the object's attributes and methods.

    Example:
        >>> lookup(5)
        ['__class__', '__delattr__', '__doc__', '__eq__', '__format__', ...]
    """
    return (dir(obj))
