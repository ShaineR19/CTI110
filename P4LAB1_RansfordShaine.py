# Shaine Ransford
# 3/25/2024
# P4LAB1a
# This program will make  triangle and square using the turtle import

import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(1)
t.pencolor('#89CFF0')
t.shape("turtle")

for i in (1,2,3):
        t.forward(120)
        t.left(120)

t.penup()
t.forward(180)
t.pendown()

for j in (1,2,3,4):
        t.forward(120)
        t.left(90)

win.mainloop()
