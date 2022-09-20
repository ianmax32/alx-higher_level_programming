#!/usr/bin/python3

"""This defines a class caled Rectangle"""


class Rectangle:
    """this class defines a class called reactangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """this method initialises the instance fields
            Args:
                width(int): width of the rectangle
                height(int): height of the reactangle class
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            info += self.__width * str(self.print_symbol) + "\n"
        return info[:-1]

    def __repr__(self):
        """this method returns a string representation of the
        reactangle to be anle to recreate a new instance by using
        eval()"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """this method prints a message when the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """this method returns the biggest reactangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
                return rect_1
            else:
                return rect_2
