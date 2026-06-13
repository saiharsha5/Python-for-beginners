price=list(map(int,input("Enter the price: ").split()))
new_list=[]
for i in price:
    if i>1000:
        new_list.append(i)
print(new_list)


#Simple

priz=list(map(int,input("Enter the priz: ").split()))
print([i for i in priz if i>1000])