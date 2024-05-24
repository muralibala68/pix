import csv


def get_input() -> []:
    name = input("Name? ")
    address = input("Address? ")
    return [name, address]


with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    row = get_input()
    print(row)
    writer.writerow(row)
