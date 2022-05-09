import turtle
from random import randint
import time

s = turtle.getscreen()
t = turtle.Turtle()

#WINDOW SETUP
s.bgcolor('#84cc16')
s.title('TURTLE RACE')

#to creat tack
t.speed(0)
t.penup()
t.goto(-320,200)
t.pendown()
t.color('#e7e5e4')
t.fillcolor('#e7e5e4')
t.begin_fill()
t.fd(640)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(640)
t.rt(90)
t.fd(400)
t.end_fill()

#to write turtle race on window
t.penup()
t.goto(-140,230)
t.color('white')
t.pendown()
t.write('TURTLE RACE',font=('Arial',30,'bold'))