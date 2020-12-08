#!/usr/bin/python3

h = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - h)), end="")
    if h == 0:
        h = 32
    else:
        h = 0
