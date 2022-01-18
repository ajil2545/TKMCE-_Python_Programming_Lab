#python function to check whether a string is palindrome or not
def palindrome():
    string=input("Enter the string: ")
    return string == string[::-1]
check=palindrome()
if check:
    print("String is Palindrome")
else:
    print("String is not Palindrome")