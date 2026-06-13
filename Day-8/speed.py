class Vehicle:
    def max_speed(self):
        print("Maximum Speed: 80 km/h")
class SportsCar(Vehicle):
    def max_speed(self):
        print("Maximum Speed: 250 km/h")
c1=Vehicle()
c1.max_speed()
c2=SportsCar()
c2.max_speed()
