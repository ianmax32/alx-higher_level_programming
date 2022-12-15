#!/usr/bin/python3
"""
this module has a function that finds a
peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """this function finds the peak"""
    midValue = 0
    if list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    else:
        midValue = len(list_of_integers)/2

    value = list_of_integers[midValue]
    if value > list_of_integers[midValue - 1] and
    value > list_of_integers[midValue + 1]:
        return value
    elif value > list_of_integers[midValue + 1]:
        return find_peak(list_of_integers[midValue + 1:])
    else:
        return find_peak(list_of_integers[:midValue])
