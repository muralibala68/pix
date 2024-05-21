#!/usr/bin/python

def main():
    print("Hello, World!")
    print("__name__: ", repr(__name__))
    #    print("__code__: ", repr(__code__))
    another()


def another():
    print("Hello, World!")
    print("__name__: ", repr(__name__))


#    print("__code__: ", repr(__code__))


main()
