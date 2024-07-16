from turtle import Screen, Turtle
mihir = Turtle()
print(mihir)
mihir.shape("turtle")
mihir.color("DeepPink3")

for c in ("DeepPink3", "black"):
    for x in range(1, 1000):
        mihir.color(c)
        mihir.speed("fastest")
        mihir.forward(10*x)
        mihir.right(179)

my_screen = Screen()
my_screen.canvheight = 300
print(my_screen.canvheight)
my_screen.exitonclick()
