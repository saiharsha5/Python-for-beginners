def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped =True
        if not swapped:
            break
    return arr
arr=[3,24,567,8,4,2,1]
k=bubble_sort(arr)
print(k)
