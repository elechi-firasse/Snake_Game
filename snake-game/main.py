import time
from snake import Snake
from turtle import Screen
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect eating food
    if snake.head.distance(food) < 18:
        food.refresh()
        score_board.update()


    #detect end game
    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or -280 >snake.head.ycor() or snake.head.ycor() > 280 :
        game_is_on = False
        score_board.game_over()



























screen.exitonclick()