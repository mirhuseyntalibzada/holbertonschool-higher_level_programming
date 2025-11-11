#!/usr/bin/env python3
"""
This module demonstrates the use of mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """
    Mixin class that adds swimming ability.
    """

    def swim(self):
        """
        Print that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds flying ability.
    """

    def fly(self):
        """
        Print that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying abilities from mixins.
    """

    def roar(self):
        """
        Print that the dragon roars.
        """
        print("The dragon roars!")
