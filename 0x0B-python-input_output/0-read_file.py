#!/usr/bin/python3
"""THE READ_FILE"""


def read_file(filename=""):
    """reads a text in utf-8"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read(), end="")
