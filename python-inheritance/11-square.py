#!/usr/bin/python3
"""This module contains a Square class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Initialize the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the size of the square"""
        return (f"[Square] {self.__size}/{self.__size}")
