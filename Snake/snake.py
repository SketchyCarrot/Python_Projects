from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_bits = []
        self.create_snake()
        self.head = self.snake_bits[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_body(-20 * i, 0)

    def add_body(self, x, y):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(x, y)
        self.snake_bits.append(body)

    def grow(self):
        self.add_body(self.snake_bits[-1].xcor(), self.snake_bits[-1].ycor())
        # body = Turtle("square")
        # body.speed("fastest")
        # body.color("black")
        # body.hideturtle()
        # body.penup()
        # self.snake_bits.append(body)
        # body.showturtle()
        # body.color("white")

    def slither(self):
        for i in range(len(self.snake_bits) - 1, 0, -1):
            x = self.snake_bits[i - 1].xcor()
            y = self.snake_bits[i - 1].ycor()
            self.snake_bits[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)