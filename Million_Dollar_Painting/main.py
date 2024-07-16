import turtle
from turtle import Turtle, Screen
import random
import colorgram as col

aristortle = Turtle()
turtle.colormode(255)
aristortle.shape("turtle")
aristortle.speed("fastest")
aristortle.pensize(1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


colors = [(246, 233, 209), (247, 223, 235), (217, 242, 228), (238, 216, 74), (215, 229, 242), (230, 153, 84), (114, 173, 206), (35, 113, 165), (213, 135, 166), (224, 68, 109), (119, 192, 164), (239, 160, 187), (39, 181, 124), (158, 58, 102), (237, 75, 43), (205, 70, 25), (194, 177, 15), (236, 216, 4), (27, 139, 98), (140, 219, 188), (21, 173, 203), (173, 16, 48), (247, 165, 150), (182, 178, 224), (101, 112, 181)]
dimension = 10
coordinate = -40*dimension/2
aristortle.penup()
aristortle.hideturtle()
aristortle.goto(coordinate, coordinate)

for n in range(1, dimension + 1):
    for m in range(0, dimension):
        aristortle.dot(15, random.choice(colors))
        aristortle.penup()
        aristortle.forward(40)
    aristortle.goto(coordinate, coordinate + 40*n)


## STEREOGRAPH
# for n in range(0, 360):
#     aristortle.color(random_color())
#     aristortle.circle(170)
#     aristortle.right(1)


# # RANDOM WALK
# direction = [0, 180, 90, 270]
# for n in range(0, 1000):
#     aristortle.color(random_color())
#     aristortle.forward(15)
#     aristortle.right(random.choice(direction))


# # DRAWING SHAPES
# for m in range(3, 15):
#     aristortle.color(random_color())
#     for n in range(1, m+1):
#         aristortle.forward(100)
#         aristortle.right(360/m)

screen = Screen()
screen.exitonclick()