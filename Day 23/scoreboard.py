from turtle import Turtle


FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-390, 265)
        self.update_scoreboard()


    # UPDARE SCOREBOARD EACH SUCCESSFULL LEVEL UP
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)


    # INCREASE LEVEL UP WHEN CROSS THE ROAD
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font=FONT)