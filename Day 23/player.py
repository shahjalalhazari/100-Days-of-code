from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.at_starting_position()


    # MOVE TURTLE
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    
    # GO TO STARTING POSITION
    def at_starting_position(self):
        self.goto(STARTING_POSITION)

    # LEVEL UP SUCCESSFULLY
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False