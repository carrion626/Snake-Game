from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >\
            280 or snake.segments[0].ycor() < -280:
        score.game_over()
        game_on = False
    if snake.segments[0].distance(food) < 10:
        food.refresh()
        snake.extend()
        score.score_plus()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            score.game_over()

screen.exitonclick()
