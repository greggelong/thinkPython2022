# really simple koch easy to see the recursion



import turtle

greg = turtle.Turtle()


def koch(t,l):
    if l < 90:       ## this is the exit condition and size of lines that make up koch
        t.forward(l) ##  it defacto sets the level
    else:
        koch(t,l/3)
        t.left(60)
        koch(t,l/3)
        t.right(120)
        koch(t,l/3)
        t.left(60)
        koch(t,l/3)

def koch2(t,level,size):   ## here the level is set explicitly and 
    if level ==0:          ## the exit condition is the level
        t.forward(size)
    else:
        koch2(t,level-1,size/3)
        t.left(60)
        koch2(t,level-1,size/3)
        t.right(120)
        koch2(t,level-1,size/3)
        t.left(60)
        koch2(t,level-1,size/3)



greg.penup()
greg.sety(100)
greg.setx(-500)
greg.pendown()
koch(greg,900) 
print("done")       
    
greg.penup()
greg.sety(-100)
greg.setx(-500)
greg.pendown()
koch2(greg,2,900) 





turtle.exitonclick()
