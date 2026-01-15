from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400 )

start_y = -120
spacing = 50

turtles = []
colors = [ "red", "orange", "blue", "black", "purple", "yellow", "violet" ]
random.shuffle(colors)


for turtle_index in range(0, 6):
    t = Turtle(shape = "turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-230, start_y + turtle_index * spacing)
    turtles.append(t)

user_input = screen.textinput("Take your pick", " Choose your winning color : " )
print(user_input)

race_on = True
winning_color = None

while race_on is True:
    for t in turtles:
        t.forward(random.randint(1,10))
        if t.xcor() >= 230:
            winning_color = t.pencolor()
            race_on = False
            break



if user_input.lower() == winning_color.lower():
    print( winning_color + " WON...The " + winning_color + " turtle is the WINNER   !!!!!!!!!! " )
else:
    print( user_input + " turtle lost. The " + winning_color + " turtle is the winner" ) 

screen.exitonclick()
