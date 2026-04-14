from turtle import Turtle, Screen
import random


timmy=Turtle()
screen=Screen()
screen.colormode(255)

def radncolo():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    a=(r, g, b)
    return a
directions=[0, 90, 180, 270]
timmy.speed(0)
timmy.pensize(15)
for i in range(300):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    timmy.color(radncolo())












# def drw_shape(num):
#     for i in range(num):
#         timmy.forward(100)
#         timmy.left(360/num)
#
# timmy.shape("turtle")
# timmy.color('green')
# timmy.speed(3)
# for _ in range(3, 11):
#     drw_shape(_)
#     timmy.color(random.choice(colours))

# for i in range (50):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)

# timmy.speed(7)
# timmy.shape('turtle')
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

#timmy.color('orangered')
# timmy.forward(150)
# timmy.right(150)
# timmy.forward(200)
# timmy.right(150)
# timmy.forward(200)
# timmy.right(150)
# timmy.forward(200)
# timmy.right(150)
# timmy.forward(150)
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.hideturtle()



screen=Screen()
screen.exitonclick()