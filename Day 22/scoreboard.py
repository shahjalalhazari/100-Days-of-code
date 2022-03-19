from sys import flags
from turtle import Turtle, onclick


ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """Show both paddles score and update Scoreboard."""
        self.clear() # To clear old points
        # Show left paddle's score
        self.goto(-100, 260)
        self.write(self.l_score, False, align=ALIGNMENT, font=FONT)
        # Show right paddle's score
        self.goto(100, 260)
        self.write(self.r_score, False, align=ALIGNMENT, font=FONT)


    # Add points into left paddle
    def l_point(self):
        """Add 1 point each time in left paddle's scoreboard."""
        self.l_score += 1
        self.update_scoreboard()


    # Add points into right paddle
    def r_point(self):
        """Add 1 point each time in right paddle's scoreboard."""
        self.r_score += 1
        self.update_scoreboard()