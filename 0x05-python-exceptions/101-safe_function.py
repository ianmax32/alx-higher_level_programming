#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        for i in args:
            a = fct(args[i])
            return a
    except Exception:
        a = None
        print("Exception: {}".format(a), file=sys.stderr)
        return a
