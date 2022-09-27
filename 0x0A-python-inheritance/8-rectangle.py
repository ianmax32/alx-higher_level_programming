#!/usr/bin/python3

"""This module contains the class
BaseGeometry and Ractangle that inherits
from basegeometry
"""


class BaseGeometry:
    """class that has the basic
    functions of geometry"""
    def area(self):
        """method to calculate
        area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class for rectangle"""


class Rectangle(BaseGeometry):
    """class for rectangle and inherits
    from the base geometry class"""

    def __init__(self, width, height):
        """initialization method for fields
        Args:
            width(int) : width for rectangle
            height(int) : height for rectangle
            """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
