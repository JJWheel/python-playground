# make a spiral
import turtle as t
import math
# defining variables
t.speed(0)
a = .5
theta = 0

for i in range(3600):
    r = a * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t.goto(x, y)
    theta += 0.05
t.done