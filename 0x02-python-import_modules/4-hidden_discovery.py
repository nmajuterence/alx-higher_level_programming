#!/usr/bin/python3
"""This program prints
all named functions in
a compiled file."""

if __name__ == "__main__":
    from hidden_4 import *
    namedfs = dir()
    for x in range(0, len(namedfs)):
        if namedfs[x][:2] == "__":
            continue
        else:
            print("{}".format(namedfs[x]))
