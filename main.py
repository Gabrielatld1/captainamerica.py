import turtle as t
import math

screen = t.Screen()
screen.bgcolor("white")


def set_position(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.pensize(2)
    t.speed(10)


def draw(r, color):
    x_point = 0
    y_pont = -r
    set_position(x_point, y_pont)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def star(r, color):
    set_position(0, 0)
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    t.setheading(162)
    t.forward(r)
    t.setheading(0)
    for i in range(5):
        t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
        t.right(144)
    t.end_fill()


def white_middle(r, color):
    set_position(-18, 27)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(6):
        t.forward(r)
        t.right(60)
    t.end_fill()
    t.hideturtle()


draw(288, "red")
draw(234, "white")
draw(174, "red")
draw(126, "dark blue")
star(87, "white")
white_middle(35, "white")
t.done()
