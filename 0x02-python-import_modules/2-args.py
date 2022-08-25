#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    a = len(argv) - 1
    if a == 1:
        print("{} argument:".format(a))
    elif a > 0:
        print("{} arguments".format(a))
    else:
        print("{} arguments.".format(a))
    for b, arg in enumerate(argv[1:]):
        print("{}: {}".format(b + 1, arg))
