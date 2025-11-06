from turtle import *

t = Turtle()

t.color('red')
t.width(5)


t.begin_fill()
for x in range(5):
    t.forward(150)
    t.left(144)
t.end_fill()

done()