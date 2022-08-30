#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (matrix)
    for i in matrix:
        for a in i:
            print("{:d}".format(a), end=' ')
        print()
