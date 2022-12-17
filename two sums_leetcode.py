num=[]
for x in range(4):
    x=int(input("Enter the list elements: "))
    num.append(x)
print(num)
n=int(input("Check the no. you want to check: "))
for i in range(len(num)):
    for j in range(i+1,len(num)-1):
        if num[i]+num[j]==n:
            print('The indexes are - ',i,j)
            break