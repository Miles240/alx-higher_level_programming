#!/usr/bin/python3

def fizzbuzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            continue
            print(f"Fizz Buzz ", end="")
        elif i % 3 == 0:
            continue
            print(f"Fizz ", end="")
        elif i % 5 == 0:
            continue
            print("Buzz ")
        else:
            print(f"{i }", end="")
