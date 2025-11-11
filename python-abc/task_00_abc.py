#!/usr/bin/env python3
"""
This module defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    Subclasses must implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses
        to return the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Dog class that implements the sound method.
    """

    def sound(self):
        """
        Return the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that implements the sound method.
    """

    def sound(self):
        """
        Return the sound of a cat.
        """
        return "Meow"
