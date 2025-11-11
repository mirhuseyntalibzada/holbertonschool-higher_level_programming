from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area (may be signed for some shapes)."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the (non-negative) perimeter/circumference."""
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        r = abs(self.radius)
        return math.pi * (r ** 2)

    def perimeter(self):
        r = abs(self.radius)
        return 2 * math.pi * r


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
