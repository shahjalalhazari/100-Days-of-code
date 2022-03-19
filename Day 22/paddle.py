from turtle import Turtle


class Paddle(Turtle): # Inherit Turtle class

    # Create Paddle
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # To change turtle/shape size.
        self.penup()
        self.goto(position)

    # Move Paddle
    def up(self):
        new_y = self.ycor() + 20 # 'ycor' for current 'y' position.
        self.goto(self.xcor(), new_y) # 'xcor' for current 'x' position.

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)