list=list(map(int,input("Enter the list ").split()))
print(f"Sorted list{sorted(list,reverse=True)[-3:]}")