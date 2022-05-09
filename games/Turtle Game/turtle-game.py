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

#TO CREAT FINISH LINE
def f_line(x,y,color):
    t.speed(0)
    gap_size = 20
    t.penup()
    t.goto(x,y)
    t.shape('square')
    t.color(color)
    for i in range(10):
        t.goto(x,(y-(i*gap_size*2)))
        t.stamp()
        
f_line(250,170,'white')
f_line(230,190,'white')
f_line(230,170,'black')
f_line(250,190,'black')

# to draw starting line
t.shape('arrow')
t.penup()
t.goto(-270,170)
t.pendown()
t.pensize(2)
t.color('cyan')
t.rt(90)
t.stamp()
t.lt(90)
t.bk(340)
t.rt(90)
t.stamp()

#to import players
def importp(color,y):
    
    p = t.clone()
    p.speed(0)
    p.shapesize(2)
    p.color(color)
    p.shape('turtle')
    p.penup()
    p.goto(-270,y)
    p.pendown()
    return p

p1 = importp('blue',135)
p2 =importp('yellow',45)
p3= importp('lime',-45)
p4 = importp('peru',-135)

#to pause for 2 secs    
time.sleep(2)

# to run turtles
def race(p):
    p.speed = 0
    p.fd(randint(1,10))
    time.sleep(0.05)
    
while p1.xcor()< 240 and p2.xcor()<240 and p3.xcor()<240 and p4.xcor()<240:
    race(p1)
    race(p2)
    race(p3)
    race(p4)

# to declare winner
i = 0

if p1.xcor()>=240:
    print('Blue turtle is winner')
    for i in range(72):
        i = i +1
        p1.lt(5)
        p1.shapesize(i/20)
           
elif p2.xcor()>=240:
    print('Yellow turtle is winner')
    for i in range(72):
        i = i +1
        p2.lt(5)
        p2.shapesize(i/20)
         
elif p3.xcor()>=240:    
    print('Green turtle is winner')
    for i in range(72):
        i = i +1
        p3.lt(5)
        p3.shapesize(i/20)
             
elif p4.xcor()>=240:   
    print('Brown turtle is winner')
    for i in range(72):
        i = i +1
        p4.lt(5)
        p4.shapesize(i/20)
# to write winner on screen
t.penup()
t.hideturtle()
t.goto(-100,-30)
t.color('grey')
t.write('WINNER',font =('cursive',40,'bold') )     

    
