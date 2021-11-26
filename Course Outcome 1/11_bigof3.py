print("Enter three number")
a=float(input())
b=float(input())
c=float(input())
if((a<c)and(b<c)):
    print("Greater number is ",c)
elif((a>c)and(a>b)):
    print("Greater number is ",a)
else:
    print("Greater number is ",b)
