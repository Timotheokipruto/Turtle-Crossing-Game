from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        super().__init__()
        self.cars=[]
        self.car_speeds = STARTING_MOVE_DISTANCE
       
        


    def create_car(self):

        rand_chance = random.randint(1,6)

        if rand_chance ==1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            y_pos = random.randint(-250,250)
            car.goto(250,y_pos)
            self.cars.append(car)

   
        
    def move_car(self):

        for car in self.cars:
            car.backward(self.car_speeds)

    
    def level_up(self):
        self.car_speeds+=MOVE_INCREMENT