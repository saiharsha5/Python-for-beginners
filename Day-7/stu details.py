class Student():
    def __init__(self,name,age):
        print("Student object is created..!")
        self.name=name
        self.age=age
def details(self):
    print("-----------------")
    print(f"name is {self.name}")
    print(f"age is {self.age}")
s1=Student('scott',23)
details(s1)
s2=Student('ram',21)
details(s2)
s3=Student('Raj',23)
details(s3)
s4=Student('ravi',19)