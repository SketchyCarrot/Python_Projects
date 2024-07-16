from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 1/2
        self.ymove = 1/2
        self.move_speed = 0.0015

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def screen_bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.95

    def restart(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.move_speed = 0.0015