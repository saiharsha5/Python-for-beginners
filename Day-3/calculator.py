print("Calculator ")
def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
    print("---------------------------------")
def sub(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
    print("---------------------------------")
def mul(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")
    print("---------------------------------")
def div(a,b):
    print(f"Division of {a} and {b} is {a/b}")
    print("---------------------------------")
def rem(a,b):
    print(f"Remainder of {a} and {b} is {a%b}")
    print("---------------------------------")

while True:
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Modulus')
    print('6. Exit')
    choice=int(input("Enter your choice: "))
    if choice==6:
        break
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    if choice==1:
        add(a,b)
    elif choice==2:
        sub(a,b)
    elif choice==3:
        mul(a,b)
    elif choice==4:
        div(a,b)
    elif choice==5:
        rem(a,b)

