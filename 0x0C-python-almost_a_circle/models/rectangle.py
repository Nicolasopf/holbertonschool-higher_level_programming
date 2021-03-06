#!/usr/bin/python3
"""
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter
"""
from models.base import Base


class Rectangle(Base):
    """
    Why private attributes with getter/setter? Why not public attribute?

    Because we want to protect attributes of our class.\
    With a setter, you are able to validate what a developer is trying to\
    assign to a variable.\
    So after, in your class you can “trust” these attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ aereaaaaaaaaa """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Return width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set width depending of some conditions """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Return height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set height depending of some conditions """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Return X """
        return self.__x

    @x.setter
    def x(self, x):
        """ set X depending of some conditions """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Return Y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Set Y depending of some conditions """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle with # """
        if self.__y >= 1:
            print('\n' * (self.__y - 1))
        for i in range(self.__height):
            print(" " * self.__x, end='')
            for h in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ Prints the string """
        i1 = '(' + str(self.id) + ') ' + str(self.__x) + '/'
        i2 = str(self.__y) + ' - ' + str(self.__width)
        return "[Rectangle] " + i1 + i2 + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """ Update the rectangle """
        dic = ['id', 'width', 'height', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, dic[i], args[i])
        else:
            for d in kwargs:
                setattr(self, d, kwargs[d])

    def to_dictionary(self):
        """ Return a dict """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
