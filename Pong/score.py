from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right = 0
        self.left = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.left, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 150)
        self.write(self.right, align="center", font=("Courier", 50, "normal"))

    def lpoint(self):
        self.left += 1
        self.update_score()

    def rpoint(self):
        self.right += 1
        self.update_score()
