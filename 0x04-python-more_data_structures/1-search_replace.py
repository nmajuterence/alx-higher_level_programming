#!/usr/bin/python3
"""function that replaces
all occurrences of an element
by another in a new list."""


def search_replace(my_list, search, replace):
    newList = list(my_list)
    for i in range(len(newList)):
        if newList[i] == search:
            newList[i] = replace
    return newList
