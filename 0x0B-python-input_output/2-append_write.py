#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8)\
 and returns the number of characters added """


def append_write(filename="", text=""):
    """ same as above """
    with open(filename, encoding="UTF-8", mode="a") as f:
        return f.write(text)
