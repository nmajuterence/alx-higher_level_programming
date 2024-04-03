#!/usr/bin/python3
"""analyze the bytecode and
replicate its behavior in Python code."""


def magic_calculation(a, b):
    result = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            result += (a ** b) / x
        except:
            result += a + b
            break
    return result
