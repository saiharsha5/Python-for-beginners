# write a function that takes the radius of a circle as input and return its area 
# use the formula area = pi x r^2


def rad(r):
    area = 3.14 * r**2
    print(area)
#r=int(input("r: "))
rad(5)

#using lambda fn

area= lambda r:3.14*r**2
print(area(5))

#square of a number

square=lambda a:a*a
print(square(5))