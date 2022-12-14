#!/usr/bin/python3

"""This defines a class caled Rectangle"""


class Rectangle:
    """this class defines a class called reactangle
    """
    def __init__(self, width=0, height=0):
        """this method initialises the instance fields
            Args:
                width(int): width of the rectangle
                height(int): height of the reactangle class
        """
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

    def area(self):
        """this method calculates the area of recctangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this method returns the parameter of the ractangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """this method prints the reactabgle with character #"""
        info = ""
        if self.__width == 0 or self.__height == 0:
            return info
        for i in range(self.__height):
            info += self.__width * "#" + "\n"
        return info[:-1]

    def __repr__(self):
        """this method returns a string representation of the
        reactangle to be anle to recreate a new instance by using
        eval()"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
