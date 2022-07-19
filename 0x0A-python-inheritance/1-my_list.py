#!/usr/bin/python3
"""Module my_list define the  class MyList"""


class MyList(list):
    """ create subclass MyList """
    def print_sorted(self):
        """print list in sorted order """
        print(sorted(self))