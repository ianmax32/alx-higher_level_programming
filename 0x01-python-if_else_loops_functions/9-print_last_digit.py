#!/usr/bin/python3
def print_last_digit(number):
    value = str(number)[-1]
    print("{}".format(value), end="")
    return int(value)
