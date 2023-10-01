from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.chk = 0
        self.goto(0, 270)
        self.write(f'Score: {self.chk}', align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.write(f'FENITA', align='center', font=('Arial', 20, 'normal'))

    def score_plus(self):
        self.clear()
        self.chk += 1
        self.write(f'Score: {self.chk}', align='center', font=('Arial', 20, 'normal'))
