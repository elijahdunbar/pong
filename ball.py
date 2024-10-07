from turtle import Turtle
MOVE_SPEED = 10

class Ball(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_move = MOVE_SPEED
    self.y_move = MOVE_SPEED

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def y_bounce(self):
    self.y_move *= -1

  def x_bounce(self):
    self.x_move *= -1
