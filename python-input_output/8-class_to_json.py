#!/usr/bin/python3
"""
This module defines a function that returns
the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: Instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary containing all serializable attributes.
    """
    return obj.__dict__
