from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        ny = self.ycor() + 20
        self.goto(self.xcor(), ny)

    def go_down(self):
        ny = self.ycor() - 20
        self.goto(self.xcor(), ny)
