num=[]
for x in range(3):
    x=int(input("Enter the list elements: "))
    num.append(x)
print(num)
n=int(input("Check the no. you want to check: "))
for i in range(len(num)):
    for j in range (i+1,len(num)):
        if num[i]+num[j]==n:
            print('The indexes are - ',i,j)
            break