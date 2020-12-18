#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    idx = 1
    for letter in roman_string:
        if letter == "X":
            num += 10
        elif letter == "M":
            num += 1000
        elif letter == "D":
            num += 500
        elif letter == "V":
            num += 5
        elif letter == "L":
            num += 50
        elif letter == "I":
            num += 1
        idx += 1
    return num
