import numpy as np
l=[]
n=int(input("How many elements do you want to enter- "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
print(l)
print(np.array(l))
print(l)
print(np.shape(l))