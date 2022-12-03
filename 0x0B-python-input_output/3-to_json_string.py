#!/usr/bin/python3
"""
this module returns a json representation of an object
"""


import json


def to_json_string(my_obj):
    """this converts the string to json"""
    return json.dumps(my_obj)
