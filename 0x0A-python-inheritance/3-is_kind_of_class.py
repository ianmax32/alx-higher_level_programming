#!/usr/bin/python3
"""
this module contains a function that
compares the instance of a classes
and the object
"""


def is_kind_of_class(obj, a_class):
    """method to compare an object
    and a class and return true or
    false
    Args:
        obj(Object): object to compare
        a_class(class):class of the instance
    """

    if not isinstance(obj, a_class):
        return False
    else:
        return True
