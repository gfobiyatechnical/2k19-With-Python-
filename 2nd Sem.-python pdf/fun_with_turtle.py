# Author : Rakesh Yadav


import turtle
turtle.bgcolor("black")
turtle.pensize(4)
turtle.speed(100)


def Yadav_ji():
    turtle.speed(100)
    for i in range(200):
        turtle.speed(100)
        turtle.right(1)
        turtle.forward(1)

def blank():
    turtle.speed(100)
    turtle.color("black")
    turtle.right(40)
    turtle.forward(120)
    I()
    
def I():
    turtle.speed(100)
    turtle.color("white")
    turtle.left(0)
    turtle.forward(50)
    turtle.color("pink")
    turtle.backward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.color("pink")
    turtle.backward(50)
    
    turtle.color("black")
    turtle.left(-145)
    turtle.forward(70)
    turtle.right(120)
    lv()

def lv():
    turtle.speed(100)
    turtle.color("pink")
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(45)
    
    turtle.left(120)
    turtle.forward(35)
    turtle.backward(35)
    turtle.right(55)
    turtle.forward(35)
    turtle.backward(35)

    turtle.color("black")
    turtle.left(-145)
    turtle.forward(150)


        
turtle.speed(100)
turtle.color("red","red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(150.65)
Yadav_ji()
turtle.left(140)
Yadav_ji()
turtle.forward(149.50)
turtle.end_fill()

blank()

#turtle.hideturtle()
