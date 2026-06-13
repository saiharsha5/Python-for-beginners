class Product():
    def __init__(self,name,price):
        print("Product object is created..!")
        self.name=name
        self.price=price
p1=Product('phone',2000)
print("======================")
print(f"name={p1.name}")
print(f"price={p1.price}")

p2=Product('iphone',120000)
print("======================")
print(f"name={p2.name}")
print(f"price={p2.price}")

p3=Product('oppo',3000)
print("======================")
print(f"name={p3.name}")
print(f"price={p3.price}")

p4=Product('mi',15000)
print("======================")
print(f"name={p4.name}")
print(f"price={p4.price}")