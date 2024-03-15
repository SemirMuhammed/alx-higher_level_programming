#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    print("{} {}".format(argc, "argument" if argc == 1 else "arguments"), end="")
    print("{}".format("." if argc == 0 else ":"))
    if argc > 0:
        i = 1
        for arg in argv[1:]:
            print("{} : {}".format(i, arg))
            i += 1
