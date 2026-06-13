print("Program starts...")
a=10
print("a=",a)
try:
    print(a/0)
except ZeroDivisionError as e:
    print("not possible to divide with zero if you divide it gives",e)
print("program ends")