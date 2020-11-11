#BUTTERFLY
import turtle

def circle(diam):
    n = 50
    f = diam * 3.14 / n
    r = 360/n
    for i in range(n):
        turtle.left(r)
        turtle.forward(f)

turtle.shape('turtle')
turtle.left(90)
N = 10
D1 = 50
D2 = 10
for D in range (D1, D1+D2*N+1, D2):
    for i in 1,2:
        circle(D)
        turtle.left(180)


    
