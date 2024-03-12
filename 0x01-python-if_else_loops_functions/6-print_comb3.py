#!/usr/bin/python3

for first_digit in range(8):
    for last_digit in range(first_digit + 1, 10):
        print(f"{first_digit}{last_digit}", end=", ")

print(89)
