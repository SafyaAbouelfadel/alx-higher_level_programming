#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sm: list(map(lambda k: k**2, sm)), matrix))
