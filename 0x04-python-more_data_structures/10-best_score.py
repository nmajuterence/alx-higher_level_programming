#!/usr/bin/python3
"""function that returns
a key with the biggest
integer value."""


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxScore = 0
    for k, v in a_dictionary.items():
        if v > maxScore:
            maxScore = v
    for k, v in a_dictionary.items():
        if v == maxScore:
            return k
