#!/usr/bin/python3
for i in range(10):
    for b in range(i + 1, 10):
        print("{}{}".format(i, b), end="")
        if i + 1 < 9:
            print(", ", end="")
print("")
