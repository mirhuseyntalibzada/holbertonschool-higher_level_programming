#!/usr/bin/python3
"""Defines a function that returns Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing the Pascal’s triangle of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing Pascal’s triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        # Each value (except the ends) is the sum of the two above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
