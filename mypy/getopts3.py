#!/usr/bin/python3

import getopt
import sys


def usage():
    print("Usage: ", sys.argv[0], "--help --first_name <firstName> --sur_name <surName>")
    exit(1)


def main():
    print("Trying out getopt feature")

    # should work with both short and long options
    opts, args = getopt.getopt(
        sys.argv[1:],
        'hf:s:',
        ['help', 'first_name=', 'sur_name='],
    )

    first_name = 'undefined'
    sur_name = 'undefined'

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        if opt in ('-f', '--first_name'):
            first_name = arg
        if opt in ('-s', '--sur_name'):
            sur_name = arg

    print("first_name", first_name)
    print("sur_name", sur_name)


main()
