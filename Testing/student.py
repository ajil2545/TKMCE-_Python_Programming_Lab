class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course=course
def display(s):
    print(s.name,"\t",s.roll,"\t",s.course,"\n")
studentlist=[]
n=int(input("Enter the number of students: "))
for i in range(0,n):
    fullname=input("Enter the Name: ")
    rollno=input("Enter the Roll no: ")
    c=input("Enter the Course: ")
    studentlist.append(Student(fullname,rollno,c))
print("\n\nStudents List\n")
for i in range(0,n):
    display(studentlist[i])