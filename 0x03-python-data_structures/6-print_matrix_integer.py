#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    """Prints a matrix of integers"""
    if matrix:
        for row in matrix:
            for index, number in enumerate(row):
                print("{:d}{}".format(number,
                                      " " if index != len(row) - 1 else ""),
                      end="")
            print()
