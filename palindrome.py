x=input("Enter the number: ")
v=x==x[::-1]
if(v==True):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")