n=int(input("Enter the number of elements of the list- "))
l1=[]
l2=[]
for i in range(n):
    a=int(input('Enter the elements of the first list: '))
    l1.append(a)
for i in range(n):
    b=int(input("Enter the elements of the second list:"))
    l2.append(b)
c=set(l1)
d=set(l2)
e=c.issubset(d)
if (e==True):
    print("The L2 list is a sublset of L1")
else:
    print("The L2 list is not a subset of L1")