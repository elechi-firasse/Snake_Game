from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.font = "Comic Sans MS"
        self.font_size = 18
        self.font_type = "normal"
        self.write(f"Score: {self.score}", align="center", font=(self.font, self.font_size, self.font_type))


    def update(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.score +=1
        self.write(f"Score: {self.score}", align="center", font=(self.font, self.font_size, self.font_type))