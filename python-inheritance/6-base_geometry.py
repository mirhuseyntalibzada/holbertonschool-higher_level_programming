#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area() method.
    """

    def area(self):
        """
        Raise an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")
