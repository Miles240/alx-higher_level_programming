#!/usr/bin/python

from add_0 import add

a = 1
b = 2

print(int("{} + {} = {}").format(a, b,( add(a, b))))

if __name__ == "__main__":
    add(a, b)
