#!/usr/bin/python
"""function that prints an
integer with "{:d}".format()."""


def safe_print_integer(value):
    try:
            #value = int(value)
            print("{:d}".format(value))
            return True
    except ValueError:
            print(value)
            return False
