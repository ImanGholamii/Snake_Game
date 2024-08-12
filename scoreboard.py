from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=283)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(x=0, y=0)
        self.color("light pink")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()
