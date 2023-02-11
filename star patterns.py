'''n=int(input('Input the no. of lines you want to print '))
for i in range (0,n):
    for j in range(0,i+1):
        print("*",end=' ')
    print ("\r")'''

'''n=int(input("Enter the number of lines you want to print "))
k=2*n-2
for i in range (1,n):
    for j in range(0,k):
        print(end=' ')
    for k in range (0,i+1):
        print("*",end=" ")
    print("\r")'''

'''n=int(input('Enter the number of lines you want to print '))
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range (1,2*(n-i)+2):
        print("*",end=' ')
    print()'''
'''
n = int(input("Enter the number of lines you want to print:"))
k = 0
for i in range(1, n + 1):
    for j in range (1, (n - i)):
        print(" ",end = " ")
    while k != (2 * i - 1):
        print("*", end = " ")
        k = k + 1
    k = 0   
    print()  
 
k = 2
m = 1
for i in range(1, n):
    for j in range (1, k):
        print(" ",end = " ")
    k = k + 1	  
    while m <= (2 * (n - i)-1):
        print("*", end = " ")
        m=m+1
    m = 1
    print()
'''
'''
# pyramid star pattern
n = int(input("Enter the number of lines you want to print: "))
for i in range(n):
    for j in range(n-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()
    '''
'''
# hollow diamond star pattern
n = 5
# upward hollow pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
'''#V shape
n=5
for i in range(n):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()'''
'''
# inverted hollow triangle
n = int(input("Enter rows: "))
for a in range(1, n + 1):
    for b in range(1, a + 1):
        print("*", end='')
    for s in range(n - a):
        print(" ", end='')
    for c in range(a, 0, -1):
        print("*", end='')
    print()
'''
print("    *")
print('   * *')
print('  *   *')
print(' *     *')
print('* * * * *')