# Day-3





### Function:



&#x09;	\~ a function is a block of code that has a name and you can call it, instead of writing something 100times , you can create a function and then call it 100 times

&#x09;	\~ this adds reusability and modularity to the code

&#x09;	\~ function can take arguments and return value



##### Types of functions:



1. User defined functions
2. Built in functions
3. Lambda functions
4. Recursion Functions





#### Syntax: Non parametarized fn



&#x09;

&#x09;def Function\_name():

&#x09;		Local variable

&#x09;		block of statement

&#x09;		return (variable or expression)



#### Syntax: parametarized fn



&#x09;def Function\_name(para1, para2....):

&#x09;		Local variable

&#x09;		block of statement

&#x09;		return (variable or expression)



Return Statement:

&#x09;

&#x09;	\~ Return statement can be used to return something from the function

&#x09;	\~ In python, it is possible to return one or more variable/ values



Syntax: return (variable or expression);



def add(y):

&#x09;x =10

&#x09;c = x+y

&#x09;return c

sum = add(20)

print(sum)





Example:



\#without return statements



def add(a,b):

&#x20;   print(f"Addition of {a} and {b} is {a+b}")

add(10,30)

add(20,5)





\#with return statements



def add(a,b):

&#x20;   return a+b

print(add(20,30))

print(add(40,40))





### NESTED FUNCTIONS:



&#x09;			\~ When we define one function inside another function, it is known as nested function or function nesting

Example:



&#x09;	def disp():

&#x09;		def show():

&#x09;			print("Show function")
print("Disp function")

&#x09;		show()

&#x09;	disp()



#### Arguments:

###### &#x09;	-> Formal arguments: Function definition parameters are called as formal args

###### &#x09;	-> Actual arguments: Function call arguments are actual args





#### Types of Actual arguments:



1. Positional arguments
2. key word arguments
3. default arguments
4. variable length arguments
5. keyword variable length arguments



1. positional arguments:

&#x09;

&#x09;		def pa(x,y):

&#x09;			z=x\*\*y

&#x09;			print(z)

&#x09;		pa(6,4)



2\. keyword arguments:



&#x09;		def show(name, age):

&#x09;			print(name,age)

&#x09;		show(name="Kalki" ,  age=12)



3\. default arguments:

&#x09;

&#x09;		def show(name,age=24):

&#x09;			print(name,age)

&#x09;		show(name="ram",age=32)



4\. variable length arguments:



&#x09;			def add(\*num):

&#x09;				z= num\[0]+num\[1]+num\[2]

&#x09;				print(z)

&#x09;			add(5,2,4)



5\. keyword variable length arguments:



&#x09;				def add(\*\*num):

&#x09;					z=num\['a']+num\['b']+num\['c']

&#x09;					print(z)

&#x09;				add(a=5,b=3,c=6)



6\. lambda function:

&#x09;

&#x09;		\~ a function without a name is called as anonymous function,

&#x09;		\~ it is also known as lambda function

&#x09;		\~ Anonymous function are not defined using def keyword rather they are defined using lambda keyword



syntax:

&#x09;	lambda argument\_list: expression



Example:

&#x09;	lambda x : print9x)

&#x09;	lambda x,y : print x + y





#### Pass a function as parameter:



\~ we can pass a function as parameter to another function



example:

&#x20;		def disp(sh):

&#x09;		print("Disp function"+sh())

&#x09;	def two():

&#x09;		return "Second function"

&#x09;	disp(two)





Area of circle







#### List:

&#x09;	

&#x09;\~ List represents a group of elements

&#x09;\~ Lists are very similar to array but there is major difference, 

&#x09;	an array can store only







##### LIST 



1. Creating lists
2. Accessing lists
3. Slicing lists
4. Reassigning lists(mutable)
5. Deleting elements
6. multi dimensional lists
7. concatenation of lists
8. operations on lists
9. literating on a list
10. list comprehension
11. built in functions
12. built in methods





#### Built in functions in lists



1. len()
2. max()
3. min()
4. sum()
5. sorted()
6. list()
7. any()
8. all()





#### Built in methods in lists



1. append()
2. insert()
3. remove()
4. pop()
5. clear()
6. index()
7. count()
8. sort()
9. reserve()



Concatenation of list:

&#x20;

&#x09;		\~ the + operator is used to concatenate the list



repeation operator: 



&#x09;		\~ the \* operator is used to repeat the list



























































