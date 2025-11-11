#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Fish class with swimming and habitat behaviors.
    """

    def swim(self):
        """
        Print that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class with flying and habitat behaviors.
    """

    def fly(self):
        """
        Print that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird.
    Overrides methods to reflect its unique behavior.
    """

    def swim(self):
        """
        Print that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
