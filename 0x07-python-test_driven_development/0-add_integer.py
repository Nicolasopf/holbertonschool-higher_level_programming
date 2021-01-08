#!/usr/bin/python3
"""Add an integer, test cases in tests/"""


def add_integer(a, b=98):
    """Check if is int or float, if is float, cast, if other raise an error"""
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    else:
        return int(a + b)
