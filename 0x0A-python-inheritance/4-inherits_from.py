#!/usr/bin/python3
""" Returns true if the obj is instance of a class inherited indrectly
or not, from the specified class """


def inherits_from(obj, a_class):
    """ Idk why we need this comment in these files when
    there only exist one function. """
    return True if issubclass(type(obj), a_class) and type(obj) is not\
        a_class else False
