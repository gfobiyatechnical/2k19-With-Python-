import turtle

turtle.bgcolor("black")
turtle.pensize(4)
turtle.color("yellow","pink")

print("\t1. Square\n\t2. Hexagon ")
n=int(input("\t\t"))
if n==1: 
    for i in range(5):
        turtle.left(90)
        turtle.forward(125.84)
elif n==2:
    for i in range(7):
        turtle.left(60)
        turtle.forward(125.84)
