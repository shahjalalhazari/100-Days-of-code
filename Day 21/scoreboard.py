from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    # Update score each time when snake eat food.
    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    # Game over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
    
    # Increase Score Board.
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()