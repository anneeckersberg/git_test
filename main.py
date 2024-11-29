from turtle import Turtle, Screen
import random




screen = Screen()
screen.setup(500,400) #resize window, center of x and y is always 0,0

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []

game_on = False

for i in range(6):
    t = Turtle("turtle")
    t.penup()
    t.goto(x=-230, y=-130 + i*50)
    t.color(colors[i])
    turtles_list.append(t)


for i in range(10):
    obstacle = Turtle("square")
    obstacle.penup()
    obstacle.goto(random.randint(-250, 250), random.randint(-200, 200))

if user_bet: #means if user_bet exists
    game_on = True

winner_turtle = ""

while game_on:

    for x in turtles_list:

        if x.xcor() >= screen.window_width() / 2 - 30:
            winner_turtle = x
            game_on = False
            if winner_turtle.pencolor() == user_bet:
                print(f"You win. The winner is {winner_turtle.pencolor()}")
            else:
                print(f"You loose. The winner is {winner_turtle.pencolor()}")

        random_speed = random.randint(1, 10)
        x.forward(random_speed)

screen.exitonclick()