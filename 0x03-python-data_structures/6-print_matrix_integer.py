#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            delim = ""
            for j in range(len(matrix[i])):
                print("{:s}{:d}".format(delim, matrix[i][j]), end='')
                delim = " "
            print()
