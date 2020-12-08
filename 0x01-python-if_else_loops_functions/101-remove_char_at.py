#!/usr/bin/python3


def remove_char_at(str, n):
    i = 0
    str_r = ""
    for h in str:
        if i != n:
            str_r += h
        i += 1
    return (str_r)
