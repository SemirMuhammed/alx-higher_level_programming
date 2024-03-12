#!/usr/bin/python3

for first_digit in range(10):
    for last_digit in range(10):
        if first_digit and last_digit == 9:
            continue
        print("{}{}".format(first_digit, last_digit), end=", ")

print(99)
