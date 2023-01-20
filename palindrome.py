x=input("Enter the string/number: ")
v=x==x[::-1]
if(v==True):
    print("This is a palindrome element")
else:
    print("This is not a palindrome element")