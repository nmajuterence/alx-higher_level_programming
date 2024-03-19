#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:  # Check if sentence is empty
        return (0, None)  # Return (0, None) if sentence is empty
    else:
        return (len(sentence), sentence[0])  # Return length and first character
