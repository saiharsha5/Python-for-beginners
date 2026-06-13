# Day-2



### Membership operator:

&#x09;\~ the membership operator are useful to test for membership in a sequence such as string, list, tuples and dictionaries.

&#x09;\~ there are two types of operators:

1. in

&#x09;	2. not in



Example:



\#in \& not in



List = \[10,30,25,35,20,25,20]



print(10 in List)

print(44 in List)

print(50 not in List)

print(10 not in List)



print("python" in 'I am working in python')

print("Python" in 'I am working in python')



OUTPUT:

True

False

True

False

True

False





### Identity operator:

&#x09;\~ the identity operators compare the memory locations of two objects.

&#x09;\~ hence, it is possible to know whether two objects are same or not

&#x09;\~ there are two types of identity operators:

&#x09;	1. is

&#x09;	2. is not

**Example:**



num1=10

print(num1)

print(id(num1))



num2 ='10'

print(num2)

print(id(num2))



print(num1 is num2)



**OUTPUT:**



10

140726029273816

10

3072147430624

False







### PEMDAS - Rule

P - Paranthesis

E - Exponential

M - Multiplication

D - Division

A - Addition

S - Subtraction







### Type conversion in python



\-> Implicit

\-> Explicit - 1. int() , 2. float() , 3. bin()  , 4.oct() , 5.hex()



#### Explicit:

&#x09;\~ the programmer converts one data type to another data type

\-> int(n)

\-> float(n)

\-> complex(n)

\-> str(n)

\-> list(n)

\-> tuple(n)

\-> bin(n)

\-> oct(n)

\-> hex(n)





#### USER INPUTS:



Example:



name=input("what is your name? ")

age=int(input("what is your age? "))



print("Hello, ",name, "! you are ",age, "years old.")



print(f"Hello ,{name}! You are {age} years old.")



OUTPUT:



what is your name? Ram

what is your age?21

Hello,  Ram ! you are  21 years old.

Hello ,Ram! You are 21 years old.





### Control statements:

&#x09;\~the flow control statements are divided into three categories



Flow control:



1. conditional statements: 1.if
2.if-else

&#x09;		   3.if-elif-else

&#x09;		   4.nested if-else



2\. transfer statements: 1.break

&#x09;		2.continue

&#x09;		3.pass



3\. iterative statements: 1.for

&#x09;		 2.while





#### Condition statements:



##### IF :

&#x09;if condition:

&#x09;	statement 1

&#x09;	statement 2

##### IF - ELSE:

&#x09;	if condition:

&#x09;		statement 1

&#x09;	else:

&#x09;		statement 2





###### Q) write a python prgm to read input from user and check if age is valid or not



age=int(input("Enter your age : "))



if (age>=18):

&#x20;   print(f"Your age is {age} and you are eligible to vote")

else:

&#x20;   print("You are not eligible to vote")





\#ternery operator



res='eligible' if (age>=18) else "not eligible"

print(f"you are {res} to vote")



OUTPUT:



Enter your age : 21

Your age is 21 and you are eligible to vote

you are eligible to vote









Q)WAP to check whether the user enter year is a leap year or not





## Loops



#### for loop:



&#x09;\~Known number of iteration

&#x09;\~ for loop in python is used to iterate over a sequence (like list , tuple, string or range) and execute a block of code repeatedly for each item in sequence



Example:



###### Q) WAP to print hello world for 5 times



for i in range(1,6):

&#x20;   print("Hello world")



###### Q)WAP to print 1st n natural numbers



num=int(input("Enter a number: "))



for i in range(0,num+1):

&#x20;   print(i)







###### Q)WAP to print natural numbers form n to 1



num=int(input("Enter a number: "))



for i in range(num,0,-1):

&#x20;   print(i)







###### Q) WAP to print even numbers till n



num=int(input("Enter a number: "))



for i in range(1,num+1):

&#x20;   if i%2==0:

&#x20;       print(i)



print("-"\*20)



for i in range(2,num+1,2):

&#x20;   print(i)







###### Q) WAP to print odd numbers form 1 to n



num=int(input("Enter a number: "))



for i in range(1,num+1):

&#x20;   if i%2!=0:

&#x20;       print(i)



print("-"\*20)



for i in range(1,num+1,2):

&#x20;   print(i)



###### Q) WAP to calculate the sum of n natural numbers



num=int(input("Enter a number: "))

sum=0

for i in range(1,num+1):

&#x20;   sum=sum+i

print(sum)



###### Q) WAP to print the factorial of n



num=int(input("Enter a number: "))

fact=1

for i in range(1,num+1):

&#x20;   fact=fact\*i

print("the factorial of ",num,"is",fact )



###### Q) WAP to print the multiplication table of n



num=int(input("number: "))



for i in range (1,11):

&#x20;   print(f"{num} \* {i} = {num\*i}")





###### Q)WAP to print reversed multiplication of n



num=int(input("number: "))



for i in range (10,0,-1):

&#x20;   print(f"{num} \* {i} = {num\*i}")







###### Q) WAP to print multiplication tables from 1 to n



num=int(input("number: "))

for i in range(1,num+1):

&#x20;   print(f"Multiplication table of {i}: ")

&#x20;   print('===============================')

&#x20;   for j in range (1,11):

&#x20;       print(f"{i} \* {j} = {i\*j}")



###### Q)WAP to print multiplication tables from n to 1





num=int(input("number: "))

for i in range(num,0,-1):

&#x20;   print(f"Multiplication table of {i}: ")

&#x20;   print('===============================')

&#x20;   for j in range (1,11):

&#x20;       print(f"{i} \* {j} = {i\*j}")





###### Q) WAP to print reversed multiplication tables from 1 to n



num=int(input("number: "))

for i in range(1,11):

&#x20;   print(f"Multiplication table of {i}: ")

&#x20;   print('===============================')

&#x20;   for j in range (10,0,-1):

&#x20;       print(f"{i} \* {j} = {i\*j}")





#### WHILE LOOP:

&#x09;		\~Unknown number of iterations



&#x09;		\~while loop is used to repeatedly excutes a block of code as long as a given condition is true.

&#x09;		\~It keeps looping until the condition becomes false



while condition :

&#x09;body





Q) WAP to print natural numbers from 1 to n



num=int(input("Enter a number: "))



i=1

while (i<=num):

&#x20;   print(i)

&#x20;   i+=1



### Transfer statements



in python transfer statements are used to alter the program's way of execution in a certain manner.

for this purpose , we use three types of transfer statements

1.break statement


&#x09;2.continue statement

&#x09;3.pass statement



##### CONTINUE STATEMENT

&#x09;		\~ It skips the current iteration and moves to next iteration









###### Q) WAP to print the mulipication table of 5 with only even multiples



n=5

for i in range(1,11):

&#x20;   if i%2==0:

&#x20;       print(f"{n}\*{i}={n\*i}")



Q)WAP to read integer value as input from user and find the count of the digits without using builtin functions

\---

num=int(input("Enter a number: "))

count=0

rem=0

while num!=0:

&#x20;   rem=num%10

&#x20;   count+=1

&#x20;   num=num//10

print("Number of digits: ",count)



OUTPUT:



Enter a number: 745

Number of digits:  3

