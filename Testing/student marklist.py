#display the details of the student (name,rollno,mark1,mark2,mark3,total%)
class Student:
    def __init__(self, name, roll, mark1, mark2, mark3, total):
        self.name = name
        self.roll = roll
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.total=total
def display(s):
    print(s.name,"\t",s.roll,"\t",s.total,"%\n")
studentlist=[]
n=int(input("Enter the number of students: "))
for i in range(0,n):
    fullname=input("Enter the Name: ")
    rollno=input("Enter the Roll no: ")
    m1=int(input("Enter the Mark1: "))
    m2=int(input("Enter the Mark2: "))
    m3=int(input("Enter the Mark3: "))
    t=((m1+m2+m3)/300)*100
    studentlist.append(Student(fullname,rollno,m1,m2,m3,t))
print("\n\nList\n")
for i in range(0,n):
    display(studentlist[i])