arr=[10,20,30,40]

#append - insert at END O(1)
arr.append(50)
print(arr)

# Insert at index O(n)
arr.insert(2,55)
print(arr)

#Extend - add multiple O(k)
arr.extend([60,70])
print(arr)

# +operator - concatenate O(n+m)
new_arr=arr+[80,90]
print(new_arr)