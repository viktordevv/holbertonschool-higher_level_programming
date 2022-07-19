#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """A class wiht public instance methods area """
    def area(self):
        """raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
