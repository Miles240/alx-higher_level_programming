import csv

# file = open("phonebook.csv", "a")

# name = input("Name: ")
# number = input("Number: ")

# writer = csv.writer(file)

# writer.writerow([name,  number])
# file.close()


with open("Grade book - Overview.csv", "r") as file:
    name = input("name: ")
    writer = csv.writer(file)
    writer.writerow(name)
