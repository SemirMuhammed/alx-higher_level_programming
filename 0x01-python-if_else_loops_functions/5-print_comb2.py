#!/usr/bin/python3

for number in range(99):
    print("{}{}".format("0" if number < 10 else "", number), end=", ")

print(99)
