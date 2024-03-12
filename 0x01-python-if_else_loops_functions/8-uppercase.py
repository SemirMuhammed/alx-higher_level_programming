#!/usr/bin/python3

def uppercase(str):
    for c in str:
        ASCII_code = ord(c)
        if ASCII_code > 96 and ASCII_code < 123:
            print(chr(ASCII_code - 32), end="")
        else:
            print(c, end="")
    print("")

    return str
