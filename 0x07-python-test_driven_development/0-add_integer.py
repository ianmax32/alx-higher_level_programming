#!/usr/bin/python3

"""Module for add integer function"""

def add_integer(a, b=98):
    """this is a function for adding two
    integers"""

    x = 0
    y = 0
    try:
        x = a + 10
        y = b + 10
    except TypeError:
        if not y:
            return "b must be an integer"
        if not x:
            return "a must be an integer"
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
