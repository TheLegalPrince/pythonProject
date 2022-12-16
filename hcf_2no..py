#Greatest Common Divisior
a=int(input("Enter the first number "))
b=int(input('Enter the second number '))

'''Either use the min() function below or use a conditional statement with if else which is -
if a<b:
a=small
else:
b=small'''

for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        hcf=i
print('HCF is',hcf)