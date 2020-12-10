#!/usr/bin/python3

import sys

if __name__ == "__main__":
    sum = 0
    args = sys.argv[1:]
    for i in args:
        h = int(i)
        sum += h
    print(sum)
