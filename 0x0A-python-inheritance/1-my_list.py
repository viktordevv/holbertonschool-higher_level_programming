#!/usr/bin/python3
"""Module 1-my_list
define the child class MyList
"""


class MyList(list):
    """ create subclass MyList """

    def print_sorted(self):
        """print list in sorted order """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
    