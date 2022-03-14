from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Make Screen with Black BG
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Make Snake
snake = Snake()

# Make Food
food = Food()

score_board = ScoreBoard()


# Control Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


# Move Snake Forward
alive = True
while alive:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score_board.increase_score()

    # Detect collision with Wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        alive = False
        score_board.game_over()

    # Detect collision with Tail.
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            alive = False
            score_board.game_over()


screen.exitonclick()