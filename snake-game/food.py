from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.wid = self.resize()
        self.refresh()


    def refresh(self):
        rd_x = random.randint(-280, 280)
        rd_y = random.randint(-280, 280)
        self.goto(rd_x,rd_y)
    def resize(self):
        rd_wid = random.random()*10
        # rd_len = random.random()*5
        self.shapesize(stretch_wid=rd_wid, stretch_len=rd_wid)
        return rd_wid
