class Customer:
    def __init__(self):
        pass
    #mutator or setter method
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def set_age(self,age):
        self.age=age
    #accessor or getter method
    def get_name(self):
        print(f"Name is {self.name}")
    def get_id(self):
        print(f"Id is {self.id}")
    def get_age(self):
        print(f"Age is {self.age}")
c1=Customer()
c1.set_id(101)
c1.set_name("Ram")
c1.set_age(23)
c1.get_id()
c1.get_name()
c1.get_age()