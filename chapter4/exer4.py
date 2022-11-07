import turtle
import math
greg = turtle.Turtle()

def square(t,d):
    for i in range(4):
        t.fd(d)
        t.lt(90)


def poly(t,s,d):
    for i in range(s):
        t.fd(d)
        t.lt(360/s)

def circle(t,r):
    circum = 2*math.pi*r
    n= 50
    leng = circum/n
    poly(t,n,leng)


poly(greg,5,100)
square(greg,200)
circle(greg,200)

turtle.exitonclick()
