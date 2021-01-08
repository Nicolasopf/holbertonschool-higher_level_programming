#!/usr/bin/python3
""" Prints the name of a person and the last name """


def say_my_name(first_name, last_name=""):
    """ Check the type of the names """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
