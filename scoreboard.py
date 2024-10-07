from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self, position) -> None:
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.score = 0
    # self.r_score = 0
    self.goto(position)
    self.update_score()

  def point(self):
    self.score += 1
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(self.score, align="center", font=("Courier", 80, "normal"))

  def game_over(self, win_paddle):
    self.goto(0, 0)
    self.write(f"{win_paddle} Paddle wins", align="center", font=("Courier", 25, "normal"))

