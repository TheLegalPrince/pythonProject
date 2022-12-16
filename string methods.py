'''k=str(input("Enter the string to be operated upon: "))
print("The uppercase string is: ", k.upper())
print("The lowercase string is: ", k.lower())
print("The capitalized string is: ", k.capitalize())
print("The titled string is: ", k.title())
print("The case-swappped string is: ", k.swapcase())

s = input("Enter the string: ")
k=''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        k=k+chr(ord(i))-32
    else:
        k=k+i
'''
n=str(input("Enter the 1st string: "))
j=str(input("Enter the 2nd String: "))
print("The final string after splitting is: ",n.split(), j.split())