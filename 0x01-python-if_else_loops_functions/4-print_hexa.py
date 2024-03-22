#!/usr/bin/python3
for i in range(99):
    print("{:d} 0x{:02X}".format(i, i), end='\n' if i % 10 == 9 else ' ')
