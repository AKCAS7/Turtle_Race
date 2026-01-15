from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400 )
user_input = screen.textinput("Take your pick", " Choose your winning color : " )
'''
t4.penup()
t4.goto(x = -230, y = 80 )
t4.down()

t5.penup()
t5.goto(x = -230, y = -80 )
t5.down()

t6.penup()
t6.goto(x = -230, y = -120 )
t6.down()
#print(user_input)
'''
a = -200
speeds= [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
positions = [ --70, --40, 0, 80, 120 ]
start_y = -120
spacing = 50

turtles = []

for turtle_index in range(0, 6):
    t = Turtle(shape = "turtle")
    t.penup()
    t.goto(-230, start_y + turtle_index * spacing)
    turtles.append(t)
   
    


    


