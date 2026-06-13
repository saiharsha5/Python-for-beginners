month=int(input("Enter the month number: "))

if(month>=1 and month<=12):
    print(month,"is a valid month")
else:
    print(month, " is not a valid month")

if (month in [1,3,5,7,8,10,12]):
    print(month ," has 31 days")
elif(month in [4,6,9,11]):
    print(month," has 30 days")
elif(month==2):
    print(month," has 28 or 29 days")
else:
    print("month number is invalid")
