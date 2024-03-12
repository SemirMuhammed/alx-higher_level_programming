#!/usr/bin/python3

for i in range(25, -1, -1):
    if i % 2 == 0:
        num = 65
    else:
        num = 97
    print("{}".format(chr(num + i)), end="")
