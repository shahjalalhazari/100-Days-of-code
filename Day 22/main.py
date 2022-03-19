from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Game Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # To turn off animation


# Paddles
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()


# Move Paddles by Kyes.
screen.listen()
# Move Right Paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Move Left Paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move() # Move ball continuously

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # Bounce into y direction

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() -340:
        ball.bounce_x() # Bounce into x direction

    # Right Paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position() # Reset ball position
        scoreboard.l_point()

    # Left Paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position() # Reset ball position
        scoreboard.r_point()

screen.exitonclick()