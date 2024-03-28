#!/usr/bin/python3
"""magic calculator in python"""
if __name__ == "__main__":
    from magic_calculation_102 import add, sub

    def magic_calculation(a, b):
        if a < b:
            c = sub(a, b)
            return (c)
        else:
            for i in range(4, 6):
                c = add(c, i)
            return (c)
