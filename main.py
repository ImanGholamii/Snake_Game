from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Score

# Screen configs
screen = Screen()
screen.setup(width=600, height=620)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

t_obj = Turtle()

# imported module objects
snake = Snake()
food = Food()
score = Score()

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

    if snake.head.distance(food) <= 10:
        food.refresh()
        score.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 282 or snake.head.ycor() < -286:
        game_is_on = False

screen.exitonclick()
