import time
from turtle import Turtle, Screen
import random
import obstacles
from obstacles import Car
from player import Animal

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("beige")
screen.title("Animal Crossing")
screen.tracer(0)
play = True
protagonist = Animal()

screen.listen()
screen.onkey(protagonist.move, "Up")

car = Car()

while play:
    time.sleep(0.005)
    screen.update()
    car.create_car()
    car.dash()

    for c in car.cars:
        if c.distance(protagonist) < 20:
            play = False

    if protagonist.xcor() == 290:
        protagonist.goto(0, -270)
        car.upgrade()

screen.exitonclick()