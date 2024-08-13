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
def screen_config():
    screen.listen()
    screen.onkey(fun=snake.move_up, key="Up")
    screen.onkey(fun=snake.move_down, key="Down")
    screen.onkey(fun=snake.move_right, key="Right")
    screen.onkey(fun=snake.move_left, key="Left")


def game():
    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(0.1)  # refresh the page every 0.1 seconds

        snake.move()

        if snake.head.distance(food) <= 15:
            food.refresh()
            score.add_score()
            snake.extend_snake()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 282 or snake.head.ycor() < -300:
            score.reset()
            snake.reset()
            game_is_on = False

        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
                game_is_on = False


def main():
    while True:
        screen_config()
        game()
        user_prompt = screen.textinput(title="Try again?", prompt="yes / no")
        if user_prompt != "yes" or user_prompt is None:
            break

        score.reset()
        snake.reset()
        food.refresh()
        screen_config()

    screen.exitonclick()


if __name__ == "__main__":
    main()
