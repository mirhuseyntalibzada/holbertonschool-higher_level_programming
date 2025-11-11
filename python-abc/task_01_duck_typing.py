#!/usr/bin/python3
"""
Module for task_01_duck_typing.
Defines Shape, Circle, and Rectangle classes, and a shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for a shape."""

    @abstractmethod
    def area(self):
        """
        Abstract method to return the area of the shape.
        """
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to return the perimeter of the shape.
        """
        raise NotImplementedError


class Circle(Shape):
    """
    Concrete Circle class inheriting from Shape.
    """
    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        Args:
            radius (float or int): The radius of the circle.
        """
        # A negative radius is physically meaningless,
        # so we can store its absolute value.
        self.radius = abs(radius)

    def area(self):
        """
        Calculates the area of the circle.
        Area = pi * r^2
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.
        Perimeter = 2 * pi * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete Rectangle class inheriting from Shape.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle with a given width and height.
        Args:
            width (float or int): The width of the rectangle.
            height (float or int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        Area = width * height
        This may be negative if dimensions are negative.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Perimeter = 2 * (|width| + |height|)
        This will always be positive.
        """
        # This is the corrected line:
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """
    Prints the area and perimeter of any object
    that has .area() and .perimeter() methods (duck typing).
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())