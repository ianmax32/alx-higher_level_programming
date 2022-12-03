#!/usr/bin/python3
"""
this module writes a string to a text file and
returns the number of characters written
"""

def write_file(filename="", text=""):
    """this opens and writes to the file"""
    a = 0
    with open(filename, 'w') as wr_file:
        for i in text:
            wr_file.write(i)
            a+=1
    return a
