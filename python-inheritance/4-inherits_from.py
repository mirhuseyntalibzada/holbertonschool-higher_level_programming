#!/usr/bin/python3
"""
This module defines the function inherits_from.
It checks if an object is an instance of a subclass of a given class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
