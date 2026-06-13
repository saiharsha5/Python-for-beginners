def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[14,23,456,75,3,2,4,5]
target=4
idx=linear_search(arr,target)
print(idx)
