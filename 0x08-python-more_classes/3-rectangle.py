#!/usr/bin/python3
""" Defines a rectangle based in 1-rectangle.py """


class Rectangle:
    """ Print the rectangle area and perimeter """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.height + self.height + self.width + self.width

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return (("#" * self.__width + '\n') * self.__height)[:-1]
