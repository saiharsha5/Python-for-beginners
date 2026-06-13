class Mobile():
    def __init__(self,brand,price,color):
            print("Student object is created..!")
            self.brand=brand
            self.price=price
            self.color=color
def details(self):
        print("---------------------")
        print(f"Brand = {self.brand}")
        print(f"Price = {self.price}")
        print(f"Color = {self.color}")
s1=Mobile('mi',20000,'red')
details(s1)
s2=Mobile('samsung',70000,'black')
details(s2)