def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:return mid
        elif arr[mid] < target: left=mid+1
        else:right=mid-1

    return -1
#arr=[14,24,56,89,3,2,578,56,5]
arr=['a','f','e','y','u']
target='f'
#target=249
k=sorted(arr)
print(k)
m=binary_search(k,target)
print(m)
