'''
#to print first 10 even numbers in a single line
with open('a.txt', "w+") as f:
    for i in range (1,21):
        if(i%2==0):
            f.write(str(i)+' ')
        else:
            continue
'''
'''
#to print first 10 odd numbers in multiple line
with open('a.txt', "w+") as f:
    for i in range(1, 21):
        if (i % 2 != 0):
            f.write(str(i) + '\n')
        else:
            continue
'''
'''
#to print 5 rando numbers between a given bound
import random
with open('a.txt', "w+") as f:
    for i in range(5):
        f.write(str(int(random.uniform(50,61))) + ' ')
'''
#to calculate the percentage of vowels and consonants in a file
'''
with open('a.txt', "r+") as f:
    v=0
    c=0
    l=str(f.readlines())
    l=l.lower()
    print("The lines in file are =", l)
    for i in range(len(l)):
        if l[i] in ('a', "e", "i", "o", "u"):
            v = v+1
        elif ('a'<=l[i]<='z'):
            c = c+1
print("The number of vowels are = ", v)
print("The number of consonants are = ", c)
print("The vowel's percentage in this file = ", v/26*100,'%')
print("The consonant's percentage in this file = ", c/26*100,'%')
'''
'''
with open('a.txt', "r+") as f:
    l=str(f.readlines())
    print(l)
    c=input("Enter the character you want to search: ")
    count=0
    for i in range(len(l)):
        if (l[i] == c):
            count = count + 1
        else:
            continue
print("The occurence of the character is - ",count)
'''
# to print the longest line in the file
with open('a.txt', "r+") as f:
    l=f.readlines()
    print(l)
    l.sort()
    print(l)
print("The longest line in the file is - ",l[0])