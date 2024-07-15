from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_pos()
       

    
    def move_up(self):
        self.forward(MOVE_DISTANCE)


    def reset_pos(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def at_finish_line(self):
        return self.ycor()>FINISH_LINE_Y
