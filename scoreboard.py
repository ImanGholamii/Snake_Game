from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
with open("data.txt") as f:
    high_score = f.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score)
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=283)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
