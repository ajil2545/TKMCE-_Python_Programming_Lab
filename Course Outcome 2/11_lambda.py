square=lambda a: a*a
side=int(input("Enter the side of square: "))
print("Area of square: ",square(side))
rectangle=lambda l,b: 2*(l+b)
length=int(input("Enter the length of rectangle: "))
bredth=int(input("Enter the breadth of rectangle: "))
print(rectangle(length,bredth))
triangle=lambda b,h: 0.5*b*h
base=int(input("Enter the base of triangle: "))
height=int(input("Enter the height of triangle: "))
print(triangle(base,height))