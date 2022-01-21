#program to copy odd lines of one file to other.

file1=open("text.txt","r")
file2=open("newfile.txt", "w")
list1=file1.readlines()
print("\nContents in 'text.txt'\n")
for i in range(0,len(list1)):
    print("Line",i+1,": ",list1[i])
file1.close()

#code for writing content on file
for i in range(0,len(list1)):
    if  i%2==0:
        file2.write(list1[i])
file2.close()

file2=open("newfile.txt", "r")
list2=file2.readlines()
print("\nContents in 'newfile.txt'\n")
for i in range(0,len(list2)):
    print("Line",i+1,": ",list2[i])
file2.close()