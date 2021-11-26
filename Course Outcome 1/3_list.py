l=[-1,-4,-9,0,1,4,-97,2]
m=[x for x in l if x>0]
print("Positive list of numbers:",m)

print("Enter the number of elements:")
n=int(input())
a=[]
b=[]
print("Enter the elements")
for i in range(0,n):
    s=int(input())
    a.append(s)
    b.append(s**2)
print("List : ",a,"\nSquareList : ",b)

v=['a','e','i','o','u']
s=input("Enter a string: ")
o=[x for x in s if x in v]
print("Vowels in ",s," : ",o)

p=[ord(x) for x in s]
print("Ordinal values: ",p)