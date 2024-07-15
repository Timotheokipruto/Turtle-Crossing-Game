from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-220,270)
        self.write(f"Level: {self.level}", align="center",font=FONT)
       
        


    def update_scoreboard(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}", align="center",font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!",align="center", font=FONT)
        
