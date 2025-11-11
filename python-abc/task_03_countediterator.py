#!/usr/bin/env python3
"""
This module defines the CountedIterator class, which wraps an iterator
and counts how many items have been retrieved from it.
"""


class CountedIterator:
    """
    Iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself (needed for iteration protocols).
        """
        return self

    def __next__(self):
        """
        Fetch the next item from the underlying iterator.
        Increment the counter each time an item is retrieved.

        Raises:
            StopIteration: If no more items are available.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items retrieved so far.

        Returns:
            int: The number of items iterated.
        """
        return self.count
