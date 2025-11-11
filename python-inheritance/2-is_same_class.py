#!/usr/bin/python3
"""This module provides a function to check if an object is exactly an instance
of a specified class.

It defines the function `is_same_class()` which takes two arguments:
an object and a class, and returns True if the object is exactly an instance
of that class (not a subclass).

Usage:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    This function will return True if the object's type is exactly the same
    as the specified class, without considering inheritance or subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
              False otherwise.

    Example:
        >>> is_same_class(5, int)
        True
        >>> is_same_class(5, str)
        False
    """
    return (type(obj) is a_class)
