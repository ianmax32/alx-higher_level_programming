#!/usr/bin/python3

"""
this module demonstrates the class square
"""


class Square:
    """this class is an instance of the square class

    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size=0):
        """This method initialises theinstance of this class
        Args:
            size (int):the size of the square or return 0
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """this method calculates the ares and returns
        the area of the current square
        """
        return (self.__size ** 2)
