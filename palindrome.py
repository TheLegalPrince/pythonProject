x=int(input("Enter the number: "))
v=str(x) == str(x)[::-1]
if(v==True):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")