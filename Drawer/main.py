from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.left(90)
t.speed("fastest")

def forward():
    t.forward(15)

def backward():
    t.right(180)
    t.forward(15)

def right():
    t.right(15)

def left():
    t.left(15)

def clear():
    t.clear()
    t.penup()
    t.hideturtle()
    t.home()
    t.pendown()
    t.showturtle()

screen.listen()
screen.onkey(key = "w", fun = forward)
screen.onkey(key = "s", fun = backward)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "a", fun = left)
screen.onkey(clear, "c")

screen.exitonclick()