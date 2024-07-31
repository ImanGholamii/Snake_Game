from turtle import Turtle
from random import choice

class Food(Turtle):
    coordinates = []
    for x in range(-280, 280, 2):
        for y in range(-280, 260, 2):
            coordinates.append((x, y))
    random_cor = choice(coordinates)
    print(random_cor)

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("gold")
        self.shape("circle")
        self.shapesize(stretch_wid=0.49, stretch_len=0.49)
        self.speed("fastest")
        self.goto(self.random_cor)
