import csv
with open('Course Outcome 5/Program3/csvfile.csv') as csv_file:
    data=csv.reader(csv_file)
    list=[]
    for i in data:
        list.append(i)
print(list)