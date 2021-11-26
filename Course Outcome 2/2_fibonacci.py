n=int(input("Enter the number: "))
f=0
s=1
if(n>2):
    i=3
    print("Fibonacii Series: \n")
    print(f)
    print(s)
    while(i<=n):
        t=f+s
        f=s
        s=t
        print(t)
        i=i+1
elif(n==2):
    print("Fibonacii Series: \n")
    print(f)
    print(s)
elif(n==1):
    print("Fibonacii Series: \n")
    print(f)