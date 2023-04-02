import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter s color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is winner!" )
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        steps = random.randint(0, 10)
        turtle.forward(steps)





screen.exitonclick()