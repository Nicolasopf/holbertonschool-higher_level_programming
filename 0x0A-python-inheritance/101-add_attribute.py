#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, key, value):
    """ ye, you still know """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
