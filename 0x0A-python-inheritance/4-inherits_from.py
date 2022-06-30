#!/usr/bin/python3
"""contains the is_kind_of_class function"""

def inherits_from(obj, a_class):
    """True if obj is an instance or inherited  else false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
