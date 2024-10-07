from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong the Movie the Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True
while game_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  #Detect ball collision with top and bottom
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.y_bounce()

  #Detect collision with r_paddle
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
    ball.x_bounce()

  if ball.xcor() > 380 or ball.xcor() < -380:
    game_on = False


screen.exitonclick()
