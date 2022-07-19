#!/usr/bin/python3
"""Module with class Square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class from Rectangle"""

    def __init__(self, size):
        """initialize a square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return a description"""
        return str(f"[Square] {self.__size}/{self.__size}")

    def area(self):
        """return the area of the square"""
        return self.__size * self.__size
