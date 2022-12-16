year=int(input("Enter the year to be checked: "))
if(year%4)==0 or (year%100)==0 and (year%400)==0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")