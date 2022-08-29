#!/usr/bin/python3

def no_c(my_string):
    str1 = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        str1 += x
    return (str1)
