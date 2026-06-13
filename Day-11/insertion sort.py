def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key=arr[i]
        print("initial : ",arr)
        print("key : ",key)
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print("after : ",arr)
        print("=================================")
    return arr
insertion_sort([50,22,1,4,55,3])


# Complexity Best=O(n) ,  avg= O(n**2) , worst = O(n**2) ,, space = O(1)