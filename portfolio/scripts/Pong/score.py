from turtle import Turtle
from ball import Ball
class Score(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setpos(positions)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score}", False, 'center', ('Courier', 35, 'normal'))