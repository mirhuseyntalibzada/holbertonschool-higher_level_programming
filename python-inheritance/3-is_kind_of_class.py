#!/usr/bin/python3
"""
This module defines the function is_kind_of_class.
It checks if an object is an instance of, or inherits from, a given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a subclass of it,
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherits from it,
        else False.
    """
    return isinstance(obj, a_class)
