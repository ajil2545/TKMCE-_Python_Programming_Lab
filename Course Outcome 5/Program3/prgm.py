import csv
with open('csvfile.csv') as csv_file:
    data=csv.reader(csv_file)
    list=[]
    for i in data:
        list.append(i)
for i in range(0,len(list)):
    print(list[i])
