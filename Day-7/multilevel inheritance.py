class Vehicle:
    def __init__(self,b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
class Bike(Vehicle):
    def __init__(self,b,p,c,s,g):
        super().__init__(b,p,c,s)
        self.g=g
        print("Bike constructor")
