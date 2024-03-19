#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:  # Check if empty
        return (0, None)  # Return (0, None) if empty
    else:
        return (len(sentence), sentence[0])
