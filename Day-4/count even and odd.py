list=[]

size=int(input("Enter size of list: "))

for i in range(size):
    n=int(input("Enter the elements: "))
    list.append(n)
print(list)
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
