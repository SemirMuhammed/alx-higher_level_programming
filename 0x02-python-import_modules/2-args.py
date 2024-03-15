#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv) - 1
    print("{} {}".format(ac, "argument" if ac == 1 else "arguments"), end="")
    print("{}".format("." if ac == 0 else ":"))
    if ac > 0:
        i = 1
        for arg in argv[1:]:
            print("{} : {}".format(i, arg))
            i += 1
