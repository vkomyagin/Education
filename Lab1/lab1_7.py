import turtle

n=1000
r = 10
f = 2
turtle.shape('turtle')
for i in range(0, n):
    turtle.forward(f+i/30)
    turtle.left(r)
    
