import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.create_cars()
    # Detect Player win
    if player.ycor() > 280:
        score.add_score()
        score.update_scoreboard()
        player.reset_game()
        cars.increase_movement()
        cars.create_cars()

    # Detect Player Collision with cars
    for car in cars.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()










