#SMILE
import turtle

def circled(diam, ugol):
    n = 30
    p = ugol/360
    nn = int(n*p)
    f = diam*3.14*p/nn
    r = ugol/nn
    #print(n,p,nn,f,r)
    for i in range(nn):
        turtle.forward(f)
        turtle.right(r)

turtle.shape('turtle')
print(turtle.heading(), turtle.xcor(), turtle.ycor()) #1
turtle.color("black","yellow")
turtle.begin_fill()
circled(200,360)
turtle.end_fill()
turtle.penup()
turtle.goto(-35, -35)
turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
circled(20,360)
turtle.end_fill()
turtle.penup()
turtle.goto(35, -35)
turtle.pendown()
turtle.begin_fill()
circled(20,360)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.width(10)
turtle.goto(0, -100)
turtle.penup()
turtle.goto(50, -120)
turtle.right(90)
turtle.pendown()
turtle.color("red")
circled(90,180)
