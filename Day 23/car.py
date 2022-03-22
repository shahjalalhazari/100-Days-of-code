from hashlib import new
from turtle import Turtle
import random



COLORS = ["red", "green", "orange", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # CREATE NEW CAR
    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(400, random_y)
            self.cars.append(new_car)

    # MOVE CARs BACKWARD
    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # INCREASE CAR SPEED WHEN LEVEL UP
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT