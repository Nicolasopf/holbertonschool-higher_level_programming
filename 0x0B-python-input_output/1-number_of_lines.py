#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the\
 number of characters written """


def read_file(filename=""):
    """ same as above """
    with open(filename) as r:
        return len(r.readlines())
