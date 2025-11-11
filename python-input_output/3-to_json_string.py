#!/usr/bin/python3
"""
This module defines a function that returns
the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
