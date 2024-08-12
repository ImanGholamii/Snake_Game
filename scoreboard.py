from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
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
            with open("data.txt", mode="w") as new_data:
                new_data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
