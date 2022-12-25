import random
l=['ROCK','PAPER','SCISSORS']
countp=0
countc=0
print("1.ROCK\n2.PAPER\n3.SCISSORS")
n=input("Enter you choice: ").upper()
e=random.choice(l)
print("Computer's choice: ",e)
while True:
    if(e==n):
        print("DRAW")
    elif(e=='ROCK')and(n=="PAPER"):
        countp=countp+1
        print("You WIN!!")
    elif (e == 'ROCK') and (n == "SCISSORS"):
        countc=countc+1
        print("Computer WON!!")
    elif (e == 'SCISSORS') and (n == "PAPER"):
        countc=countc+1
        print("Computer WON!!")
    else:
        countp = countp+1
        print("You WIN!!")
    break
print('Times computer won:- ',countc)
print('Times you won:- ',countp)
if(countc==countp):
    print("It's a DRAW, DAMNN!!")
elif(countc>countp):
    print("The computer won more matches than you")
else:
    print("You won more matches than computer")
