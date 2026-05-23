from turtle import *

t = Turtle()


t.color('black')
t.width(10)
t.pendown()
t.shape('circle')
t.speed(3)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def keyUp():
    t.goto(t.xcor(),t.ycor()+5)

def keyDown():
    t.goto(t.xcor(),t.ycor()-5)

def keyLeft():
    t.goto(t.xcor()-5,t.ycor())

def keyRight():
    t.goto(t.xcor()+5,t.ycor())




def keyGreen():
    t.color('green')

def keyCyan():
    t.color('cyan')

def keyMaroon():
    t.color('maroon')

def keyIndigo():
    t.color('indigo')

def keyBlack():
    t.color('black')




def keyBegin_fill():
    t.begin_fill()

def keyEnd_fill():
    t.end_fill()



scr = t.getscreen()

scr.onscreenclick(move)

t.ondrag(draw)

scr.onkey(keyUp,'Up')
scr.onkey(keyDown,'Down')
scr.onkey(keyLeft,'Left')
scr.onkey(keyRight,'Right')

scr.onkey(keyGreen,'g')
scr.onkey(keyCyan,'c')
scr.onkey(keyMaroon,'m')
scr.onkey(keyIndigo,'i')
scr.onkey(keyBlack,'b')

scr.onkey(keyBegin_fill,'z')
scr.onkey(keyEnd_fill,'x')

scr.listen()
