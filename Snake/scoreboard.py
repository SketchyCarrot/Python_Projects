from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 310)
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 20, "normal"))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 20, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Ariel", 25, "normal"))