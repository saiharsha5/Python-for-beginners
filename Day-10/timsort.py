arr=[64,34,25,12,22,11,90]

# python built in Tim sort O(n log n)

arr.sort()
arr.sort(reverse=True)
s=sorted(arr)
print(s)

#sort by key 

words=['banana','apple','cherry']
words.sort(key=len)
print(words)