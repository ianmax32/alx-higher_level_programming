#!/usr/bin/python3

"""This module contains a method for
lookup for available attributes"""

def lookup(obj):
    """method for lookup for arguments
    Args:
        obj(Object) : object to be checked
    """
    return dir(obj)
