#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
convert = number

if number < 0:
        convert = -(number)
        last_digit = convert % 10
        last_digit = -(last_digit)

if last_digit == 0:
        str = "and is 0"
elif last_digit < 6:
        str = "and is less than 6 and not 0"
else:
        str = "and is greater than 5"
print("Last digit of {:d} is {:d}".format(number, last_digit), str)
