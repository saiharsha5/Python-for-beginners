# Day-7



#### procedural oriented programming system:



###### &#x09;-->Top down approach



#### Object oriented programming system:

&#x09;

###### &#x09;-->Bottom up approach



1. Inheritance
2. polymorphism
3. encapsulation
4. abstraction





Entity: Anything which has the existance or anything which exists.

Class:  1. Class is a logical entity or a blueprint or a plan to create multiple objects

&#x09;2. Multiple objects created by using the same class are known as identical objects or similar objects

&#x09;3. each object is unique



Object: it is a real world physical entity



Attribute: Attributes are represented by variable that contains data

method: method performs an action or tasks. it is similar to function.



ClassName Rules:



1. the class name can be any valid identifier
2. it can't be python reserved word
3. a valid class name starts with a letter, followed by any number of letter,numbers,underscores
4. a class name generally starts with capital letters.



How to create a class:



to define a class , we use the class keyword

this was an empty class



&#x09;	class Mobile:



syntax:



&#x09;object\_name = class\_name()

&#x09;object\_name = class\_name(arg)



ex: Mobile = Apple()







object:



&#x09;-> Ststes : 1. States represent attributes or properties of an entity

&#x09;	    2. data member



&#x09;-> Behaviour : 1. Functionality or action or work performed by entity

&#x09;	       2. methods





#### DATAMENBERS:



1. #### variable:



&#x09;	\~ Global variable: A variable which is declared within the class but outside the method , constructor or blo1ack is called global variable.

&#x09;			--> global scope



&#x09;			1. static variable:  represents class copy

&#x09;			2. non static variable: represents object copy / instance copy









&#x09;	\~ local varible: a variable which is declared within the class but inside the method , constructor, or bloack is called local variable

&#x09;			--> local or limited scope



2\. constants:





student:

1. Attributes or properties :

   1. name
   2. age
   3. branch
   4. percentage
   5. id
2. Functionality :

&#x09;1. studying

&#x09;2. using mobiles

&#x09;3. bunking classes

&#x09;4. exams







CONSTRUCTOR:



1. python supports a special type of methos called constructor for initializing the instance variable of a class
2. a class constructor , if defined is called whenever a program creates an object of that class



Types of constructors:



1. parameterized:

&#x09;	-> Parameterized constructors are ones which have parameters(other than self) defined in the \_\_init\_\_ method's paramete list

&#x09;	-> this type of constructors can take arguments from the user



2\. non-parameterized:

&#x09;	-> It is also known as the default constructor

&#x09;	-> the \_\_init\_\_ method includes a single parameter self

&#x09;	-> no other parameters are present in \_\_init\_\_'s parameter list

&#x09;	-> consequently, this constructor takes no arguments while creating a new object.







### \_\_init\_\_() method:



1. this is a magic method (dunder method) , which we can use to initialize variables for classes(ibjects)







##### self keyword:



\-> self is a default variable that contains the memory address of the current object.

\-> this variable is used to refer all the instance variable and method.

\-> when we create object of a class, the object name contains the memory location of the object.

\-> the memory location is internally passed to self, as self know the memory address of the object







TYPES OF METHODS:

* Instance methods

  * accessor methods(getter method)
  * mutator methods(setter method)
* class methods
* static method









ACCESSOR METHOD:



* this method is used to access or read data of the variable
* this method do not modify the data in variable
* this is also called as " **getter method "**



ex:-



def get\_value(self):

def det\_result(self):

def get\_name(self):







CLASS METHOD:

* class methods are the methods which act upon the class variables or static variable of the class
* Decorator @classmethod need to write above the class method
* by default, the first parameter of class method is cls which refers to class itself





INHERITANCE:



\~ Acquiring the properties of one class to another class



Super class : parent class/ base class / generic class

sub class: derived class / extended class / child class





Single inheritance : class b -> class a



multi level inheritance : c -> b -> a



multiple inheritance : c -> a \& c -> b



hierarchical inheritance : b, c, d --> a



hybrid inheritance : d -> b,d -> a

&#x09;

