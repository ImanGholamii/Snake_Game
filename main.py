from turtle import Turtle, Screen
from time import sleep
from snake import Snake

# Screen configs
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

t_obj = Turtle()
food = Turtle()

# background
score = 0
t_obj.color("white")
t_obj.hideturtle()
t_obj.teleport(x=0, y=260)
t_obj.write(f"Score: {score}", align="center", font=("Courier", 20, 'bold'))


# Food
food.shape('circle')
food.color('gold')
food.penup()
food.shapesize(0.5)
food.goto((0, 50))
# # Keys
# screen.onkey(fun=move_fd(), key="w")
# screen.onkey(fun=backward, key="s")
# screen.onkey(fun=go_to_right, key="d")
# screen.onkey(fun=go_to_left, key="a")

snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    sleep(1)


screen.exitonclick()
