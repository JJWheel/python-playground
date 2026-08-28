# a program that simulates a spiral
# importing turtle and math
import turtle as t
import math

# turtle config
t.bgcolor('black')
t.color('white')
t.shape('turtle')
t.pensize(3)

# defining variables
a = 0.5 # growth factor
b = 0.3 # growth rate
theta = 5 # starting angle

# draw
for i in range(360):
    r = a * math.exp(b * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t.goto(x, y)
    theta += 0.1
t.done