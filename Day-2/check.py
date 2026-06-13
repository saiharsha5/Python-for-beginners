age=int(input("Enter your age : "))

if (age>=18):
    print(f"Your age is {age} and you are eligible to vote")
else:
    print("You are not eligible to vote")


#ternery operator

res='eligible' if (age>=18) else "not eligible"
print(f"you are {res} to vote")
