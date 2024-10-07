from turtle import Turtle
POSITION = (350, 0)
MOVE = 25

class Paddle(Turtle):

  def __init__(self, position):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(position)

  def up(self):
    x_cor = self.xcor()
    y_cor = self.ycor()
    self.goto(x_cor, y_cor + MOVE)

  def down(self):
    x_cor = self.xcor()
    y_cor = self.ycor()
    self.goto(x_cor, y_cor - MOVE)


