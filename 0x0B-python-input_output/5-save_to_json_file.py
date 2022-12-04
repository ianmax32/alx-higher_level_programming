#!/usr/bin/python3
"""this module writes an object to a text file
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """this opens the file and wites the object"""
    with open(filename, 'w') as wr_file:
        wr_file.write(json.dump(my_obj))
