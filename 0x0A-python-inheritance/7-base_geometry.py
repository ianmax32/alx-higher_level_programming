#!/usr/bin/python3

"""This module contains the class
BaseGeometry
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
