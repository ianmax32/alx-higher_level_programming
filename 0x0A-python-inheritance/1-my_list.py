#!/usr/bin/python3

"""This module has classes list and
mylist class which inherists from list
"""


class Mylist(list):
    """this class inherits from
    the list class"""

    def print_sorted(self):
        """prints the elements of the
        list in a sotred asc order
        """

        list_return = self[:]
        list_return.sort()
        print(list_return)
