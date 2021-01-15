#!/usr/bin/python3
""" Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """Check if is a matrix of ints or floats and return the matrix divided"""

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    tmp = [row[:] for row in matrix]
    for i in range(len(matrix)):
        if type(matrix[i]) is not list or len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for h in range(len(matrix[i])):
            if type(tmp[i][h]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
            tmp[i][h] = round(tmp[i][h] / div, 2)
    return tmp
