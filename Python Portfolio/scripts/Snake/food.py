from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.setpos(rand_x, rand_y)