#!/usr/bin/python3
"""
this module returns an object representation of a json string
"""


import json


def from_json_string(my_str):
    """this converts the json to object"""
    return json.loads(my_str)
