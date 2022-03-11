from turtle import Turtle, Screen

tim = Turtle()
tim.color("red")


screen = Screen()

# move forward
def move_forward():
    tim.forward(10)

# move backward
def move_backward():
    tim.backward(10)

# turn right 15 degree
def turn_right():
    tim.right(15)

# tuen left 15 degree
def turn_left():
    tim.left(15)

# clear the screen and re-position the turtle
def reset_turtle():
    tim.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(reset_turtle, "c")
screen.exitonclick()