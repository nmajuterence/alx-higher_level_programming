#!/usr/bin/python3
"""this function converts a
Roman numeral to an integer."""


def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) is not str:
        return 0
    rndata = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integers = [rndata[y] for y in roman_string] + [0]
    rment = 0

    for x in range(len(integers) - 1):
        if integers[x] >= integers[x+1]:
            rment += integers[x]
        else:
            rment -= integers[x]

    return rment
