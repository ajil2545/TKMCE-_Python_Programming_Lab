import csv
with open('csvfile.csv') as csv_file:
    data=csv.reader(csv_file)
    for i in data:
        print(i)