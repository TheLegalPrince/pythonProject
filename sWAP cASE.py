def swap_case(s):
    lst = []
    for i in s:
        if i.islower():
            lst.append(i.upper())
        else:
            lst.append(i.lower())
    return "".join(lst)

if __name__ == '__main__':
    s = input("Enter the string: ")
    result = swap_case(s)
    print('The string with swapped case is:',result)