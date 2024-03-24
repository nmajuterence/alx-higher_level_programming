#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        # for a negative number
        lastDigit = number % -(10)
        print(-(lastDigit), end="")
    else:
        # for a positive number
        lastDigit = number % 10
        print(lastDigit, end="")
    return abs(lastDigit)
print()
