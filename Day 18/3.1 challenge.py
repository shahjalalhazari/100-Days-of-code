from mimetypes import read_mime_types
from turtle import Turtle, Screen

from pkg_resources import declare_namespace

tim = Turtle()

def triangle():
    for _ in range(3):
        tim.pencolor("rosy brown")
        tim.right(120)
        tim.forward(100)

def square():
    for _ in range(4):
        tim.pencolor("cornflower blue")
        tim.right(90)
        tim.forward(100)

def pentagon():
    for _ in range(5):
        tim.pencolor("cyan")
        tim.right(72)
        tim.forward(100)

def hexagon():
    for _ in range(6):
        tim.pencolor("medium spring green")
        tim.right(60)
        tim.forward(100)

def heptagon():
    for _ in range(7):
        tim.pencolor("gold")
        tim.right(51.428)
        tim.forward(100)

def octagon():
    for _ in range(8):
        tim.pencolor("firebrick")
        tim.right(45)
        tim.forward(100)

def nonagon():
    for _ in range(9):
        tim.pencolor("deep pink")
        tim.right(40)
        tim.forward(100)

def decagon():
    for _ in range(10):
        tim.pencolor("dark slate blue")
        tim.right(36)
        tim.forward(100)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()



screen = Screen()
screen.exitonclick()