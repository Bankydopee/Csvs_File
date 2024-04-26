import csv


header = ["id", "name", "age"]

with open("new.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(header)