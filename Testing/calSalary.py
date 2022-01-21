class Employee:
    def __init__(self, name, dailysalary):
        self.name=name
        self.dailysalary=dailysalary
class Salary(Employee):
    def __init__(self,name,dailysalary,noDays):
        Employee.__init__(self, name, dailysalary)
        self.noDays=noDays
    def __mul__(self,obj):
        return self.dailysalary*obj.noDays
emp1=Salary("Vishnu",1000,30)
print("Salary of ",emp1.name," is ",emp1*emp1)
emp2=Salary("Gokul",1200,28)
print("Salary of ",emp2.name," is ",emp2*emp2)