#!/usr/bin/python3
""" Returns a boolean depending if obj is exactly an instance of a_class """


def is_same_class(obj, a_class):
    """ Check the type and returns True or False """
    if type(obj) is a_class:
        return True
    return False
