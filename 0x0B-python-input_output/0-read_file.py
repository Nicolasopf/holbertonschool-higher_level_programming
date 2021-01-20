#!/usr/bin/python3
""" Reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ with is more optimal than a loop """
    with open(filename, encoding='UTF-8') as r:
            print(r.read(), end='')
