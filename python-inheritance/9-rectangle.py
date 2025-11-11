#!/usr/bin/python3
"""
This module defines the Rectangle class with area and __str__.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle defines a rectangle with area calculation
    and string representation.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated width and height.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
