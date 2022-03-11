import random
from turtle import Turtle, Screen

from pkg_resources import declare_namespace

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
]

def draw_shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(shape_sides)


screen = Screen()
screen.exitonclick()