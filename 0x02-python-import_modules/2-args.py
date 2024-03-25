#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    def print_arguments():
        num_args = len(sys.argv) - 1

        if num_args == 0:
            print("0 argument(s).")
            print(".")
        else:
            print("{} argument(s):".format(num_args))
            for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))


    print_arguments()
