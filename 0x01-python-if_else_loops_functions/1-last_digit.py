#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number >= 0:
    rest = number % 10
elif number < 0:
    rest = ((number * -1) % 10) * -1
if rest > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, rest))
elif rest == 0:
    print("Last digit of {0} is {1} and is 0".format(number, rest))
elif rest < 6 and rest != 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, rest))
