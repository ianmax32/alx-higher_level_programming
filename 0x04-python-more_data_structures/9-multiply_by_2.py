#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dic_new = a_dictionary.copy()
    for x in a_dictionary:
        dic_new[x] *= 2
    return (dic_new)
