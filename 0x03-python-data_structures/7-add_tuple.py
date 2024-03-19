#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract elements from the tuples, using 0 if a tuple is smaller than 2
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Perform addition for each element and return the result as a tuple
    return (a[0] + b[0], a[1] + b[1])
