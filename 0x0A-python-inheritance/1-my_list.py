#!/usr/bin/python3
'''
Print my list in sorted order
'''


class MyList(list):
    """subclass for print_sorted"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
