l=[20,22,23,34,45,67,88]

print("original list: ",l)

l.append(255)
print("after append: ",l)

l.insert(3,"Raj")
print("Inserted : ",l)

l.pop()
print("pop ",l)

l.remove(23)
print(l)

print(l.index(67))

l.reverse()
print(l)

print(l.reverse())


front_end= ['html','css','js','bs','react']
lang=['python','django','flask','nodejs']

print("front_end tech",front_end)
print("languages ",lang)

lang.extend(front_end)
print("all tech : ",lang)


# count method

list=[1,2,3,4,5,6,1,2,1,2,1]
print(list.count(1))

list.sort()
print(list)

list.clear()
print(list)