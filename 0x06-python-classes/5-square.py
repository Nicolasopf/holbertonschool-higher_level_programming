#!/usr/bin/python3

""" Class with private instance size """


class Square:
    """ Check if size is less than 0, if it is an int and return area """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size is 0:
            print()
