#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square defines a square with equal sides.
    """

    def __init__(self, size):
        """
        Initialize a Square with validated size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size
