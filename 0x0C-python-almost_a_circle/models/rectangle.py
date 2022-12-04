#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = Rectangle.__width
        self.height = Rectangle.__height
        self.x = Rectangle.__x
        self.y = Rectangle.__y

    @property
    def width(self):
        """get the private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value
