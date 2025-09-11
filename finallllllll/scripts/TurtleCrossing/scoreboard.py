from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.setposition(-230, 250)
        self.score=0
        self.score_output()

    def score_output(self):
        self.clear()
        self.write(f"Level: {self.score}", False, 'center', FONT)

    def inc_score(self):
        self.score+=1
        self.score_output()

    def game_over(self):
        self.home()
        self.write("Game over", False, 'center', FONT)
