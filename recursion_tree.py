import turtle
import random


def ct():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    return t


def leaf(t):
    t.pencolor("green")
    t.pensize(5)
    t.right(30)
    t.forward(7)
    t.left(60)
    t.forward(7)
    t.pencolor("orange")
    t.left(120)
    t.forward(7)
    t.left(60)
    t.forward(7)
    t.left(150)


def tree(branchLen, t, width):
    if (branchLen > 4) and (width > 0):
        color = "#B07D1E"
        t.pensize(width)
        t.pencolor(color)
        t.forward(branchLen)

        angle = random.randint(10, 30)
        delta = random.randint(0, int(branchLen/2))

        t.left(angle)
        tree(branchLen-delta, t, width-1)

        t.right(angle*2)
        tree(branchLen-delta, t, width-1)

        t.left(angle)
        t.pencolor(color)
        t.backward(branchLen)
        return 0

    leaf(t)


W = turtle.Screen()
tree(100, ct(), 10)
W.exitonclick()

