#!/usr/bin/python3
"""Write a function that prints
an integer and logs a value err
to stderr"""
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=stderr)
        return False
    else:
        return True
