from turtle import Turtle, Screen
from time import sleep

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
    food.shapesize(0.5)


# Food
food.shape('circle')
food.color('red')
# # Keys
# screen.onkey(fun=move_fd(), key="w")
# screen.onkey(fun=backward, key="s")
# screen.onkey(fun=go_to_right, key="d")
# screen.onkey(fun=go_to_left, key="a")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(1)
    for snake in range(len(snake_list) - 1, 0, -1):
        new_x = snake_list[snake - 1].xcor()
        new_y = snake_list[snake - 1].ycor()
        print(snake-1, new_x, new_y)
        snake_list[snake].goto(new_x, new_y)
    snake_list[0].fd(20)

screen.exitonclick()
