import turtle
greg = turtle.Turtle()

def square(t,d):
    for i in range(4):
        t.fd(d)
        t.lt(90)


def poly(t,s,d):
    for i in range(s):
        t.fd(d)
        t.lt(360/s)




poly(greg,5,100)
square(greg,200)

turtle.exitonclick()
