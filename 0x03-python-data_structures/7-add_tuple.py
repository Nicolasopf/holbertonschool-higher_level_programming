#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tmp = tuple_a + (0, 0)
    tmp2 = tuple_b + (0, 0)
    return tmp[0] + tmp2[0], tmp[1] + tmp2[1]
