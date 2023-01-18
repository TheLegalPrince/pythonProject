import numpy as np
l=[]
n=int(input("How many elements do you want to enter- "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
print(np.array(l))
print(np.shape(l))
print(np.reshape(l,(2,2)))