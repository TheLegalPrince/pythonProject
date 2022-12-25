if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}
    s=0
    l=[]
    for _ in range(n):
        name, *line = input("Enter the name and scores: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Which student's average mark you want to check: ")
    k=list(student_marks.keys())
    print(k)
    for i in range(len(k)):
        if query_name==k[i]:
            l=student_marks.get(query_name)
    for j in l:
        s=s+j
    print(s/len(l))