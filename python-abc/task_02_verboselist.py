#!/usr/bin/env python3
"""
This module defines the VerboseList class, which extends list
and provides notifications for modifications.
"""


class VerboseList(list):
    """
    VerboseList extends Python's built-in list to print messages
    when items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at index (default last).
        Print a notification about the popped item.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
