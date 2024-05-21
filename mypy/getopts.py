#!/usr/bin/python3

import getopt
import sys


def usage():
    print("Usage: ", sys.argv[0], "--help --firstname <firstName> --surname <surName>")


def main():
    print("Trying out getopt feature")

    opts, args = getopt.getopt(
        sys.argv[1:],
        'hf:s:',
        ['help', 'firstname', 'surname'],
    )

    first_name: str = 'undefined'
    sur_name: str = 'undefined'

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        if opt in ('-f', '--firstname'):
            first_name = arg
        if opt in ('-s', '--surname'):
            sur_name = arg

    print("first_name", first_name)
    print("sur_name", sur_name)


main()
