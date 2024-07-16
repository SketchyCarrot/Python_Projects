import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

slithering = True

while slithering:
    screen.update()
    time.sleep(0.1)
    snake.slither()
    if snake.head.distance(food) <=15:
        food.refresh()
        snake.grow()
        score.increment_score()

    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        slithering = False
        score.gameover()

    for segment in snake.snake_bits[1:]:
        if snake.head.distance(segment) < 9:
            slithering = False
            score.gameover()



screen.exitonclick()