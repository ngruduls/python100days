# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow"]
y_positions = [-70, -40, -10]
all_turtles = []

for turtle_indexx in range(0, 3):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_indexx])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[turtle_indexx])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    winning_colors = []
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colors.append(turtle.pencolor())

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

    if is_race_on == False:
        if user_bet in winning_colors:
            print(f"Youve won. {winning_colors} won")
        else:
            print(f"Youve lost. {winning_colors} won")

screen.exitonclick()