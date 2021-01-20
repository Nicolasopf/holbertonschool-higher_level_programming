#!/usr/bin/python3
""" Class bassed on 6-base_geometry.py """


class BaseGeometry:
    """ Function to raise an exception, other to valid if nums are int """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
