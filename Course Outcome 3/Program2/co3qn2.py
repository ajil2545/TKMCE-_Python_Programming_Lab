from graphics.rectangle import *
from graphics._3D_graphics.cuboid import *
from graphics._3D_graphics.sphere import *
from graphics.circle import *
print("-------Rectangle-------")
l=int(input("Enter the length: "))
b=int(input("Enter the breadth: "))
arearect(l,b)
perirect(l,b)
h=int(input("Enter the height of cuboid: "))
cuboidarea(l,b,h)
cuboidperi(l,b,h)
print("-------Circle-------")
r=int(input("Enter the radius: "))
areac(r)
circumc(r)
sphere(r)