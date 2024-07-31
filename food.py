from turtle import Turtle, Screen

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("gold")
        self.shape("circle")
        self.shapesize(0.5)


food = Food()

screen = Screen()
screen.exitonclick()
