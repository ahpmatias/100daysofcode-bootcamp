import time
from turtle import Screen, Turtle
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
screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.clear()
    scoreboard.show_scoreboard()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increment_score()





# 1. Create a turtle that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.

# 2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge
# of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for
# our little turtle).

# 3. Detect when the turtle player collides with a car and stop the game if this happens.

# 4. Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this
# happens, return the turtle to the starting position and increase the speed of the cars.

# 5. Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.

screen.exitonclick()