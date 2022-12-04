#!/usr/bin/python3
"""this module create a object from a json
file
"""


import json


def load_from_json_file(filename):
    """this opens a file and reads the file"""
    with open(filename) as rd_file:
        obj = rd_file.read()
        json.loads(obj)
