import csv
fields = ['Name','MFC','DC','DS','ASE']
rows = [['Gokul Krishna',89,90,92,91],
        ['Rohit R',88,90,85,85],
        ['Aravind A',90,63,70,80],
        ['Abinav Raj',90,92,95,99],
        ['Nithin S',80,75,78,80],
        ['Sadique Samad',85,90,83,96],
        ['Abhijith M',81,90,96,98],
        ['Rahul Raj',39,56,78,88],
        ['Ajay R',56,67,87,92],
        ['Arfaz A',67,74,88,65]]
file1="Testing/student.csv"
with open(file1,'w') as csvfile:
    write=csv.writer(csvfile)
    write.writerow(fields)
    write.writerows(rows)
avgmfc=0
avgdc=0
avgds=0
avgase=0
with open('Testing/student.csv') as csv_file:
    data=csv.DictReader(csv_file)
    print("-----Average of each student-----")
    for row in data:
        print(row['Name'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100)
        avgmfc=avgmfc+int(row['MFC'])
        avgdc=avgdc+int(row['DC'])
        avgds=avgds+int(row['DS'])
        avgase=avgase+int(row['ASE'])
print("\n-----Average of subjects-----")
print("MFC: ",avgmfc/10)
print("DC: ",avgdc/10)
print("DS: ",avgds/10)
print("ASE: ",avgase/10)