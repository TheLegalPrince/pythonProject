import time
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

n=int(input("Enter the range: "))
if n > 0:
    print("Fibonacci sequence:")
    for i in range(n):
        time.sleep(.2)
        print(fibo(i))
else:
    print("WRONG VALUE!!")
