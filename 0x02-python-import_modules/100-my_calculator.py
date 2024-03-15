#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = argv[1]
    b = argv[3]
    operator = argv[2]
    for key, value in operators.items():
        if key == operator:
            print("{} {} {} = {}".format(a, key, b, value(int(a), int(b))))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
