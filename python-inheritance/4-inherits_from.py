#!/usr/bin/python3
"""This module defines a function that checks if an object is an instance of
a class that inherits (directly or indirectly) from a specified class.

It defines the function `inherits_from()` which checks whether an object is
an instance of a subclass (excluding direct instances of the class itself)
of the specified class.

Usage:
    inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherits (directly
    or indirectly) from the specified class.

    This function returns True if the object is an instance of a subclass of
    the specified class (excluding direct instances of the class itself).
    It uses `isinstance()` to check for subclass relationships and `type()`
    to ensure that the object is not an instance of the specified class itself.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        bool: True if the object is an instance of a subclass of the specified
              class, excluding instances of the class itself. False otherwise.

    Example:
        >>> inherits_from(5, int)
        False
        >>> inherits_from(True, int)
        True  # bool is a subclass of int
        >>> inherits_from(5, object)
        True  # int is a subclass of object
        >>> inherits_from("hello", str)
        False  # str is not a subclass of str
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
