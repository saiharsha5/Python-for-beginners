std={
    101:'scott',102:'queen',103:'king',104:'tiger'
}

print(std)
std[106]='xyz'
print(std)

del std[101]
del std[106]
print(std)

print(101 in std)
print(104 in std)
print(105 in std)
print(106 not in std)

print(std.values())
print(std.keys())

