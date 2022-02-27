from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.resizemode(rmode="user")
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.car_loc()
        self.setheading(180)

    def car_loc(self):
        x_cor = 300
        y_cor = random.randint(-230, 250)
        self.goto(x_cor, y_cor)

    def move_car(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.forward(self.speed)


