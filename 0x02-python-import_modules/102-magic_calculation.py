#!/usr/bin/python3
def magic_calculation(a, b):
    from  magic_calculation import add, sub
    if a < b:
        c = add(a, b)
        for x in range(4, 6):
            c = add(a, x)
            return (c)
    else:
        return(sub(a, b))
