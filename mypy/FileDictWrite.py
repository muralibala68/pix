import csv


def get_input() -> {}:
    name = input("Name? ")
    address = input("Address? ")
    return {"name" : name, "address" : address}


with open('students.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'address'])
    row = get_input()
    print(row)
    writer.writerow(row)
