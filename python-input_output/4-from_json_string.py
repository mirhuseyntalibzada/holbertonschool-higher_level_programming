#!/usr/bin/python3
"""
This module defines a function that returns
a Python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
