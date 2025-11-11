#!/usr/bin/python3
"""Module 7-base_geometry.
Defines the BaseGeometry class with an unimplemented area() method and
an integer validator for positive integers.
"""


class BaseGeometry:
    """BaseGeometry class with area() placeholder and integer validation."""

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that `value` is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
