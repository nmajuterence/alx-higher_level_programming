#!/usr/bin/python3
"""function that returns a
new dictionary with all values
multiplied by 2"""


def multiply_by_2(a_dictionary):
    multdict = dict(a_dictionary)
    for i, j in multdict.items():
        multdict[i] = j * 2
    return multdict
