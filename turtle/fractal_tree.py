# make a recursive tree
import turtle
t = turtle.Turtle()

sides = 20
turn = 45
around = 90
forward = 50

# t.shape('arrow')
t.color('red')
t.fillcolor('red')
t.pensize(2)
t.forward(50)
for i in range(sides):
    t.left(turn)
    t.forward(forward)
    forward = forward/1.2
t.done()