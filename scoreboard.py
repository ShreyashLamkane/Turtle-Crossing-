FONT = ("Courier", 16, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def update_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):

        self.goto(-70, 0)
        self.write("Game Over!", move=False, font=FONT)
