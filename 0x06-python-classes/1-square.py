#!/usr/bin/python3

"""
this module demonstrates the class square
"""


class Square:
    """this class is an instance of the square class

    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size):
        """This method initialises theinstance of this class
        Args:
            size (int):the size of the square
        """
        self.__size = size
