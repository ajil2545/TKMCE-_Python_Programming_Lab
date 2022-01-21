#program to read a file line by line and store it into a list.
read=open('textfile.txt','r')
list=read.readlines()
print("List: ",list)
for i in range(0,len(list)):
    print("Line",i+1,": ",list[i])