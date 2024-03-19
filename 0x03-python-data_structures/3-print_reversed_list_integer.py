#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    # Iterate through the list in reverse order
    if my_list is None:
        my_list = []
    for i in range(len(my_list) - 1, -1, -1):
        # Print the integer using str.format()
        print(str.format("{}", my_list[i]))

