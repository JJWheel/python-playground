# make a spiral
# importing
import turtle as t
import math
# turtle config
t.speed(0)
t.shapesize(.25)
t.shape('circle')

# variables
a = 5
theta = 0

# a loop that makes the turtle go
for i in range(1800):
    r = a * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t.goto(x, y)
    theta += 0.05
t.done