from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.speed(0)

    def create_paddle(self, posx, posy):
        self.setposition(posx, posy)

    def move_up(self):
        self.forward(60)

    def move_down(self):
        self.backward(60)