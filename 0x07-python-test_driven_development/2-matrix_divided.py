#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): number to divide the matrix by.

    Returns:
        list: list of lists of integers or floats.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
        TypeError: if matrix contains rows of different sizes.
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is equal to 0.
    """

    if (
        not isinstance(matrix, list)
        or len(matrix) == 0
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            isinstance(element, (int, float)) for row in matrix for element in row
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
