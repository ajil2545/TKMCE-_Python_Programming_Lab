n=int(input("Enter the number: "))
i=n
fact=1
while(i>0):
    fact=fact*i
    i-=1
print("Factorial is", fact)