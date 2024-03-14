#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    if len(argv) > 1:
        for number in argv[1:]:
            sum += int(number)
    print(sum)
