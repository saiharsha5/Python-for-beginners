a= int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

if (a>b and a>c):
    print(a,"is the greatest number")
elif(b>a and b>c):
    print(b,"is the greatest number")
else:
    print(c,"is the greatest number")

print(min(a,b,c), "is the smallest number")

if(a<=b<=c )or(c<=b<=a):
    print(b,"is the middle number")
elif(b<=a<=c)or(c<=a<=b):
    print(a,"is the middle number")
else:
    print(c, " is the middle number")