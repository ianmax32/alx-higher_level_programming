#!/usr/bin/python3

"""
this module demonstrates the class square
"""


class Square:
    """this class is an instance of the square class

    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """This method initialises theinstance of this class
        Args:
            size (int):the size of the square or return 0
        """
        self.__size = size
        self.__position = position

    def area(self):
        """this method calculates the ares and returns
        the area of the current square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """this method retrives the size variable"""
        return self.__size

    @size.setter
    def size(self, value):
        """this method is used to set the value of size
        Args:
            value (int):the value to set size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """this method returns the private instance field position"""
        return self.__position

    @position.setter
    def position(self, value):
        """this method sets the value of the private field position to a certain
        value
        """
        if (value[0] < 0 or value[1] < 0 or not isinstance(value, tuple) or
                len(value) is not 2 or not isinstance(value[0], int) or
                not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """this method prints the stdout of the square with the
        character #
        """
        if self.__size == 0:
            print("")
            return
        for b in range(self.__position[1]):
            print("")
        for a in range(self.__size):
            print("{}{}".format(self.__position[0] * " ",self.__size * "#"), end="")
            print("")
