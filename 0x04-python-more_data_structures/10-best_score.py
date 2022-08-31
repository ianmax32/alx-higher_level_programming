#!/usr/bin/python3

def best_score(a_dictionary):
    best = 0
    name = ""
    if a_dictionary is None:
        return (None)
    for a, i in a_dictionary.items():
        if i > best:
            best = i
            name = a
    return (name)
