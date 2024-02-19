from turtle import *

shape('turtle')
shapesize(2)
bgcolor('black')
color('white')
speed(11)
goto(0, 0)

def linezzzz(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)

def circle(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)
        length = length + 1

circle(300, 25, 90)



penup()
goto(400,-25)
pendown()
color('red')

def polylines(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)

def spiral(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)
        length = length + 0.5

spiral(350, 25, 290)


penup()
goto(-400, -25)
pendown()
color('blue')

def plolines(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)

def spinn(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)
        length = length + 0.5

spinn(275, 1, 45)

