
lst=[]
p=7

for i in range(p):
    ele=int(input(f'Enter the revenue for day {i+1}: '))
    lst.append(ele)
print(f"Total Revenue :{sum(lst)} | Best day :{max(lst)} | Worst day :{min(lst)}")



# simple logic

revenue=list(map(int,input("Enter the revenue for 7 days: ").split()))
print(f"Total Revenue :{sum(revenue)} | Best day :{max(revenue)} | Worst day :{min(revenue)}")
