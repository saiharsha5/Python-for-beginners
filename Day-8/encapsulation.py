class BankAccount:
    def __init__(self,name,acc,pin):
        self.__name=name
        self.__acc=acc
        self.__pin=pin
        print("Bank Account is created")
    def get_name(self):
        print(self.__name)
    def get_acc(self):
        print(self.__acc)
    def get_pin(self):
        print(self.__pin)
b1=BankAccount('RAM',123454321,1212)
b1.get_name()
b1.get_acc()
b1.get_pin()
    

        