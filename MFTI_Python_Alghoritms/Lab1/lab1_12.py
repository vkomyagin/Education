#COIL SPRING
import turtle

def circled(diam, ugol):
    n = 30
    p = ugol/360
    nn = int(n*p)
    f = diam*3.14*p/nn
    r = ugol/nn
    print(n,p,nn,f,r)
    for i in range(nn):
        turtle.forward(f)
        turtle.right(r)

turtle.shape('turtle')
N=5
D1=100
D2=20
turtle.left(84)
for i in range(N):
    circled(D1, 180)
    circled(D2, 180)
    
