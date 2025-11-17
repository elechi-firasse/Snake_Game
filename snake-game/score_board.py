from turtle import Turtle
FONT = ("Comic Sans MS",  18, "normal")
ALIGN =  "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME_OVER",align=ALIGN,font=FONT)


    def update(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.score +=1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)