#!/usr/bin/python3
""" Function to prints a square of # """


def print_square(size):
    """ Check the size and do the for """
    if type(size) is not int or type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
            print("#" * size)
