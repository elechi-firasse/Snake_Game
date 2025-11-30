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
game_is_on = False

def start_up():
    global game_is_on
    game_is_on = True
    snake.up()

def start_down():
    global game_is_on
    game_is_on = True
    snake.down()

def start_left():
    global game_is_on
    game_is_on = True
    snake.left()

def start_right():
    global game_is_on
    game_is_on = True
    snake.right()

screen.listen()

# Arrow keys: start the game AND set direction
screen.onkey(start_up, "Up")
screen.onkey(start_down, "Down")
screen.onkey(start_left, "Left")
screen.onkey(start_right, "Right")

# Main loop always runs so key events work
while True:
    screen.update()
    time.sleep(0.1)

    if not game_is_on:
        continue   # wait until an arrow key starts the game

    snake.move()

    # detect eating food
    if snake.head.distance(food) < food.wid:
        food.refresh()
        snake.extend()
        # food.wid = food.resize()
        score_board.update()

    # detect end game (wall collision)
    if (
        snake.head.xcor() < -300 or snake.head.xcor() > 300 or
        snake.head.ycor() < -300 or snake.head.ycor() > 300
    ):
        game_is_on = False
        score_board.game_over()

    # detect any collision with tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
