def string(s):
    if len(s)>=3:
        if s[-3:]=="ing":
            print(s+"ly")
        else:
            print(s+"ing")
        return s
    else:
        print(s+'ing')
s=input("Enter the string : ")
string(s)