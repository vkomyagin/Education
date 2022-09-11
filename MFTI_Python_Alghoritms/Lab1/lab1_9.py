import turtle

n1=3
n2= n1+10

def nugol(n):
    for i in range(0, n):
        turtle.left(360/n)
        turtle.forward(30*n/4)
        

turtle.shape('turtle')    
for i in range(n1, n2+1):
    turtle.left((180 - 360/i)/2)
    nugol(i)
    turtle.right((180 - 360/i)/2)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


    
