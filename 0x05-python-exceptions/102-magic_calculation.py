#!/usr/bin/python3
"""analyze the bytecode and
replicate its behavior in Python code."""


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except:
            result += a + b
            break
    return result