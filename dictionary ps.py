import string
'''
#program to print the grades based on numbers
n=int(input("Enter the iterations: "))
while(n<=4):
    if(n==1):
        print("1 = Poor")
    elif(n==2):
        print("2 = Good")
    elif (n==3):
        print("3 = V.Good")
    elif (n==4):
        print("4 = Excellent")
    n=n+1
'''

'''
#to print a dictionary
d={}
n=int(input("Enter the number of elements/keys you want the dictionary for: "))
for i in range(1,n+1):
    d[i]=i*i
    print(d)
'''
'''
#fibonacci series
d={}
n=int(input("Enter the number of elements/keys you want the dictionary for: "))
a=0
b=1
for i in range(1,n+1):
    for j in range(n):
        c=a+b
        a=b
        b=c
    d[i]=b
print(d)
'''
''''
#alphabet lowercase=key & uppercase=value
d = {}
for i in string.ascii_lowercase:
    for j in string.ascii_uppercase:
        if (i.upper()==j):
            d[i]=j
        else:
            continue
print(d)
'''

#string with no. occurrence
s=input("Enter a string: ")
l=[s]
d={}
for i in range(len(s)):
    d[i]=s[i]
print(d)