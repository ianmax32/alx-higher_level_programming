#!/usr/bin/python3

"""This module contains the class
BaseGeometry and Ractangle that inherits
from basegeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
