#!/usr/bin/python3
""" Class Square that inherits from Rectangle (9-rectangle.py) """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ You know ..... """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return Rectangle.area(self)
