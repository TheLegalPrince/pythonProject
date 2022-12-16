#finding the runner up
n = int(input("Enter the number of scores: "))
arr = map(int, input("Enter the scores: ").split())
l=sorted(set(arr))
print(l[-2])