from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food

# Screen configs
screen = Screen()
screen.setup(width=600, height=620)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

t_obj = Turtle()

# background
score = 0
t_obj.color("white")
t_obj.hideturtle()
t_obj.teleport(x=0, y=283)
t_obj.write(f"Score: {score}", align="center", font=("Courier", 20, 'bold'))

# imported module objects
snake = Snake()
food = Food()

# # Keys
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)  # refresh the page every 1 seconds

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
