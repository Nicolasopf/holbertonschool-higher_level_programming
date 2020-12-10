#!/usr/bin/python3

from sys import argv as ar
from calculator_1 import *

if __name__ != "__main__":
    exit()

args = len(ar) - 1
if args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if ar[2] == '+':
    op = add
elif ar[2] == '-':
    op = sub
elif ar[2] == '*':
    op = mul
elif ar[2] == '/':
    op = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

n1 = int(ar[1])
n3 = int(ar[3])
result = op(n1, n3)
print(n1, ar[2], n3, "=", result)
