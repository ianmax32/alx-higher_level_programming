#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for x in range(len(tuple_a)):
        a[x] = tuple_a[x]
    for y in range(len(tuple_b)):
        b[y] = tuple_b[y]
    tuple_return = ((a[0] + b[0]), (b[1] + a[1]))
    return (tuple_return)
