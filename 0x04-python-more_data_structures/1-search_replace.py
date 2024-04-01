#!/usr/bin/python3
"""function that replaces
all occurrences of an element
by another in a new list."""


def search_replace(my_list, search, replace):
    newList = list(my_list)
    for x in range(len(newList)):
        if newList[x] == search:
            newList[x] = replace
    return newList
