import csv


members = []

with open("members.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        members.append(row)

for member in members:
    print("first_name:", member['first_name'], end=" ~!~ ")
    print("sur_name:", member['sur_name'], end=" ~!~ ")
    print("age:", member['age'])
