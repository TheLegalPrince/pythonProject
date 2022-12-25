import random
import time
l=[]
print("-------DICE GAME-------")
n=int(input("How many throws?? "))
for _ in range(n):
    r=random.randint(1,6)
    time.sleep(0.5)
    print('The Computer threw - ',r)
    if(r==6):
        l.append(r)
while (len(l)>0):
    if len(l)%3==0:
        print("LUCKY OH, MY GOD!!!!!")
    else:
        print("Not Lucky")
        break