#!/usr/bin/python3
"""function that deletes keys with
a specific value in a dictionary."""


def complex_delete(my_dict, value):
    dictcopy = my_dict.copy()
    for key, val in dictcopy.items():
        if value == val:
            my_dict.pop(key)
    return my_dict
