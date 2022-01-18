class Employee:
    def __init__(self, name, salaryperday):
        self.name=name
        self.salaryperday=salaryperday
    def salarycal(self,days):
        self.days=days
        self.salary=self.salaryperday * self.days
        return (self.salary)
    #def __mul__(self, days):
    #    self.days=days
    #def __lt__(self, e2):

emp1= Employee("AROMAL", 1000)
print(emp1.salarycal(int(input("Enter the number of days worked: "))))
emp2= Employee("BIJIL", 1200)
print(emp2.salarycal(int(input("Enter the number of days worked: "))))
print(emp1 < emp2)