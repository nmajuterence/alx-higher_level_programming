#!/usr/bin/python3
if __name__ == "__main__":
    from magic_calculation import add, sub
    def magic_calculation(a, b):
        if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(c, x)
            return (c)
        else:
            return (sub(a, b))
