from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    # After erasing previous score, inrease new score by one
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # After Each succesfull crossing speed of car will increase as level will also increase 
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

   # If collission occurs, Game over text will appear at (0,0)
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
