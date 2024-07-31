from turtle import Turtle
from random import choice

class Food(Turtle):
    coordinates = []
    for x in range(-278, 278, 1):
        for y in range(-278, 260, 1):
            coordinates.append((x, y))


    def __init__(self):
        super().__init__()
        self.penup()
        self.color("gold")
        self.shape("circle")
        self.shapesize(stretch_wid=0.49, stretch_len=0.49)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_cor = choice(self.coordinates)
        self.goto(random_cor)
