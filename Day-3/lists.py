
# indexing of lists
#     0   1   2   3   4   5   6   7   8   9
roll=[1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
#    -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

print(roll)
# deleting an element in a list

del roll[0]
print(roll)

print("++++++++++++++")

del roll[4]
print(roll)




#using while loop
i=0
while i<len(roll):
    print(roll[i])
    i+=1


for i in range(len(roll)):
    print(f"index {i}: {roll[i]}")



for i in roll:
    print(i)    


'''
print("accessing the list using the positive indexing: ")

print(roll[0])
print(roll[1])
print(roll[2])

print("accessing the list using the negative indexing: ")

print(roll[-6])
print(roll[-5])

'''