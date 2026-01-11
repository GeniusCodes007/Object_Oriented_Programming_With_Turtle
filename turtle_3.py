from turtle import *

def start(t:Turtle, my_color:str, my_width:float, my_size:float):
    t.color(my_color)
    t.width(my_width)

    t.begin_fill()

    for x in range(5):
        t.forward(my_size)
        t.left(144)
    t.end_fill()

    done()

tur_t_= Turtle()
start(tur_t_, 'green', '')