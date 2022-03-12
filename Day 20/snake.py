from turtle import Turtle

X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# Make Snake class
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    # Create Snake
    def create_snake(self):
        for position in X_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)

    # Move Forward
    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
           new_x_pos = self.snakes[snake_num - 1].xcor()
           new_y_pos = self.snakes[snake_num - 1].ycor()
           self.snakes[snake_num].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVE_DISTANCE)


    # Move Up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Move Down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Turn Right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    # Turn Left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)