import csv
l=input("Enter the column name:")
with open('txt.csv') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print(row[l])
