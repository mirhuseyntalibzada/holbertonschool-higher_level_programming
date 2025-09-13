#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for the function max_integer(list=[])."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_list_with_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_with_mixed_numbers(self):
        """Test with a list of positive, negative, and zero."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate numbers."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 9.9, 3.5]), 9.9)

    def test_ints_and_floats(self):
        """Test with a list of mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 9.9]), 9.9)

    def test_string(self):
        """Test with a string."""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["one", "two", "three"]), "two")

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertIsNone(max_integer(""))

if __name__ == '__main__':
    unittest.main()
