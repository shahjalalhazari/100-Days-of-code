from turtle import Screen, right
from snake import Snake
import time

# Make Screen with Black BG
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Make snake
snake = Snake()


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


screen.exitonclick()