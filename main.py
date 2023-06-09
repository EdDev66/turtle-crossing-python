from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_running = True
while game_is_running:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_running = False
            scoreboard.game_over()

    # Detect succesful crossing
    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()