#!/usr/bin/python3
"""the function student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
