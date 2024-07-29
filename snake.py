from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            self.snake_segments.append(new_segment)
            new_segment.goto(position)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            print(seg_num - 1, new_x, new_y)
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].fd(20)


