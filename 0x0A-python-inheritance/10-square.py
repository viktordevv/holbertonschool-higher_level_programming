#!/usr/bin/python3
"""
Module for Square subclass
BaseGeometry Class and subclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2