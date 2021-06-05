from turtle import *

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            highscore = data.read()
        self.high_score = int(highscore)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.update_score()
    #     self.goto(0, 0)
    #     self.write("Game over", align=ALIGNMENT, font=FONT)



