#!/usr/bin/env python3
# coding=utf-8

import turtle

turtle.speed(0)
turtle.hideturtle()

def draw_rrectangle(color, cx, cy, w, h, r):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(cx - w / 2 + r, cy - h / 2)
    turtle.down()
    for i in range(2):
        turtle.fd(w - 2 * r)
        turtle.circle(r, 90)
        turtle.fd(h - 2 * r)
        turtle.circle(r, 90)
    turtle.end_fill()

def draw_line(color, x1, y1, x2, y2):
    turtle.pencolor(color)
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)

#рисуем кабель
draw_rrectangle("#505750", -2, -55, 16, 40, 5)
draw_rrectangle("#505750", 30, -67, 70, 16, 5)
turtle.pencolor("#505750")
draw_rrectangle("#505750", -2, -55, 14, 38, 5)
#рисуем узор на кабеле
draw_line("#ffffff", -2, -45, -2, -67)
draw_line("#ffffff", -3, -45, -3, -67)
draw_line("#ffffff", -1, -45, -1, -67)
draw_line("#ffffff", -2, -66, 80, -66)
draw_line("#ffffff", -2, -67, 80, -67)
draw_line("#ffffff", -2, -68, 80, -68)
draw_line("#000000", 50, -59, 50, -75)
#обрезали кабель
turtle.pencolor("#ffffff")
draw_rrectangle("#ffffff", 60, -67, 19, 20, 1)
#рисуем золотые вилки
turtle.pencolor("#000000")
draw_rrectangle("#ffa81d", -40, 25, 50, 20, 2)
for i in range(8):
    j = 21 + i
    draw_line("#ac7600", j * (-1), 16, -20, j - 2)
for i in range(15):
    draw_line("#ffd095", -60 + i, 16, -44 + i, 35)
for i in range(5):
    draw_line("#ffff8f", -55 + i, 16, -39 + i, 35)
turtle.pencolor("#000000")
draw_rrectangle("#ffa81d", -45, -25, 50, 20, 2)
for i in range(8):
    j = 21 + i
    k = -23
    draw_line("#ac7600", j * (-1), -34, -20, k)
    j += 1
    k += 1
for i in range(15):
    draw_line("#ffd095", -60 + i, -34, -44 + i, -15)
for i in range(5):
    draw_line("#ffff8f", -55 + i, -34, -39 + i, -15)
#рисуем прямоугольник задний
turtle.pencolor("#000000")
draw_rrectangle("#000000", 10, 0, 60, 100, 5)
#рисуем тени верхние и нижние
draw_rrectangle("#ffffff", 10, 25, 60, 50, 5)
draw_rrectangle("#505750", 10, -25, 60, 50, 5)
#рисуем поверх теней перекрывающий прямугольник
turtle.pencolor("#d0d8d0")
draw_rrectangle("#d0d8d0", 10, 0, 58, 90, 5)
#рисуем прямоугольник задний для кнопки
turtle.pencolor("#000000")
draw_rrectangle("#000000", 0, 0, 20, 70, 9)
#рисуем тени нижние и верхние
draw_rrectangle("#505750", 0, 20, 20, 30, 9)
draw_rrectangle("#ffffff", 0, -20, 20, 30, 9)
#рисуем поверх теней перекрывающий прямугольник
turtle.pencolor("#d0d8d0")
draw_rrectangle("#d0d8d0", 0, 0, 18, 60, 9)

#рисуем линию
draw_line("#000000", -2, 50, -2, -50)


turtle.done()