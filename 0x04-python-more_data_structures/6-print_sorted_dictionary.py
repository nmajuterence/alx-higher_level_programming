#!/usr/bin/python3
"""function that prints a
dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    newSorted = sorted(a_dictionary)
    for j in newSorted:
        print(f"{j}: {a_dictionary[j]}")
