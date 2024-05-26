import re

mail = input("Email address?")
mail_pattern = re.compile(r"^([\w.]+)@([\w.]+)$")


def printMatch(match):
    print(match)
    print(match[0])
    print(match[1])
    print(match[2])
    print("...alternatively, using match.groups()...")
    for group in match.groups():
        print(group)


# re.search tries to find a match anywhere in the input string
# unless the pattern is anchored then re.search & re.match behaves alike
print("\n>>> re.search()")
if m1 := re.search(mail_pattern, mail):
    print("Valid and is", len(mail), "long")
    printMatch(m1)
else:
    print("Invalid")

# re.match tries to find a match at the beginning of the input string
# unless the pattern is anchored then re.search & re.match behaves alike
print("\n>>> re.match()")
# walrus operator ;}
if m2 := re.match(mail_pattern, mail):
    printMatch(m2)
else:
    print("Invalid")

# re.findall tries to find all possible matches in the input string as a list!!!
# unless the pattern is anchored then re.findall, re.search & re.match behaves alike
print("\n>>> re.findall()")
# walrus operator ;}
if listOfTuples := re.findall(mail_pattern, mail):
    print("list of matches:", listOfTuples)
    for t in listOfTuples:
        print("tuple:", t)
        for g in t:
            print("captured group:", g)
else:
    print("Invalid")

# Same as re.findall but returns an iterable Match object
print("\n>>> re.finditer()")
# walrus operator ;}
if it := re.finditer(mail_pattern, mail):
    for m in it:
        printMatch(m)
else:
    print("Invalid")
