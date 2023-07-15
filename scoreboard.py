from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.goto(-290, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align='left', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 24, 'normal'))

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()