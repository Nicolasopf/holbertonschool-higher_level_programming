#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the\
 number of characters written """


def write_file(filename="", text=""):
    """ same as above """
    with open(filename, encoding="UTF-8", mode="w+") as r:
        return r.write(text)
