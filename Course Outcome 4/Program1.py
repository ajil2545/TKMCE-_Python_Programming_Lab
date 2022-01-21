class Rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return (2*(self.length+self.breadth))
l1=int(input("Enter the length of 1st rectangle: "))
b1=int(input("Enter the breadth of 1st rectangle: "))
r1=Rectangle(l1,b1)
l2=int(input("Enter the length of 2nd rectangle: "))
b2=int(input("Enter the breadth of 2nd rectangle: "))
r2=Rectangle(l2,b2)
a1=Rectangle.area(r1)
p1=Rectangle.perimeter(r1)
a2=Rectangle.area(r2)
p2=Rectangle.perimeter(r2)
print("Area of 1st rectangle: ",a1)
print("Perimeter of 1st rectangle: ",p1)
print("Area of 2nd rectangle: ",a2)
print("Perimeter of 2nd rectangle: ",p2)
if a1>a2:
    print("\n1st rectangle has more area")
elif a1==a2:
    print("\nBoth rectangle has same area")
else:
    print("\n2nd rectangle has more area")