from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=283)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, 'bold'))

