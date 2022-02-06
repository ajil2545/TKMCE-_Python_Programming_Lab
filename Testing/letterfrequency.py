import csv
csvfile=open("letters.csv","w")
writer=csv.DictWriter(csvfile, fieldnames=["Letter", "Number"])
writer.writeheader()
string="button"
dict = {}
for n in string:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
for i in dict:
    writer.writerow({"Letter": dict[i], "Number": dict[i]})