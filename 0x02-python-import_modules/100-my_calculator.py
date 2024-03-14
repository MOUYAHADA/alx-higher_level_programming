#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }

    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
