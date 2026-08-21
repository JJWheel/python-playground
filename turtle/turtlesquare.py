# make a square using turtle
import turtle
t = turtle.Turtle()

sides = 4
turn = 90

# t.shape('arrow')
t.color('red')
t.fillcolor('red')
t.pensize(10)
# t.forward(100)
t.begin_fill()
for i in range(sides):
    t.forward(100)
    t.left(turn)
t.end_fill()

t.done()