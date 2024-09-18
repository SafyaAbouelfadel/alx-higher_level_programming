#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = list(map(lambda submat: list(map(lambda x: x ** 2, submat)), matrix))
    return square
