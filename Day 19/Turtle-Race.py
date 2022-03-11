import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=500)
user_choice = screen.textinput(title="Make your choice.", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
race_start = False
all_turtles = []

# y pisitions for turtles
y_positions = [-125, -75, -25, 25, 75, 125]

# create six turtles for race with random color
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_positions[turtle])
    all_turtles.append(new_turtle)

# if user choice their turtle
if user_choice:
    race_start = True

while race_start:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            race_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()