from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

     #detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increse_score()
        food.refresh()



screen.exitonclick()