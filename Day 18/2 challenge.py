from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(10):
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()



screen = Screen()
screen.exitonclick()