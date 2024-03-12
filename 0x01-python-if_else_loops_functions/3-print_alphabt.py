#!/usr/bin/python3

for ASCII_code in range(97, 123):
    if format(ASCII_code, 'c') not in {'q', 'e'}:
        print(f"{format(ASCII_code, 'c')}", end="")
