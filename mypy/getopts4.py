#!/usr/bin/python3

import getopt
import sys
from typing import List, Tuple

first_name = "undefined"
sur_name = "undefined"


def usage():
    print("Usage: ", sys.argv[0], "--help --first_name <first_name> --sur_name <sur_name>")
    exit(1)


def parse_args():
    global first_name
    global sur_name
    opts: list[tuple[str, str]]

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'hf:s:',
            ['help', 'first_name=', 'sur_name='],
        )
    except getopt.GetoptError as err:
        print(err)
        usage()
        exit(1) # to avoid intellij warning

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-f', '--first_name'):
            first_name = arg
        elif opt in ('-s', '--sur_name'):
            sur_name = arg
        else:
            assert False, "unknown option ;("

    print("first_name", first_name)
    print("sur_name", sur_name)


def main():
    parse_args()
    print("first_name", first_name)
    print("sur_name", sur_name)


if __name__ == "__main__":
    main()
