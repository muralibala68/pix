#!/usr/bin/python3

import sys


def main():
    print("sys.argv[0]:", sys.argv[0])
    print("sys.argv len:", len(sys.argv))
    if len(sys.argv) > 1:
        print("sys.argv[1]:", sys.argv[1])
    for arg in sys.argv:
        print("arg:", arg)


main()
