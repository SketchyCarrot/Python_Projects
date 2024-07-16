from turtle import Turtle, Screen
import random

screen = Screen()

race_on = False
screen.setup(1000, 270)
bet = screen.textinput(title = "Make your bets!", prompt = "Which color turtle will win the race?")

color = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for turtle in range(0, 6):
    t = Turtle()
    t.speed("fast")
    t.shape("turtle")
    t.color(color[turtle])
    t.penup()
    t.goto(-480, -100 + 40*turtle)
    turtles.append(t)

if bet:
    race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 455:
            winner = t.pencolor()
            if winner == "bet":
                print(f"You won the bet! The {winner} turtle is the winner")
            else:
                print(f"You lost the bet. The {winner} turtle is the winner")
                race_on = False
                
        distance = random.randint(0, 15)
        t.forward(distance)

screen.exitonclick()