# really simple koch easy to see the recursion



import turtle
import random

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


def snowFlake(t,level,size):
    t.penup()
    t.sety(200)
    t.setx(0)
    t.pendown()
    t.right(60)
    koch2(t,level,size)
    t.right(120)
    koch2(t,level,size)
    t.right(120)
    koch2(t,level,size)                                                                   


def kochRnd(t,level,size):   ## here the level is set explicitly and 
    ang1 = 60
    ang2 = 120
    ang3 = 60
    if level ==0:          ## the exit condition is the level
        t.forward(size)
    else:
        koch2(t,level-1,size/3)
        if (random.randint(0,1)==0):
            ang1 =ang1*-1
            print("bing",ang1)
        t.left(ang1)
        koch2(t,level-1,size/3)
        if (random.randint(0,1)==0):
            ang2 =ang2*-1
            print("bong",ang2)
        t.right(ang2)
        koch2(t,level-1,size/3)
        if (random.randint(0,1)==0):
            ang3 =ang3*-1
            print("pop",ang3)
        t.left(ang3)
        koch2(t,level-1,size/3)



    
snowFlake(greg,3,300)

greg.penup()
greg.setheading(0)
greg.sety(100)
greg.setx(-500)
greg.pendown()
koch(greg,900) 
print("done")       
    
greg.penup()
greg.sety(-100)
greg.setx(-500)
greg.pendown()
kochRnd(greg,4,900) 





turtle.exitonclick()
