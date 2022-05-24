#!/usr/bin/python3
""" Square class
Esto escribe una funcion """


class Square:
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
