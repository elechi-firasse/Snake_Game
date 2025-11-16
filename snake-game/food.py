from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rd_x = random.randint(-280, 280)
        rd_y = random.randint(-280, 280)
        self.goto(rd_x,rd_y)
