#!/usr/bin/python3
"""
This module defines the function is_same_class.
It checks if an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class, otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class, else False.
    """
    return type(obj) is a_class
