#!/usr/bin/python3
"""
this module returns a json representation of an object
"""


import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
