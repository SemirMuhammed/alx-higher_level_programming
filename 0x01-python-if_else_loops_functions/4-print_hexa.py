#!/usr/bin/python3

for number in range(99):
    print("{} = 0x{}".format(format(number, 'd'), format(number, 'x')))
