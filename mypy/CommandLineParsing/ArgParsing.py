import argparse

parser = argparse.ArgumentParser(description="Argument parsing example using argparse module")
parser.add_argument("-f", "--first_name", default="first_name_not_given", help="First Name", type=str)
parser.add_argument("-l", "--last_name", default="last_name_not_given", help="Last Name", type=str)
parser.add_argument("-a", "--age", choices=[n for n in range(1, 100)], help="Age", type=int, required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose on")
args = parser.parse_args()

print("first_name:", args.first_name)
print("last_name", args.last_name)
print("age", args.age)
print("verbose on?", args.verbose)
