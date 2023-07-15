from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_cars()

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            cars = Turtle()
            cars.shape("square")
            cars.color(random.choice(COLORS))
            cars.setheading(180)
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.penup()
            cars.goto(random.randrange(320, 340), random.randrange(-300, 300))
            #cars.goto(random.randrange(-100, 100), random.randrange(-100, 100))
            self.car_list.append(cars)

    def move(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_movement(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
