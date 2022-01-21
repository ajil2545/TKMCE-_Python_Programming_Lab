class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __lt__(self,obj):
        return self.salary < obj.salary

emp1=Employee("Vishnu",30000)
emp2=Employee("Akshay",25000)
if(emp1<emp2):
    print("emp2 has more salary")
else:
    print("emp1 has more salary")