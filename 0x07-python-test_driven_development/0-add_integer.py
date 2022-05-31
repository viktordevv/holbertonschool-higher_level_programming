#!/usr/bin/python3
""" add_integer - add two integers
    a: first integer
    b: second integer
    return a + b
    typeerror: if a or b is not an integer"""


def add_integer(a, b=98):
    """ add_integer - add two integers
        a: first integer
        b: second integer
        default value = 98"""

    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
