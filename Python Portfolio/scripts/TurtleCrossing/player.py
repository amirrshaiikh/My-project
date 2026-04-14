from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, cr):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.sc=Scoreboard()
        self.crr=cr


    def move(self):
        self.forward(MOVE_DISTANCE+20)
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.sc.inc_score()
            self.crr.level_up()

    def restart(self):
        self.goto(STARTING_POSITION)
        self.sc.score=0
        self.sc.score_output()
