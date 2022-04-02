from turtle import Screen
import time
from player import Player
from car import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)


# PLAYER / TURTLE
player = Player()
# CAR
car_manager = CarManager()
# SCOREBOARD
scoreboard = Scoreboard()


# MOVE TURTLE
screen.listen()
screen.onkey(player.move_forward, "Up") # movw turtle forward by UP key.


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() # create new cars.
    car_manager.move_cars() # move cars backward.

    # DETECT COLLISION WITH CARS
    for car in car_manager.cars:
        if car.distance(player) < 20: # if turtle hit with car.
            scoreboard.game_over() # show game over text.
            game_on = False # stop the game.

    # SUCCESSFULLY CROSSED THE ROAD
    if player.at_finish_line(): # if turtle finish the level.
        player.at_starting_position() # move turtle into starting position.
        car_manager.increase_speed() # and increase the cars speed.
        scoreboard.increase_level() # increase turtle level up.


screen.exitonclick()