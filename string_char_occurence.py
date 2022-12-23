s = input("Enter the string: ").lower()
d = {}
for i in s:
    d[i]=s.count(i)
print(d)