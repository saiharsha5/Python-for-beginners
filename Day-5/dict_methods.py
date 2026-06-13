colors={

}
keys=(101,102,103)
values='red'
print(colors.fromkeys(keys,values))


std={
    101:'scott',102:'queen',103:'king',104:'tiger',105:'virat'
}
print(std.get(101))
print(std.get(105))
print(std[105])
print(std.items())

std.update({102:'ram'})
print(std)

std.pop(103)
print(std)
print(std.popitem())
print(std)


std.setdefault(107,'null')
print(std)