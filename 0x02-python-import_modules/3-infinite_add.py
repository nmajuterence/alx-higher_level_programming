#!/usr/bin/python
if __name__ == "__main__":
    # the program add an infinite len of integers
    from sys import argv

    sum = 0
    for x in range(1, len(argv)):
        sum += int(argv[x])
    print("{}".format(sum))