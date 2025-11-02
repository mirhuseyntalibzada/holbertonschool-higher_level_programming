#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a geometric square."""

    def __init__(self, size=0):
        """Initializes a Square instance with its size."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise TypeError("size must be >= 0")
        
        self.__size = size
