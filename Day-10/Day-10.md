# Day-10







#### Arrays



&#x09;\~ An array is a collection of elements stored at contiguous memory locations , all of same data type , accessed via a numeric index starting from 0.

&#x09;\~ array is homogeneous means stores only one datatype



\-> Array stores elements in contiguous (side by side) memory blocks

\-> If the base address is 1000 and each integer takes 4 bytes





* Address = Base + i \* size of (data type)



size of int = 4bytes





#### Array Traversal :



&#x09;	-> Traversal means visiting every element exactly onces - from index 0 to n-1

&#x09;	-> Time Complexity for array traversal is O(n)



SEARCHING ALGORITHMS:



1. Linear search : check every element from start to end - one by one, the **simplest search** that works on any list  O(n)
2. Binary search : Divide a sorted list in half each step. Eliminates half the data every comparison - **super fast  O(log n)**
3. Jump search : Jump ahead sqrt(n), then scan back linearly. a sweet spot b/w linear and binary search            O(sqrt(n))
4. Interpolation search : smarter than binary search







Linear search :



def linear\_search(arr,target):

&#x20;   for i in range (len(arr)):

&#x20;       if arr\[i]==target:

&#x20;           return i

&#x20;   return -1

arr=\[14,23,456,75,3,2,4,5]

target=4

idx=linear\_search(arr,target)

print(idx)





EXapmles of linear search :



1. contact search
2. playlist scan
3. cart check
4. text search







Binary search :



def binary\_search(arr,target):

&#x20;   left=0

&#x20;   right=len(arr)-1



&#x20;   while left<=right:

&#x20;       mid=(left+right)//2



&#x20;       if arr\[mid]==target:return mid

&#x20;       elif arr\[mid] < target: left=mid+1

&#x20;       else:right=mid-1



&#x20;   return -1

\#arr=\[14,24,56,89,3,2,578,56,5]

arr=\['a','f','e','y','u']

target='f'

\#target=249

k=sorted(arr)

print(k)

m=binary\_search(k,target)

print(m)





Example:

1. git bisect
2. game high score
3. npm versions
4. dictionary lookups







##### Divide \& conquer :



\-> Split a problem into independent subproblems, solve each recursively then merge results.

\-> the sub problem must not over lap what it distuinguish 



##### Dynamic programming:



\-> Breaking overlapping subproblems into a table. solve each once and reuse



##### Greedy algorithm:



\-> make the locally optimal choice at each step, betting it leads to a globally optimal soultions.









NumPy Arrays:  



\-> NumPy ndarray is a typed , fixed size,multi-dimensional array .

\-> It's 10-100x faster than python lists for numerical work because operations are vectorized in c,

\-> All elements must be the same dtype.








n dim array's:



Zero dim - \[9]

one dim - \[1,23,5,3]

two dim - \[\[1,2,3],\[2,4,1]]

three dim - \[\[\[1,2,3],\[4,5,6]],\[\[2,5,7],\[65,4,3]]]

































































