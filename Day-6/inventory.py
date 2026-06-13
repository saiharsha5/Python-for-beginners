list1=list(map(int, input("Godown 1: ").split()))
list2=list(map(int, input("Godown 2: ").split()))
print(f"Merged: {list(set(list1+list2))} | Total: {len(set(list1+list2))}")
