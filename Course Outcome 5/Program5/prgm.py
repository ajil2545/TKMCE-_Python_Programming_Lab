import csv
dict_columns = ['Name','Mark']
dict_rows=[
    {'Name' : 'Abhinav' , 'Mark' : 40},
    {'Name' : 'Akshay' , 'Mark' : 45},
    {'Name' : 'Basith' , 'Mark' : 25},
    {'Name' : 'Kiran' , 'Mark' : 28},
    {'Name' : 'Sreeja' , 'Mark' : 28},
    {'Name' : 'Thomas' , 'Mark' : 22},
    ]
with open('dict.csv' , 'w') as csvwrite:
    write = csv.DictWriter(csvwrite , fieldnames = dict_columns)
    write.writeheader()
    write.writerows(dict_rows)
n=0
with open('dict.csv') as csvread:
    read = csv.DictReader(csvread)
    for data in read:
        if n == 0:
            print(f'{"  ".join(data)}')
            n=n+1
        print(f'{data["Name"]}  {data["Mark"]}')
