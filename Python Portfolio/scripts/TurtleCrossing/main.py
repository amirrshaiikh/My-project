import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing")
screen.listen()

cars=CarManager()
pl=Player(cars)
screen.onkeypress(pl.move, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for card in cars.all_cars:
        if card.distance(pl)< 20:
            game_is_on=False
            pl.sc.game_over()


screen.exitonclick()