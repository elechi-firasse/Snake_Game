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
    if snake.head.distance(food) < food.wid:
        food.refresh()
        snake.extend()
        #food.wid = food.resize()
        score_board.update()


    #detect end game
    if -300 > snake.head.xcor() or snake.head.xcor() > 300 or -300 >snake.head.ycor() or snake.head.ycor() > 300 :
        game_is_on = False
        score_board.game_over()

    #detect any collision with tail
    for segment in snake.turtles[1:]:
        # if head collides with any segments of the tail tigger game over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
































screen.exitonclick()