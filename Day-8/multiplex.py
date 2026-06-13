class Ticket:
    def price(self):
        print("Ticket price: 150rs")
class VIPTicket:
    def price(self):
        print("Ticket price: 500rs")
cls=Ticket()
cls.price()
vip=VIPTicket()
vip.price()