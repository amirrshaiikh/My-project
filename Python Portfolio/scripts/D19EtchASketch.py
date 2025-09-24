from turtle import Turtle, Screen


tim=Turtle()
screen=Screen()
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    tim.setheading(tim.heading()+10)
def turn_right():
    tim.setheading(tim.heading() -10)
def clearall():
    tim.clear()

screen.listen()
tim.pensize(2)
screen.onkeypress(move_forwards ,"w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkeypress(clearall, 'c')
screen.exitonclick()
