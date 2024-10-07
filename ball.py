from turtle import Turtle
SPEED_MULTIPLIER = 0.85
DEFAULT_SPEED = 0.1

class Ball(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.movespeed = DEFAULT_SPEED

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def y_bounce(self):
    self.y_move *= -1

  def x_bounce(self):
    self.x_move *= -1
    self.movespeed *= SPEED_MULTIPLIER

  def reset(self):
    self.goto(0, 0)
    self.movespeed = DEFAULT_SPEED
    self.x_move *= -1
