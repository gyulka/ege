import turtle

t = turtle.Turtle()
k = 30
t.speed(0)
for i in range(3):
    t.forward(5 * k)
    t.left(270)
    t.forward(9 * k)
    t.right(90)
t.left(315)
for i in range(4):
    t.forward(11 * k)
    t.right(90)
    t.forward(5 * k)
    t.left(270)
t.penup()
for i in range(10):
    for j in range(-10, 5):
        t.goto(i * k, j * k)
        t.dot()
input()
