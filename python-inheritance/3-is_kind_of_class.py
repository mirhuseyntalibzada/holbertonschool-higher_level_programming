#!/usr/bin/python3
"""This module provides a function to check if an object is an instance of,
or if the object is an instance of a subclass of, a specified class.

It defines the function `is_kind_of_class()` which checks if the object is
either an instance of the specified class or an instance of a subclass of it.

Usage:
    is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is instance of specified class or subclass of it.

    This function uses the `isinstance()` method to check if the object is
    an instance of the specified class, or an instance of any subclass
    of that class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class,
              or an instance of a subclass of it. False otherwise.

    Example:
        >>> is_kind_of_class(5, int)
        True
        >>> is_kind_of_class(5, str)
        False
        >>> is_kind_of_class(True, int)
        True  # bool is a subclass of int
    """
    return (isinstance(obj, a_class))
