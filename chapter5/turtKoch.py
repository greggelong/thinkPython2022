# really simple koch easy to see the recursion


import turtle

greg = turtle.Turtle()


def koch(t,l):
    if l < 90:       ## this is the exit condition and size of lines that make up koch
        t.forward(l)
    else:
        koch(t,l/3)
        t.left(60)
        koch(t,l/3)
        t.right(120)
        koch(t,l/3)
        t.left(60)
        koch(t,l/3)

greg.penup()
greg.setx(-500)
greg.pendown()
koch(greg,900)        
    





turtle.exitonclick()
