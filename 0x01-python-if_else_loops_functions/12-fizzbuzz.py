#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print(f"Fizz Buzz ", end=" ")
            continue
        elif i % 3 == 0:
            print(f"Fizz ", end=" ")
            continue
        elif i % 5 == 0:
            print("Buzz ", end=" ")
            continue
        else:
            print(f"{i }", end=" ")
