#!/usr/bin/python3
""" Return true if obj is an instance of,
or is an instance of a class inherited from """


def is_kind_of_class(obj, a_class):
    """ If obj is an instance of a class inherited from, return true,
    if it not, then returns false"""
    if isinstance(obj, a_class):
        return True
    return False
