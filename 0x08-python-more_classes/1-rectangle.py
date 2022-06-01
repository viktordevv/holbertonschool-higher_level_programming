#!/usr/bin/python3
"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """Class simple rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
