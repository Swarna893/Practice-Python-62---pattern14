# Practice-Python-62---pattern14

from turtle import *
import colorsys
bgcolor('black')
pensize(2)
tracer(2)

h = 2
goto(0, 0)
for x in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    fillcolor(c)
    h += 0.999
    begin_fill()
    up()
    forward(x)
    down()
    right(9)
    forward(x)
    right(100)
    right(107)
    end_fill()

hideturtle()
done()
