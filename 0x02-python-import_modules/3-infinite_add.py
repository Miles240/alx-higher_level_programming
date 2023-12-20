#!/usr/bin/python3

if __name__ == "__main__":
    import sys

counter = 0
num_arg = len(sys.argv) - 1
for i in range(1, num_arg + 1):
    counter += int(sys.argv[i])
print("{}".format(counter))
