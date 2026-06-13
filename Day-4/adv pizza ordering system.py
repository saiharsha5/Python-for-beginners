print("Pizza ordering system")
#print("Menu for ordering pizza ")
piz=int(input("Enter the number of pizza: "))
small=10
medium=15
large=20

cheese=2
pepperoni=3
olives=5
jalapenos=5

total=0
while True:
    print("1. Medium")
    print("2. Large")
    print("3. Small")
    choice=int(input("Choose the size of pizza: "))
    if choice==1:
        total=total+medium
    elif choice==2:
        total=total+large
    elif choice==3:
        total=total+small
    else:
        print("Enter a valid choice")

    print("\n")

    
    while True:
        print("1. cheese")
        print("2. pepperoni")
        print("3. olives")
        print("4. jalapenos")
        numoftop=int(input("Enter the number of toppings:  "))
       
        for i in range(numoftop):
            choice=int(input("Choose the toppings: "))
            if choice==1:
                total=total+cheese
            elif choice==2:
                total=total+pepperoni
            elif choice==3:
                total=total+olives
            elif choice==4:
                total=total+jalapenos
            else:
                print("Enter a valid choice")
        break
    break
print(f"Your total bill amount is {total}")

                       