#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for fil in matrix:
        for col in fil:
            print("{:d}".format(col), end=" " if col != fil[-1] else "")
            print()
