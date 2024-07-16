import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("red")
        x = random.randint(-16, 16)
        y = random.randint(-16, 16)
        self.goto(x*20, y*20)
        self.showturtle()

    def refresh(self):
        x = random.randint(-16, 16)
        y = random.randint(-16, 16)
        self.goto(x*20, y*20)
