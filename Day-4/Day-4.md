# Day-4







MOVIE TICKET PRICE BASED ON AGE



Q) WAP to determine the age of





size=int(input("Enter the size of list : "))



Age=\[]

for i in range(size):

&#x20;   ele=int(input("Enter the age: "))

&#x20;   Age.append(ele)

print ( Age)

for i in Age:

&#x20;   if (i>=1 and i<=100):

&#x20;       if(i<12):

&#x20;           print(f"{i}----------> $10")

&#x20;       elif (i>=12 and i<=60):

&#x20;           print(f"{i}----------> $15")

&#x20;       else:

&#x20;           print(f"{i}----------> $12")







ATM MANAGEMENT SYSTEM

Q) WAP TO CREATE AN ATM SYSTEM THAT VALIDATES A PIN BEFORE ALLOWING TRANSACTION. the system should support deposit , withdrawal, balance inquiry, transaction history and exit





pin=int(input("Enter the pin : "))



acc\_bal=0

if pin==1234:

&#x20;   print("Welcome to bank ")



&#x20;   #Deposit, withdrawal, balance inquiry, exit

&#x20;   while True:

&#x20;       print("1. Deposit")

&#x20;       print("2. Withdraw")

&#x20;       print("3. Balance inquiry")

&#x20;       print("4. Exit")



&#x20;       choice=int(input("Enter your choice: "))

&#x20;       print("\\n")



&#x20;       if(choice==1):

&#x20;           amount=int(input("Enter the amount to deposit: "))

&#x20;           acc\_bal=acc\_bal+amount

&#x20;           print(f"Dear customer your account xxxxxxxxx1234 is credited with {amount}")

&#x20;       elif(choice==2):

&#x20;           amount=int(input("Enter the amount to withdraw: "))

&#x20;           if acc\_bal>=amount:

&#x20;               print(f"Dear customer your account xxxxxxxxx1234 is debited with {amount}")

&#x20;               acc\_bal=acc\_bal-amount

&#x20;           else:

&#x20;               print("Insufficient balance ")

&#x20;       elif (choice==3):

&#x20;           print(f"Dear customer your account xxxxxxxxx1234 has  {acc\_bal}")

&#x20;       else:

&#x20;           print("Thank you....")

&#x20;           break

else:

&#x20;   print("You entered incorrect pin")







PIZZA SHOP ORDERING SYSTEM



Q) CREATE A PIZZA ORDERING SYSTEM THAT ALLOWS CUSTOMERS TO CHOOSE PIZZA SIZE AND TOPPINGS. CALCULATE AND DISPLAY THE TOTAL BILL



print("Pizza ordering system")

\#print("Menu for ordering pizza ")

small=10

medium=15

large=20



cheese=2

pepperoni=3

olives=5

jalapenos=5



total=0

while True:

&#x20;   print("1. Medium")

&#x20;   print("2. Large")

&#x20;   print("3. Small")

&#x20;   choice=int(input("Choose the size of pizza: "))

&#x20;   if choice==1:

&#x20;       total=total+medium

&#x20;   elif choice==2:

&#x20;       total=total+large

&#x20;   elif choice==3:

&#x20;       total=total+small

&#x20;   else:

&#x20;       print("Enter a valid choice")



&#x20;   print("\\n")



&#x20;

&#x20;   while True:

&#x20;       print("1. cheese")

&#x20;       print("2. pepperoni")

&#x20;       print("3. olives")

&#x20;       print("4. jalapenos")

&#x20;       numoftop=int(input("Enter the number of toppings:  "))

&#x20;

&#x20;       for i in range(numoftop):

&#x20;           choice=int(input("Choose the toppings: "))

&#x20;           if choice==1:

&#x20;               total=total+cheese

&#x20;           elif choice==2:

&#x20;               total=total+pepperoni

&#x20;           elif choice==3:

&#x20;               total=total+olives

&#x20;           elif choice==4:

&#x20;               total=total+jalapenos

&#x20;           else:

&#x20;               print("Enter a valid choice")

&#x20;       break

&#x20;   break

print(f"Your total bill amount is {total}")



&#x20;





Q) allow customers to order multiple pizzas in a single order





CHARACTER FREQUENCY COUNTER



Q)COUNT THE FREQUENCY OF EVERY CHARACTER IN A STRING



































































&#x20;

&#x20;

