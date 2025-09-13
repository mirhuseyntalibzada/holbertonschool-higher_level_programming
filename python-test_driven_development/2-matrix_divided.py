#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the results of the division, rounded
              to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers,
                   if the rows of the matrix are not the same size,
                   or if div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg_type)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg_type)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError(msg_size)

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(msg_type)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
