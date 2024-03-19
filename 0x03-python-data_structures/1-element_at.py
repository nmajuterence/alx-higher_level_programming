#!/usr/bin/python3
def element_at(my_list, idx):
    # Check for invalid index conditions:
    if idx < 0 or idx >= len(my_list):
        return None

    # Index is valid, return the element:
    return my_list[idx]
