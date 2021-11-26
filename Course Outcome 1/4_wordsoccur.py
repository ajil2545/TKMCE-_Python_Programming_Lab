s=input("Enter  one sentence with words repeating\n")
for i in list(set(s.split())):
    print(i,"has occured",s.split().count(i),"times")
