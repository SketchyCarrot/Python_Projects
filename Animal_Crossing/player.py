from turtle import Turtle

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.left(90)
        self.goto(0, -270)

    def move(self):
        ynew = self.ycor() + 10
        self.goto(self.xcor(), ynew)

