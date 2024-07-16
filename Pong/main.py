from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score = Score()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


play = True
while play:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.screen_bounce()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.restart()
        score.lpoint()

    if ball.xcor() < -380:
        ball.restart()
        score.rpoint()


screen.exitonclick()