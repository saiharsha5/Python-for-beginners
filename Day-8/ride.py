class Ride:
    def fare(self):
        print("Fare: 100rs")
class LuxaryRide(Ride):
    def fare(self):
        print("Fare: 300rs")
LR=LuxaryRide()
LR.fare()
r=Ride()
r.fare()