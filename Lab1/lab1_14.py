#STARS
import turtle

def star(diam,n):
    r = 180-180/n
    for i in range(n):
        turtle.forward(diam)
        turtle.right(r)

turtle.shape('turtle')
star(100,5)
turtle.penup()
turtle.forward(200)
turtle.pendown()
star(100,11)
