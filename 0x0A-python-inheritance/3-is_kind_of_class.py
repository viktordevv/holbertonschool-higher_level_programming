#!/usr/bin/python3
"""
contains the is_kind_of_class
"""


def inherits_from(obj, a_class):
    """ inherited from a_class, else false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
