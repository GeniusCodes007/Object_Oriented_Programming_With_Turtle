from turtle import *

def start(t:Turtle, my_color, my_width, my_size):
    t.color(my_color)
    t.width(my_width)

    t.begin_fill()

    for x in range(5):
        t.forward(my_size)
        t.left(144)
    t.end_fill()

    done()

