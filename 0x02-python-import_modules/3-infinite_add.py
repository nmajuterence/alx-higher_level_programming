#!/usr/bin/python
if __name__ == "__main__":
    import sys

    def addition_of_arguments():
        total = sum(int(arg) for arg in sys.argv[1:])
        print(total)

    addition_of_arguments()
