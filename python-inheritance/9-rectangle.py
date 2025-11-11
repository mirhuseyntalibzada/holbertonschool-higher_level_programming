#!/usr/bin/python3
"""This module contains a Rectangle class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle."""

    def __init__(self, width, height):
        """Initialize the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function that computes the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the width and height of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
