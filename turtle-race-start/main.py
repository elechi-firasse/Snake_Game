from turtle import Turtle, Screen
import random


screen = Screen()

race_on = False
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter the color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
turtles = []
for index in range(0,6):
    tim1 = Turtle(shape="turtle")
    tim1.color(colors[index])
    tim1.penup()
    tim1.goto(-240, y[index])
    turtles.append(tim1)

if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won")
            else:
                print(f"you've lost the winner is {winning_color}")
            break

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()