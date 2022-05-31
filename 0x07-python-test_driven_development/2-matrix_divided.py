#!/usr/bin/python3

def matrix_divided(matrix, div):

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    return [[round(n / div, 2) for n in row] for row in matrix]
