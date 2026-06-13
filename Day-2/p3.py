num=int(input("Enter a number: "))
count=0
rem=0
while num!=0:
    rem=num%10
    count+=1
    num=num//10
print("Number of digits: ",count)