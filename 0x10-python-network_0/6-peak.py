#!/usr/bin/python3
""" Implement merge sort algorithm"""


def find_peak(list_of_integers):
    maxx = 0
    for item in list_of_integers:
        if maxx < item:
            maxx = item
    if maxx == 0:
        return None
    return maxx
