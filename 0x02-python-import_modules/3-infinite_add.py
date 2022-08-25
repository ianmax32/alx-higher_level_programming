#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    a = 0
    for b in argv[1:]:
        a += int(b)
    print(a)
