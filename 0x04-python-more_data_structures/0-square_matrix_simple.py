#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[value ** 2 for value in row] for row in matrix]
    return new
