import random
from turtle import Turtle, Screen



def randcolor():
    r=random.randint(0,255)
    g = random.randint(0,255)
    b=random.randint(0,255)
    a=(r, g, b)
    return a

timmy=Turtle()
screen=Screen()
screen.colormode(255)
timmy.speed(0)

num=2
for i in range(int(360/num)):
    timmy.pensize(1.5)
    timmy.circle(100)
    timmy.color(randcolor())
    timmy.tilt(10)
    timmy.setheading(timmy.heading()+num)







screen.exitonclick()
