class Customer:
    def __init__(self):
        pass
    def delivery_charges(self):
        print("Delivery charges: 50rs")
class PrimeCustomer(Customer):
        def __init__(self):
             super().__init__()
        def delivery_charges(self):
             print("Delivery charges: 20rs")

c1=PrimeCustomer()
c1.delivery_charges()
c2=Customer()
c2.delivery_charges()

