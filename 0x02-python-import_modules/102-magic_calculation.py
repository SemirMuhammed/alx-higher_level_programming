#!/usr/bin/python3
from dis import dis


def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        return c
    return sub(a, b)

dis(magic_calculation)
