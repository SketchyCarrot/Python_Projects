import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s = turtle.bgcolor('black')
t.speed("fastest")
t.hideturtle()

h = 0

# PRINTING A SPIRAL
n = 500
for i in range(1, 1000):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.right(250/i)
    t.forward(5)
    t.circle(i)




# # # PRINT A SQUARE GRADIENT
# t.penup()
# coordinate = 500
# t.goto(-coordinate/2, -coordinate/2)
# t.pendown()
# t.pensize(1)
# n = coordinate
# h = 0
# for i in range(coordinate):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 1/n
#     t.color(c)
#     for j in range(1):
#         t.forward(coordinate)
#         t.penup()
#         t.goto(-coordinate/2, -coordinate/2 + i)
#         t.pendown()

s = turtle.exitonclick()