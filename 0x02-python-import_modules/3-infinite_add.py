#!/usr/bin/python
if __name__ == "__main__":
    # the program add an infinite len of integers
    import sys

    totalAddition = 0
    for x in range(len(sys.argv) - 1):
        totalAddition += int(sys.argv[x + 1])
    print("{}".format(totalAddition))
