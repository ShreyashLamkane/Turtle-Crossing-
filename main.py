import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_list = []
score=Scoreboard()

track = 0
game_is_on = True
while game_is_on:
    screen.onkey(player.move_up, "Up")

    if track % 6 == 0:
        car_list.append(CarManager())
    time.sleep(0.1)
    for car in car_list:
        car.move_car()
        if player.distance(car) < 30:
            game_is_on = False
            score.game_over()
        if player.ycor() > 280:
            player.home()
            player.create_player()
            car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
            score.update_score()

    track += 1
    screen.update()

screen.exitonclick()
