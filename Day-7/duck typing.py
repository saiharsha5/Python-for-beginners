class Duck:
    def walk(self):
        print("Thapak thapak thapak thapak ")
class Horse:
    def walk(self):
        print("tadak tadak tadak tadak")

def myfunction(obj):
    obj.walk()

d=Duck()
myfunction(d)
h=Horse()
myfunction(h)