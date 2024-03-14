#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argv = argv[1:]
    print("{} {}".format(len(argv),
          "argument" if len(argv) == 1 else "arguments"),
          end="")
    if len(argv) > 0:
        print(":")
        for index, value in enumerate(argv):
            print("{}: {}".format(index + 1, value))
    else:
        print(".")
