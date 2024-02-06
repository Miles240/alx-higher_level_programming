import csv

with open("Grade book - Overview.csv", "r") as file:
    name = input("name: ")
    writer = csv.writer(file)
    writer.writerow(name)
