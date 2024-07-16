from turtle import Turtle
import random

colors = ["red", "orange", "cyan", "blue", "purple", "gray", "brown", "Pink3", "black"]
speed = 1
class Car(Turtle):
    def __init__(self):
        self.cars = []
        self.carspeed = 1.5

    def create_car(self):
        chance = random.randint(0, 25)
        if chance == 6:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 3)
            car.penup()
            color = random.choice(colors)
            car.color(color)
            car.goto(590, random.randrange(-20, 20)*10)
            self.cars.append(car)

    def dash(self):
        for c in self.cars:
            c.backward(self.carspeed)

    def upgrade(self):
        self.carspeed += speed
