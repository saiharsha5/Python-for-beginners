string="pYthOn ProGraMming"

print(string.islower()) # False
print(string.isupper()) # False it's not in uppercase because of the lowercase 'p' in 'pYthOn' and 'ProGraMming'
print(string.istitle()) # False its not in title case because of the lowercase 'p' in 'ProGraMming'
print(string.lower()) # python programming converts all characters to lowercase
print(string.upper()) # PYTHON PROGRAMMING converts all characters to uppercase
print(string.title()) # Python Programming converts first character of each word to uppercase and rest to lowercase
print(string.capitalize()) # Python programming converts first character to uppercase and rest to lowercase
print(string.swapcase()) # PyTHoN pROgRAmmING converts uppercase to lowercase and vice versa
print(string.count('o')) # 2 counts the number of occurrences of 'o' in the string

print(string.center(30, '*')) # *****pYthOn ProGraMming***** centers the string within a field of width 30 and fills the extra space with '*'


Str="Python Strings"
for i in Str:
    print(i) # prints each character of the string on a new line


print(string.startswith("p"))
print(string.endswith("n"))