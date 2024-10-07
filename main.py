from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
MAX_SCORE = 1

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong the Movie the Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-100, 175))
r_scoreboard = Scoreboard((100, 175))

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
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
    ball.x_bounce()

  #Detect when right paddle misses the ball
  if ball.xcor() > 380:
    ball.reset()
    l_scoreboard.point()

  #Detect when left paddle misses the ball
  if ball.xcor() < -380:
    ball.reset()
    r_scoreboard.point()

  if r_scoreboard.score == MAX_SCORE:
    game_on = False
    r_scoreboard.game_over("right")
  elif l_scoreboard.score == MAX_SCORE:
    game_on = False
    l_scoreboard.game_over("left")



screen.exitonclick()
