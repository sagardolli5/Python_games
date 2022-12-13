import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-70, -40, -10, 20, 50, 80]
is_race_on = False
turtle_players = []

for turtle_index in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y_axis[turtle_index])
    turtle_players.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_players:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)


screen.exitonclick()