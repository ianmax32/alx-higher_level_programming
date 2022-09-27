#!/usr/bin/python3
"""
this module contains a function that
compares the instance of classes
"""


def is_same_class(obj, a_class):
    """method to compare an object
    and a class and return true or
    false
    Args:
        obj(Object): object to compare
        a_class(class):class of the instance
    """

    if type(obj) == a_class:
        return True
    else:
        return False
