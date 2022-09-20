#!/usr/bin/python3

"""This defines a class caled Rectangle"""


class Rectangle:
    """this class defines a class called rectangle"""
    def __init__(self, width=0, height=0):
        """this method initialises the instance fields"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """this method returns the value of field width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this method sets the width to a certain value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """this method returns the value of field height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this method sets the height to a certain value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
