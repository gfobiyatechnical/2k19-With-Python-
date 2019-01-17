#Aim : Program that calculates the number of rectangular tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the user.
# Developer : Rakesh Yadav

a,ch,b = list((input("Enter dimensions of floor (in m):  ").split(' ')))
d1 = int(a)
d2 = int(b)
floor = d1*d2
m,Ch,n = list((input("Enter dimensions of tile (in m):  ").split(' ')))
D1 = float(m)
D2 = float(n)
tile = D1*D2
num_tiles = floor / tile
print("Numbers of Tiles : %.2f" %num_tiles )
