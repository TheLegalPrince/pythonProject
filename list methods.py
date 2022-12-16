'''n=int(input("How many elements you want to insert in the list? - "))
l=[]
for i in range(n):
    e=int(input('Enter the elements of the list: '))
    l.append(e)
print(l)'''

l=[]
for i in range(200,500):
    for j in range(2,i-1):
        if(i%j==0):
            break
        else:
          l.append(i)
    i=i+1
print(l)

'''n=int(input("Enter the number of elements of the list- "))
l1=[]
l2=[]
for i in range(n):
    e=int(input('Enter the elements of the list: '))
    l1.append(e)
print('The list is', l1)
l2=l1.copy()
print(l2)
for e in l1:
    if e in l2:
        continue
    else:
        l2.append(e)
print("The list with unique elements is: ", l2)'''