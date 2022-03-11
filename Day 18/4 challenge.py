import random
from turtle import Turtle, Screen

tim = Turtle()

colors = [
    "rosy brown",
    "dark slate blue",
    "deep pink",
    "firebrick",
    "cornflower blue",
    "gold",
    "cyan",
    "medium spring green",
    "orange red",
    "pale goldenrod",
    "midnight blue",
    "dark slate gray",
    "medium aquamarine",
    "medium sea green",
    "orange",
    "beige",
    "slate blue",
    "indigo",
]


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(8)


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()