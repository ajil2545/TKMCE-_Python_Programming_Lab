class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
        self.area=self.__length*self.__width
    def __lt__(self,obj):
        return self.area < obj.area

r1=Rectangle(20,30)
r2=Rectangle(15,25)
if(r1<r2):
    print("r2 has largest area")
else:
    print("r1 has largest area")