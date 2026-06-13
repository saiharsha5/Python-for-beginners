pin=int(input("Enter the pin: "))
try:
    if pin==1234:
        print("Login is successful")
    else:
        raise TypeError("Incorrect pin")
except TypeError as t:
    print(t)