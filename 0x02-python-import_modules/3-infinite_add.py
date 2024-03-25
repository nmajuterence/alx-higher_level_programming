#!/usr/bin/python
if __name__ == "__main__":
    # the program add an infinite len of integers
    import sys

    total = 0
    for x in range(len(sys.argv) - 1):
        total += int(sys.argv[x + 1])
    print("{}".format(total))