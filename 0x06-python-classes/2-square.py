#!/usr/bin/python3
""" Class with private instance size """


class Square:
    """ Check if size is less than 0 and if it is an int """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
