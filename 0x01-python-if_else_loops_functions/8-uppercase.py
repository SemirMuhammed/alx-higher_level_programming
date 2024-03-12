#!/usr/bin/python3

def uppercase(str):
    str_upper = ""
    for c in str:
        ASCII_code = ord(c)
        if ASCII_code > 96 and ASCII_code < 123:
            str_upper += chr(ord(c) - 32)
        else:
            str_upper += c
    print("{}".format(str_upper))

    return str
