#!/usr/bin/python3

for i in range(0, 10):
    for n in range(1, 10):
        if n > i:
            print("{}{}".format(i, n), end="")
            if i != 8 or n != 9:
                print(", ", end="")
print("")
