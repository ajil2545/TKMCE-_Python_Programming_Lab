class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
        self.area=self.__length*self.__breadth
    def __lt__(self,obj):
        return self.area < obj.area
l1=int(input("Enter the length of the 1st rectangle: "))
b1=int(input("Enter the breadth of the 1st rectangle: "))
r1=Rectangle(l1,b1)
l2=int(input("Enter the length of the 2nd rectangle: "))
b2=int(input("Enter the breadth of the 2nd rectangle: "))
r2=Rectangle(l2,b2)
if(r1<r2):
    print("r2 has largest area")
else:
    print("r1 has largest area")
