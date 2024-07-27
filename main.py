from turtle import Turtle, Screen

t_obj = Turtle()
food = Turtle()
# background
score = 0
t_obj.color("white")
t_obj.hideturtle()
t_obj.teleport(x=0, y=260)
t_obj.write(f"Score: {score}", align="center", font=("Courier", 20, 'bold'))
# Snake
snake_list = []
start_positions = [(0, 0), (-20, 0), (-40, 0)]
for i in range(3):
    snake = Turtle()
    snake.shape('square')
    snake.color('white')
    snake.penup()
    snake_list.append(snake)
    snake.goto(start_positions[i])


class MoveSnake:
    def move(self):
        pass


class Forward(MoveSnake):
    def __init__(self, turtle_obj):
        self.turtle_obj = turtle_obj

    def move(self):
        """takes obj lists and move them forward"""
        for obj in self.turtle_obj:
            obj.forward(60)


forward_move = Forward(snake_list)


def move_fd():
    forward_move.move()


# Food
food.shape('circle')
food.color('red')
food.shapesize(0.5)

screen = Screen()
screen.setup(width=600, height=600)
print(screen.screensize())
screen.bgcolor("black")
screen.title("Snake Game")
screen.onkey(fun=move_fd(), key="w")
# screen.onkey(fun=backward, key="s")
# screen.onkey(fun=go_to_right, key="d")
# screen.onkey(fun=go_to_left, key="a")
screen.exitonclick()
