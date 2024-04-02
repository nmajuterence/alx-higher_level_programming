#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    itemsnum = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]))
            itemnum += 1
    except IndexError:
        pass
    print()