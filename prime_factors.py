def prime_factors(n):
    l=[]
    i=2
    while i<=n:
        if n%i==0:
            l.append(i)
            n=n/i
        else:
            i+=1
    return l
num=int(input("Enter the number: "))
print ('The prime factors are: ',prime_factors(num))