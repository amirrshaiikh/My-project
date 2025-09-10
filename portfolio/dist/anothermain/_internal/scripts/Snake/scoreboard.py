from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 250)
        self.hideturtle()
        self.color("white")
        self.score=0
        with open(r"C:\Users\moham\Documents\portfolio\scripts\Snake\main.txt" , mode="r") as file:
            self.high_score=int(file.read())
        self.update_scoreboard()

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, 'center', ('Courier', 14, 'normal'))

    # def game_over(self):
    #     self.home()
    #     self.write("Game over!", False, 'center', ('Courier', 14, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'C:\Users\moham\Documents\portfolio\scripts\Snake\main.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score=0
        self.update_scoreboard()
