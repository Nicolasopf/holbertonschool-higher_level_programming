#!/usr/bin/python3
""" Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """Check if is a matrix of ints or floats and return the matrix divided"""

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        if len(matrix[0]) is 0:
            raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        if len(matrix[0]) is not len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in matrix[i]:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda n: round((n / div), 2), sub)) for sub in matrix]
