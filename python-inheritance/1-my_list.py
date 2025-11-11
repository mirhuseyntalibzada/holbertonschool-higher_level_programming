#!/usr/bin/python3
"""This script defines a custom list subclass called `MyList`.

`MyList` extends the built-in `list` class by adding a method to print
the list in a sorted order.

Usage:
    You can create an instance of `MyList`, add items to it, and then
    call the `print_sorted()` method to print the items in ascending order.

Example:
    my_list = MyList([3, 1, 2])
    my_list.print_sorted()  # Output: [1, 2, 3]
"""


class MyList(list):
    """A subclass of the built-in list class that adds a method to print
    the list in sorted order.

    Methods:
        print_sorted(): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """Prints the list in sorted (ascending) order.

        This method does not modify the original list, it just prints
        the sorted version of the list.
        """
        print(sorted(self))
