#07 Line Drawing Project

#Diego Torres
#car

#Init
import turtle
diego = turtle.Turtle()
diego.speed(10)
yareli=turtle.Turtle()
yareli.speed(10)

#Function
#diego
def bothCars():
    diegoCar()
    car()
def diegoCar():
    diego.pensize(8)
    wheelAndbottom()
    shell()
    bumper()
def wheel():
    diego.dot(100)
    diego.dot(50,'white')
#diego
def bottom():
    diego.penup()
    diego.goto(-250,-150)
    diego.pendown()
    diego.left(180)
    for i in range(2):
        diego.circle(15,180)
        diego.forward(500)

#diego
def wheelAndbottom():
    bottom()
    diego.penup()
    diego.goto(-180,-165)
    diego.pendown()
    wheel()
    diego.left(180)
    diego.penup()
    diego.forward(330)
    diego.pendown()
    wheel()
#diego
def front():
    diego.penup()
    diego.goto(-150,-50)
    diego.pendown()
    diego.left(180)
    diego.circle(100,90)
#diego
def back():
    diego.penup()
    diego.goto(-150,-50)
    diego.pendown()
    diego.left(90)
    diego.forward(25) 
    diego.circle(75,45)
    diego.forward(15)
    diego.circle(-150,45)
    diego.forward(35)
    diego.circle(-175,90)
#diego
def shell():
    front()
    back()
#diego
def bumper():
    diego.penup()
    diego.goto(-250,-150)
    diego.pendown()
    diego.left(270)
    diego.circle(-15,200)
    diego.penup()
    diego.goto(255,-150)
    diego.pendown()
    diego.circle(15,235)

#yareli
def car():
    windowOne()
    windowTwo()
    handle()
#yareli
def windowOne():
    yareli.pensize(8)
    yareli.up()
    yareli.goto(20,-60)
    yareli.left(90)
    yareli.pd()
    yareli.forward(65)
    yareli.left(90)
    yareli.circle(70,90)
    yareli.left(90)
    yareli.forward(70)
    yareli.right(90)
    yareli.forward(80)
#yareli
def windowTwo():
    yareli.right(90)
    yareli.pensize(8)
    yareli.up()
    yareli.goto(50,5)
    yareli.pd()
    yareli.left(90)
    yareli.forward(70)
    yareli.left(90)
    yareli.forward(150)
    yareli.left(120)
    yareli.circle(143,70)
#yareli
def handle():
    yareli.up()
    yareli.goto(5,-110)
    yareli.pd()
    yareli.pensize(4)
    yareli.right(10)
    for i in range(2):
        yareli.forward(40)
        yareli.right(90)
        yareli.forward(20)
        yareli.right(90)
#main
bothCars()
