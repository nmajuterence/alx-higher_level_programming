#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if index is negative
    if idx < 0:
        return my_list

    # Check if index out of range
    if idx >= len(my_list):
        return my_list

    # Replace an element at a specified index
    my_list[idx] = element
    return my_list
