from snake import *
from turtle import *
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Down", fun=snake.move_down)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.add_score()
        food.refresh()
        snake.extend()

#Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        time.sleep(1)
        snake.reset()

#Detect collision with tail
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            time.sleep(1)
            snake.reset()


screen.exitonclick()
