import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=player.move_up, key="Up")



game_is_on = True

while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()


    #detect collision of turtle with car
    for car in car_manager.cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    #detect if player is at finish line
    if player.at_finish_line():
        player.reset_pos()
        scoreboard.update_scoreboard()
        car_manager.level_up()


  
screen.exitonclick()

