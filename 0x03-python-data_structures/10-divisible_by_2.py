#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if not my_list or my_list is None:
        return (None)
    for i in my_list:
        if not i % 2:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
