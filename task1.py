#Create a hexagon, each side with a different colour

from turtle import *

draw = Turtle()

color= ['red', 'blue', 'green', 'pink', 'cyan', 'brown', 'indigo']

for x in color:
    #color of the line
    draw.color(x)
    #thickness of line
    draw.width(7)
    #length of line
    draw.fd(70)
    #angle
    draw.rt(360/7)

done()