from turtle import Turtle
FONT = ("Comic Sans MS",  18, "normal")
ALIGN =  "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()




    def update(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.score +=1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)