#python program to write a append content of one file on another file. 
#write a python function to capitalize each word in a file.
file1=open("text.txt","r")

file2=open("newtxt.txt","a")
list1=file1.read()
print("\nContents in 'text.txt'\n")
print(list1)
file1.close()
for i in range(0,len(list1)):
    file2.write(list1[i])
file2.close()
file2=open("newtxt.txt","r")
list2=file2.read()
print("\nContents in 'newtxt.txt'\n")
print(list2)
file2.close()