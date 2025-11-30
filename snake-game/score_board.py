from turtle import Turtle
FONT = ("Comic Sans MS",  18, "normal")
ALIGN =  "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())

        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()




    def update(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.score +=1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)