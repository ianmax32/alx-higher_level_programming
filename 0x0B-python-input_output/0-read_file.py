#!/usr/bin/python3
"""this module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """this function is opening and reading the file"""
    with open(filename, encoding='utf-8') as rd_file:
        print(rd_file.read(), end="")
