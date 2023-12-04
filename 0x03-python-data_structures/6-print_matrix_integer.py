#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for row in matrix:
        for i, j in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d} ".format(j), end="")
         print()
